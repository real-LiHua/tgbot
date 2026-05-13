package bot

import (
	"fmt"
	"log"
	"strings"

	"github.com/celestix/gotgproto/dispatcher/handlers"
	"github.com/celestix/gotgproto/dispatcher/handlers/filters"
	"github.com/celestix/gotgproto/ext"
	"github.com/gotd/td/tg"
)

func (b *Bot) registerHandlers() {
	d := b.client.Dispatcher

	d.AddHandler(handlers.NewCommand("start", b.handleStart))
	d.AddHandler(handlers.NewCommand("ping", b.handlePing))
	d.AddHandler(handlers.NewCommand("models", b.handleModels))
	d.AddHandler(handlers.NewCommand("skill", b.handleSkill))

	d.AddHandler(handlers.NewCallbackQuery(filters.CallbackQuery.Prefix("feature:"), b.handleFeatureCallback))

	d.AddHandler(handlers.NewMessage(filters.Message.Text, b.handleChat))
}

func (b *Bot) handleStart(ctx *ext.Context, update *ext.Update) error {
	user := update.EffectiveUser()
	_, err := ctx.Reply(update, ext.ReplyTextString(
		fmt.Sprintf("Hello %s! Welcome to the bot.\n\nCommands:\n/ping - Health check\n/models - List AI models\n/skill - Manage skills",
			user.FirstName),
	), nil)
	return err
}

func (b *Bot) handlePing(ctx *ext.Context, update *ext.Update) error {
	_, err := ctx.Reply(update, ext.ReplyTextString("pong"), nil)
	return err
}

func (b *Bot) handleModels(ctx *ext.Context, update *ext.Update) error {
	models, err := b.aiClient.ListModels()
	if err != nil {
		_, replyErr := ctx.Reply(update, ext.ReplyTextString(fmt.Sprintf("Error: %v", err)), nil)
		return replyErr
	}
	_, replyErr := ctx.Reply(update, ext.ReplyTextString(
		fmt.Sprintf("Available models:\n%s", strings.Join(models, "\n")),
	), nil)
	return replyErr
}

func (b *Bot) handleSkill(ctx *ext.Context, update *ext.Update) error {
	msg := update.EffectiveMessage
	args := strings.Fields(msg.Text)
	if len(args) < 2 {
		_, err := ctx.Reply(update, ext.ReplyTextString(
			"Usage:\n/skill find <query>\n/skill list\n/skill info <name>\n/skill add <url>",
		), nil)
		return err
	}
	sub := args[1]
	switch sub {
	case "list":
		_, err := ctx.Reply(update, ext.ReplyTextString("skills.sh integration not yet implemented"), nil)
		return err
	default:
		_, err := ctx.Reply(update, ext.ReplyTextString(fmt.Sprintf("Unknown subcommand: %s", sub)), nil)
		return err
	}
}

func (b *Bot) handleFeatureCallback(ctx *ext.Context, update *ext.Update) error {
	query := update.CallbackQuery
	data := string(query.Data)
	log.Printf("callback: %s", data)

	answer := &tg.MessagesSetBotCallbackAnswerRequest{
		QueryID: query.QueryID,
		Message: "Callback received",
	}
	_, err := ctx.AnswerCallback(answer)
	return err
}

func (b *Bot) handleChat(ctx *ext.Context, update *ext.Update) error {
	msg := update.EffectiveMessage
	if msg.Text == "" || strings.HasPrefix(msg.Text, "/") {
		return nil
	}

	var chatID int64
	switch peer := msg.PeerID.(type) {
	case *tg.PeerUser:
		chatID = peer.UserID
	case *tg.PeerChat:
		chatID = peer.ChatID
	case *tg.PeerChannel:
		chatID = peer.ChannelID
	default:
		return nil
	}

	sent, err := ctx.Reply(update, ext.ReplyTextString("..."), nil)
	if err != nil {
		return err
	}

	messages := []map[string]any{
		{"role": "user", "content": msg.Text},
	}

	full := ""
	ch, err := b.aiClient.ChatStream(messages, chatID)
	if err != nil {
		ctx.EditMessage(chatID, &tg.MessagesEditMessageRequest{
			ID:      sent.ID,
			Message: fmt.Sprintf("Error: %v", err),
		})
		return nil
	}

	for event := range ch {
		if event.Type == "done" {
			break
		}
		if event.Type == "delta" {
			full += event.Text
			if len(full) < 4000 {
				ctx.EditMessage(chatID, &tg.MessagesEditMessageRequest{
					ID:      sent.ID,
					Message: full,
				})
			}
		}
	}

	if full != "" {
		parts := splitMessage(full, 4000)
		ctx.EditMessage(chatID, &tg.MessagesEditMessageRequest{
			ID:      sent.ID,
			Message: parts[0],
		})
		for _, p := range parts[1:] {
			ctx.SendMessage(chatID, &tg.MessagesSendMessageRequest{
				Message: p,
			})
		}
	}
	return nil
}

func splitMessage(text string, limit int) []string {
	var parts []string
	for len(text) > 0 {
		if len(text) <= limit {
			parts = append(parts, text)
			break
		}
		parts = append(parts, text[:limit])
		text = text[limit:]
	}
	return parts
}
