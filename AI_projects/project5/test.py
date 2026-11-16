import requests
import os

url = "https://api-main.aiml.asu.edu"
TOKEN = os.environ.get('CREATEAI_SERVICE_TOKEN')

if not TOKEN:
    raise RuntimeError('Set OPENAI_API_KET before running this program.')

# Production with service token
headers = {
    "Authorization": f"Bearer {TOKEN}",  # eyjh...
    "Content-Type": "application/json"
}

# Service token uses project settings — only query is needed
# You can add your question in 'query'
payload = {
    "action": "query",
    "model_providor":"gpt4o",
    "query": "What is artificial intelligence?",
    "model_params":{
        "temperature": 0.1,
        "system_prompt":"You are a helpful assistant.",
        "top_p":0.01,
    },
    "response_format":{"type":"json"},
}

response = requests.post(
    f"{url}/query",
    headers=headers,
    json=payload,
    timeout=60,
)

print("Status code:", response.status_code)

try:
    data = response.json()
except ValueError:
    print("Non-JSON response:")
    print(response.text)
    raise SystemExit(1)

if response.ok:
    # Generated model text
    print("\nResponse:")
    result = data.get('response')
    if isinstance(result, dict):
        print(result.get('response', 'No text returned'))
    else:
        print(result or 'No text returned')

    # Optional query identifier
    print("\nQuery ID:", data.get("query_id"))
else:
    print("\nAPI error:")
    print(data)

