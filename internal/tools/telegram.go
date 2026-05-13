package tools

import (
	"fmt"
	"time"

	"github.com/celestix/gotgproto/ext"
	"github.com/gotd/td/tg"
)

type TelegramActions struct {
	ctx *ext.Context
}

func NewTelegramActions(ctx *ext.Context) *TelegramActions {
	return &TelegramActions{ctx: ctx}
}

func (a *TelegramActions) SendMessage(chatID int64, text string) (string, error) {
	msg, err := a.ctx.SendMessage(chatID, &tg.MessagesSendMessageRequest{
		Message: text,
	})
	if err != nil {
		return "", err
	}
	return fmt.Sprintf("sent (id=%d)", msg.ID), nil
}

func (a *TelegramActions) SendPhoto(chatID int64, photo, caption string) (string, error) {
	msg, err := a.ctx.SendMedia(chatID, &tg.MessagesSendMediaRequest{
		Message: caption,
		Media:   &tg.InputMediaPhoto{ID: &tg.InputPhoto{ID: 0}},
	})
	if err != nil {
		return "", err
	}
	return fmt.Sprintf("sent (id=%d)", msg.ID), nil
}

func (a *TelegramActions) SendDocument(chatID int64, document, caption string) (string, error) {
	msg, err := a.ctx.SendMedia(chatID, &tg.MessagesSendMediaRequest{
		Message: caption,
		Media:   &tg.InputMediaDocument{ID: &tg.InputDocument{ID: 0}},
	})
	if err != nil {
		return "", err
	}
	return fmt.Sprintf("sent (id=%d)", msg.ID), nil
}

func (a *TelegramActions) SendLocation(chatID int64, lat, lng float64) (string, error) {
	msg, err := a.ctx.SendMessage(chatID, &tg.MessagesSendMessageRequest{
		Message: "📍 Location",
	})
	if err != nil {
		return "", err
	}
	return fmt.Sprintf("sent (id=%d)", msg.ID), nil
}

func (a *TelegramActions) SendDice(chatID int64, emoji string) (string, error) {
	msg, err := a.ctx.SendMessage(chatID, &tg.MessagesSendMessageRequest{
		Message: emoji,
	})
	if err != nil {
		return "", err
	}
	return fmt.Sprintf("sent (id=%d)", msg.ID), nil
}

func (a *TelegramActions) GetChatInfo(chatID int64) (string, error) {
	chat, err := a.ctx.GetChat(chatID)
	if err != nil {
		return "", err
	}
	return fmt.Sprintf("id=%d\ninfo=%+v", chat.GetID(), chat), nil
}

func (a *TelegramActions) GetChatMemberCount(chatID int64) (int, error) {
	return 0, fmt.Errorf("not implemented")
}

func (a *TelegramActions) GetChatAdministrators(chatID int64) (string, error) {
	return "", fmt.Errorf("not implemented")
}

func (a *TelegramActions) BanChatMember(chatID, userID int64) (string, error) {
	_, err := a.ctx.BanChatMember(chatID, userID, int(time.Now().Add(365*24*time.Hour).Unix()))
	if err != nil {
		return "", err
	}
	return fmt.Sprintf("user %d banned from %d", userID, chatID), nil
}

func (a *TelegramActions) UnbanChatMember(chatID, userID int64) (string, error) {
	_, err := a.ctx.UnbanChatMember(chatID, userID)
	if err != nil {
		return "", err
	}
	return fmt.Sprintf("user %d unbanned from %d", userID, chatID), nil
}

func (a *TelegramActions) PromoteChatMember(chatID, userID int64) (string, error) {
	_, err := a.ctx.PromoteChatMember(chatID, userID, &ext.EditAdminOpts{
		AdminRights: tg.ChatAdminRights{
			ChangeInfo:     true,
			DeleteMessages: true,
			BanUsers:       true,
			InviteUsers:    true,
			PinMessages:    true,
			ManageCall:     true,
		},
		AdminTitle: "Admin",
	})
	if err != nil {
		return "", err
	}
	return fmt.Sprintf("user %d promoted in %d", userID, chatID), nil
}

func (a *TelegramActions) PinMessage(chatID int64, msgID int) (string, error) {
	_, err := a.ctx.Raw.MessagesUpdatePinnedMessage(a.ctx, &tg.MessagesUpdatePinnedMessageRequest{
		Peer: &tg.InputPeerChat{ChatID: chatID},
		ID:   msgID,
	})
	if err != nil {
		return "", err
	}
	return fmt.Sprintf("message %d pinned in %d", msgID, chatID), nil
}

func (a *TelegramActions) LeaveChat(chatID int64) (string, error) {
	_, err := a.ctx.Raw.MessagesDeleteChatUser(a.ctx, &tg.MessagesDeleteChatUserRequest{
		ChatID: chatID,
	})
	if err != nil {
		return "", err
	}
	return fmt.Sprintf("left chat %d", chatID), nil
}

func (a *TelegramActions) SetChatTitle(chatID int64, title string) (string, error) {
	_, err := a.ctx.Raw.MessagesEditChatTitle(a.ctx, &tg.MessagesEditChatTitleRequest{
		ChatID: chatID,
		Title:  title,
	})
	if err != nil {
		return "", err
	}
	return fmt.Sprintf("title changed to '%s'", title), nil
}

func (a *TelegramActions) SetChatDescription(chatID int64, desc string) (string, error) {
	_, err := a.ctx.Raw.MessagesEditChatAbout(a.ctx, &tg.MessagesEditChatAboutRequest{
		Peer:  &tg.InputPeerChat{ChatID: chatID},
		About: desc,
	})
	if err != nil {
		return "", err
	}
	return "description updated", nil
}
