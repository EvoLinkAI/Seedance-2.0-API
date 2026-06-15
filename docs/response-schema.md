# Seedance 2.0 Response Schema

## Create Task Response

```json
{
  "id": "task-unified-1774857405-abc123",
  "model": "seedance-2.0-text-to-video",
  "object": "video.generation.task",
  "status": "pending",
  "progress": 0,
  "type": "video",
  "task_info": {
    "can_cancel": true,
    "estimated_time": 165,
    "video_duration": 5
  },
  "usage": {
    "billing_rule": "per_second",
    "credits_reserved": 50,
    "user_group": "default"
  }
}
```

## Completed Task Response

```json
{
  "id": "task-unified-1774857405-abc123",
  "status": "completed",
  "progress": 100,
  "model": "seedance-2.0-text-to-video",
  "results": [
    "https://media.evolink.ai/..."
  ]
}
```

## Failed Task Response

```json
{
  "id": "task-unified-1774857405-abc123",
  "status": "failed",
  "error": {
    "code": "invalid_request",
    "message": "Explain what went wrong."
  }
}
```

Generated video URLs are temporary. Save completed results to your own storage promptly.
