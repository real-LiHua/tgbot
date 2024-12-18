from huggingface_hub import AsyncInferenceClient
from dotenv import load_dotenv
import asyncio
load_dotenv()
client = AsyncInferenceClient()

messages = [
	{
		"role": "user",
		"content": "What is the capital of France?"
	}
]

async def main():
    completion = await client.chat_completion(
        model="Qwen/Qwen2.5-72B-Instruct", 
	messages=messages, 
	#max_tokens=500
    )
    print(completion.choices[0].message)
asyncio.run(main())
