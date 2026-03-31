import requests

response = requests.post(
    'https://api.evolink.ai/v1/videos/generations',
    headers={
        'Authorization': 'Bearer YOUR_API_KEY',
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
