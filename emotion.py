import json
import requests

def emotion(text):

    API_KEY = "AIzaSyD5YgzYMtIKLq3m4hfmNrajLAdQhKVR0Uo"

    url = f'https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent?key={API_KEY}'
    headers = {'Content-Type': 'application/json'}
    data = {
        "contents": [
            {
                "parts": [{"text": "你現在是一名寵物醫生，要根據貓咪的描述文字，判斷牠的情緒狀態"+text}]
            }
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    print(f"emotion response status_code: {response.status_code}")

    return response.json()["candidates"][0]["content"]["parts"][0]["text"].strip()
