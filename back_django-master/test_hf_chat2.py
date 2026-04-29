import urllib.request
import json
import os
from decouple import Config, RepositoryEnv

env_path = os.path.join(os.path.dirname(__file__), 'back', '.env')
config = Config(RepositoryEnv(env_path))
api_key = config('HUGGINGFACE_API_KEY')

url = "https://api-inference.huggingface.co/v1/chat/completions"
req = urllib.request.Request(url, data=b'{"model": "mistralai/Mistral-Nemo-Instruct-2407", "messages": [{"role": "user", "content": "Bonjour"}]}', headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"})
try:
    resp = urllib.request.urlopen(req)
    print(resp.getcode())
    print(resp.read().decode('utf-8'))
except urllib.error.HTTPError as e:
    print(f"HTTP Error: {e.code}")
    print(e.read().decode('utf-8'))
except Exception as e:
    print(f"Error: {e}")
