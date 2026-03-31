const response = await fetch('https://api.evolink.ai/v1/videos/generations', {
  method: 'POST',
  headers: {
    Authorization: `Bearer ${process.env.EVOLINK_API_KEY}`,
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    model: 'seedance-2.0-fast-text-to-video',
    prompt: 'A moody neon-lit street at night, wet pavement, cinematic camera movement',
    duration: 5,
    quality: '720p',
    aspect_ratio: '16:9',
    generate_audio: true
  })
});

const data = await response.json();
console.log(data);
