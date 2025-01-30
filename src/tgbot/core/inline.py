from telethon import TelegramClient, events, functions, types, Button
from .data import ChatData

"""
InlineQuery.Event(original_update=UpdateBotInlineQuery(query_id=4477228874536774855, user_id=1042436080, query='测试', offset='', geo=None, peer_type=InlineQueryPeerTypeMegagroup()), query=UpdateBotInlineQuery(query_id=4477228874536774855, user_id=1042436080, query='测试', offset='', geo=None, peer_type=InlineQueryPeerTypeMegagroup()), pattern_match=None)

UpdateNewMessage(message=Message(id=436, peer_id=PeerUser(user_id=1042436080), date=datetime.datetime(2025, 1, 30, 21, 20, 7, tzinfo=datetime.timezone.utc), message='AI 思考中...', out=False, mentioned=False, media_unread=False, silent=False, post=False, from_scheduled=False, legacy=False, edit_hide=False, pinned=False, noforwards=False, invert_media=False, offline=False, video_processing_pending=False, from_id=None, from_boosts_applied=None, saved_peer_id=None, fwd_from=None, via_bot_id=7527776928, via_business_bot_id=None, reply_to=None, media=None, reply_markup=ReplyInlineMarkup(rows=[KeyboardButtonRow(buttons=[KeyboardButtonCallback(text='刷新助手回复', data=b'yes', requires_password=False)])]), entities=[], views=None, forwards=None, replies=None, edit_date=None, post_author=None, grouped_id=None, reactions=None, restriction_reason=[], ttl_period=None, quick_reply_shortcut_id=None, effect=None, factcheck=None), pts=478, pts_count=1)

CallbackQuery.Event(original_update=UpdateInlineBotCallbackQuery(query_id=4477228874917326799, user_id=1042436080, msg_id=InputBotInlineMessageID(dc_id=5, id=4477228871770526727, access_hash=-773944628118007854), chat_instance=-1905119960704860251, data=b'yes', game_short_name=None), query=UpdateInlineBotCallbackQuery(query_id=4477228874917326799, user_id=1042436080, msg_id=InputBotInlineMessageID(dc_id=5, id=4477228871770526727, access_hash=-773944628118007854), chat_instance=-1905119960704860251, data=b'yes', game_short_name=None), data_match=None, pattern_match=None)

UpdateEditMessage(message=Message(id=436, peer_id=PeerUser(user_id=1042436080), date=datetime.datetime(2025, 1, 30, 21, 20, 7, tzinfo=datetime.timezone.utc), message='测试', out=False, mentioned=False, media_unread=False, silent=False, post=False, from_scheduled=False, legacy=False, edit_hide=True, pinned=False, noforwards=False, invert_media=False, offline=False, video_processing_pending=False, from_id=None, from_boosts_applied=None, saved_peer_id=None, fwd_from=None, via_bot_id=7527776928, via_business_bot_id=None, reply_to=None, media=None, reply_markup=None, entities=[], views=None, forwards=None, replies=None, edit_date=datetime.datetime(2025, 1, 30, 21, 20, 14, tzinfo=datetime.timezone.utc), post_author=None, grouped_id=None, reactions=None, restriction_reason=[], ttl_period=None, quick_reply_shortcut_id=None, effect=None, factcheck=None), pts=479, pts_count=1)
"""


async def init(bot: TelegramClient, data: ChatData, config: dict[str, list[dict]]):
    @bot.on(events.CallbackQuery)
    async def callback(event:events.CallbackQuery.Event):
        print(event)
        if event.data == b"yes":
            await event.edit("测试")

    @bot.on(events.InlineQuery)
    async def inline(event:events.InlineQuery.Event):
        print(event)
        builder = event.builder
        await event.answer(
            [
                builder.article(
                    "AI 助手",
                    text="AI 思考中...",
                    buttons=Button.inline("刷新助手回复", data="yes"),
                ),
            ]
        )
