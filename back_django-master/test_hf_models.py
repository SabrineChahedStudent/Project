import urllib.request
import json
import os
from decouple import Config, RepositoryEnv

env_path = os.path.join(os.path.dirname(__file__), 'back', '.env')
config = Config(RepositoryEnv(env_path))
API_KEY = config('HUGGINGFACE_API_KEY')
MODELS = [
    "mistralai/Mistral-7B-Instruct-v0.2",
    "mistralai/Mistral-7B-Instruct-v0.3",
    "HuggingFaceH4/zephyr-7b-beta",
    "mistralai/Mixtral-8x7B-Instruct-v0.1",
    "google/gemma-7b-it",
    "Qwen/Qwen2.5-7B-Instruct"
]

for model in MODELS:
    url = f"https://api-inference.huggingface.co/models/{model}"
    req = urllib.request.Request(url, data=b'{"inputs":"Bonjour"}', headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"})
    try:
        resp = urllib.request.urlopen(req)
        print(f"{model}: {resp.getcode()}")
    except urllib.error.HTTPError as e:
        print(f"{model}: {e.code}")
    except Exception as e:
        print(f"{model}: {e}")
