<div align="center">

# tgbot

[![Python version](https://img.shields.io/badge/Python-3.14-blue?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![aiogram](https://img.shields.io/badge/aiogram-3.x-0088cc?style=flat-square)](https://docs.aiogram.dev)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)

</div>

A modern Telegram bot built with [aiogram 3](https://docs.aiogram.dev), powered by [Docker Agent](https://docker.github.io/docker-agent/) for AI inference and tool orchestration. Designed for production deployments with Docker, graceful shutdown, health checks, and zero-downtime rolling updates.

> [!NOTE]
> This project uses [uv](https://github.com/astral-sh/uv) for fast Python package management and requires Python 3.14+.

## Features

- **Async-first** — Built on asyncio with aiogram 3.x for non-blocking request handling
- **AI integration** — OpenAI / Anthropic / AI Gateway providers via Docker Agent
- **AI chat** — Non-command messages are routed to Docker Agent for intelligent, tool-assisted responses
- **Image generation & editing** — Generate and edit images via built-in AI tools
- **Agent skills** — Search, view, and manage skills from [skills.sh](https://skills.sh)
- **MCP support** — Connect to MCP servers (HTTP or stdio) to list and use tools
- **Hot reload** — Dynamically register AI-proposed tools and handlers without restarting the bot
- **Code sandbox** — Isolated code execution via Docker (with security hardening) for hot-loaded tool safety
- **Health check endpoint** — Exposes `/health` on port 8080 for container orchestration
- **Graceful shutdown** — Handles SIGTERM/SIGINT signals for clean container termination
- **Docker-ready** — Multi-stage Dockerfile with health checks and Compose deployment
- **Zero-downtime deployments** — Docker Compose config with rolling updates (start-first), parallelism, and rollback

## Architecture

```
┌──────────────────┐   SSE stream       ┌──────────────────────────┐
│  Bot (thin       │ ◄──────────────►   │  Docker Agent API Server │
│  client)         │  POST /api/sessions│                          │
│                  │  /:id/agent/agent  │  - AI model inference    │
│  - Telegram I/O  │                    │  - Agent loop            │
│  - Formatting    │                    │  - Session persistence   │
│  - Inline        │                    │  - Tool orchestration    │
│    keyboards     │                    └──────────┬───────────────┘
│  - Hot reload    │                               │ HTTP (tool calls)
│  - Sandbox       │                               ▼
│  - Tool HTTP API │                  ┌──────────────────────┐
│    (/api/tools/) │◄─────────────────│  Bot Tool HTTP Server  │
└──────────────────┘                  │  POST /api/tools/{name}│
                                      └──────────────────────┘
```

Docker Agent manages AI sessions and tool orchestration. When it needs to call a Telegram API method, it uses its OpenAPI tool to POST to the Bot's tool server, which executes the actual Telegram Bot API call.

## Getting started

### Prerequisites

- Python 3.14+
- [uv](https://github.com/astral-sh/uv) installed
- A Telegram bot token from [@BotFather](https://t.me/botfather)
- [Docker Agent](https://docker.github.io/docker-agent/) binary (for local development without Docker)

### Installation

```bash
# Clone the repository
git clone https://github.com/real-LiHua/tgbot.git
cd tgbot

# Create environment and install dependencies
uv sync

# Configure your bot token
cp .env.example .env
# Edit .env and set your BOT_TOKEN
```

### Run the bot

```bash
# Start Docker Agent first
docker-agent serve api agent.yaml &

# Then start the bot
uv run python -m src
```

## Docker

### Build and run

```bash
docker compose up --build -d
```

### Sandbox service only

```bash
docker compose up --build -d sandbox
```

### Deployment configuration

The [docker-compose.yml](docker-compose.yml) includes production-ready settings:

- **2 replicas** for high availability
- **Rolling updates** with `start-first` order (zero-downtime)
- **Rollback on failure** with `stop-first` strategy
- **60s grace period** for clean shutdown

## Project structure

```
.
├── src/
│   ├── __init__.py
│   ├── __main__.py            # Entry point: HTTP server + bot polling
│   ├── config.py              # Environment configuration
│   ├── sandbox_client.py      # Sandbox service HTTP client
│   ├── ai/
│   │   ├── provider.py        # AI model factory (for image generation tools)
│   │   ├── tools.py           # AI tool definitions (34+ Telegram tools)
│   │   └── tool_server.py     # OpenAPI spec + tool execution HTTP endpoints
│   ├── handlers/
│   │   ├── start.py           # /start command
│   │   ├── ping.py            # /ping command
│   │   ├── models.py          # /models command (list AI models)
│   │   ├── skill.py           # /skill command (skills.sh integration)
│   │   ├── mcps.py            # /mcps command (MCP server tools)
│   │   ├── chat.py            # (catch-all) AI chat handler via SSE
│   │   └── callback.py        # Inline keyboard callback handler
│   ├── keyboards/
│   │   └── reply.py           # Keyboard builders
│   ├── ai_service_client.py   # Docker Agent SSE client
│   ├── hotloader.py           # Hot-reload system for dynamic tools/handlers
│   └── sandbox_client.py      # Sandbox service HTTP client
├── sandbox/
│   ├── Dockerfile             # Sandbox service Docker image
│   ├── main.py                # FastAPI code execution sandbox
│   └── requirements.txt
├── agent.yaml                 # Docker Agent configuration
├── docker-agent.Dockerfile    # Docker Agent Docker image
├── dynamic/
│   └── handlers/              # Hot-loaded handler persistence
├── Dockerfile                 # Bot multi-stage Docker build
├── docker-compose.yml         # Production Compose config
├── pyproject.toml             # Project metadata and dependencies
└── .env.example               # Environment variable template
```

## Configuration

| Variable | Required | Description |
|---|---|---|
| `BOT_TOKEN` | Yes | Telegram bot token from @BotFather |
| `DOCKER_AGENT_URL` | No | Docker Agent URL (default: `http://localhost:8080`) |
| `AI_PROVIDER` | No | AI provider for image generation: `openai`, `anthropic`, or `ai_gateway` (default: `openai`) |
| `AI_MODEL_ID` | No | Model ID override for image generation (default varies by provider) |
| `OPENAI_API_KEY` | No | OpenAI API key (for both Docker Agent and image generation) |
| `ANTHROPIC_API_KEY` | No | Anthropic API key |
| `AI_GATEWAY_API_KEY` | No | AI Gateway API key |
| `SANDBOX_URL` | No | Sandbox service URL (default: `http://localhost:8080`) |
| `SANDBOX_API_KEY` | No | API key for Sandbox authentication |

## Available commands

| Command | Description |
|---|---|
| `/start` | Welcome message |
| `/ping` | Health check — responds with "pong" |
| `/models` | List available AI models from Docker Agent |
| `/skill` | Agent skill management (find / info / add / list / init) |
| `/mcps` | MCP server tool management (http / stdio) |

Non-command messages are automatically handled by the **AI chat** system — routed via SSE to Docker Agent for intelligent, tool-assisted conversation.

### /skill subcommands

| Subcommand | Description |
|---|---|
| `/skill find <query>` | Search skills from skills.sh |
| `/skill info <source/slug>` | View skill details and SKILL.md content |
| `/skill add <source/slug>` | Fetch skill content |
| `/skill list` | Trending skills leaderboard |
| `/skill init <name>` | Generate a SKILL.md template |

### /mcps subcommands

| Subcommand | Description |
|---|---|
| `/mcps http <url>` | Connect to an HTTP MCP server and list tools |
| `/mcps stdio <cmd> [args...]` | Start a stdio MCP process and list tools |

## Sandbox service

The sandbox service provides isolated code execution in a Docker container:

```
POST /create              Create a new sandbox session
POST /run                 Run a command in a sandbox
POST /read                Read a file from a sandbox
POST /write               Write files to a sandbox
POST /stop/{sandbox_id}   Stop and clean up a sandbox
```

Security features: `cap_drop: ALL`, `no-new-privileges`, read-only filesystem with tmpfs (`/tmp`), resource limits (1 CPU / 256MB / 60s timeout), and non-root user.

## Extending

### Static handlers

Additional command handlers can be added in `src/handlers/`. Create a new router file and include it in `__main__.py`:

```python
from src.handlers.my_handler import router as my_router

dp.include_router(my_router)
```

### Dynamic hot-loading

The bot supports **hot-loading** AI-proposed features without restarting. The AI agent can propose new tools (`@ai.tool`) or handlers (`Router`) via the `propose_new_feature` tool, which submits them for admin approval through an inline keyboard callback. Once approved, they are registered immediately:

- **Tools** are compiled via `exec()` and executed inside the Docker sandbox for isolation
- **Handlers** are written to `dynamic/handlers/{chat_id}/{name}.py`, imported dynamically, and registered with a `F.chat.id == chat_id` filter

Hot-loaded handlers persist across bot restarts via `auto_discover()` on startup.

## Dependencies

- [aiogram](https://docs.aiogram.dev) — Telegram Bot API framework
- [python-dotenv](https://github.com/theskumar/python-dotenv) — Environment variable loading
- [aiohttp](https://docs.aiohttp.org) — HTTP server (tool API, health check)
- [httpx](https://www.python-httpx.org) — HTTP client (Docker Agent sessions, SSE streaming)
- [vercel-ai-sdk](https://github.com/vercel/ai-sdk-python) — Tool definitions, hooks, and image generation (bot-side)
