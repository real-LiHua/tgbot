import base64
from collections.abc import Sequence
from typing import Any

import ai
from aiogram import Bot

from src.ai.provider import get_model
from src.handlers.callback import add_pending, make_fid, approve_kb
from src.hotloader import get_dynamic_tools
from aiogram.types import BufferedInputFile, ChatPermissions, InputMediaPhoto, InputMediaVideo
from aiogram.utils.formatting import Bold, Pre, Text, as_list


def make_telegram_tools(bot: Bot, chat_id: int | None = None) -> Sequence[ai.Tool[..., Any]]:
    """Create AI tools wrapping Telegram Bot API operations."""

    @ai.tool
    async def send_message(chat_id: str, text: str) -> str:
        """Send a text message to a chat or group."""
        msg = await bot.send_message(chat_id=int(chat_id), text=text)
        return f"sent (id={msg.message_id})"

    @ai.tool
    async def send_photo(chat_id: str, photo: str, caption: str = "") -> str:
        """Send a photo to a chat or group. Accepts a URL or file_id."""
        msg = await bot.send_photo(chat_id=int(chat_id), photo=photo, caption=caption or None)
        return f"sent (id={msg.message_id})"

    @ai.tool
    async def send_document(chat_id: str, document: str, caption: str = "") -> str:
        """Send a document/file to a chat or group. Accepts a URL or file_id."""
        msg = await bot.send_document(chat_id=int(chat_id), document=document, caption=caption or None)
        return f"sent (id={msg.message_id})"

    @ai.tool
    async def send_video(chat_id: str, video: str, caption: str = "") -> str:
        """Send a video to a chat or group. Accepts a URL or file_id."""
        msg = await bot.send_video(chat_id=int(chat_id), video=video, caption=caption or None)
        return f"sent (id={msg.message_id})"

    @ai.tool
    async def send_audio(chat_id: str, audio: str, caption: str = "") -> str:
        """Send an audio file to a chat or group. Accepts a URL or file_id."""
        msg = await bot.send_audio(chat_id=int(chat_id), audio=audio, caption=caption or None)
        return f"sent (id={msg.message_id})"

    @ai.tool
    async def send_voice(chat_id: str, voice: str, caption: str = "") -> str:
        """Send a voice message to a chat or group. Accepts a URL or file_id (must be an OGG file)."""
        msg = await bot.send_voice(chat_id=int(chat_id), voice=voice, caption=caption or None)
        return f"sent (id={msg.message_id})"

    @ai.tool
    async def send_sticker(chat_id: str, sticker: str) -> str:
        """Send a sticker to a chat or group. Accepts a file_id."""
        msg = await bot.send_sticker(chat_id=int(chat_id), sticker=sticker)
        return f"sent (id={msg.message_id})"

    @ai.tool
    async def send_animation(chat_id: str, animation: str, caption: str = "") -> str:
        """Send an animation (GIF) to a chat or group. Accepts a URL or file_id."""
        msg = await bot.send_animation(chat_id=int(chat_id), animation=animation, caption=caption or None)
        return f"sent (id={msg.message_id})"

    @ai.tool
    async def send_video_note(chat_id: str, video_note: str) -> str:
        """Send a video note (round video) to a chat or group. Accepts a URL or file_id."""
        msg = await bot.send_video_note(chat_id=int(chat_id), video_note=video_note)
        return f"sent (id={msg.message_id})"

    @ai.tool
    async def send_media_group(chat_id: str, media_type: str = "photo", urls: str = "", captions: str = "") -> str:
        """Send an album of 2-10 media items. media_type: 'photo' or 'video'. urls: comma-separated. captions: comma-separated (optional)."""
        url_list = [u.strip() for u in urls.split(",") if u.strip()]
        cap_list = [c.strip() for c in captions.split(",")] if captions else []
        if not url_list:
            return "no urls provided"
        media = []
        for i, url in enumerate(url_list):
            cap = cap_list[i] if i < len(cap_list) else None
            if media_type == "video":
                media.append(InputMediaVideo(media=url, caption=cap))
            else:
                media.append(InputMediaPhoto(media=url, caption=cap))
        msgs = await bot.send_media_group(chat_id=int(chat_id), media=media)
        return f"sent {len(msgs)} items"

    @ai.tool
    async def send_location(chat_id: str, latitude: float, longitude: float) -> str:
        """Send a location pin to a chat or group."""
        msg = await bot.send_location(chat_id=int(chat_id), latitude=latitude, longitude=longitude)
        return f"sent (id={msg.message_id})"

    @ai.tool
    async def send_dice(chat_id: str, emoji: str = "🎲") -> str:
        """Send a dice with random value. emoji: 🎲, 🎯, 🏀, ⚽, 🎳, 🎰."""
        msg = await bot.send_dice(chat_id=int(chat_id), emoji=emoji)
        return f"sent value={msg.dice.value} (id={msg.message_id})"

    @ai.tool
    async def send_contact(chat_id: str, phone_number: str, first_name: str, last_name: str = "") -> str:
        """Send a phone contact to a chat or group."""
        msg = await bot.send_contact(
            chat_id=int(chat_id), phone_number=phone_number, first_name=first_name, last_name=last_name or None
        )
        return f"sent (id={msg.message_id})"

    @ai.tool
    async def get_chat_info(chat_id: str) -> str:
        """Get detailed information about a chat or group."""
        chat = await bot.get_chat(chat_id=int(chat_id))
        return (
            f"id={chat.id}\ntype={chat.type}\ntitle={chat.title or ''}\n"
            f"username={chat.username or ''}\ndescription={chat.description or ''}\n"
            f"member_count={chat.full_member_count if hasattr(chat, 'full_member_count') else 'N/A'}"
        )

    @ai.tool
    async def get_chat_member_count(chat_id: str) -> int:
        """Get the number of members in a chat or group."""
        return await bot.get_chat_member_count(chat_id=int(chat_id))

    @ai.tool
    async def get_chat_administrators(chat_id: str) -> str:
        """Get the list of administrators in a chat or group."""
        admins = await bot.get_chat_administrators(chat_id=int(chat_id))
        lines = [f"{m.user.id} @{m.user.username or ''} {m.user.full_name}" for m in admins]
        return "\n".join(lines)

    @ai.tool
    async def get_chat_member(chat_id: str, user_id: str) -> str:
        """Get information about a specific member in a chat."""
        m = await bot.get_chat_member(chat_id=int(chat_id), user_id=int(user_id))
        return (
            f"user_id={m.user.id}\nusername=@{m.user.username or ''}\n"
            f"name={m.user.full_name}\nstatus={m.status}"
        )

    @ai.tool
    async def ban_chat_member(chat_id: str, user_id: str, revoke_messages: bool = False) -> str:
        """Ban a user from a chat or group. Requires admin approval."""
        approval = await ai.hook(
            f"ban_{chat_id}_{user_id}",
            payload=ai.ToolApproval,
            metadata={"tool": "ban_chat_member", "chat_id": chat_id, "user_id": user_id},
        )
        if not approval.granted:
            return f"cancelled: {approval.reason or 'denied'}"
        await bot.ban_chat_member(
            chat_id=int(chat_id), user_id=int(user_id), revoke_messages=revoke_messages
        )
        return f"user {user_id} banned from {chat_id}"

    @ai.tool
    async def unban_chat_member(chat_id: str, user_id: str) -> str:
        """Unban a user from a chat or group. Requires admin approval."""
        approval = await ai.hook(
            f"unban_{chat_id}_{user_id}",
            payload=ai.ToolApproval,
            metadata={"tool": "unban_chat_member", "chat_id": chat_id, "user_id": user_id},
        )
        if not approval.granted:
            return f"cancelled: {approval.reason or 'denied'}"
        await bot.unban_chat_member(chat_id=int(chat_id), user_id=int(user_id))
        return f"user {user_id} unbanned from {chat_id}"

    @ai.tool
    async def restrict_chat_member(
        chat_id: str,
        user_id: str,
        can_send_messages: bool = True,
        can_send_media: bool = True,
        can_send_polls: bool = False,
    ) -> str:
        """Restrict permissions of a user in a supergroup. Admin permission required."""
        perms = ChatPermissions(
            can_send_messages=can_send_messages,
            can_send_media_messages=can_send_media,
            can_send_polls=can_send_polls,
            can_add_web_page_previews=True,
            can_change_info=False,
            can_invite_users=False,
            can_pin_messages=False,
        )
        await bot.restrict_chat_member(
            chat_id=int(chat_id), user_id=int(user_id), permissions=perms
        )
        return f"user {user_id} restricted in {chat_id}"

    @ai.tool
    async def promote_chat_member(chat_id: str, user_id: str) -> str:
        """Promote a user to admin. You must have can_promote_members. Requires admin approval."""
        approval = await ai.hook(
            f"promote_{chat_id}_{user_id}",
            payload=ai.ToolApproval,
            metadata={"tool": "promote_chat_member", "chat_id": chat_id, "user_id": user_id},
        )
        if not approval.granted:
            return f"cancelled: {approval.reason or 'denied'}"
        await bot.promote_chat_member(
            chat_id=int(chat_id),
            user_id=int(user_id),
            can_change_info=True,
            can_invite_users=True,
            can_pin_messages=True,
            can_manage_topics=True,
        )
        return f"user {user_id} promoted in {chat_id}"

    @ai.tool
    async def pin_message(chat_id: str, message_id: str) -> str:
        """Pin a message in a chat. Admin permission required."""
        await bot.pin_chat_message(chat_id=int(chat_id), message_id=int(message_id))
        return f"message {message_id} pinned in {chat_id}"

    @ai.tool
    async def unpin_message(chat_id: str, message_id: str) -> str:
        """Unpin a message in a chat. Admin permission required."""
        await bot.unpin_chat_message(chat_id=int(chat_id), message_id=int(message_id))
        return f"message {message_id} unpinned in {chat_id}"

    @ai.tool
    async def unpin_all_messages(chat_id: str) -> str:
        """Unpin all messages in a chat. Requires admin approval from a user with pin privileges."""
        approval = await ai.hook(
            f"unpin_all_{chat_id}",
            payload=ai.ToolApproval,
            metadata={"tool": "unpin_all_messages", "chat_id": chat_id},
        )
        if not approval.granted:
            return f"cancelled: {approval.reason or 'denied'}"
        await bot.unpin_all_chat_messages(chat_id=int(chat_id))
        return f"all messages unpinned in {chat_id}"

    @ai.tool
    async def leave_chat(chat_id: str) -> str:
        """Leave a chat or group."""
        await bot.leave_chat(chat_id=int(chat_id))
        return f"left chat {chat_id}"

    @ai.tool
    async def export_chat_invite_link(chat_id: str) -> str:
        """Export a primary invite link for a chat. Admin permission required."""
        link = await bot.export_chat_invite_link(chat_id=int(chat_id))
        return link

    @ai.tool
    async def set_chat_title(chat_id: str, title: str) -> str:
        """Change the title of a chat or group. Admin permission required."""
        await bot.set_chat_title(chat_id=int(chat_id), title=title)
        return f"title changed to '{title}'"

    @ai.tool
    async def set_chat_description(chat_id: str, description: str) -> str:
        """Change the description of a chat or group. Admin permission required."""
        await bot.set_chat_description(chat_id=int(chat_id), description=description)
        return "description updated"

    @ai.tool
    async def generate_image(chat_id: str, prompt: str, size: str = "1024x1024", n: int = 1) -> str:
        """Generate image(s) from a text prompt using AI. Sends the result to the chat."""
        try:
            msg = await ai.generate(
                get_model(),
                [ai.user_message(prompt)],
                ai.ImageParams(n=n, size=size),
            )
        except Exception:
            return "generation failed"

        ids = []
        for part in msg.parts:
            if isinstance(part, ai.FilePart):
                data = part.data
                if isinstance(data, str):
                    try:
                        data = base64.b64decode(data)
                    except Exception:
                        data = data.encode()
                sent = await bot.send_photo(
                    chat_id=int(chat_id),
                    photo=BufferedInputFile(data if isinstance(data, bytes) else data.encode(), filename="image.png"),
                )
                ids.append(str(sent.message_id))
        return f"generated {len(ids)} image(s): {', '.join(ids)}" if ids else "no images generated"

    @ai.tool
    async def set_bot_name(name: str) -> str:
        """Set the bot's display name."""
        await bot.set_my_name(name=name)
        return f"bot name set to '{name}'"

    @ai.tool
    async def set_bot_description(description: str) -> str:
        """Set the bot's description (shown in the bot profile)."""
        await bot.set_my_description(description=description)
        return "bot description updated"

    @ai.tool
    async def set_bot_short_description(short_description: str) -> str:
        """Set the bot's short description (shown on the bot start page)."""
        await bot.set_my_short_description(short_description=short_description)
        return "bot short description updated"

    @ai.tool
    async def set_bot_photo(photo_base64: str) -> str:
        """Set the bot's profile photo. Accepts a base64-encoded image."""
        data = base64.b64decode(photo_base64)
        await bot.set_my_photo(photo=BufferedInputFile(data, filename="photo.jpg"))
        return "bot photo updated"

    @ai.tool
    async def delete_bot_photo() -> str:
        """Delete the bot's profile photo."""
        await bot.delete_my_photo()
        return "bot photo deleted"

    @ai.tool
    async def propose_new_feature(chat_id: str, name: str, description: str, code: str, target: str = "") -> str:
        """Propose adding a new feature (handler, tool, or command). Sends for admin approval via inline keyboard."""
        fid = make_fid(name)
        add_pending(fid, {"name": name, "description": description, "code": code, "target": target, "chat_id": int(chat_id)})
        content = as_list(
            Text("🤖 我想添加一个新功能:"),
            Text("名称: ", Bold(name)),
            Text("描述: ", Bold(description)),
            Pre(code[:2000], language="python"),
            "请审批:",
            sep="\n\n",
        )
        await bot.send_message(chat_id=int(chat_id), reply_markup=approve_kb(fid), **content.as_kwargs())
        return f"feature '{name}' proposed, awaiting approval"

    @ai.tool
    async def get_bot_info() -> str:
        """Get the bot's current name, description, and short description."""
        name = await bot.get_my_name()
        desc = await bot.get_my_description()
        sdesc = await bot.get_my_short_description()
        return (
            f"name: {name.name or ''}\n"
            f"description: {desc.description or ''}\n"
            f"short_description: {sdesc.short_description or ''}"
        )

    @ai.tool
    async def edit_image(chat_id: str, prompt: str, image_file_id: str) -> str:
        """Edit an existing image using AI. image_file_id is a Telegram file_id from a previously sent photo."""
        try:
            file = await bot.get_file(image_file_id)
            image_bytes = await bot.download_file(file.file_path)
            raw = image_bytes.read()
            result = await ai.generate(
                get_model(),
                [ai.user_message(prompt, ai.file_part(raw, media_type="image/png"))],
                ai.ImageParams(n=1),
            )
        except Exception:
            return "edit failed"

        for part in result.parts:
            if isinstance(part, ai.FilePart):
                data = part.data
                if isinstance(data, str):
                    try:
                        data = base64.b64decode(data)
                    except Exception:
                        data = data.encode()
                sent = await bot.send_photo(
                    chat_id=int(chat_id),
                    photo=BufferedInputFile(data if isinstance(data, bytes) else data.encode(), filename="edited.png"),
                    caption=prompt,
                )
                return f"sent (id={sent.message_id})"
        return "no edited image returned"

    return [
        send_message,
        send_photo,
        send_document,
        send_video,
        send_audio,
        send_voice,
        send_sticker,
        send_animation,
        send_video_note,
        send_media_group,
        send_location,
        send_dice,
        send_contact,
        get_chat_info,
        get_chat_member_count,
        get_chat_administrators,
        get_chat_member,
        ban_chat_member,
        unban_chat_member,
        restrict_chat_member,
        promote_chat_member,
        pin_message,
        unpin_message,
        unpin_all_messages,
        leave_chat,
        export_chat_invite_link,
        set_chat_title,
        set_chat_description,
        generate_image,
        edit_image,
        propose_new_feature,
        set_bot_name,
        set_bot_description,
        set_bot_short_description,
        set_bot_photo,
        delete_bot_photo,
        get_bot_info,
        *get_dynamic_tools(chat_id),
    ]
