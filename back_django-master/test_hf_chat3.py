import urllib.request
import json
import os
from decouple import Config, RepositoryEnv

env_path = os.path.join(os.path.dirname(__file__), 'back', '.env')
config = Config(RepositoryEnv(env_path))
api_key = config('HUGGINGFACE_API_KEY')

MODELS = [
    "mistralai/Mistral-7B-Instruct-v0.3",
    "HuggingFaceH4/zephyr-7b-beta",
    "meta-llama/Meta-Llama-3-8B-Instruct"
]

for model in MODELS:
    url = f"https://api-inference.huggingface.co/models/{model}/v1/chat/completions"
    payload = {"model": model, "messages": [{"role": "user", "content": "Bonjour"}]}
    req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"})
    try:
        resp = urllib.request.urlopen(req)
        print(f"{model}: {resp.getcode()}")
    except urllib.error.HTTPError as e:
        print(f"{model}: {e.code} - {e.read().decode('utf-8')[:50]}")
    except Exception as e:
        print(f"{model}: Error {e}")
