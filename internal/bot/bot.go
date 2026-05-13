package bot

import (
	"context"
	"fmt"
	"log"
	"time"

	"github.com/celestix/gotgproto"
	"github.com/celestix/gotgproto/sessionMaker"
	"github.com/glebarez/sqlite"

	"github.com/real-LiHua/tgbot/internal/ai"
	"github.com/real-LiHua/tgbot/internal/config"
	"github.com/real-LiHua/tgbot/internal/sandbox"
	"github.com/real-LiHua/tgbot/internal/tools"
)

type Bot struct {
	cfg        *config.Config
	client     *gotgproto.Client
	aiClient   *ai.Client
	sandboxCli *sandbox.Client
	mcpServer  *tools.MCPServer
}

func New(cfg *config.Config) *Bot {
	return &Bot{
		cfg:        cfg,
		aiClient:   ai.NewClient(cfg),
		sandboxCli: sandbox.NewClient(cfg),
		mcpServer:  tools.NewMCPServer(cfg),
	}
}

func (b *Bot) Start(ctx context.Context) error {
	client, err := gotgproto.NewClient(
		b.cfg.AppID,
		b.cfg.APIHash,
		gotgproto.ClientTypeBot(b.cfg.BotToken),
		&gotgproto.ClientOpts{
			Session: sessionMaker.SqlSession(sqlite.Open("bot_session")),
		},
	)
	if err != nil {
		return fmt.Errorf("create gotgproto client: %w", err)
	}
	b.client = client

	telegramActions := tools.NewTelegramActions(client.CreateContext())
	b.mcpServer.SetActions(telegramActions)

	b.registerHandlers()

	return nil
}

func (b *Bot) Wait() {
	if b.client != nil {
		b.client.Idle()
	}
}

func (b *Bot) Run(ctx context.Context) error {
	log.Printf("starting MCP HTTP server on %s", b.cfg.ListenAddr)
	if err := b.mcpServer.Start(ctx, b.cfg.ListenAddr); err != nil {
		return fmt.Errorf("MCP server error: %w", err)
	}
	return nil
}

func (b *Bot) Shutdown() {
	if b.mcpServer != nil {
		ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
		defer cancel()
		b.mcpServer.Shutdown(ctx)
	}
}
