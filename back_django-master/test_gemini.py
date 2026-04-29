import urllib.request
import json
import os
from decouple import Config, RepositoryEnv

env_path = os.path.join(os.path.dirname(__file__), 'back', '.env')
config = Config(RepositoryEnv(env_path))
api_key = config('GEMINI_API_KEY')
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
payload = {
    "contents": [{"parts": [{"text": "Bonjour"}]}]
}
req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers={"Content-Type": "application/json"})
try:
    resp = urllib.request.urlopen(req)
    print(resp.getcode())
    print(resp.read().decode('utf-8'))
except urllib.error.HTTPError as e:
    print(f"HTTP Error: {e.code}")
    print(e.read().decode('utf-8'))
except Exception as e:
    print(f"Error: {e}")
