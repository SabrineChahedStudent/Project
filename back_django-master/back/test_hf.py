import requests
import json

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-Nemo-Instruct-2407"
payload = {"inputs": "Bonjour"}

# We'll see if we get a 404
resp = requests.post(API_URL, json=payload)
print(resp.status_code)
print(resp.text)
