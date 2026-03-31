# Seedance 2.0 Text-to-Video Guide

Seedance 2.0 text-to-video generates videos directly from prompt text.

## Supported models

- `seedance-2.0-text-to-video`
- `seedance-2.0-fast-text-to-video`

## Endpoint

```http
POST https://api.evolink.ai/v1/videos/generations
```

## Required parameters

| Parameter | Type | Description |
|---|---|---|
| `model` | string | one of the Seedance 2.0 text-to-video model IDs |
| `prompt` | string | text prompt describing the desired video |

## Optional parameters

| Parameter | Type | Default | Description |
|---|---|---:|---|
| `duration` | integer | `5` | `4-15` seconds, or `-1` for smart duration |
| `quality` | string | `720p` | `480p` or `720p` |
| `aspect_ratio` | string | `16:9` | `16:9`, `9:16`, `1:1`, `4:3`, `3:4`, `21:9`, or `adaptive` |
| `generate_audio` | boolean | `true` | generate synchronized audio |
| `callback_url` | string | — | HTTPS callback URL |

## Extended model parameters

Pass extended options under `model_params`.

| Parameter | Type | Default | Description |
|---|---|---:|---|
| `web_search` | boolean | `false` | allows the model to optionally use web search for more up-to-date content |

## Example request

```bash
curl --request POST \
  --url https://api.evolink.ai/v1/videos/generations \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data '{
    "model": "seedance-2.0-text-to-video",
    "prompt": "A realistic cinematic shot of a train crossing a snowy bridge at dawn, cold blue light, drifting fog",
    "duration": 8,
    "quality": "720p",
    "aspect_ratio": "16:9",
    "generate_audio": true,
    "model_params": {
      "web_search": false
    }
  }'
```

## Notes

- text-to-video does not accept `image_urls`, `video_urls`, or `audio_urls`
- result video URLs remain valid for 24 hours
- smart duration reserves billing first, then settles by actual output length
