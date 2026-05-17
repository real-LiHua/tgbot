# tgbot — 代理指南

## 快速开始

```bash
cp .env.example .env         # 设置 APP_ID, API_HASH, BOT_TOKEN
go run ./cmd/bot/            # 运行 bot（需要先启动 docker-agent）
```

## 命令

| 操作 | 命令 |
|---|---|
| 运行 bot | `go run ./cmd/bot/` |
| 构建 bot | `go build -o bot ./cmd/bot/` |
| 运行 docker-agent | `docker-agent serve api agent.yaml` |
| 安装依赖 | `go mod tidy` |
| 添加依赖 | `go get <package>` |
| Docker | `docker compose up --build -d` |
| Docker（仅沙盒） | `docker compose up --build -d sandbox` |
| Docker（仅 New API） | `docker compose up --build -d new-api` |

## 架构

前后端分离架构：

```
┌──────────────────┐   SSE 流 (HTTP)   ┌──────────────────────────┐
│  Bot (Go 客户端)  │ ◄──────────────► │  Docker Agent API Server │
│                  │  POST /api/sessions│                          │
│  - gotgproto     │  /:id/agent/agent │  - AI 模型调用           │
│    (MTProto)     │                    │  - Agent 循环管理         │
│  - 接收 Telegram  │                   │  - 会话管理 (SQLite)     │
│    消息           │                   │  - Tool 编排分发          │
│  - 内联键盘        │                   └──────────┬───────────────┘
│  - 执行 Telegram  │                               │ MCP / HTTP
│    工具           │                               ▼
│  - MCP 服务器      │                  ┌──────────────────────┐
│    (/mcp SSE)     │◄─────────────────│  Bot MCP/HTTP Server  │
│  - OpenAPI 兼容    │                  │  /mcp (SSE)           │
│    (/api/openapi)  │                  │  /api/openapi.json    │
└──────────────────┘                   └──────────────────────┘

┌──────────────────────────────────────────────────────────────────┐
│  New API (AI Gateway)                    端口 3000               │
│  - 多模型聚合与分发                                             │
│  - 用量统计与成本核算                                           │
│  - 密钥管理与速率限制                                           │
│  - OpenAI / Claude / Gemini 兼容 API                             │
└──────────────────────────────────────────────────────────────────┘
```

- **Bot** (`cmd/bot/` + `internal/`): Go 客户端，使用 **gotgproto** 通过 MTProto 连接 Telegram。处理消息收发、格式化、内联键盘以及 Telegram 工具的执行。通过 MCP 协议（SSE）暴露工具供 Docker Agent 调用，同时保留 OpenAPI 兼容端点。
- **Docker Agent** (`agent.yaml` + 二进制): Docker Agent API Server，管理 AI 模型、Agent 循环、会话持久化。通过 MCP toolset 导入 Bot 暴露的 Telegram 工具，在需要时调用 Bot 执行。
- **Sandbox** (`sandbox/`): 独立的代码执行沙盒（FastAPI），用于隔离执行 AI 提议的工具代码。
- **New API** (`new-api` 服务): AI 网关层，聚合多个 AI 提供商 (OpenAI, Anthropic, Google, DeepSeek 等) 为统一 OpenAI 兼容 API。Bot 和 Docker Agent 均可将其作为 AI provider 端点使用，提供密钥管理、用量统计、速率限制等功能。

通信协议：Bot 创建 Docker Agent 会话，通过 `POST /api/sessions/:id/agent/agent` 发送消息并接收 SSE 事件流。当需要调用 Telegram 工具时，Docker Agent 通过 MCP 协议或 OpenAPI HTTP 调用 Bot 端点，Bot 执行后返回结果。

### Docker Agent API

| 端点 | 方法 | 描述 |
|---|---|---|
| `/api/agents` | GET | 列出可用 Agent |
| `/api/sessions` | POST | 创建新会话 |
| `/api/sessions/:id` | GET | 获取会话详情 |
| `/api/sessions/:id` | DELETE | 删除会话 |
| `/api/sessions/:id/agent/:agent` | POST | 运行 Agent（SSE 流） |
| `/api/ping` | GET | 健康检查 |

### Bot HTTP API

| 端点 | 方法 | 描述 |
|---|---|---|
| `/mcp` | GET/POST | MCP 协议 SSE 传输端点 |
| `/api/openapi.json` | GET | OpenAPI 3.0 spec（向后兼容） |
| `/health` | GET | 健康检查 |

- **入口点**: `cmd/bot/main.go`（通过 `go run ./cmd/bot/` 运行）
- **配置**: `APP_ID`, `API_HASH`, `BOT_TOKEN` 来自环境变量（在 `internal/config/config.go` 中）
- **gotgproto**: 使用 MTProto 连接 Telegram，通过 `dispatcher.AddHandler()` 注册处理器
- **MCP**: 使用 `modelcontextprotocol/go-sdk` 定义和注册工具，通过 SSE/HTTP 传输
- **健康检查**: HTTP 服务器在 `:8080/health` 上运行
- **关闭**: SIGTERM/SIGINT 信号处理器触发优雅关闭

## 包管理器

使用 **go mod**（Go 内置）。锁定文件: `go.sum`。Docker 使用 `go build`。

## 添加处理器

1. 在 `internal/bot/handlers.go` 中创建处理函数，如 `func (b *Bot) handleCmd(ctx *ext.Context, update *ext.Update) error`
2. 在 `registerHandlers()` 中注册: `d.AddHandler(handlers.NewCommand("cmd", b.handleCmd))`

## 处理器列表

| 函数 | 命令 | 描述 |
|---|---|---|
| `handleStart` | `/start` | 欢迎信息 |
| `handlePing` | `/ping` | 健康检查，回复 pong |
| `handleModels` | `/models` | 列出 AI 可用模型 |
| `handleSkill` | `/skill` | 管理 Agent 技能 |
| `handleFeatureCallback` | callback_query | 处理内联键盘回调 |
| `handleChat` | (catch-all) | 非命令消息通过 SSE 发送到 Docker Agent 进行 AI 对话 |

## AI 集成

两层架构：

### `Docker Agent`（AI 引擎）

- 通过 `agent.yaml` 配置 AI provider、model、system prompt
- 支持 `openai` / `anthropic` / `ai_gateway` 三种 provider
- 通过 MCP toolset 导入 Bot 暴露的 Telegram 工具 schema，每个工具成为独立 function calling
- 自动管理会话历史（SQLite 持久化）
- 最大 10 轮 Tool 调用循环（`max_iterations: 10`）

### `internal/tools/`（Bot 端工具定义与执行）

- `telegram.go` — Telegram 操作封装（sendMessage, banChatMember 等）
- `mcp.go` — MCP 服务器，注册所有工具到 `modelcontextprotocol/go-sdk`，处理 `tools/list` 和 `tools/call`

### `internal/ai/client.go`

Bot 端 Docker Agent HTTP 客户端：
- `ChatStream()` — 创建/复用会话，发送消息并接收 SSE 流，自动处理 `tool_call_confirmation`（自动批准）和 `agent_choice`（文本 delta）
- `ListModels()` — 获取可用模型列表
- 每个 chat 独立会话，通过 `sessions` 字典缓存

## 沙盒服务 (`sandbox/`)

独立的代码执行沙盒服务，运行在 Docker 中：

- `sandbox/main.py` — FastAPI 服务，兼容 `vercel.sandbox` 接口风格
- `sandbox/Dockerfile` — 基于 python:3.14-slim + nodejs
- `internal/sandbox/client.go` — 与 bot 集成的 Go 客户端
- docker-compose 配置: 1 副本, 安全限制 (cap_drop ALL, no-new-privileges, read_only, tmpfs /tmp:64m), 资源限制 (1 CPU, 256MB)

## 配置 (`internal/config/config.go`)

| 变量 | 默认值 | 描述 |
|---|---|---|
| `APP_ID` | (必填) | Telegram App ID（来自 https://my.telegram.org/apps） |
| `API_HASH` | (必填) | Telegram API Hash |
| `BOT_TOKEN` | (必填) | Telegram Bot Token |
| `AI_PROVIDER` | `openai` | AI 提供商 (`openai` / `anthropic` / `ai_gateway`) |
| `AI_MODEL_ID` | provider 默认 | 模型 ID 覆盖 |
| `DOCKER_AGENT_URL` | `http://localhost:8080` | Docker Agent 地址 |
| `LISTEN_ADDR` | `0.0.0.0:8080` | HTTP 服务器监听地址 |
| `NEW_API_SESSION_SECRET` | - | New API 会话密钥（多实例必需） |
| `NEW_API_CRYPTO_SECRET` | - | New API 加密密钥（使用 Redis 时必需） |
| `NEW_API_SQL_DSN` | - | New API 外部数据库连接串（默认 SQLite） |
| `NEW_API_REDIS_CONN_STRING` | - | New API Redis 连接串 |

## 动态目录 (`dynamic/`)

- `dynamic/handlers/{chat_id}/{name}.py` — 热加载的处理器持久化存储
- `dynamic/handlers/.gitkeep` — 占位文件

## 约定

- `internal/` 是 Go 内部包
- 使用绝对导入: `github.com/real-LiHua/tgbot/internal/...`
