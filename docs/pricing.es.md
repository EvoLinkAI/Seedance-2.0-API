# Guía de precios de Seedance 2.0

Esta página resume los precios documentados actualmente en este repositorio.

This page summarizes the pricing currently documented in this repository.

## Standard models

### Text-to-Video

| Resolution | Unit Price |
|:----------:|:----------:|
| 480p | $0.0919 (6.251 credits) /sec |
| 720p | $0.1985 (13.50 credits) /sec |
| WebSearch | $0.0006 (0.04 credits) /call |

### Image-to-Video

| Resolution | Unit Price |
|:----------:|:----------:|
| 480p | $0.0919 (6.251 credits) /sec |
| 720p | $0.1985 (13.50 credits) /sec |

### Reference-to-Video

**Without video input:**

| Resolution | Unit Price |
|:----------:|:----------:|
| 480p | $0.0919 (6.251 credits) /sec |
| 720p | $0.1985 (13.50 credits) /sec |

**With video input:**

| Resolution | Unit Price |
|:----------:|:----------:|
| 480p | $0.0560 (3.807 credits) /sec |
| 720p | $0.1209 (8.222 credits) /sec |

## Fast models

### Fast Text-to-Video

| Resolution | Unit Price |
|:----------:|:----------:|
| 480p | $0.0745 (5.063 credits) /sec |
| 720p | $0.1608 (10.935 credits) /sec |
| WebSearch | $0.0006 (0.04 credits) /call |

### Fast Image-to-Video

| Resolution | Unit Price |
|:----------:|:----------:|
| 480p | $0.0745 (5.063 credits) /sec |
| 720p | $0.1608 (10.935 credits) /sec |

### Fast Reference-to-Video

**Without video input:**

| Resolution | Unit Price |
|:----------:|:----------:|
| 480p | $0.0745 (5.063 credits) /sec |
| 720p | $0.1608 (10.935 credits) /sec |

**With video input:**

| Resolution | Unit Price |
|:----------:|:----------:|
| 480p | $0.0443 (3.012 credits) /sec |
| 720p | $0.0957 (6.506 credits) /sec |

## Billing notes

- Text-to-video and image-to-video are billed by output video duration and selected resolution.
- Reference-to-video with video inputs uses `max(total input video duration, output video duration)` as the billable input duration.
- Generated audio does not incur additional charges.
- Web search is billed separately and only when actually triggered.