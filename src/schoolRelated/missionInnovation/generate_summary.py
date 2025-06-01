import sys
import requests
from json import dumps
from pyWrkspPackage import load_from_file
from dotenv import load_dotenv
from os import getenv

load_dotenv()
api_key = getenv("AI_API_KEY")

model = sys.argv[1]
input_text = sys.stdin.read()
prompt = load_from_file("prompt.md")

url = "https://api.mistral.ai/v1/chat/completions"
headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
payload = {
    "model": model,
    "messages": [
        {"role": "system", "content": prompt},
        {"role": "user", "content": input_text},
    ],
}

response = requests.post(url, headers=headers, json=payload)

print(dumps(response.json()))
