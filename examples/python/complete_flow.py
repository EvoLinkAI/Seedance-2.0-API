import os
import time
import requests

api_key = os.environ.get("EVOLINK_API_KEY")
if not api_key:
    raise SystemExit("Set EVOLINK_API_KEY first")

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
}

create_resp = requests.post(
    "https://api.evolink.ai/v1/videos/generations",
    headers=headers,
    json={
        "model": "seedance-2.0-text-to-video",
        "prompt": "A cinematic aerial shot of a futuristic city at sunrise",
        "duration": 5,
        "quality": "720p",
        "aspect_ratio": "16:9",
        "generate_audio": True,
    },
    timeout=60,
)

if create_resp.status_code >= 400:
    raise SystemExit(f"Create task failed: {create_resp.status_code} {create_resp.text}")

task = create_resp.json()
task_id = task.get("id")
if not task_id:
    raise SystemExit(f"Create task did not return id: {task}")

for _ in range(120):
    poll_resp = requests.get(
        f"https://api.evolink.ai/v1/tasks/{task_id}",
        headers={"Authorization": f"Bearer {api_key}"},
        timeout=30,
    )
    if poll_resp.status_code >= 400:
        raise SystemExit(f"Poll failed: {poll_resp.status_code} {poll_resp.text}")

    task = poll_resp.json()
    status = task.get("status")
    if status == "completed":
        print(task)
        raise SystemExit(0)
    if status == "failed":
        raise SystemExit(f"Task failed: {task}")
    time.sleep(3)

raise SystemExit(f"Timed out waiting for task {task_id}")
