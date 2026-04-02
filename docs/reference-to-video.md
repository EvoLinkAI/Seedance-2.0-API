# Seedance 2.0 Reference-to-Video Guide

This page covers both the standard and fast reference-to-video models for Seedance 2.0.

## Supported models

- `seedance-2.0-reference-to-video`
- `seedance-2.0-fast-reference-to-video`

## Shared capabilities

- multimodal generation with image, video, audio, and prompt inputs
- supports generation, editing, extension, and guided creative workflows
- async task workflow with task polling

## Fast model reference

# Seedance 2.0 Fast Reference-to-Video Multimodal API Reference

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
| 480p | $0.0590 (4.1254 credits) /sec |
| 720p | $0.1273 (8.9100 credits) /sec |

**With video input:** Input video duration is billed with a minimum duration rule:

```
Billable input duration = max(Total input video duration, Output video duration)
Cost = (Billable input duration + Output video duration) (seconds) × Resolution unit price
```

> Example: 10s output (720p) with 5s input video → Billable input = max(5, 10) = 10s → Cost = (10 + 10) × $0.0758 = $1.516

| Resolution | Unit Price |
|:----------:|:----------:|
| 480p | $0.0351 (2.4546 credits) /sec |
| 720p | $0.0758 (5.3015 credits) /sec |

- **Audio generation:** No additional charge

---

## Standard model note

The standard `seedance-2.0-reference-to-video` model uses the same multimodal request pattern:

- `image_urls`: up to 9
- `video_urls`: up to 3
- `audio_urls`: up to 3
- audio cannot be supplied alone

For implementation, the main field that changes is usually the `model` name.

---

> **Early Access:** You can integrate against the docs today. Once Seedance API opens up, we’ll notify early-access users.
