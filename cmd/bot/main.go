package main

import (
	"context"
	"log"
	"os"
	"os/signal"
	"syscall"

	"github.com/real-LiHua/tgbot/internal/bot"
	"github.com/real-LiHua/tgbot/internal/config"
)

func main() {
	cfg := config.Load()
	if cfg.AppID == 0 || cfg.APIHash == "" || cfg.BotToken == "" {
		log.Fatal("APP_ID, API_HASH, and BOT_TOKEN must be set")
	}

	b := bot.New(cfg)
	ctx, cancel := context.WithCancel(context.Background())
	defer cancel()

	if err := b.Start(ctx); err != nil {
		log.Fatalf("failed to start bot: %v", err)
	}

	// Start MCP/HTTP server in background
	go func() {
		log.Printf("starting server on %s", cfg.ListenAddr)
		if err := b.Run(ctx); err != nil {
			log.Printf("server error: %v", err)
			cancel()
		}
	}()

	// Handle shutdown signals
	sigCh := make(chan os.Signal, 1)
	signal.Notify(sigCh, syscall.SIGTERM, syscall.SIGINT)
	go func() {
		<-sigCh
		log.Println("shutting down...")
		b.Shutdown()
		cancel()
	}()

	log.Println("bot started, waiting for messages...")
	b.Wait()
}
