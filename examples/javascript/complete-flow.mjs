const apiKey = process.env.EVOLINK_API_KEY;
if (!apiKey) {
  throw new Error("Set EVOLINK_API_KEY first");
}

async function requestJson(url, options = {}) {
  const response = await fetch(url, options);
  const text = await response.text();
  const data = text ? JSON.parse(text) : {};
  if (!response.ok) {
    throw new Error(`${response.status} ${response.statusText}: ${JSON.stringify(data)}`);
  }
  return data;
}

const task = await requestJson("https://api.evolink.ai/v1/videos/generations", {
  method: "POST",
  headers: {
    Authorization: `Bearer ${apiKey}`,
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    model: "seedance-2.0-text-to-video",
    prompt: "A cinematic aerial shot of a futuristic city at sunrise",
    duration: 5,
    quality: "720p",
    aspect_ratio: "16:9",
    generate_audio: true
  })
});

if (!task.id) {
  throw new Error(`Create task did not return id: ${JSON.stringify(task)}`);
}

for (let attempt = 0; attempt < 120; attempt += 1) {
  const current = await requestJson(`https://api.evolink.ai/v1/tasks/${task.id}`, {
    headers: { Authorization: `Bearer ${apiKey}` }
  });

  if (current.status === "completed") {
    console.log(JSON.stringify(current, null, 2));
    process.exit(0);
  }
  if (current.status === "failed") {
    throw new Error(`Task failed: ${JSON.stringify(current)}`);
  }
  await new Promise((resolve) => setTimeout(resolve, 3000));
}

throw new Error(`Timed out waiting for task ${task.id}`);
