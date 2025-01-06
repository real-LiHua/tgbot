tools = [
    {
        "type": "function",
        "function": {
            "name": "send_message",
            "description": "Sends a message",
            "parameters": {
                "type": "object",
                "properties": {
                    "message": {
                        "type": "string",
                        "description": "The message to be sent, or another message object to resend.The maximum length for a message is 35,000 bytes or 4,096 characters. Longer messages will not be sliced automatically, and you should slice them manually if the text to send is longer than said length.",
                    }
                },
            },
        },
    }
]
"""
,
                    "reply_to": {
                        "type": "int",
                        "description": "Whether to reply to a message or not. If an integer is provided, it should be the ID of the message that it should reply to.",
                    },
                    "link_preview": {
                        "type": "bool",
                        "description": "Should the link preview be shown?",
                    },
                },
            },
        },
    },
]"""
