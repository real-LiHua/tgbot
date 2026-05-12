<div align="center">

# tgbot

[![Python version](https://img.shields.io/badge/Python-3.14-blue?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![aiogram](https://img.shields.io/badge/aiogram-3.x-0088cc?style=flat-square)](https://docs.aiogram.dev)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)

</div>

A modern Telegram bot built with [aiogram 3](https://docs.aiogram.dev), designed for production deployments with Docker, graceful shutdown, health checks, and zero-downtime rolling updates.

> [!NOTE]
> This project uses [uv](https://github.com/astral-sh/uv) for fast Python package management and requires Python 3.14+.

## Features

- **Async-first** — Built on asyncio with aiogram 3.x for non-blocking request handling
- **AI integration** — OpenAI / Anthropic / AI Gateway providers via Vercel AI SDK
- **Agent skills** — Search, view, and manage skills from [skills.sh](https://skills.sh)
- **MCP support** — Connect to MCP servers (HTTP or stdio) to list and use tools
- **Code sandbox** — Isolated code execution service via Docker (with security hardening)
- **Health check endpoint** — Exposes `/health` on port 8080 for container orchestration
- **Graceful shutdown** — Handles SIGTERM/SIGINT signals for clean container termination
- **Docker-ready** — Multi-stage Dockerfile with health checks and Compose deployment
- **Zero-downtime deployments** — Docker Compose config with rolling updates (start-first), parallelism, and rollback

## Getting started

### Prerequisites

- Python 3.14+
- [uv](https://github.com/astral-sh/uv) installed
- A Telegram bot token from [@BotFather](https://t.me/botfather)

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

The Dockerfile uses a [multi-stage build](Dockerfile) with `uv sync --frozen --no-dev` for minimal image size. The container exposes a health check endpoint at `http://localhost:8080/health`.

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
│   ├── __main__.py            # Entry point with bot polling and health check
│   ├── config.py              # Environment configuration
│   ├── sandbox_client.py      # Sandbox service HTTP client
│   ├── ai/
│   │   └── provider.py        # AI model factory (openai/anthropic/ai_gateway)
│   ├── handlers/
│   │   ├── start.py           # /start command
│   │   ├── ping.py            # /ping command
│   │   ├── models.py          # /models command (list AI models)
│   │   ├── skill.py           # /skill command (skills.sh integration)
│   │   └── mcps.py            # /mcps command (MCP server tools)
│   └── keyboards/
│       └── reply.py           # Keyboard builders
├── sandbox/
│   ├── Dockerfile             # Sandbox service Docker image
│   ├── main.py                # FastAPI code execution sandbox
│   └── requirements.txt
├── Dockerfile                 # Bot multi-stage Docker build
├── docker-compose.yml         # Production Compose config
├── pyproject.toml             # Project metadata and dependencies
└── .env.example               # Environment variable template
```

## Configuration

| Variable | Required | Description |
|---|---|---|
| `BOT_TOKEN` | Yes | Telegram bot token from @BotFather |
| `AI_PROVIDER` | No | AI provider: `openai`, `anthropic`, or `ai_gateway` (default: `openai`) |
| `AI_MODEL_ID` | No | Model ID override (default varies by provider) |
| `OPENAI_API_KEY` | No | OpenAI API key |
| `ANTHROPIC_API_KEY` | No | Anthropic API key |
| `AI_GATEWAY_API_KEY` | No | AI Gateway API key |
| `SANDBOX_URL` | No | Sandbox service URL (default: `http://localhost:8080`) |

## Available commands

| Command | Description |
|---|---|
| `/start` | Welcome message |
| `/ping` | Health check — responds with "pong" |
| `/models` | List available AI models from the configured provider |
| `/skill` | Agent skill management (find / info / add / list / init) |
| `/mcps` | MCP server tool management (http / stdio) |

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

Additional command handlers can be added in `src/handlers/`. Create a new router file and include it in `__main__.py`:

```python
from src.handlers.my_handler import router as my_router

dp.include_router(my_router)
```

## Dependencies

- [aiogram](https://docs.aiogram.dev) — Telegram Bot API framework
- [aiohttp](https://docs.aiohttp.org) — HTTP server for health checks
- [vercel-ai-sdk](https://github.com/vercel/ai-sdk-python) — Vercel AI SDK (for AI-powered features)
- [vercel](https://github.com/vercel/vercel) — Vercel Python SDK (sandbox, blob, etc.)
