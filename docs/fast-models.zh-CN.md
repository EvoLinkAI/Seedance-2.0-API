# Seedance 2.0 Fast 模型指南

Seedance 2.0 Fast 系列与标准版使用相同的输入模式，但更适合快速迭代工作流。

The Seedance 2.0 fast models mirror the same input patterns as the standard models, but are positioned for faster iteration workflows.

## Fast model IDs

- `seedance-2.0-fast-text-to-video`
- `seedance-2.0-fast-image-to-video`
- `seedance-2.0-fast-reference-to-video`

## When to use fast models

Use fast models when you want:

- quicker creative iteration
- faster prompt testing
- shorter feedback loops in prototyping
- lower waiting time during batch ideation

## Input parity

The fast family maps directly to the standard family:

| Standard | Fast |
|---|---|
| `seedance-2.0-text-to-video` | `seedance-2.0-fast-text-to-video` |
| `seedance-2.0-image-to-video` | `seedance-2.0-fast-image-to-video` |
| `seedance-2.0-reference-to-video` | `seedance-2.0-fast-reference-to-video` |

## Docs navigation

- [Text-to-Video Guide](./text-to-video.md)
- [Image-to-Video Guide](./image-to-video.md)
- [Reference-to-Video Guide](./reference-to-video.md)
- [Pricing](./pricing.md)

## Notable format difference

Fast image-related models accept more input image formats in the provided docs, including:

- `bmp`
- `tiff`
- `gif`

## Recommendation

If you are building a public demo, internal creative tool, or prompt-iteration workflow, fast models are a strong default starting point.

---

> **Now Available:** Seedance Gateway Service can be integrated today. Use the examples in this repo to create tasks, poll task status, and retrieve generated video URLs.