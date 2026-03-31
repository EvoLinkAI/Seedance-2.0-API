# Seedance 2.0 Reference-to-Video Guide

Seedance 2.0 reference-to-video is the most flexible mode in the model family. It supports multimodal references across images, videos, audio, and text prompts.

## Supported models

- `seedance-2.0-reference-to-video`
- `seedance-2.0-fast-reference-to-video`

## Input limits

| Parameter | Type | Limit |
|---|---|---:|
| `image_urls` | string[] | `0-9` |
| `video_urls` | string[] | `0-3` |
| `audio_urls` | string[] | `0-3` |

> Audio cannot be supplied alone. At least one reference image or reference video must also be included.

## Typical uses

- multimodal guided generation
- style and composition transfer
- video editing with reference media
- video extension and continuation
- background music or sound reference alignment

## Video requirements

- formats: `mp4`, `mov`
- duration: `2-15` seconds per video
- up to `3` videos, total input video length `<= 15s`
- resolution: `480p` or `720p`
- aspect ratio: `0.4-2.5`
- file size: under `50 MB` each
- fps: `24-60`

## Audio requirements

- formats: `wav`, `mp3`
- duration: `2-15` seconds per file
- up to `3` files, total input audio length `<= 15s`
- file size: under `15 MB` each

## Example request

```bash
curl --request POST \
  --url https://api.evolink.ai/v1/videos/generations \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data '{
    "model": "seedance-2.0-reference-to-video",
    "prompt": "Use video 1 for camera movement, use audio 1 as background music, and keep the product style from image 1",
    "image_urls": ["https://example.com/product.jpg"],
    "video_urls": ["https://example.com/movement.mp4"],
    "audio_urls": ["https://example.com/music.mp3"],
    "duration": 10,
    "quality": "720p",
    "aspect_ratio": "16:9",
    "generate_audio": true
  }'
```

## Billing note

Reference video duration is included in billing. If you provide video references, your cost is based on:

```text
(input reference video duration + output video duration) × resolution price
```
