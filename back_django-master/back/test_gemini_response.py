import urllib.request
import urllib.error
import json
import os

def test_api():
    GEMINI_API_KEY = ''
    try:
        with open('.env', 'r') as f:
            for line in f:
                if line.startswith('GEMINI_API_KEY='):
                    GEMINI_API_KEY = line.strip().split('=', 1)[1]
    except FileNotFoundError:
        pass

    API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent?key={GEMINI_API_KEY}"
    
    payload = {
        "contents": [{"role": "user", "parts": [{"text": "Hello, respond with exactly 'SUCCESS'"}]}]
    }

    try:
        req = urllib.request.Request(API_URL, data=json.dumps(payload).encode('utf-8'), headers={"Content-Type": "application/json"})
        resp = urllib.request.urlopen(req, timeout=10)
        data = json.loads(resp.read().decode('utf-8'))
        text = data.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "")
        print("HTTP STATUS: 200 SUCCESS")
        print("RESPONSE:", text)
    except urllib.error.HTTPError as e:
        print(f"HTTP ERROR: {e.code}")
        print(e.read().decode('utf-8'))

if __name__ == '__main__':
    test_api()
