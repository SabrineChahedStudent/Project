import urllib.request
import json
import os
from decouple import Config, RepositoryEnv

env_path = os.path.join(os.path.dirname(__file__), 'back', '.env')
config = Config(RepositoryEnv(env_path))
api_key = config('HUGGINGFACE_API_KEY')

url = "https://router.huggingface.co/hf-inference/models/mistralai/Mistral-7B-Instruct-v0.3"
req = urllib.request.Request(url, data=b'{"inputs":"Bonjour"}', headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"})
try:
    resp = urllib.request.urlopen(req)
    print(resp.getcode())
    print(resp.read().decode('utf-8'))
except urllib.error.HTTPError as e:
    print(f"HTTP Error: {e.code}")
    print(e.read().decode('utf-8'))
except Exception as e:
    print(f"Error: {e}")
