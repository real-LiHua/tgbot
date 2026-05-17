#!/bin/bash
set -euo pipefail

# ─── tgbot Podman Deployment ──────────────────────────────────
# Two modes:
#   1. Compose  — podman-compose up (simple, dev)
#   2. Quadlet  — systemd-integrated (production)
#
# Usage: ./pod/podman-deploy.sh [compose|quadlet|build|clean|status|logs]
# ───────────────────────────────────────────────────────────────

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
QUADLET_DIR="${XDG_CONFIG_HOME:-$HOME/.config}/containers/systemd"
ENV_FILE="$PROJECT_DIR/.env"
COMPOSE_FILE="$PROJECT_DIR/podman-compose.yml"

cmd=${1:-compose}

ensure_env() {
  if [ ! -f "$ENV_FILE" ]; then
    echo "ERROR: .env file not found at $ENV_FILE"
    echo "Copy from .env.example: cp .env.example .env"
    exit 1
  fi
}

build_images() {
  echo "==> Building images..."
  podman build -t localhost/tgbot-bot:latest -f "$PROJECT_DIR/Dockerfile" "$PROJECT_DIR"
  podman build -t localhost/tgbot-docker-agent:latest -f "$PROJECT_DIR/docker-agent.Dockerfile" "$PROJECT_DIR"
  podman build -t localhost/tgbot-sandbox:latest -f "$PROJECT_DIR/sandbox/Dockerfile" "$PROJECT_DIR/sandbox"
  echo "==> All images built"
}

## ─── Compose mode ─────────────────────────────────────────

compose_up() {
  ensure_env
  build_images
  echo "==> Starting services (podman-compose)..."
  cd "$PROJECT_DIR"
  podman-compose -f "$COMPOSE_FILE" up -d
}

compose_down() {
  cd "$PROJECT_DIR"
  podman-compose -f "$COMPOSE_FILE" down
}

compose_logs() {
  cd "$PROJECT_DIR"
  podman-compose -f "$COMPOSE_FILE" logs -f
}

## ─── Quadlet mode ─────────────────────────────────────────

quadlet_install() {
  ensure_env
  build_images

  mkdir -p "$QUADLET_DIR"

  # Copy Quadlet files (network, volume, containers)
  cp "$SCRIPT_DIR"/*.network "$QUADLET_DIR/" 2>/dev/null || true
  cp "$SCRIPT_DIR"/*.volume "$QUADLET_DIR/" 2>/dev/null || true
  cp "$SCRIPT_DIR"/*.container "$QUADLET_DIR/" 2>/dev/null || true

  # Symlink .env into the expected location
  ENV_LINK="$QUADLET_DIR/.env"
  if [ ! -f "$ENV_LINK" ]; then
    ln -sf "$ENV_FILE" "$ENV_LINK"
  fi

  echo "==> Quadlet files installed to $QUADLET_DIR"
  echo "==> Reloading systemd..."
  systemctl --user daemon-reload
}

quadlet_start() {
  quadlet_install
  echo "==> Starting tgbot services..."
  systemctl --user start tgbot-docker-agent.service
  systemctl --user start tgbot-sandbox.service
  systemctl --user start tgbot-new-api.service
  systemctl --user start tgbot-bot.service
}

quadlet_stop() {
  systemctl --user stop tgbot-bot.service 2>/dev/null || true
  systemctl --user stop tgbot-docker-agent.service 2>/dev/null || true
  systemctl --user stop tgbot-sandbox.service 2>/dev/null || true
  systemctl --user stop tgbot-new-api.service 2>/dev/null || true
}

quadlet_enable() {
  quadlet_start
  systemctl --user enable tgbot-docker-agent.service
  systemctl --user enable tgbot-sandbox.service
  systemctl --user enable tgbot-new-api.service
  systemctl --user enable tgbot-bot.service
}

quadlet_logs() {
  local service="${2:-}"
  if [ -n "$service" ]; then
    journalctl --user -fu "tgbot-${service}.service"
  else
    journalctl --user -fu tgbot-bot.service
  fi
}

## ─── Common ───────────────────────────────────────────────

status() {
  echo "=== podman ps ==="
  podman ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
  echo ""
  echo "=== podman images ==="
  podman images --format "table {{.Repository}}:{{.Tag}}\t{{.Size}}" | head -5
}

clean() {
  echo "==> Removing all tgbot containers..."
  podman rm -f tgbot-bot tgbot-docker-agent tgbot-sandbox tgbot-new-api 2>/dev/null || true
  echo "==> Removing tgbot images..."
  podman rmi localhost/tgbot-bot:latest localhost/tgbot-docker-agent:latest localhost/tgbot-sandbox:latest 2>/dev/null || true
}

## ─── Main ─────────────────────────────────────────────────

case "$cmd" in
  compose)
    compose_up
    ;;
  down)
    compose_down
    ;;
  quadlet)
    quadlet_start
    ;;
  enable)
    quadlet_enable
    ;;
  stop)
    quadlet_stop
    ;;
  build)
    build_images
    ;;
  clean)
    clean
    ;;
  status)
    status
    ;;
  logs)
    compose_logs
    ;;
  *)
    echo "Usage: $0 [compose|down|quadlet|enable|stop|build|clean|status|logs]"
    echo ""
    echo "  compose   — Build & start with podman-compose (default)"
    echo "  down      — podman-compose down"
    echo "  quadlet   — Install Quadlet files & start systemd services"
    echo "  enable    — Quadlet mode + enable on boot"
    echo "  stop      — Stop Quadlet services"
    echo "  build     — Build all container images"
    echo "  clean     — Remove all tgbot containers & images"
    echo "  status    — Show running containers"
    echo "  logs      — Follow compose logs"
    ;;
esac
