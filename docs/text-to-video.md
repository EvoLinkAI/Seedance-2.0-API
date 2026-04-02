# Seedance 2.0 Fast Text-to-Video API Reference

> - Generate videos from pure text prompts with faster processing speed; supports web search for enhanced timeliness
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
| `model` | string | Fixed value: `seedance-2.0-fast-text-to-video` |
| `prompt` | string | Text prompt describing the desired video. Supports both Chinese and English. Recommended: no more than 500 Chinese characters or 1,000 English words |

> This model is text-to-video only. It does not accept `image_urls`, `video_urls`, or `audio_urls` inputs.

#### Generation Parameters (Optional)

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `duration` | integer | `5` | Video duration in seconds. Range: `4`--`15`. Duration directly affects billing |
| `quality` | string | `720p` | Video resolution. Options: `480p`, `720p` |
| `aspect_ratio` | string | `16:9` | Aspect ratio. Options: `16:9`, `9:16`, `1:1`, `4:3`, `3:4`, `21:9`, `adaptive`. When set to `adaptive`, the model intelligently selects based on the prompt |
| `generate_audio` | boolean | `true` | Whether to generate synchronized audio (voice, sound effects, background music) at no additional cost. Tip: place dialogue within double quotes for better results |
| `callback_url` | string | -- | HTTPS callback URL. A notification is sent when the task completes or fails |

#### Model Extension Parameters (Optional)

Passed via the `model_params` object:

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `web_search` | boolean | `false` | Web search. When enabled, the model autonomously decides whether to search the internet based on the prompt (e.g., products, weather). This can improve timeliness but may add some latency. Fees are only incurred when a search is actually triggered; multiple searches may occur per request |

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
  "model": "seedance-2.0-fast-text-to-video",
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

### Basic Text-to-Video

```bash
curl -X POST https://api.evolink.ai/v1/videos/generations \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "seedance-2.0-fast-text-to-video",
    "prompt": "A macro lens focuses on a translucent glass frog perched on a leaf. The focus gradually shifts from its smooth skin to its fully transparent abdomen, where a bright red heart beats powerfully and rhythmically.",
    "duration": 8,
    "quality": "720p",
    "aspect_ratio": "16:9",
    "generate_audio": true
  }'
```

### Web Search Example

```bash
curl -X POST https://api.evolink.ai/v1/videos/generations \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "seedance-2.0-fast-text-to-video",
    "prompt": "Today New York weather forecast, with animated city skyline and temperature overlay display",
    "duration": 8,
    "aspect_ratio": "16:9",
    "model_params": { "web_search": true }
  }'
```

---

## Billing

```
Cost = Output video duration (seconds) x Resolution unit price
```

| Resolution | Unit Price |
|:----------:|:----------:|
| 480p | $0.0590 (4.1254 credits) /sec |
| 720p | $0.1273 (8.9100 credits) /sec |
| WebSearch | $0.00058 (0.04 credits) /call |

- **Web search:** Billed separately; charged only when actually triggered (a single request may trigger multiple searches)
- **Audio generation:** No additional charge

---

> **Early Access:** You can integrate against the docs today. Once Seedance API opens up, we’ll notify early-access users.

