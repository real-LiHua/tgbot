from huggingface_hub import InferenceClient
from dotenv import load_dotenv
load_dotenv()
client = InferenceClient()

messages = [
	{
		"role": "user",
		"content": "What is the capital of France?"
	}
]

completion = client.chat.completions(
    model="Qwen/Qwen2.5-72B-Instruct", 
	messages=messages, 
	#max_tokens=500
)

print(completion.choices[0].message)
