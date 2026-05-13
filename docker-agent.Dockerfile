FROM alpine:latest

RUN apk add --no-cache ca-certificates curl && \
    ARCH=$(uname -m); \
    case "$ARCH" in \
      x86_64) ARCH=amd64 ;; \
      aarch64) ARCH=arm64 ;; \
    esac && \
    curl -L "https://github.com/docker/docker-agent/releases/latest/download/docker-agent-linux-${ARCH}" -o /usr/local/bin/docker-agent && \
    chmod +x /usr/local/bin/docker-agent

RUN addgroup -S app && adduser -S app -G app

COPY agent.yaml /app/agent.yaml

RUN mkdir -p /app && chown -R app:app /app

WORKDIR /app

USER app

HEALTHCHECK --start-period=10s --interval=15s --timeout=5s --retries=3 \
  CMD curl -sf http://localhost:8080/api/ping || exit 1

CMD ["docker-agent", "serve", "api", "--listen", "0.0.0.0:8080", "/app/agent.yaml"]
