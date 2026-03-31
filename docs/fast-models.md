# Seedance 2.0 Fast Models Guide

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

## Notable format difference

Fast image-related models accept more input image formats in the provided docs, including:

- `bmp`
- `tiff`
- `gif`

## Recommendation

If you are building a public demo, internal creative tool, or prompt-iteration workflow, fast models are a strong default starting point.
