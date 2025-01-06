tools = [
    {
        "type": "function",
        "function": {
            "name": "send_message",
            "description": "The default parse mode is the same as the official applications (a custom flavour of markdown). **bold**, `code` or __italic__ are available. In addition you can send [links](https://example.com) and [mentions](@username) (or using IDs like in the Bot API: [mention](tg://user?id=123456789)) and pre blocks with three backticks.",
            "parameters": {
                "type": "object",
                "properties": {
                    "message": {
                        "type": "string",
                        "description": "The message to be sent, or another message object to resend.The maximum length for a message is 35,000 bytes or 4,096 characters. Longer messages will not be sliced automatically, and you should slice them manually if the text to send is longer than said length.",
                    },
                    "reply_to": {
                        "type": "int",
                        "description": "Whether to reply to a message or not. If an integer is provided, it should be the ID of the message that it should reply to.",
                    },
                },
            },
        },
    },
]
