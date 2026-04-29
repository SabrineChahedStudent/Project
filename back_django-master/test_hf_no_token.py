import urllib.request
import json

url = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"
req = urllib.request.Request(url, data=b'{"inputs":"Bonjour"}', headers={"Content-Type": "application/json"})
try:
    resp = urllib.request.urlopen(req)
    print(resp.getcode())
    print(resp.read().decode('utf-8'))
except urllib.error.HTTPError as e:
    print(f"HTTP Error: {e.code}")
    print(e.read().decode('utf-8'))
except Exception as e:
    print(f"Error: {e}")
