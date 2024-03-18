# 單個文字和圖片
import json
import requests
import base64

def picture(imgName):

    API_KEY = "AIzaSyD5YgzYMtIKLq3m4hfmNrajLAdQhKVR0Uo"

    with open(str(imgName)+".jpg", "rb") as image_file:
        image_base64_string = base64.b64encode(image_file.read()).decode('utf-8')

    url = f'https://generativelanguage.googleapis.com/v1/models/gemini-pro-vision:generateContent?key={API_KEY}'
    headers = {'Content-Type': 'application/json'}
    data = {
        "contents": [
            {
                "parts": [
                    {"text": "圖片中是一隻貓咪。請回答他的姿勢與動作，越詳細越好"},
                    {
                        "inline_data": {
                            "mime_type": "image/jpeg",
                            "data": image_base64_string
                        }
                    }
                ]
            },
        ]
    }
    response = requests.post(url, headers=headers, json=data)
    print(f"img response status_code: {response.status_code}")

    return response.json()["candidates"][0]["content"]["parts"][0]["text"].strip()

    # print(json.dumps(response.json(), indent=4, ensure_ascii=False))
