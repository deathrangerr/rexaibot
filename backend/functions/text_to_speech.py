import requests
import json
from decouple import config

def convert_text_to_speech(content):
    url = "https://play.ht/api/v2/tts/stream"
    raw_content = content
    text = raw_content
    print(text)
    print(type(text))
    payload = json.dumps({
        "voice": "larry",
        "text": text,
    })

    headers = {
        'Authorization': config("playhtauthtoken"),
        'X-User-ID': config("playhtuserid"),
        'accept': 'audio/mpeg',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    if response.status_code == 200:
        return response.content
    else:
     return
