# Seedance 2.0 Callback / Webhook

Pass `callback_url` in the create request if you want EvoLink to notify your server when the task completes, fails, or is cancelled.

```json
{
  "callback_url": "https://your-server.example.com/evolink-webhook"
}
```

Requirements:

- Use HTTPS.
- Use a publicly reachable endpoint.
- Do not use localhost or private IP addresses for production callbacks.
- Keep the URL under 2048 characters.
- Return a 2xx response quickly.
- Expect a 10 second callback timeout.
- EvoLink retries failed callbacks up to 3 times, at roughly 1, 2, and 4 seconds after failure.
- Store the task ID so you can poll `GET /v1/tasks/{task_id}` as a fallback.

Example callback payload:

```json
{
  "id": "task-unified-1774857405-abc123",
  "status": "completed",
  "model": "seedance-2.0-text-to-video",
  "results": [
    "https://media.evolink.ai/..."
  ]
}
```
