# tgbot — 代理指南

## 快速开始

```bash
uv sync                      # 安装依赖
cp .env.example .env         # 设置 BOT_TOKEN
uv run python -m src         # 运行 bot（需要先启动 ai-service）
```

## 命令

| 操作 | 命令 |
|---|---|
| 运行 bot | `uv run python -m src` |
| 运行 ai-service | `uv run uvicorn ai-service.main:app --port 8000` |
| 安装依赖 | `uv sync` |
| 添加依赖 | `uv add <package>` |
| Docker | `docker compose up --build -d` |
| Docker（仅沙盒） | `docker compose up --build -d sandbox` |

未配置测试、lint、格式化和类型检查命令。

## 架构

前后端分离架构：

```
┌──────────────────┐     HTTP/SSE     ┌──────────────────────┐
│  Bot (薄客户端)    │ ◄──────────────► │  AI Service (FastAPI) │
│                  │    POST /api/chat │                      │
│  - 接收 Telegram  │   (流式 SSE 交互)  │  - AI 模型调用         │
│    消息           │                  │  - Agent 循环管理      │
│  - 格式化消息      │                  │  - Tool 编排分发       │
│  - 内联键盘        │                  │  - MCP 工具管理        │
│  - 执行 Telegram  │                  └──────────┬───────────┘
│    工具 (send等)   │                             │
└──────────────────┘                              │
       │                                          │ HTTP
       ▼                                          ▼
┌──────────────────┐                  ┌──────────────────────┐
│  Sandbox (已有)   │                  │  Sandbox (代码执行)   │
└──────────────────┘                  └──────────────────────┘
```

- **Bot** (`src/`): 薄客户端，处理 Telegram 消息收发、格式化、内联键盘，以及 Telegram 工具的执行。AI 相关的推理交给 AI Service。
- **AI Service** (`ai-service/`): FastAPI 服务，管理 AI 模型、Agent 循环、工具编排。通过 SSE 流式返回结果。
- **Sandbox** (`sandbox/`): 独立的代码执行沙盒。

通信协议：Bot 发起 `POST /api/chat`，AI Service 通过 SSE 事件流返回结果。当需要调用 Telegram 工具时，AI Service 发出 `tool_call` 事件，Bot 执行后通过 `POST /api/chat/result` 回传结果。

### AI Service API

| 端点 | 方法 | 描述 |
|---|---|---|
| `/api/chat` | POST | 流式聊天 (SSE)，Tool 调用通过事件交互 |
| `/api/chat/result` | POST | 提交 Tool 执行结果 |
| `/api/models` | POST | 列出可用 AI 模型 |
| `/api/hooks/resolve` | POST | 解析 human-in-the-loop hook |
| `/health` | GET | 健康检查 |

- **入口点**: `src/__main__.py`（通过 `python -m src` 运行）
- **配置**: `BOT_TOKEN` 来自 `os.environ["BOT_TOKEN"]`（在 `src/config.py` 中，导入时若未设置会报错）
- **aiogram 3**: `Router` 对象位于 `src/handlers/`，通过 `dp.include_router()` 注册到 `Dispatcher`
- **健康检查**: aiohttp 服务器在 `:8080/health` 上与 bot 轮询并行运行，使用 `asyncio.TaskGroup`
- **关闭**: SIGTERM/SIGINT 信号处理器绑定事件循环，TaskGroup 上下文管理器负责清理

## 包管理器

使用 **uv**（非 pip 或 poetry）。锁定文件: `uv.lock`。Docker 使用 `uv sync --frozen --no-dev`。

## 添加处理器

1. 在 `src/handlers/my_feature.py` 中创建 `Router`，如 `router = Router(name="my_feature")`
2. 使用 `@router.message(Command("cmd"))` 装饰
3. 在 `src/__main__.py` 中导入并调用 `dp.include_router(my_router)`

## 处理器列表

| 文件 | 命令 | 描述 |
|---|---|---|
| `start.py` | `/start` | 欢迎信息 |
| `ping.py` | `/ping` | 健康检查，回复 pong |
| `models.py` | `/models` | 列出 AI 可用模型（通过 AI Service） |
| `skill.py` | `/skill` | 管理 Agent 技能 (find/info/add/list/init)，集成 skills.sh |
| `mcps.py` | `/mcps` | 管理 MCP 服务器工具 (http/stdio) |
| `callback.py` | callback_query | 处理内联键盘回调 (feature:approve/reject/revise) |

所有处理器使用 `argparse` 解析子命令和生成帮助信息。

## AI 集成

两层架构：

### `ai-service/`（后端）

- `main.py` — FastAPI 服务，管理 AI 模型和 Agent 循环
- 支持 `openai` / `anthropic` / `ai_gateway` 三种 provider
- 依赖 `ai` 模块（`vercel-ai-sdk` 包）
- 通过 SSE 流式返回聊天结果，Tool 调用通过 HTTP 回传分发

### `src/ai/`（Bot 端 Telegram 工具）

- `tools.py` — AI 工具集合，包括消息发送、群管、bot 信息编辑 (name/photo/desc)、以及 `propose_new_feature`（bot 自主提议新功能，通过 callback 审批）
- Bot 将工具 schema 发给 AI Service，AI Service 需要执行 Telegram 工具时通过 SSE 事件回调 Bot

### `src/ai_service_client.py`

Bot 端 AI Service HTTP 客户端：
- `chat_stream()` — 发送消息并接收 SSE 流，自动处理 tool_call 回调
- `list_models()` — 获取可用模型列表

## 沙盒服务 (`sandbox/`)

独立的代码执行沙盒服务，运行在 Docker 中：

- `sandbox/main.py` — FastAPI 服务，兼容 `vercel.sandbox` 接口风格
- `sandbox/Dockerfile` — 基于 python:3.14-slim + nodejs
- `src/sandbox_client.py` — 与 bot 集成的客户端（`SandboxClient.create()` / `run_command()` / `stop()`）
- docker-compose 配置: 2 副本, 安全限制 (cap_drop, no-new-privileges, read_only, tmpfs)

## 热加载 (`src/hotloader.py`)

Bot 新增的功能支持热更新：

- **工具热加载**: AI 提议的工具代码 (`@ai.tool`) 通过 `exec()` 动态编译注册，无需重启
- **处理器热加载**: AI 提议的 handler 代码写入 `src/handlers/{name}.py` 后通过 `importlib` 动态导入并注册到 Dispatcher
- **持久化**: 启动时 `auto_discover()` 扫描 `src/handlers/` 自动加载历史动态生成的 handler 文件
- **流程**: `propose_new_feature` → callback 审批 ✅ → `hotloader.register_tool/handler()` → 即时生效

## 约定

- `src/` 是 Python 包（src-layout），使用绝对导入: `from src.config import ...`
- 不使用相对导入（如 `from .config`）
- 所有处理器是返回 `None` 的异步函数
- 基于子命令的处理器使用 `argparse` 解析参数和生成帮助文本
