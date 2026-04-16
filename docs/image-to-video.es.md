# Guía de Seedance 2.0 Image-to-Video

Esta página cubre los modelos standard y fast de image-to-video de Seedance 2.0.

This page covers both the standard and fast image-to-video models for Seedance 2.0.

## Supported models

See also: [Pricing](./pricing.md)


- `seedance-2.0-image-to-video`
- `seedance-2.0-fast-image-to-video`

## Shared behavior

- 1 image -> first-frame image-to-video
- 2 images -> first-and-last-frame image-to-video
- async task workflow
- output video links stay valid for 24 hours

## Standard model reference

# Seedance 2.0 Image-to-Video Gateway Service Reference

> - 1 image generates a first-frame video; 2 images generate a first-and-last-frame video — automatically detected
> - Async processing mode — use the returned task ID to query status
> - Generated video links are valid for 24 hours; please save them promptly

## Create Video Generation Task

```
POST https://api.evolink.ai/v1/videos/generations
Authorization: Bearer YOUR_API_KEY
Content-Type: application/json
```

### Request Parameters

#### Required Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `model` | string | Fixed value: `seedance-2.0-image-to-video` |
| `prompt` | string | Text prompt describing the desired video. Supports both Chinese and English; recommended ≤500 Chinese characters or ≤1000 English words |
| `image_urls` | string[] | Image URL array, **1–2 images** |

> This model does not support `video_urls` or `audio_urls` input.

#### Image Rules

| Number of Images | Behavior | Role |
|:----------------:|----------|------|
| 1 | First-frame image-to-video | Automatically set as `first_frame` |
| 2 | First-and-last-frame image-to-video | 1st image → `first_frame`, 2nd image → `last_frame` |

**Image Requirements:**
- Supported formats: jpeg, png, webp
- Aspect ratio (width/height): 0.4 – 2.5
- Width/height pixels: 300 – 6000 px
- Max size per image: < 30 MB
- Total request body size must not exceed 64 MB
- When providing first and last frames, the two images may be identical. If aspect ratios differ, the first frame takes priority and the last frame is automatically cropped to match
- Image URLs must be directly accessible by the server

#### Generation Parameters (optional)

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `duration` | integer | `5` | Video duration in seconds. Range: `4`–`15` |
| `quality` | string | `720p` | Video resolution. Options: `480p`, `720p` |
| `aspect_ratio` | string | `16:9` | Aspect ratio. When set to `adaptive`, the closest aspect ratio is automatically selected based on the first-frame image. Options: `16:9`, `9:16`, `1:1`, `4:3`, `3:4`, `21:9`, `adaptive` |
| `generate_audio` | boolean | `true` | Whether to generate synchronized audio; no extra charge |
| `callback_url` | string | — | HTTPS callback URL |

### Aspect Ratio Pixel Values

**480p**

| Aspect Ratio | Pixels |
|:------------:|:------:|
| 16:9 | 864 × 496 |
| 4:3 | 752 × 560 |
| 1:1 | 640 × 640 |
| 3:4 | 560 × 752 |
| 9:16 | 496 × 864 |
| 21:9 | 992 × 432 |

**720p**

| Aspect Ratio | Pixels |
|:------------:|:------:|
| 16:9 | 1280 × 720 |
| 4:3 | 1112 × 834 |
| 1:1 | 960 × 960 |
| 3:4 | 834 × 1112 |
| 9:16 | 720 × 1280 |
| 21:9 | 1470 × 630 |

---

## Response

```json
{
  "id": "task-unified-1774857405-abc123",
  "model": "seedance-2.0-image-to-video",
  "object": "video.generation.task",
  "status": "pending",
  "progress": 0,
  "type": "video",
  "task_info": { "can_cancel": true, "estimated_time": 165 },
  "usage": { "billing_rule": "per_second", "credits_reserved": 50, "user_group": "default" }
}
```

## Query Task Status

```
GET https://api.evolink.ai/v1/tasks/{task_id}
Authorization: Bearer YOUR_API_KEY
```

---

## Examples

### First-Frame Image-to-Video

```bash
curl -X POST https://api.evolink.ai/v1/videos/generations \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "seedance-2.0-image-to-video",
    "prompt": "The camera slowly pushes in, and the scene gradually comes to life",
    "image_urls": ["https://example.com/first-frame.jpg"],
    "duration": 5,
    "aspect_ratio": "adaptive"
  }'
```

### First-and-Last-Frame Image-to-Video

```bash
curl -X POST https://api.evolink.ai/v1/videos/generations \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "seedance-2.0-image-to-video",
    "prompt": "A smooth transition between the two scenes",
    "image_urls": [
      "https://example.com/first.jpg",
      "https://example.com/last.jpg"
    ],
    "duration": 6,
    "aspect_ratio": "16:9"
  }'
```

---

## Billing

```
Cost = output video duration (seconds) × resolution unit price
```

| Resolution | Unit Price |
|:----------:|:----------:|
| 480p | $0.0919 (6.251 credits) /sec |
| 720p | $0.1985 (13.50 credits) /sec |

- **Audio generation:** No additional charge

---

## Fast model reference

# Seedance 2.0 Fast Image-to-Video Gateway Service Reference

> - Input 1 image to generate a first-frame video, or input 2 images to generate a first-and-last-frame video -- the model determines the mode automatically
> - Faster processing speed compared to the standard version
> - Asynchronous processing mode -- use the returned task ID to query status
> - Generated video links are valid for 24 hours; please save them promptly

## Create Video Generation Task

```
POST https://api.evolink.ai/v1/videos/generations
Authorization: Bearer YOUR_API_KEY
Content-Type: application/json
```

### Request Parameters

#### Required Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `model` | string | Fixed value: `seedance-2.0-fast-image-to-video` |
| `prompt` | string | Text prompt describing the desired video. Supports both Chinese and English. Recommended: no more than 500 Chinese characters or 1,000 English words |
| `image_urls` | string[] | Image URL array, **1--2 images** |

> This model does not accept `video_urls` or `audio_urls` inputs.

#### Image Rules

| Image Count | Behavior | Role |
|:-----------:|----------|------|
| 1 | First-frame image-to-video | Automatically set to `first_frame` |
| 2 | First-and-last-frame image-to-video | Image 1 -> `first_frame`, Image 2 -> `last_frame` |

**Image Requirements:**
- Formats: jpeg, png, webp, bmp, tiff, gif
- Aspect ratio (width/height): 0.4 -- 2.5
- Width/height pixels: 300 -- 6,000 px
- Max size per image: < 30 MB
- Total request body size must not exceed 64 MB
- Do not use Base64 encoding for large files
- When providing first and last frames, both images may be identical. If aspect ratios differ, the first frame takes priority and the last frame is automatically cropped to match
- Image URLs must be directly accessible by the server

#### Generation Parameters (Optional)

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `duration` | integer | `5` | Video duration in seconds. Range: `4`--`15` |
| `quality` | string | `720p` | Video resolution. Options: `480p`, `720p` |
| `aspect_ratio` | string | `16:9` | Aspect ratio. When set to `adaptive`, the closest aspect ratio is automatically selected based on the first-frame image. Options: `16:9`, `9:16`, `1:1`, `4:3`, `3:4`, `21:9`, `adaptive` |
| `generate_audio` | boolean | `true` | Whether to generate synchronized audio at no additional cost |
| `callback_url` | string | -- | HTTPS callback URL |

### Aspect Ratio Pixel Values

**480p**

| Aspect Ratio | Pixels |
|:------------:|:------:|
| 16:9 | 864 x 496 |
| 4:3 | 752 x 560 |
| 1:1 | 640 x 640 |
| 3:4 | 560 x 752 |
| 9:16 | 496 x 864 |
| 21:9 | 992 x 432 |

**720p**

| Aspect Ratio | Pixels |
|:------------:|:------:|
| 16:9 | 1280 x 720 |
| 4:3 | 1112 x 834 |
| 1:1 | 960 x 960 |
| 3:4 | 834 x 1112 |
| 9:16 | 720 x 1280 |
| 21:9 | 1470 x 630 |

---

## Response

```json
{
  "id": "task-unified-1774857405-abc123",
  "model": "seedance-2.0-fast-image-to-video",
  "object": "video.generation.task",
  "status": "pending",
  "progress": 0,
  "type": "video",
  "task_info": { "can_cancel": true, "estimated_time": 165 },
  "usage": { "billing_rule": "per_second", "credits_reserved": 50, "user_group": "default" }
}
```

## Query Task Status

```
GET https://api.evolink.ai/v1/tasks/{task_id}
Authorization: Bearer YOUR_API_KEY
```

**Success:** `status: "completed"` -- the `results` array contains the video URL.
**Failure:** `status: "failed"` -- the `error` object contains `code` and `message`.

---

## Examples

### First-Frame Image-to-Video

```bash
curl -X POST https://api.evolink.ai/v1/videos/generations \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "seedance-2.0-fast-image-to-video",
    "prompt": "The camera slowly pushes in, and the scene gradually comes to life",
    "image_urls": ["https://example.com/first-frame.jpg"],
    "duration": 5,
    "aspect_ratio": "adaptive"
  }'
```

### First-and-Last-Frame Image-to-Video

```bash
curl -X POST https://api.evolink.ai/v1/videos/generations \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "seedance-2.0-fast-image-to-video",
    "prompt": "A smooth transition between the two scenes",
    "image_urls": [
      "https://example.com/first.jpg",
      "https://example.com/last.jpg"
    ],
    "duration": 6,
    "aspect_ratio": "16:9"
  }'
```

---

## Billing

```
Cost = Output video duration (seconds) x Resolution unit price
```

| Resolution | Unit Price |
|:----------:|:----------:|
| 480p | $0.0745 (5.063 credits) /sec |
| 720p | $0.1608 (10.935 credits) /sec |

- **Audio generation:** No additional charge

---

## Summary of differences

| Item | Standard | Fast |
|---|---|---|
| Model ID | `seedance-2.0-image-to-video` | `seedance-2.0-fast-image-to-video` |
| Positioning | general production use | faster iteration |
| Extra input formats in docs | `jpeg`, `png`, `webp` | `jpeg`, `png`, `webp`, `bmp`, `tiff`, `gif` |

---

> **Early Access:** Ya puedes avanzar con la integración siguiendo la documentación. En cuanto Seedance Gateway Service se abra oficialmente, avisaremos a los usuarios de Early Access.