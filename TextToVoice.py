# -*- coding: utf-8 -*-
"""autogenerator.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1nk5sSVtGdZf94V4WVPCEaVXmitTtCG2p
"""

import requests

CHUNK_SIZE = 1024
url = "https://api.elevenlabs.io/v1/text-to-speech/21m00Tcm4TlvDq8ikWAM"

headers = {
  "Accept": "audio/mpeg",
  "Content-Type": "application/json",
  "xi-api-key": "3d9d39cf7b3f5dad7511879fdf1f5c94"
}

data = {
  "text": " العالم قرية صغيرة",
  "model_id": "eleven_multilingual_v2",
  "voice_settings": {
    "stability": 1,
    "similarity_boost": 0.5
  }
}

response = requests.post(url, json=data, headers=headers)
with open('output.mp3', 'wb') as f:
    for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
        if chunk:
            f.write(chunk)

