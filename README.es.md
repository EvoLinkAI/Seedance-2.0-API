[English](./README.md) | [简体中文](./README.zh-CN.md) | [繁體中文](./README.zh-TW.md) | [Español](./README.es.md) | [Deutsch](./README.de.md) | [Français](./README.fr.md) | [日本語](./README.ja.md) | [한국어](./README.ko.md) | [Türkçe](./README.tr.md) | [Русский](./README.ru.md)

# Guía de precios, modelos y generación de video con Seedance 2.0 API

<p align="center">
  <a href="https://evolink.ai/seedance-2-0?utm_source=github&utm_medium=banner&utm_campaign=seedance-2-api">
    <img src="./assets/banner.jpg" alt="Seedance 2.0 API" width="100%" />
  </a>
</p>

<p align="center">
  Precio de Seedance 2.0 API, modelos, text-to-video, image-to-video y reference-to-video en una sola guía.
</p>

<p align="left">
  <a href="https://evolink.ai/seedance-2-0?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-api">Ver precios de Seedance 2.0</a> ·
  <a href="https://evolink.ai/signup?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-api">Obtener API Key</a> ·
  <a href="https://docs.evolink.ai">Leer documentación API</a>
</p>

## ¿Qué es Seedance 2.0 API?

Seedance 2.0 API es una API de generación de video para crear videos con IA a partir de texto, imágenes y referencias multimodales. A través de EvoLink.ai, los desarrolladores pueden acceder a toda la familia de modelos Seedance 2.0 con un flujo de API consistente:

- crear una tarea de generación
- recibir un task ID de inmediato
- consultar el estado o recibir un callback
- descargar el resultado final

Este repositorio está pensado para quienes quieren:

- entender el precio de Seedance 2.0 API y las diferencias entre modelos
- comparar text-to-video, image-to-video y reference-to-video
- entender la diferencia entre modelos estándar y fast
- copiar ejemplos listos para producción
- estimar costos antes de integrar
- descubrir recursos relacionados dentro del ecosistema GitHub de EvoLinkAI

## Modelos compatibles de Seedance 2.0

### Modelos estándar

- `seedance-2.0-text-to-video`
- `seedance-2.0-image-to-video`
- `seedance-2.0-reference-to-video`

### Modelos fast

- `seedance-2.0-fast-text-to-video`
- `seedance-2.0-fast-image-to-video`
- `seedance-2.0-fast-reference-to-video`

## Inicio rápido

```bash
curl --request POST \
  --url https://api.evolink.ai/v1/videos/generations \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data '{
    "model": "seedance-2.0-text-to-video",
    "prompt": "Una toma aérea cinematográfica de una ciudad futurista al amanecer, nubes suaves, rascacielos reflectantes y movimiento de cámara fluido",
    "duration": 5,
    "quality": "720p",
    "aspect_ratio": "16:9",
    "generate_audio": true
  }'
```

## Flujo unificado de API

### 1. Crear una tarea

```http
POST https://api.evolink.ai/v1/videos/generations
```

### 2. Consultar estado

```http
GET https://api.evolink.ai/v1/tasks/{task_id}
```

### 3. Obtener resultados

Cuando la tarea finaliza, la respuesta devuelve URLs del video generado.

### 4. Callback opcional

Puedes enviar `callback_url` si no quieres depender solo del polling.

## Comparación de modelos

| Modelo | Tipo de entrada | Mejor para | Notas |
|---|---|---|---|
| `seedance-2.0-text-to-video` | solo texto | generación basada en prompt | admite web search opcional |
| `seedance-2.0-image-to-video` | 1-2 imágenes | animación de primer frame o transición entre frames | ideal para flujos con imágenes |
| `seedance-2.0-reference-to-video` | imágenes, video, audio y texto | generación y edición multimodal avanzada | ideal para edición, extensión y control guiado |
| `seedance-2.0-fast-text-to-video` | solo texto | iteración más rápida | mismo patrón general que el modelo estándar |
| `seedance-2.0-fast-image-to-video` | 1-2 imágenes | animación de imagen más rápida | admite más formatos de imagen |
| `seedance-2.0-fast-reference-to-video` | imágenes, video, audio y texto | generación multimodal más rápida | buena opción para iteración veloz |

## Parámetros principales

| Parámetro | Tipo | Descripción |
|---|---|---|
| `model` | string | selecciona el modelo Seedance 2.0 |
| `prompt` | string | prompt de generación |
| `duration` | integer | duración de salida, `4-15` segundos o `-1` para duración inteligente |
| `quality` | string | `480p` o `720p` |
| `aspect_ratio` | string | `16:9`, `9:16`, `1:1`, `4:3`, `3:4`, `21:9` o `adaptive` |
| `generate_audio` | boolean | si se debe generar audio sincronizado |
| `callback_url` | string | callback HTTPS opcional |

## Guía por modo

### Text to Video

Usa `seedance-2.0-text-to-video` o `seedance-2.0-fast-text-to-video` si quieres generar video solo a partir de texto.

Puntos clave:
- no acepta imágenes, video ni audio como entrada
- admite `model_params.web_search`
- útil para generación conceptual y prompts con contexto reciente

### Image to Video

Usa `seedance-2.0-image-to-video` o `seedance-2.0-fast-image-to-video` si quieres animar una o dos imágenes.

Puntos clave:
- `image_urls` acepta 1-2 imágenes
- 1 imagen = animación desde primer frame
- 2 imágenes = transición del primer al último frame

### Reference to Video

Usa `seedance-2.0-reference-to-video` o `seedance-2.0-fast-reference-to-video` si necesitas el mayor control.

Puntos clave:
- admite `image_urls`, `video_urls` y `audio_urls`
- permite crear, extender, editar y recomponer videos
- la duración del video de referencia afecta el precio

## Precio de Seedance 2.0 API

### Precio por salida

```text
costo = duración del video de salida × precio por resolución
```

| Resolución | Precio |
|---|---:|
| `480p` | 4.63 créditos / segundo |
| `720p` | 10.00 créditos / segundo |

### Precio para reference-to-video

```text
costo = (duración del video de referencia + duración del video de salida) × precio por resolución
```

### Notas adicionales

- la generación de audio no tiene costo extra
- `web_search` cuesta `0.04` créditos por búsqueda real
- la duración inteligente `-1` reserva 10 segundos y luego ajusta el cobro
- 1 crédito = 10,000 UC = ¥0.10

## Ejemplos de solicitud

### Ejemplo text-to-video

```bash
curl --request POST \
  --url https://api.evolink.ai/v1/videos/generations \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data '{
    "model": "seedance-2.0-text-to-video",
    "prompt": "Un primer plano macro de una rana de cristal sobre una hoja verde, con foco en su cuerpo transparente y su corazón latiendo",
    "duration": 8,
    "quality": "720p",
    "aspect_ratio": "16:9",
    "generate_audio": true
  }'
```

### Ejemplo image-to-video

```bash
curl --request POST \
  --url https://api.evolink.ai/v1/videos/generations \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data '{
    "model": "seedance-2.0-image-to-video",
    "prompt": "La cámara se acerca lentamente mientras la imagen fija cobra vida",
    "image_urls": ["https://example.com/first-frame.jpg"],
    "duration": 5,
    "aspect_ratio": "adaptive"
  }'
```

### Ejemplo reference-to-video

```bash
curl --request POST \
  --url https://api.evolink.ai/v1/videos/generations \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data '{
    "model": "seedance-2.0-reference-to-video",
    "prompt": "Usa el movimiento de cámara del video 1 y el audio 1 como música de fondo",
    "image_urls": ["https://example.com/ref1.jpg"],
    "video_urls": ["https://example.com/reference.mp4"],
    "audio_urls": ["https://example.com/bgm.mp3"],
    "duration": 10,
    "quality": "720p",
    "aspect_ratio": "16:9",
    "generate_audio": true
  }'
```

## Casos de uso

- aplicaciones de generación de video con IA
- herramientas creativas y flujos de edición
- animación a partir de imágenes
- generación de anuncios en video
- contenido para redes sociales
- demos de producto
- edición de video multimodal
- visualización de conceptos

## FAQ

### ¿Seedance 2.0 API es síncrona?
No. Seedance 2.0 usa un flujo asíncrono por tareas.

### ¿Cuál es la diferencia entre modelos estándar y fast?
Los modelos fast siguen el mismo patrón de solicitud, pero están pensados para iteración más rápida.

### ¿Puedo generar video solo con texto?
Sí. Usa `seedance-2.0-text-to-video` o `seedance-2.0-fast-text-to-video`.

### ¿Puedo animar una imagen o crear una transición entre frame inicial y final?
Sí. Usa image-to-video.

### ¿Puedo editar o extender un video existente?
Sí. Usa reference-to-video con `video_urls`.

### ¿Las referencias afectan el precio?
Sí. La duración del video de referencia cuenta para el precio en reference-to-video.

### ¿Cuánto tiempo duran las URLs del resultado?
Las URLs del video generado son válidas durante 24 horas.

## Estructura del repositorio

```text
Seedance-2.0-API/
├── README.md
├── README.zh-CN.md
├── README.zh-TW.md
├── README.es.md
├── README.de.md
├── README.fr.md
├── README.ja.md
├── README.ko.md
├── README.tr.md
├── README.ru.md
├── assets/
│   └── banner.jpg
├── docs/
│   ├── text-to-video.md
│   ├── image-to-video.md
│   ├── reference-to-video.md
│   ├── fast-models.md
│   └── pricing.md
└── examples/
    ├── curl/
    ├── nodejs/
    └── python/
```

## Repositorios relacionados de Seedance

- [Seedance 2.0 API Price and Guide](https://github.com/EvoLinkAI/Seedance-2.0-API)
- [Seedance 2 Video Gen Skill for OpenClaw](https://github.com/EvoLinkAI/seedance2-video-gen-skill-for-openclaw)
- [Awesome Seedance 2 Guide](https://github.com/EvoLinkAI/awesome-seedance-2-guide)

## Enlaces relacionados

- [Seedance 2.0 Pricing](https://evolink.ai/seedance-2-0?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-api)
- [Get API Key](https://evolink.ai/signup?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-api)
- [EvoLink.ai](https://evolink.ai?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-api)

## Licencia

MIT
