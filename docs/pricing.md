# Seedance 2.0 Pricing

This page summarizes the latest pricing currently documented in this repository.

## Standard models

### Text-to-Video

```text
Cost = Output video duration (sec) × Resolution unit price
```

| Resolution | Unit Price (USD) | Unit Price (Credits) |
|:----------:|:----------------:|:--------------------:|
| 480p | $0.0919 /sec | 6.251 credits/sec |
| 720p | $0.1985 /sec | 13.50 credits/sec |
| Web Search | $0.0006 /call | 0.04 credits/call |

> Web search is billed separately, charged only when actually triggered. A single request may trigger multiple searches.

### Image-to-Video

```text
Cost = Output video duration (sec) × Resolution unit price
```

| Resolution | Unit Price (USD) | Unit Price (Credits) |
|:----------:|:----------------:|:--------------------:|
| 480p | $0.0919 /sec | 6.251 credits/sec |
| 720p | $0.1985 /sec | 13.50 credits/sec |

### Reference-to-Video

**Without video input:**

```text
Cost = Output video duration (sec) × Resolution unit price
```

| Resolution | Unit Price (USD) | Unit Price (Credits) |
|:----------:|:----------------:|:--------------------:|
| 480p | $0.0919 /sec | 6.251 credits/sec |
| 720p | $0.1985 /sec | 13.50 credits/sec |

**With video input:**

```text
Billable input duration = max(Total input video duration, Output video duration)
Cost = (Billable input duration + Output video duration) (sec) × Resolution unit price
```

| Resolution | Unit Price (USD) | Unit Price (Credits) |
|:----------:|:----------------:|:--------------------:|
| 480p | $0.0560 /sec | 3.807 credits/sec |
| 720p | $0.1209 /sec | 8.222 credits/sec |

> Example: Output 10 sec (720p), input 5 sec reference video → Billable input duration = max(5, 10) = 10 sec → Cost = (10 + 10) × $0.1209 = $2.42

## Fast models

### Fast Text-to-Video

```text
Cost = Output video duration (sec) × Resolution unit price
```

| Resolution | Unit Price (USD) | Unit Price (Credits) |
|:----------:|:----------------:|:--------------------:|
| 480p | $0.0745 /sec | 5.063 credits/sec |
| 720p | $0.1608 /sec | 10.935 credits/sec |
| Web Search | $0.0006 /call | 0.04 credits/call |

> Web search is billed separately, charged only when actually triggered. A single request may trigger multiple searches.

### Fast Image-to-Video

```text
Cost = Output video duration (sec) × Resolution unit price
```

| Resolution | Unit Price (USD) | Unit Price (Credits) |
|:----------:|:----------------:|:--------------------:|
| 480p | $0.0745 /sec | 5.063 credits/sec |
| 720p | $0.1608 /sec | 10.935 credits/sec |

### Fast Reference-to-Video

**Without video input:**

```text
Cost = Output video duration (sec) × Resolution unit price
```

| Resolution | Unit Price (USD) | Unit Price (Credits) |
|:----------:|:----------------:|:--------------------:|
| 480p | $0.0745 /sec | 5.063 credits/sec |
| 720p | $0.1608 /sec | 10.935 credits/sec |

**With video input:**

```text
Billable input duration = max(Total input video duration, Output video duration)
Cost = (Billable input duration + Output video duration) (sec) × Resolution unit price
```

| Resolution | Unit Price (USD) | Unit Price (Credits) |
|:----------:|:----------------:|:--------------------:|
| 480p | $0.0443 /sec | 3.012 credits/sec |
| 720p | $0.0957 /sec | 6.506 credits/sec |

> Example: Output 10 sec (720p), input 5 sec reference video → Billable input duration = max(5, 10) = 10 sec → Cost = (10 + 10) × $0.0957 = $1.91

## Billing notes

- Text-to-video and image-to-video are billed by actual output video duration and selected resolution.
- Reference-to-video with video inputs uses `max(total input video duration, output video duration)` as the billable input duration.
- Generated audio does not incur additional charges.
- Web search is billed separately and only when actually triggered.
- Video duration range is 4 to 15 seconds.
- Generated video URLs are valid for 24 hours.
