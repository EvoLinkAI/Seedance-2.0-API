# Seedance 2.0 Pricing Guide

## Resolution pricing

| Resolution | Price |
|---|---:|
| `480p` | 4.63 credits / second |
| `720p` | 10.00 credits / second |

## Standard pricing rule

For text-to-video and image-to-video:

```text
cost = output video duration × resolution price
```

## Reference-to-video pricing rule

For reference-to-video with input videos:

```text
cost = (input reference video duration + output video duration) × resolution price
```

### Example

If you upload two reference videos with total duration `8s` and generate a `10s` output at `720p`:

```text
cost = (8 + 10) × 10 = 180 credits
```

## Additional billing notes

- audio generation has no extra charge
- web search costs `0.04` credits per actual search call
- smart duration (`-1`) reserves 10 seconds first, then settles against the actual duration
- 1 credit = 10,000 UC = ¥0.10
