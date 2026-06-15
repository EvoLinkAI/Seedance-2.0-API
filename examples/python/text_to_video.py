import os
import requests

api_key = os.environ.get("EVOLINK_API_KEY")
if not api_key:
    raise SystemExit("Set EVOLINK_API_KEY first")

response = requests.post(
    'https://api.evolink.ai/v1/videos/generations',
    headers={
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    },
    json={
        'model': 'seedance-2.0-text-to-video',
        'prompt': 'A cinematic aerial shot over a futuristic city skyline at dawn',
        'duration': 5,
        'quality': '720p',
        'aspect_ratio': '16:9',
        'generate_audio': True,
    }
)

print(response.json())
