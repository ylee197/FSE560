import os
from openai import OpenAI

token = os.environ["CREATEAI_SERVICE_TOKEN"]
base_url = "https://api-main.aiml.asu.edu/v1"

client = OpenAI(
    api_key=token,
    base_url=base_url,
)

messages = [
    {"role": "system", "content": "You are a helpful assistant."}
]

print("Chatbot started. Type 'exit' to quit.")

while True:
    user_text = input("\nYou: ").strip()

    if user_text.lower() in {"exit", "quit"}:
        break

    if not user_text:
        continue

    messages.append({"role": "user", "content": user_text})

    response = client.chat.completions.create(
        model="openai/gpt4o",
        messages=messages,
    )

    answer = response.choices[0].message.content
    print("Bot:", answer)

    messages.append({"role": "assistant", "content": answer})