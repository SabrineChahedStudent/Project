import urllib.request
import json
import os
from decouple import Config, RepositoryEnv

env_path = os.path.join(os.path.dirname(__file__), 'back', '.env')
config = Config(RepositoryEnv(env_path))
api_key = config('GEMINI_API_KEY')
url = f"https://generativelanguage.googleapis.com/v1beta/models?key={api_key}"
req = urllib.request.Request(url)
try:
    resp = urllib.request.urlopen(req)
    data = json.loads(resp.read().decode('utf-8'))
    for m in data.get("models", []):
        print(m.get("name"))
except urllib.error.HTTPError as e:
    print(f"HTTP Error: {e.code} - {e.read().decode('utf-8')[:100]}")
except Exception as e:
    print(f"Error: {e}")
