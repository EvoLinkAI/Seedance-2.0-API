# Seedance 2.0 Image-to-Video Guide

Seedance 2.0 image-to-video creates videos from one or two input images.

## Supported models

- `seedance-2.0-image-to-video`
- `seedance-2.0-fast-image-to-video`

## Image behavior

| Image count | Behavior |
|---|---|
| `1` | first-frame image-to-video |
| `2` | first-frame to last-frame transition video |

## Required parameters

| Parameter | Type | Description |
|---|---|---|
| `model` | string | one of the Seedance 2.0 image-to-video model IDs |
| `image_urls` | string[] | one or two image URLs |
| `prompt` | string | optional in practice but strongly recommended for better control |

## Image requirements

### Standard image model
- formats: `jpeg`, `png`, `webp`
- aspect ratio: `0.4-2.5`
- image size: `300-6000 px`
- file size: under `30 MB` each
- total request size under `64 MB`

### Fast image model
- formats: `jpeg`, `png`, `webp`, `bmp`, `tiff`, `gif`
- aspect ratio: `0.4-2.5`
- image size: `300-6000 px`
- file size: under `30 MB` each
- total request size under `64 MB`

## Example request

```bash
curl --request POST \
  --url https://api.evolink.ai/v1/videos/generations \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data '{
    "model": "seedance-2.0-image-to-video",
    "prompt": "The camera slowly moves closer as the character breathes and the scene comes alive",
    "image_urls": ["https://example.com/first-frame.jpg"],
    "duration": 5,
    "quality": "720p",
    "aspect_ratio": "adaptive",
    "generate_audio": true
  }'
```

## Notes

- with two images, the first is treated as the start frame and the second as the end frame
- when aspect ratios differ, output follows the first image and the last image may be cropped to fit
- image-to-video does not accept `video_urls` or `audio_urls`
