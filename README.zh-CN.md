[English](./README.md) | [简体中文](./README.zh-CN.md) | [繁體中文](./README.zh-TW.md) | [Español](./README.es.md) | [Deutsch](./README.de.md) | [Français](./README.fr.md) | [日本語](./README.ja.md) | [한국어](./README.ko.md) | [Türkçe](./README.tr.md) | [Русский](./README.ru.md)

# Seedance 2.0 Gateway Service：价格、模型与视频生成指南

<p align="center">
  <a href="https://evolink.ai/seedance-2-0?utm_source=github&utm_medium=banner&utm_campaign=seedance-2-api">
    <img src="./assets/banner.jpg" alt="Seedance 2.0 Human Face Now Available Try Now" width="100%" />
  </a>
</p>

<p align="center">
  <strong>Seedance 2.0<br>Human Face Now Available<br>Try Now</strong>
</p>

<p align="center">
  在一个统一入口里查看 Seedance 2.0 Gateway Service 价格、模型、text-to-video、image-to-video 和 reference-to-video 用法。
</p>

<p align="left">
  <a href="https://evolink.ai/seedance-2-0?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-api">查看 Seedance 2.0 价格</a> ·
  <a href="https://evolink.ai/signup?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-api">获取 API Key</a> ·
  <a href="https://docs.evolink.ai?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-api">查看 API 文档</a>
</p>

## 这是什么？

这个仓库聚焦 Seedance 2.0 Gateway Service 的价格、模型差异、接入方式，以及三种核心能力：

- text-to-video
- image-to-video
- reference-to-video

同时也覆盖 Fast 系列模型，方便开发者快速比较：

- `seedance-2.0-text-to-video`
- `seedance-2.0-image-to-video`
- `seedance-2.0-reference-to-video`
- `seedance-2.0-fast-text-to-video`
- `seedance-2.0-fast-image-to-video`
- `seedance-2.0-fast-reference-to-video`

## 快速开始

```bash
curl --request POST \
  --url https://api.evolink.ai/v1/videos/generations \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data '{
    "model": "seedance-2.0-text-to-video",
    "prompt": "未来城市日出航拍镜头，云层柔和，玻璃幕墙反光，镜头平滑推进",
    "duration": 5,
    "quality": "720p",
    "aspect_ratio": "16:9",
    "generate_audio": true
  }'
```

## 统一工作流

### 1. 创建任务

```http
POST https://api.evolink.ai/v1/videos/generations
```

### 2. 查询任务状态

```http
GET https://api.evolink.ai/v1/tasks/{task_id}
```

### 3. 获取结果

任务完成后会返回视频结果 URL。

### 4. 可选回调

如果你不想只靠轮询，可以在创建任务时传入 `callback_url`。

## Seedance 2.0 Gateway Service 价格

### text-to-video / image-to-video

```text
费用 = 输出视频时长 × 分辨率单价
```

| 分辨率 | 价格 |
|---|---:|
| `480p` | 5.556 积分 / 秒 |
| `720p` | 12.00 积分 / 秒 |

### reference-to-video

如果输入了参考视频，输入视频时长也参与计费：

```text
费用 = (输入参考视频时长 + 输出视频时长) × 分辨率单价
```

### 其他说明
- 音频不额外收费
- `web_search` 按实际调用次数计费
- 智能时长 `-1` 会先预扣，再按实际时长结算
- 1 积分 = 10,000 UC = ¥0.10

## 这个仓库里有什么

- Seedance 2.0 Gateway Service 价格信息
- 模型对比
- curl / Node.js / Python 示例
- docs 目录下的能力拆解文档
- Seedance 生态仓库联动入口

## 相关 Seedance 仓库

- [Seedance 2.0 Gateway Service: Price and Guide](https://github.com/EvoLinkAI/Seedance-2.0-Gateway-Service)
- [Seedance 2 Video Gen Skill for OpenClaw](https://github.com/EvoLinkAI/seedance2-video-gen-skill-for-openclaw)
- [Awesome Seedance 2 Guide](https://github.com/EvoLinkAI/awesome-seedance-2-guide)

## 完整英文文档

如果要看完整长文档、FAQ、更多参数和示例，请直接查看：

- [README.md](./README.md)

---

> ⚠️ 接入前请先查阅 [区域可用性](./docs/regional-availability.zh-CN.md)。

> **Now Available：** 现在就可以先按文档完成接入。等 Seedance Gateway Service 正式开放后，我们会通知 Now Available 用户。
