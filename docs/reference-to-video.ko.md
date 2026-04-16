# Seedance 2.0 Reference-to-Video 가이드

이 페이지는 Seedance 2.0의 standard 및 fast reference-to-video 모델을 함께 다룹니다.

This page covers both the standard and fast reference-to-video models for Seedance 2.0.

## Supported models

See also: [Pricing](./pricing.md)


- `seedance-2.0-reference-to-video`
- `seedance-2.0-fast-reference-to-video`

## Shared capabilities

- multimodal generation with image, video, audio, and prompt inputs
- supports new generation, editing, extension, and guided creative workflows
- async task workflow with task polling
- output video links stay valid for 24 hours

## Standard model reference

# Seedance 2.0 Reference-to-Video Multimodal Gateway Service Reference

> - Input reference images (0–9) + videos (0–3) + audio (0–3) + text prompt to generate video
> - Supports new generation, video editing, and video extension
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
| `model` | string | Fixed value: `seedance-2.0-reference-to-video` |
| `prompt` | string | Text prompt describing the desired video. Supports both Chinese and English; recommended ≤500 Chinese characters or ≤1000 English words. Use natural language to specify the role of each asset, e.g., "Use image 1 as the first frame", "Use the camera movement from video 1 throughout", "Use audio 1 as background music". The model automatically understands the mapping between asset numbers and their intended roles |

#### Reference Asset Inputs (all optional, but constraints apply)

| Parameter | Type | Description |
|-----------|------|-------------|
| `image_urls` | string[] | Reference image URL array, **0–9 images** |
| `video_urls` | string[] | Reference video URL array, **0–3 videos** |
| `audio_urls` | string[] | Reference audio URL array, **0–3 clips** |

> **Important:** You cannot submit `audio_urls` alone — you must include at least 1 image (`image_urls`) or 1 video (`video_urls`).

#### Asset Role Table

| Media Type | Role | Typical Usage |
|------------|------|---------------|
| Image | `reference_image` | Style reference, product image, first/last frame (specified via prompt) |
| Video | `reference_video` | Camera movement reference, motion reference, source video for editing/extension |
| Audio | `reference_audio` | Background music, sound effects, voice/dialogue reference |

#### Image Requirements
- Supported formats: `.jpeg`, `.png`, `.webp`
- Aspect ratio (width/height): `0.4` – `2.5`
- Width/height pixels: `300` – `6000` px
- Max size per image: ≤ `30MB`
- Total request body size must not exceed `64MB`; do not use Base64 encoding
- Image URLs must be directly accessible by the server

#### Video Requirements
- Supported formats: `.mp4`, `.mov`
- Resolution: 480p, 720p
- Duration per video: `2` – `15` seconds; max 3 videos; total duration of all videos ≤ `15` seconds
- Aspect ratio (width/height): `0.4` – `2.5`
- Width/height pixels: `300` – `6000` px
- Frame pixels (width × height): `409,600` – `927,408` (e.g., 640×640 to 834×1112)
- Max size per video: ≤ `50MB`
- Frame rate: `24` – `60` FPS
- Total request body size must not exceed `64MB`; do not use Base64 encoding
- Using video references incurs additional cost (input video duration is included in billing)
- Video URLs must be directly accessible by the server

#### Audio Requirements
- Supported formats: `.wav`, `.mp3`
- Duration per clip: `2` – `15` seconds; max 3 clips; total duration of all audio ≤ `15` seconds
- Max size per clip: ≤ `15MB`
- Total request body size must not exceed `64MB`; do not use Base64 encoding
- Audio URLs must be directly accessible by the server

> **Note:** Audio cannot be submitted alone — at least 1 reference video or 1 reference image must be included.

#### Generation Parameters (optional)

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `duration` | integer | `5` | Video duration in seconds. Range: `4`–`15`. Duration directly affects billing |
| `quality` | string | `720p` | Video resolution. Options: `480p`, `720p` |
| `aspect_ratio` | string | `16:9` | Aspect ratio. Options: `16:9`, `9:16`, `1:1`, `4:3`, `3:4`, `21:9`, `adaptive`. When set to `adaptive`, priority order: video > image > prompt |
| `generate_audio` | boolean | `true` | Whether to generate synchronized audio; no extra charge |
| `callback_url` | string | — | HTTPS callback URL; triggered when the task completes, fails, or is cancelled |

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
  "model": "seedance-2.0-reference-to-video",
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

**Success:** `status: "completed"`, the `results` array contains the video URL.
**Failure:** `status: "failed"`, the `error` object contains `code` and `message`.

---

## Examples

### Multimodal Reference (Image + Video + Audio)

```bash
curl -X POST https://api.evolink.ai/v1/videos/generations \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "seedance-2.0-reference-to-video",
    "prompt": "Use the first-person perspective from video 1 throughout, and use audio 1 as background music throughout. A first-person perspective fruit tea promotional advertisement...",
    "image_urls": [
      "https://example.com/ref1.jpg",
      "https://example.com/ref2.jpg"
    ],
    "video_urls": [
      "https://example.com/reference.mp4"
    ],
    "audio_urls": [
      "https://example.com/bgm.mp3"
    ],
    "duration": 10,
    "quality": "720p",
    "aspect_ratio": "16:9",
    "generate_audio": true
  }'
```

### Video Editing (replace elements)

```bash
curl -X POST https://api.evolink.ai/v1/videos/generations \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "seedance-2.0-reference-to-video",
    "prompt": "Replace the perfume in the gift box from video 1 with the cream shown in image 1, keeping the camera movement unchanged",
    "image_urls": [
      "https://example.com/cream.jpg"
    ],
    "video_urls": [
      "https://example.com/original.mp4"
    ],
    "duration": 5,
    "aspect_ratio": "16:9"
  }'
```

### Video Extension (multi-segment concatenation)

```bash
curl -X POST https://api.evolink.ai/v1/videos/generations \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "seedance-2.0-reference-to-video",
    "prompt": "The arched window in video 1 opens, entering an art gallery interior, then transitions to video 2, after which the camera moves into the painting, followed by video 3",
    "video_urls": [
      "https://example.com/part1.mp4",
      "https://example.com/part2.mp4",
      "https://example.com/part3.mp4"
    ],
    "duration": 8,
    "aspect_ratio": "16:9",
    "generate_audio": true
  }'
```

---

## Billing

**Without video input:**

```
Cost = Output video duration (seconds) × Resolution unit price
```

| Resolution | Unit Price |
|:----------:|:----------:|
| 480p | $0.0919 (6.251 credits) /sec |
| 720p | $0.1985 (13.50 credits) /sec |

**With video input:** Input video duration is billed with a minimum duration rule:

```
Billable input duration = max(Total input video duration, Output video duration)
Cost = (Billable input duration + Output video duration) (seconds) × Resolution unit price
```

> Example: 10s output (720p) with 5s input video → Billable input = max(5, 10) = 10s → Cost = (10 + 10) × $0.0957 = $1.91

| Resolution | Unit Price |
|:----------:|:----------:|
| 480p | $0.0560 (3.807 credits) /sec |
| 720p | $0.1209 (8.222 credits) /sec |

- **Audio generation:** No additional charge

---

## Fast model reference

# Seedance 2.0 Fast Reference-to-Video Multimodal Gateway Service Reference

> - Input reference images (0--9) + reference videos (0--3) + reference audio (0--3) + text prompt to generate video
> - Supports multiple creative scenarios: new generation, video editing, video extension, and more
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
| `model` | string | Fixed value: `seedance-2.0-fast-reference-to-video` |
| `prompt` | string | Text prompt describing the desired video. Supports both Chinese and English. Recommended: no more than 500 Chinese characters or 1,000 English words. You can use natural language to specify the role of each asset, e.g., "use image 1 as first frame", "use video 1's camera movement throughout", "use audio 1 as background music". The model automatically understands the correspondence between asset numbers and their roles |

#### Media Input Parameters (Optional)

| Parameter | Type | Description |
|-----------|------|-------------|
| `image_urls` | string[] | Reference image URL array, **0--9 images** |
| `video_urls` | string[] | Reference video URL array, **0--3 videos** |
| `audio_urls` | string[] | Reference audio URL array, **0--3 clips** |

> **Note:** You cannot provide only `audio_urls`. The request must include at least 1 image (`image_urls`) or 1 video (`video_urls`).

#### Image Requirements

- Formats: jpeg, png, webp, bmp, tiff, gif
- Aspect ratio (width/height): 0.4 -- 2.5
- Width/height pixels: 300 -- 6,000 px
- Max size per image: 30 MB
- Total request body size must not exceed 64 MB
- Do not use Base64 encoding for large files
- Image URLs must be directly accessible by the server

#### Video Requirements

- Formats: mp4, mov
- Resolution: 480p, 720p
- Duration per video: 2 -- 15 seconds; max 3 videos; total duration of all videos <= 15 seconds
- Aspect ratio (width/height): 0.4 -- 2.5
- Width/height pixels: 300 -- 6,000 px
- Frame pixels (width x height): 409,600 -- 927,408 (e.g., 640x640 -- 834x1112)
- Max size per video: 50 MB
- Frame rate: 24 -- 60 FPS
- Total request body size must not exceed 64 MB; do not use Base64 encoding
- Using video references incurs additional fees (input video duration is counted in billing)
- Video URLs must be directly accessible by the server

#### Audio Requirements

- Formats: wav, mp3
- Duration per clip: 2 -- 15 seconds; max 3 clips; total duration of all audio <= 15 seconds
- Max size per clip: 15 MB
- Total request body size must not exceed 64 MB; do not use Base64 encoding
- Audio URLs must be directly accessible by the server
- Audio cannot be provided alone; at least 1 reference image or video is required

#### Media Role Reference

| Media Type | Role | Typical Usage |
|:----------:|------|---------------|
| Image | `reference_image` | Style reference, product images, character portraits, first/last frame (specified via prompt) |
| Video | `reference_video` | Camera movement reference, action reference, source video for editing/extension |
| Audio | `reference_audio` | Background music, sound effects, voice/dialogue reference |

#### Generation Parameters (Optional)

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `duration` | integer | `5` | Video duration in seconds. Range: `4`--`15`. Duration directly affects billing |
| `quality` | string | `720p` | Video resolution. Options: `480p`, `720p` |
| `aspect_ratio` | string | `16:9` | Aspect ratio. Options: `16:9`, `9:16`, `1:1`, `4:3`, `3:4`, `21:9`, `adaptive`. When set to `adaptive`, priority order: video > image > prompt |
| `generate_audio` | boolean | `true` | Whether to generate synchronized audio at no additional cost |
| `callback_url` | string | -- | HTTPS callback URL. Triggered when the task completes, fails, or is cancelled |

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
  "model": "seedance-2.0-fast-reference-to-video",
  "object": "video.generation.task",
  "status": "pending",
  "progress": 0,
  "type": "video",
  "task_info": { "can_cancel": true, "estimated_time": 120 },
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

### Multimodal Reference (Image + Video + Audio)

```bash
curl -X POST https://api.evolink.ai/v1/videos/generations \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "seedance-2.0-fast-reference-to-video",
    "prompt": "Use video 1 first-person perspective throughout, use audio 1 as background music throughout. First-person POV fruit tea promotional ad: the camera glides over a wooden table, passing tropical fruits, then focuses on a glass of iced fruit tea with condensation dripping down.",
    "image_urls": [
      "https://example.com/ref1.jpg",
      "https://example.com/ref2.jpg"
    ],
    "video_urls": [
      "https://example.com/reference.mp4"
    ],
    "audio_urls": [
      "https://example.com/bgm.mp3"
    ],
    "duration": 10,
    "quality": "720p",
    "aspect_ratio": "16:9",
    "generate_audio": true
  }'
```

### Video Editing (Element Replacement)

```bash
curl -X POST https://api.evolink.ai/v1/videos/generations \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "seedance-2.0-fast-reference-to-video",
    "prompt": "Replace the perfume in video 1 gift box with the cream from image 1, keep the camera movement unchanged",
    "image_urls": [
      "https://example.com/cream.jpg"
    ],
    "video_urls": [
      "https://example.com/original.mp4"
    ],
    "duration": 5,
    "aspect_ratio": "16:9"
  }'
```

### Video Extension (Multi-Segment Concatenation)

```bash
curl -X POST https://api.evolink.ai/v1/videos/generations \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "seedance-2.0-fast-reference-to-video",
    "prompt": "The arched window in video 1 opens, entering the art gallery interior, then continue with video 2, then the camera moves into the painting, continue with video 3",
    "video_urls": [
      "https://example.com/part1.mp4",
      "https://example.com/part2.mp4",
      "https://example.com/part3.mp4"
    ],
    "duration": 8,
    "aspect_ratio": "16:9",
    "generate_audio": true
  }'
```

---

## Billing

**Without video input:**

```
Cost = Output video duration (seconds) × Resolution unit price
```

| Resolution | Unit Price |
|:----------:|:----------:|
| 480p | $0.0745 (5.063 credits) /sec |
| 720p | $0.1608 (10.935 credits) /sec |

**With video input:** Input video duration is billed with a minimum duration rule:

```
Billable input duration = max(Total input video duration, Output video duration)
Cost = (Billable input duration + Output video duration) (seconds) × Resolution unit price
```

> Example: 10s output (720p) with 5s input video → Billable input = max(5, 10) = 10s → Cost = (10 + 10) × $0.0957 = $1.91

| Resolution | Unit Price |
|:----------:|:----------:|
| 480p | $0.0443 (3.012 credits) /sec |
| 720p | $0.0957 (6.506 credits) /sec |

- **Audio generation:** No additional charge

---

## Summary of differences

| Item | Standard | Fast |
|---|---|---|
| Model ID | `seedance-2.0-reference-to-video` | `seedance-2.0-fast-reference-to-video` |
| Positioning | general production use | faster iteration |
| Estimated time in example response | `165` | `120` |
| Pricing in provided docs | standard rate | discounted fast-reference rate |

---

> **Early Access:** 지금 문서를 기준으로 먼저 연동을 진행할 수 있습니다. Seedance Gateway Service가 정식으로 열리면 Early Access 사용자에게 안내드리겠습니다.