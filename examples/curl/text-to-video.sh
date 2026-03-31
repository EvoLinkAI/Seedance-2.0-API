#!/usr/bin/env bash

curl --request POST \
  --url https://api.evolink.ai/v1/videos/generations \
  --header "Authorization: Bearer ${EVOLINK_API_KEY}" \
  --header 'Content-Type: application/json' \
  --data '{
    "model": "seedance-2.0-text-to-video",
    "prompt": "A cinematic slow-motion shot of ocean waves crashing against black volcanic rocks at sunset",
    "duration": 5,
    "quality": "720p",
    "aspect_ratio": "16:9",
    "generate_audio": true
  }'
