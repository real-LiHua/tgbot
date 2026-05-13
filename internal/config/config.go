package config

import (
	"os"
	"strconv"
)

type Config struct {
	AppID          int
	APIHash        string
	BotToken       string
	AIProvider     string
	AIModelID      string
	DockerAgentURL string
	BotToolAPIKey  string
	SandboxURL     string
	SandboxAPIKey  string
	ListenAddr     string
}

func Load() *Config {
	return &Config{
		AppID:          getEnvInt("APP_ID", 0),
		APIHash:        os.Getenv("API_HASH"),
		BotToken:       os.Getenv("BOT_TOKEN"),
		AIProvider:     getEnv("AI_PROVIDER", "openai"),
		AIModelID:      os.Getenv("AI_MODEL_ID"),
		DockerAgentURL: getEnv("DOCKER_AGENT_URL", "http://localhost:8080"),
		BotToolAPIKey:  os.Getenv("BOT_TOOL_API_KEY"),
		SandboxURL:     getEnv("SANDBOX_URL", "http://localhost:8080"),
		SandboxAPIKey:  os.Getenv("SANDBOX_API_KEY"),
		ListenAddr:     getEnv("LISTEN_ADDR", "0.0.0.0:8080"),
	}
}

func getEnv(key, def string) string {
	if v := os.Getenv(key); v != "" {
		return v
	}
	return def
}

func getEnvInt(key string, def int) int {
	if v := os.Getenv(key); v != "" {
		if n, err := strconv.Atoi(v); err == nil {
			return n
		}
	}
	return def
}
