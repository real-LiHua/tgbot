import re
from os import getenv
import time
from dotenv import load_dotenv
from openai import AsyncOpenAI
from telegram import Message, Update, User
from telegram.ext import ContextTypes
from telegram.error import NetworkError

load_dotenv()

client = AsyncOpenAI(base_url="https://api-inference.huggingface.co/v1/")
system_prompt = f"""
当前时间是：{{}}
时区转为{getenv("TZ", time.tzname[0])}
使用 Telegram Markdown V2 格式（没有列表语法）, 不要插入反斜杠
消息跳转链接为 https://t.me/c/{{}}/消息ID
回复内容不要使用有序列表或无序列表语法
"""




async def command_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = [
        {
            "role": "system",
            "content": system_prompt.format(
                time.strftime("%a, %d %b %Y %H:%M:%S UTC", time.gmtime()),
                str(update.effective_message.chat.id)[4:],
            ),
        },
        *context.chat_data["msg"],
        {"role": "user", "content": update.effective_message.text[5:]},
    ]
    stream = await client.chat.completions.create(
        model="Qwen/Qwen2.5-72B-Instruct",
        messages=msg,
        temperature=0.5,
        max_tokens=2048,
        top_p=0.7,
        stream=True,
    )
    reply = []
    async for chunk in stream:
        reply.append(chunk.choices[0].delta.content or "")
    print("".join(reply))
    while True:
        try:
            await update.effective_message.reply_markdown_v2("".join(reply))
            break
        except NetworkError as e:
            print(e)
            pass

async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    usr: User = update.effective_user
    msg: Message = update.effective_message
    context.chat_data["msg"] = context.chat_data.get("msg", [])
    context.chat_data["msg"].append(
        {
            "role": "user",
            "content": f"消息{msg.id}:{usr.mention_markdown_v2()} 在 {msg.date.strftime("%a, %d %b %Y %H:%M:%S UTC")} 说道: {msg.text}",
        }
    )

    context.chat_data.setdefault("count", {}).setdefault(str(usr.id), 0)
    context.chat_data["count"][str(usr.id)] += 1
