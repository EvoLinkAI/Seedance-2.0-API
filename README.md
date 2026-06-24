[English](./README.md) | [简体中文](./README.zh-CN.md) | [繁體中文](./README.zh-TW.md) | [Español](./README.es.md) | [Deutsch](./README.de.md) | [Français](./README.fr.md) | [日本語](./README.ja.md) | [한국어](./README.ko.md) | [Türkçe](./README.tr.md) | [Русский](./README.ru.md)

# Seedance 2.5 Gateway Service: Early Access, API Path, and Video Generation Guide

<p align="center">
  <a href="https://evolink.ai/launch/seedance-2-5?utm_source=github&utm_medium=banner&utm_campaign=Seedance-2.5-Gateway-Service">
    <img src="./assets/banner.jpg" alt="Seedance 2.5 Early Access" width="100%" />
  </a>
</p>

<p align="center">
  <strong>Seedance 2.5 Early Access<br>Current Seedance 2 API Path<br>Get Early Access</strong>
</p>

<p align="center">
  Seedance 2.5 early access and the current Seedance 2 API path, text-to-video, image-to-video, and reference-to-video in one unified guide.
</p>

<p align="left">
  <a href="https://evolink.ai/launch/seedance-2-5?utm_source=github&utm_medium=readme&utm_campaign=Seedance-2.5-Gateway-Service">Get Seedance 2.5 Early Access and view pricing</a> ·
  <a href="https://evolink.ai/signup?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-api">Get your API key</a> ·
  <a href="https://docs.evolink.ai?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-api">Read current Seedance API docs</a>
</p>

## EvoLink Quick Start

Create a Seedance 2.0 video task through the EvoLink API:

<p align="center">
  <a href="https://evolink.ai/launch/seedance-2-5?utm_source=github&utm_medium=readme&utm_campaign=Seedance-2.5-Gateway-Service"><strong>Get Seedance 2.5 Early Access</strong></a> &nbsp;·&nbsp;
  <a href="https://docs.evolink.ai?utm_source=github&utm_medium=readme&utm_campaign=Seedance-2.5-Gateway-Service"><strong>View API Docs</strong></a> &nbsp;·&nbsp;
  <a href="https://evolink.ai/signup?utm_source=github&utm_medium=readme&utm_campaign=Seedance-2.5-Gateway-Service"><strong>Get API Key</strong></a> &nbsp;·&nbsp;
  <a href="https://github.com/EvoLinkAI/awesome-seedance-2.5-prompts"><strong>Seedance Prompts</strong></a> &nbsp;·&nbsp;
  <a href="https://github.com/EvoLinkAI/awesome-seedance-2.5-guide"><strong>Seedance Guide</strong></a> &nbsp;·&nbsp;
  <a href="https://github.com/EvoLinkAI/seedance2-video-gen-skill-for-openclaw"><strong>Skill</strong></a>
</p>

> [!NOTE]
> **Get Seedance 2.5 Early Access:** Seedance 2.5 early access is open through EvoLink. Use the current Seedance 2 API path while the 2.5 rollout is opening. [Join the rollout](https://evolink.ai/launch/seedance-2-5?utm_source=github&utm_medium=readme&utm_campaign=Seedance-2.5-Gateway-Service).

```bash
export EVOLINK_API_KEY="your_key_here"

curl --request POST \
  --url https://api.evolink.ai/v1/videos/generations \
  --header "Authorization: Bearer ${EVOLINK_API_KEY}" \
  --header 'Content-Type: application/json' \
  --data '{
    "model": "seedance-2.0-text-to-video",
    "prompt": "A cinematic aerial shot of a futuristic city at sunrise, smooth camera motion, reflective skyscrapers",
    "duration": 5,
    "quality": "720p",
    "aspect_ratio": "16:9",
    "generate_audio": true
  }'
```

## What Is Seedance 2.5 Gateway Service?

Seedance 2.5 Gateway Service is a video generation gateway service for creating AI videos from text prompts, images, and multimodal references. Through EvoLink.ai, developers can access the full Seedance 2.0 model family with one consistent API workflow:

- create a generation task
- receive a task ID immediately
- poll task status or receive a callback
- download the generated video result

This repository is designed for developers who want to:

- understand the current Seedance 2 API path while Seedance 2.5 early access is rolling out
- compare text-to-video, image-to-video, and reference-to-video modes
- understand the difference between standard and fast models
- copy production-ready request examples
- estimate pricing before shipping
- discover related Seedance resources across the EvoLinkAI GitHub ecosystem

## Current Seedance 2 API Models

### Standard models

- `seedance-2.0-text-to-video`
- `seedance-2.0-image-to-video`
- `seedance-2.0-reference-to-video`

### Fast models

- `seedance-2.0-fast-text-to-video`
- `seedance-2.0-fast-image-to-video`
- `seedance-2.0-fast-reference-to-video`

## Create a Video Task

Create a Seedance 2.0 video task with a single API call:

```bash
export EVOLINK_API_KEY="your_key_here"

curl --request POST \
  --url https://api.evolink.ai/v1/videos/generations \
  --header "Authorization: Bearer ${EVOLINK_API_KEY}" \
  --header 'Content-Type: application/json' \
  --data '{
    "model": "seedance-2.0-text-to-video",
    "prompt": "A cinematic aerial shot of a futuristic city at sunrise, soft clouds, reflective skyscrapers, smooth camera motion",
    "duration": 5,
    "quality": "720p",
    "aspect_ratio": "16:9",
    "generate_audio": true
  }'
```

Example response:

```json
{
  "id": "task-unified-1774857405-abc123",
  "model": "seedance-2.0-text-to-video",
  "object": "video.generation.task",
  "status": "pending",
  "progress": 0,
  "type": "video"
}
```

## Full First-Run Flow

Seedance generation is asynchronous. A production integration should create a task, store the task ID, poll or receive a callback, and then save the final video URL.

```bash
export EVOLINK_API_KEY="your_key_here"
bash examples/curl/complete-flow.sh
```

Complete examples:

- [cURL complete flow](./examples/curl/complete-flow.sh)
- [Python complete flow](./examples/python/complete_flow.py)
- [JavaScript complete flow](./examples/javascript/complete-flow.mjs)

## Unified API Workflow

All Seedance 2.0 models use the same task-based workflow.

### 1. Create a generation task

```http
POST https://api.evolink.ai/v1/videos/generations
```

### 2. Query task status

```http
GET https://api.evolink.ai/v1/tasks/{task_id}
```

### 3. Retrieve results

When the task is completed, the response returns generated video URLs in the result payload.

### 4. Optional callback

You can pass `callback_url` in the create request if you want asynchronous notifications instead of polling only.

Detailed lifecycle docs:

- [Response Schema](./docs/response-schema.md)
- [Error Handling](./docs/errors.md)
- [Callback / Webhook](./docs/callbacks.md)

## Model Comparison

| Model | Input Type | Best For | Notes |
|---|---|---|---|
| `seedance-2.0-text-to-video` | text only | prompt-first video generation | supports optional web search |
| `seedance-2.0-image-to-video` | 1-2 images | first-frame or first/last-frame animation | ideal for image animation workflows |
| `seedance-2.0-reference-to-video` | images, videos, audio, text | advanced multimodal generation and editing | best for editing, extension, and guided generation |
| `seedance-2.0-fast-text-to-video` | text only | faster prompt-based generation | same basic workflow as standard text model |
| `seedance-2.0-fast-image-to-video` | 1-2 images | faster image animation | supports more image formats than the standard image model |
| `seedance-2.0-fast-reference-to-video` | images, videos, audio, text | faster multimodal generation | strong default for quick iteration |

## Core Request Parameters

| Parameter | Type | Description |
|---|---|---|
| `model` | string | selects the Seedance 2.0 model |
| `prompt` | string | generation prompt, supported across all model families |
| `duration` | integer | output video duration, `4-15` seconds |
| `quality` | string | `480p`, `720p`, or `1080p`; `1080p` is only supported by standard models |
| `aspect_ratio` | string | `16:9`, `9:16`, `1:1`, `4:3`, `3:4`, `21:9`, or `adaptive` |
| `generate_audio` | boolean | whether synchronized audio should be generated |
| `callback_url` | string | optional HTTPS callback URL |

## Mode-by-Mode Guide

### Text to Video

Use `seedance-2.0-text-to-video` or `seedance-2.0-fast-text-to-video` when you want to generate a video from prompt text only.

Key points:
- no image, video, or audio inputs
- supports optional `model_params.web_search`
- good for concept generation and trend-aware prompts

Docs:
- [Text-to-Video Guide](./docs/text-to-video.md)

### Image to Video

Use `seedance-2.0-image-to-video` or `seedance-2.0-fast-image-to-video` when you want to animate one or two images.

Key points:
- `image_urls` accepts 1-2 images
- 1 image = first-frame animation
- 2 images = first-frame to last-frame transition
- useful for marketing, product visuals, social posts, and stylized motion clips

Docs:
- [Image-to-Video Guide](./docs/image-to-video.md)

### Reference to Video

Use `seedance-2.0-reference-to-video` or `seedance-2.0-fast-reference-to-video` for the most control.

Key points:
- supports `image_urls`, `video_urls`, and `audio_urls`
- can create new outputs from multimodal references
- can extend, edit, or recompose videos
- input reference videos affect billing

Docs:
- [Reference-to-Video Guide](./docs/reference-to-video.md)
- [Fast Models Guide](./docs/fast-models.md)

## Seedance 2.0 Gateway Service Pricing

### Output pricing

For text-to-video and image-to-video tasks, pricing is based on output duration:

```text
cost = output video duration in seconds × resolution price
```

| Resolution | Price |
|---|---:|
| `480p` | 4.63 credits / second |
| `720p` | 10.00 credits / second |

### Reference video pricing

For reference-to-video tasks, input reference video duration is also billed:

```text
cost = (input reference video duration + output video duration) × resolution price
```

### Extra notes

- audio generation has no extra charge
- `web_search` costs `0.04` credits per actual search call
- 1 credit = 10,000 UC = ¥0.10

Detailed breakdown:
- [Pricing Guide](./docs/pricing.md)

## Example Requests

### Text-to-video example

```bash
curl --request POST \
  --url https://api.evolink.ai/v1/videos/generations \
  --header "Authorization: Bearer ${EVOLINK_API_KEY}" \
  --header 'Content-Type: application/json' \
  --data '{
    "model": "seedance-2.0-text-to-video",
    "prompt": "A macro shot of a glass frog on a green leaf, focus shifting to its transparent body and visible beating heart",
    "duration": 8,
    "quality": "720p",
    "aspect_ratio": "16:9",
    "generate_audio": true
  }'
```

### Image-to-video example

```bash
curl --request POST \
  --url https://api.evolink.ai/v1/videos/generations \
  --header "Authorization: Bearer ${EVOLINK_API_KEY}" \
  --header 'Content-Type: application/json' \
  --data '{
    "model": "seedance-2.0-image-to-video",
    "prompt": "The camera slowly pushes in as the still image comes alive",
    "image_urls": ["https://example.com/first-frame.jpg"],
    "duration": 5,
    "aspect_ratio": "adaptive"
  }'
```

### Reference-to-video example

```bash
curl --request POST \
  --url https://api.evolink.ai/v1/videos/generations \
  --header "Authorization: Bearer ${EVOLINK_API_KEY}" \
  --header 'Content-Type: application/json' \
  --data '{
    "model": "seedance-2.0-reference-to-video",
    "prompt": "Use video 1 camera movement throughout the clip and audio 1 as background music",
    "image_urls": ["https://example.com/ref1.jpg"],
    "video_urls": ["https://example.com/reference.mp4"],
    "audio_urls": ["https://example.com/bgm.mp3"],
    "duration": 10,
    "quality": "720p",
    "aspect_ratio": "16:9",
    "generate_audio": true
  }'
```

More code:
- [curl examples](./examples/curl)
- [Node.js examples](./examples/nodejs)
- [Python examples](./examples/python)

## Python Example

```python
import os
import requests
import time

api_key = os.environ["EVOLINK_API_KEY"]
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

create_resp = requests.post(
    "https://api.evolink.ai/v1/videos/generations",
    headers=headers,
    json={
        "model": "seedance-2.0-text-to-video",
        "prompt": "A cinematic drone shot above snowy mountains at sunrise",
        "duration": 5,
        "quality": "720p",
        "aspect_ratio": "16:9"
    }
).json()

task_id = create_resp["id"]

while True:
    task = requests.get(
        f"https://api.evolink.ai/v1/tasks/{task_id}",
        headers={"Authorization": f"Bearer {api_key}"}
    ).json()

    if task.get("status") == "completed":
        print(task)
        break
    elif task.get("status") == "failed":
        print(task)
        break

    time.sleep(3)
```

## JavaScript Example

```js
const createResp = await fetch("https://api.evolink.ai/v1/videos/generations", {
  method: "POST",
  headers: {
    Authorization: `Bearer ${process.env.EVOLINK_API_KEY}`,
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    model: "seedance-2.0-fast-text-to-video",
    prompt: "A neon-lit cyberpunk alley in the rain, cinematic camera movement",
    duration: 5,
    quality: "720p",
    aspect_ratio: "16:9",
    generate_audio: true
  })
});

const task = await createResp.json();
console.log(task);
```

For production-ready polling and error handling, use [examples/javascript/complete-flow.mjs](./examples/javascript/complete-flow.mjs).

## Best Use Cases

Seedance 2.0 Gateway Service is well suited for:

- AI video generation apps
- creative tooling and editor workflows
- image animation pipelines
- video ad generation
- social media content creation
- product demo generation
- multimodal video editing workflows
- prototype filmmaking and concept visualization

## FAQ

### Is Seedance 2.0 Gateway Service synchronous?
No. Seedance 2.0 generation is asynchronous. You create a task first, then query task status later or use a callback URL.

### What is the difference between standard and fast models?
Fast models follow the same request pattern but are positioned for quicker iteration. You should compare them by workflow needs, latency expectations, and output preference.

### Can I generate video from only text?
Yes. Use `seedance-2.0-text-to-video` or `seedance-2.0-fast-text-to-video`.

### Can I animate one image or create a start/end frame transition?
Yes. Use image-to-video. One image becomes the first frame. Two images become first and last frames.

### Can I edit or extend an existing video?
Yes. Use reference-to-video with `video_urls` and a guiding prompt.

### Does reference input affect billing?
Yes. Reference video duration is included in billing for reference-to-video tasks.

### How long are result URLs valid?
Generated video URLs are valid for 24 hours. Save them promptly.

## Repository Structure

```text
Seedance-2.5-Gateway-Service/
├── README.md
├── assets/
│   └── banner.jpg
├── docs/
│   ├── text-to-video.md
│   ├── image-to-video.md
│   ├── reference-to-video.md
│   ├── fast-models.md
│   ├── response-schema.md
│   ├── errors.md
│   ├── callbacks.md
│   └── pricing.md
└── examples/
    ├── curl/
    ├── javascript/
    └── python/
```

## Documentation

- [Text-to-Video Guide](./docs/text-to-video.md)
- [Image-to-Video Guide](./docs/image-to-video.md)
- [Reference-to-Video Guide](./docs/reference-to-video.md)
- [Fast Models Guide](./docs/fast-models.md)
- [Response Schema](./docs/response-schema.md)
- [Error Handling](./docs/errors.md)
- [Callback / Webhook](./docs/callbacks.md)
- [Pricing](./docs/pricing.md)

These docs now cover both **standard** and **fast** variants for text-to-video, image-to-video, and reference-to-video.

## Related Seedance Repositories

- [Seedance 2.5 Gateway Service: Early Access and Current API Path](https://github.com/EvoLinkAI/Seedance-2.5-Gateway-Service) — this repository
- [Seedance 2 Video Gen Skill for OpenClaw](https://github.com/EvoLinkAI/seedance2-video-gen-skill-for-openclaw) — OpenClaw skill integration for Seedance workflows
- [Awesome Seedance 2 Guide](https://github.com/EvoLinkAI/awesome-seedance-2.5-guide) — broader Seedance ecosystem guide and discovery entry

## Related Links

- [Seedance 2.5 Early Access](https://evolink.ai/launch/seedance-2-5?utm_source=github&utm_medium=readme&utm_campaign=Seedance-2.5-Gateway-Service)
- [Get your API key](https://evolink.ai/signup?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-api)
- [EvoLink.ai](https://evolink.ai?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-api)

> Please review [Regional Availability](./docs/regional-availability.md) before integration.

## License

MIT
