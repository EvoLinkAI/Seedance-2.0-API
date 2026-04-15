[English](./README.md) | [简体中文](./README.zh-CN.md) | [繁體中文](./README.zh-TW.md) | [Español](./README.es.md) | [Deutsch](./README.de.md) | [Français](./README.fr.md) | [日本語](./README.ja.md) | [한국어](./README.ko.md) | [Türkçe](./README.tr.md) | [Русский](./README.ru.md)

# Seedance 2.0 Gateway Service：價格、模型與影片生成指南

<p align="center">
  <a href="https://evolink.ai/seedance-2-0?utm_source=github&utm_medium=banner&utm_campaign=seedance-2-api">
    <img src="./assets/banner.jpg" alt="Seedance 2.0 Human Face Now Available Try Now" width="100%" />
  </a>
</p>

<p align="center">
  <strong>Seedance 2.0<br>Human Face Now Available<br>Try Now</strong>
</p>

<p align="center">
  在同一份指南中掌握 Seedance 2.0 Gateway Service 價格、模型、text-to-video、image-to-video 與 reference-to-video。
</p>

<p align="left">
  <a href="https://evolink.ai/seedance-2-0?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-api">查看 Seedance 2.0 價格</a> ·
  <a href="https://evolink.ai/signup?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-api">取得 API Key</a> ·
  <a href="https://docs.evolink.ai?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-api">閱讀 API 文件</a>
</p>

## 什麼是 Seedance 2.0 Gateway Service？

Seedance 2.0 Gateway Service 是一套 AI 影片生成服務，可透過文字提示、圖片與多模態參考素材建立影片。透過 EvoLink.ai，開發者可以用一致的工作流程存取完整的 Seedance 2.0 模型家族：

- 建立生成任務
- 立即取得任務 ID
- 輪詢任務狀態或接收回呼
- 下載最終影片結果

此倉庫特別適合想要：

- 快速整合 Seedance 2.0
- 比較 text-to-video、image-to-video、reference-to-video
- 理解標準版與 fast 模型差異
- 複製可直接使用的請求範例
- 在正式接入前先估算價格
- 尋找 EvoLinkAI Seedance 生態中的其他相關資源

## 支援的 Seedance 2.0 模型

### 標準模型

- `seedance-2.0-text-to-video`
- `seedance-2.0-image-to-video`
- `seedance-2.0-reference-to-video`

### Fast 模型

- `seedance-2.0-fast-text-to-video`
- `seedance-2.0-fast-image-to-video`
- `seedance-2.0-fast-reference-to-video`

## 快速開始

使用一次呼叫建立 Seedance 2.0 影片生成任務：

```bash
curl --request POST \
  --url https://api.evolink.ai/v1/videos/generations \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data '{
    "model": "seedance-2.0-text-to-video",
    "prompt": "未來城市日出航拍鏡頭，雲層柔和，玻璃大樓反光，鏡頭平滑推進",
    "duration": 5,
    "quality": "720p",
    "aspect_ratio": "16:9",
    "generate_audio": true
  }'
```

範例回應：

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

## 統一工作流程

所有 Seedance 2.0 模型都使用同一套任務型工作流程。

### 1. 建立生成任務

```http
POST https://api.evolink.ai/v1/videos/generations
```

### 2. 查詢任務狀態

```http
GET https://api.evolink.ai/v1/tasks/{task_id}
```

### 3. 取得結果

任務完成後，回應中會在結果欄位提供生成影片的 URL。

### 4. 可選回呼

若不想只靠輪詢，可在建立任務時傳入 `callback_url`。

## 模型比較

| 模型 | 輸入類型 | 適合場景 | 備註 |
|---|---|---|---|
| `seedance-2.0-text-to-video` | 純文字 | 以提示詞為主的影片生成 | 支援可選 web search |
| `seedance-2.0-image-to-video` | 1–2 張圖片 | 首幀動畫或首尾幀過渡 | 適合圖片動畫工作流 |
| `seedance-2.0-reference-to-video` | 圖片、影片、音訊、文字 | 進階多模態生成與編輯 | 最適合影片編輯、延展與引導生成 |
| `seedance-2.0-fast-text-to-video` | 純文字 | 更快速的提示詞生成 | 與標準版流程一致 |
| `seedance-2.0-fast-image-to-video` | 1–2 張圖片 | 更快速的圖片動畫 | 支援更多圖片格式 |
| `seedance-2.0-fast-reference-to-video` | 圖片、影片、音訊、文字 | 更快速的多模態生成 | 適合快速迭代 |

## 核心請求參數

| 參數 | 類型 | 說明 |
|---|---|---|
| `model` | string | 指定 Seedance 2.0 模型 |
| `prompt` | string | 所有模型家族都支援的生成提示詞 |
| `duration` | integer | 輸出影片長度，`4-15` 秒，或 `-1` 表示智慧時長 |
| `quality` | string | `480p` 或 `720p` |
| `aspect_ratio` | string | `16:9`、`9:16`、`1:1`、`4:3`、`3:4`、`21:9` 或 `adaptive` |
| `generate_audio` | boolean | 是否生成同步音訊 |
| `callback_url` | string | 可選 HTTPS 回呼網址 |

## 模式說明

### Text to Video

當你只想用文字提示生成影片時，請使用 `seedance-2.0-text-to-video` 或 `seedance-2.0-fast-text-to-video`。

重點：
- 不接受 image、video、audio 輸入
- 支援可選的 `model_params.web_search`
- 適合概念生成與時效性內容

文件：
- [Text-to-Video Guide](./docs/text-to-video.md)

### Image to Video

當你想用一張或兩張圖片生成影片時，請使用 `seedance-2.0-image-to-video` 或 `seedance-2.0-fast-image-to-video`。

重點：
- `image_urls` 接受 1–2 張圖片
- 1 張圖 = 首幀動畫
- 2 張圖 = 首幀到尾幀過渡
- 適合行銷視覺、產品動畫、社群內容

文件：
- [Image-to-Video Guide](./docs/image-to-video.md)

### Reference to Video

若需要最高控制度，請使用 `seedance-2.0-reference-to-video` 或 `seedance-2.0-fast-reference-to-video`。

重點：
- 支援 `image_urls`、`video_urls`、`audio_urls`
- 可用多模態素材引導全新生成
- 可延長、編輯或重組影片
- 參考影片時長會影響計費

文件：
- [Reference-to-Video Guide](./docs/reference-to-video.md)
- [Fast Models Guide](./docs/fast-models.md)

## Seedance 2.0 Gateway Service 價格

### 輸出計費

對於 text-to-video 與 image-to-video，計費依輸出影片長度計算：

```text
費用 = 輸出影片秒數 × 解析度單價
```

| 解析度 | 價格 |
|---|---:|
| `480p` | 5.556 積分 / 秒 |
| `720p` | 12.00 積分 / 秒 |

### Reference 視訊計費

對於 reference-to-video，輸入參考影片時長也會納入計費：

```text
費用 = (輸入參考影片時長 + 輸出影片時長) × 解析度單價
```

### 補充說明

- 音訊生成功能不額外收費
- `web_search` 每次實際搜尋收費 `0.04` 積分
- 智慧時長 `-1` 會先預扣 10 秒，再依實際結果結算
- 1 積分 = 10,000 UC = ¥0.10

詳細說明：
- [Pricing Guide](./docs/pricing.md)

## 請求範例

### Text-to-video 範例

```bash
curl --request POST \
  --url https://api.evolink.ai/v1/videos/generations \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data '{
    "model": "seedance-2.0-text-to-video",
    "prompt": "一隻玻璃蛙停在綠葉上的微距鏡頭，焦點逐步轉向透明腹部與跳動的心臟",
    "duration": 8,
    "quality": "720p",
    "aspect_ratio": "16:9",
    "generate_audio": true
  }'
```

### Image-to-video 範例

```bash
curl --request POST \
  --url https://api.evolink.ai/v1/videos/generations \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data '{
    "model": "seedance-2.0-image-to-video",
    "prompt": "鏡頭緩慢推近，靜態畫面逐漸活起來",
    "image_urls": ["https://example.com/first-frame.jpg"],
    "duration": 5,
    "aspect_ratio": "adaptive"
  }'
```

### Reference-to-video 範例

```bash
curl --request POST \
  --url https://api.evolink.ai/v1/videos/generations \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data '{
    "model": "seedance-2.0-reference-to-video",
    "prompt": "全程沿用影片1的運鏡，並將音訊1作為背景音樂",
    "image_urls": ["https://example.com/ref1.jpg"],
    "video_urls": ["https://example.com/reference.mp4"],
    "audio_urls": ["https://example.com/bgm.mp3"],
    "duration": 10,
    "quality": "720p",
    "aspect_ratio": "16:9",
    "generate_audio": true
  }'
```

更多程式碼：
- [curl examples](./examples/curl)
- [Node.js examples](./examples/nodejs)
- [Python examples](./examples/python)

## Python 範例

```python
import requests
import time

headers = {
    "Authorization": "Bearer YOUR_API_KEY",
    "Content-Type": "application/json"
}

create_resp = requests.post(
    "https://api.evolink.ai/v1/videos/generations",
    headers=headers,
    json={
        "model": "seedance-2.0-text-to-video",
        "prompt": "日出時分飛越雪山的電影感空拍鏡頭",
        "duration": 5,
        "quality": "720p",
        "aspect_ratio": "16:9"
    }
).json()

task_id = create_resp["id"]

while True:
    task = requests.get(
        f"https://api.evolink.ai/v1/tasks/{task_id}",
        headers={"Authorization": "Bearer YOUR_API_KEY"}
    ).json()

    if task.get("status") == "completed":
        print(task)
        break
    elif task.get("status") == "failed":
        print(task)
        break

    time.sleep(3)
```

## JavaScript 範例

```js
const createResp = await fetch("https://api.evolink.ai/v1/videos/generations", {
  method: "POST",
  headers: {
    Authorization: `Bearer ${process.env.EVOLINK_API_KEY}`,
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    model: "seedance-2.0-fast-text-to-video",
    prompt: "雨夜霓虹巷道，電影感運鏡，路面有倒影",
    duration: 5,
    quality: "720p",
    aspect_ratio: "16:9",
    generate_audio: true
  })
});

const task = await createResp.json();
console.log(task);
```

## 適用場景

Seedance 2.0 Gateway Service 很適合：

- AI 影片生成應用
- 創作工具與編輯工作流
- 圖片轉動畫流程
- 廣告影片生成
- 社群媒體內容製作
- 產品展示影片
- 多模態影片編輯
- 影像概念驗證與前期製作

## FAQ

### Seedance 2.0 Gateway Service 是同步的嗎？
不是。Seedance 2.0 使用非同步任務流程。你先建立任務，再查詢狀態或使用 callback URL。

### 標準模型與 fast 模型有什麼差異？
fast 模型採用相同的請求模式，但更適合快速迭代。你可以依工作流、延遲需求與輸出偏好來選擇。

### 可以只用文字生成影片嗎？
可以，請使用 `seedance-2.0-text-to-video` 或 `seedance-2.0-fast-text-to-video`。

### 可以讓一張圖片動起來，或做首尾幀過渡嗎？
可以，請使用 image-to-video。1 張圖代表首幀，2 張圖代表首尾幀。

### 可以編輯或延長現有影片嗎？
可以，使用 reference-to-video 搭配 `video_urls` 與引導提示詞即可。

### 參考素材會影響計費嗎？
會。對 reference-to-video 而言，參考影片時長會納入計費。

### 結果 URL 會保留多久？
生成影片連結 24 小時內有效，請及時保存。

## 倉庫結構

```text
Seedance-2.0-Gateway-Service/
├── README.md
├── README.zh-CN.md
├── README.zh-TW.md
├── README.es.md
├── README.de.md
├── README.fr.md
├── README.ja.md
├── README.ko.md
├── README.tr.md
├── README.ru.md
├── assets/
│   └── banner.jpg
├── docs/
│   ├── text-to-video.md
│   ├── image-to-video.md
│   ├── reference-to-video.md
│   ├── fast-models.md
│   └── pricing.md
└── examples/
    ├── curl/
    ├── nodejs/
    └── python/
```

## 相關 Seedance 倉庫

- [Seedance 2.0 Gateway Service: Price and Guide](https://github.com/EvoLinkAI/Seedance-2.0-Gateway-Service)
- [Seedance 2 Video Gen Skill for OpenClaw](https://github.com/EvoLinkAI/seedance2-video-gen-skill-for-openclaw)
- [Awesome Seedance 2 Guide](https://github.com/EvoLinkAI/awesome-seedance-2-guide)

## 相關連結

- [Seedance 2.0 Pricing](https://evolink.ai/seedance-2-0?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-api)
- [Get API Key](https://evolink.ai/signup?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-api)
- [EvoLink.ai](https://evolink.ai?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-api)

## License

MIT

---

> ⚠️ 接入前請先查閱 [區域可用性](./docs/regional-availability.zh-TW.md)。

> **Now Available：** 現在就可以先依照文件完成接入。等 Seedance Gateway Service 正式開放後，我們會通知 Now Available 使用者。
