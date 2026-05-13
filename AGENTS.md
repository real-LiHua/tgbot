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
│  - 热加载           │                  └──────────────────────┘
│  - 执行 Telegram  │
│    工具 (send等)   │
│  - 沙盒代码执行     │
└──────────┬────────┘
           │ HTTP
           ▼
┌──────────────────────┐
│  Sandbox (代码执行)   │
└──────────────────────┘
```

- **Bot** (`src/`): 薄客户端，处理 Telegram 消息收发、格式化、内联键盘、热加载（工具/处理器）以及 Telegram 工具的执行。热加载的工具代码通过沙盒隔离执行。AI 相关的推理交给 AI Service。
- **AI Service** (`ai-service/`): FastAPI 服务，管理 AI 模型、Agent 循环、工具编排。通过 SSE 流式返回结果。
- **Sandbox** (`sandbox/`): 独立的代码执行沙盒，仅由 Bot 的热加载系统用于隔离执行 AI 提议的工具代码。

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
| `chat.py` | (catch-all) | 非命令消息通过 SSE 发送到 AI Service 进行 AI 对话 |

所有处理器使用 `argparse` 解析子命令和生成帮助信息（`chat.py` 和 `callback.py` 除外）。

## AI 集成

两层架构：

### `ai-service/`（后端）

- `main.py` — FastAPI 服务，管理 AI 模型和 Agent 循环
- 支持 `openai` / `anthropic` / `ai_gateway` 三种 provider
- 依赖 `ai` 模块（`vercel-ai-sdk` 包）
- 通过 SSE 流式返回聊天结果，Tool 调用通过 HTTP 回传分发
- 最大 10 轮 Tool 调用循环，通过 `remote_tools` 标识区分本地/远程工具

### `src/ai/`（Bot 端 Telegram 工具）

- `provider.py` — 模型工厂，根据 `AI_PROVIDER` 配置选择并初始化 AI 模型
- `tools.py` — AI 工具集合（共 34+ 个），分为以下类别：
  - **消息工具** (13): send_message, send_photo, send_document, send_video, send_audio, send_voice, send_sticker, send_animation, send_video_note, send_media_group, send_location, send_dice, send_contact
  - **群管工具** (13): get_chat_info, get_chat_member_count, get_chat_administrators, get_chat_member, ban_chat_member, unban_chat_member, restrict_chat_member, promote_chat_member, pin_message, unpin_message, unpin_all_messages, leave_chat, export_chat_invite_link, set_chat_title, set_chat_description
  - **AI 工具** (3): generate_image, edit_image, propose_new_feature
  - **Bot 管理工具** (5): set_bot_name, set_bot_description, set_bot_short_description, set_bot_photo, delete_bot_photo, get_bot_info
- 敏感操作（ban/unban/promote/unpin_all）使用 `ai.hook()` 的 human-in-the-loop 审批
- `propose_new_feature` 通过 callback 审批后交给 hotloader 注册
- Bot 将工具 schema 发给 AI Service，AI Service 通过 SSE 事件回调 Bot 执行

### `src/ai_service_client.py`

Bot 端 AI Service HTTP 客户端：
- `chat_stream()` — 发送消息并接收 SSE 流，自动处理 `tool_call` 事件回调本地工具，结果回传 AI Service
- `list_models()` — 获取可用模型列表
- 支持可选的 `X-Api-Key` 认证头

## 沙盒服务 (`sandbox/`)

独立的代码执行沙盒服务，运行在 Docker 中：

- `sandbox/main.py` — FastAPI 服务，兼容 `vercel.sandbox` 接口风格
- `sandbox/Dockerfile` — 基于 python:3.14-slim + nodejs
- `src/sandbox_client.py` — 与 bot 集成的客户端（`SandboxClient.create()` / `run_command()` / `stop()`）
- docker-compose 配置: 1 副本, 安全限制 (cap_drop ALL, no-new-privileges, read_only, tmpfs /tmp:64m), 资源限制 (1 CPU, 256MB)

## 热加载 (`src/hotloader.py`)

AI 提议的功能支持热更新，无需重启 bot：

- **速率限制**: 每 chat 每 10 秒最多 3 次操作
- **代码安全检查**: AST 静态分析，阻止危险调用 (`os.system`, `subprocess`, `eval` 等)、危险属性访问 (`__class__`, `__subclasses__`)、危险模块导入 (`socket`, `ctypes`, `subprocess`)
- **工具热加载**: AI 提议的工具代码 (`@ai.tool`) 通过 `exec()` 动态编译注册，在沙盒中隔离执行
- **处理器热加载**: AI 提议的 handler 代码写入 `dynamic/handlers/{chat_id}/{name}.py`，通过 `importlib` 动态导入，注册 chat-scoped Router（带 `F.chat.id == chat_id` 过滤）
- **持久化**: 启动时 `auto_discover()` 扫描 `dynamic/handlers/` 自动加载所有历史动态生成的 handler 文件
- **流程**: `propose_new_feature` → callback 审批 ✅ → `hotloader.register_tool/handler()` → 即时生效

## 配置 (`src/config.py`)

| 变量 | 默认值 | 描述 |
|---|---|---|
| `BOT_TOKEN` | (必填) | Telegram Bot Token |
| `AI_PROVIDER` | `openai` | AI 提供商 (`openai` / `anthropic` / `ai_gateway`) |
| `AI_MODEL_ID` | provider 默认 | 模型 ID 覆盖 |
| `AI_SERVICE_URL` | `http://localhost:8000` | AI Service 地址 |

## 键盘 (`src/keyboards/`)

- `reply.py` — `main_menu_kb()` 回复键盘构建器

## 动态目录 (`dynamic/`)

- `dynamic/handlers/{chat_id}/{name}.py` — 热加载的处理器持久化存储
- `dynamic/handlers/.gitkeep` — 占位文件

## 约定

- `src/` 是 Python 包（src-layout），使用绝对导入: `from src.config import ...`
- 不使用相对导入（如 `from .config`）
- 所有处理器是返回 `None` 的异步函数
- 基于子命令的处理器使用 `argparse` 解析参数和生成帮助文本（`chat.py` 和 `callback.py` 除外）
