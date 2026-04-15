[English](./README.md) | [简体中文](./README.zh-CN.md) | [繁體中文](./README.zh-TW.md) | [Español](./README.es.md) | [Deutsch](./README.de.md) | [Français](./README.fr.md) | [日本語](./README.ja.md) | [한국어](./README.ko.md) | [Türkçe](./README.tr.md) | [Русский](./README.ru.md)

# Seedance 2.0 Gateway Service: цены, модели и руководство по генерации видео

<p align="center">
  <a href="https://evolink.ai/seedance-2-0?utm_source=github&utm_medium=banner&utm_campaign=seedance-2-api">
    <img src="./assets/banner.jpg" alt="Seedance 2.0 Human Face Now Available Try Now" width="100%" />
  </a>
</p>

<p align="center">
  <strong>Seedance 2.0<br>Human Face Now Available<br>Try Now</strong>
</p>

<p align="center">
  Цена Seedance 2.0 Gateway Service, модели, text-to-video, image-to-video и reference-to-video в одном руководстве.
</p>

<p align="left">
  <a href="https://evolink.ai/seedance-2-0?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-api">Посмотреть цены Seedance 2.0</a> ·
  <a href="https://evolink.ai/signup?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-api">Получить API Key</a> ·
  <a href="https://docs.evolink.ai?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-api">Открыть API документацию</a>
</p>

## Что такое Seedance 2.0 Gateway Service?

Seedance 2.0 Gateway Service — это шлюзовый сервис генерации видео для создания AI-видео из текстовых промптов, изображений и мультимодальных референсов. Через EvoLink.ai разработчики получают доступ ко всей линейке моделей Seedance 2.0 по единому API-процессу:

- создать задачу генерации
- сразу получить ID задачи
- опрашивать статус или использовать callback
- скачать итоговый результат

Этот репозиторий подходит разработчикам, которые хотят:

- понять цены Seedance 2.0 Gateway Service и различия между моделями
- сравнить text-to-video, image-to-video и reference-to-video
- понять разницу между стандартными и fast-моделями
- копировать готовые к продакшену примеры
- оценить стоимость до интеграции
- находить другие Seedance-ресурсы внутри GitHub-экосистемы EvoLinkAI

## Поддерживаемые модели Seedance 2.0

### Стандартные модели

- `seedance-2.0-text-to-video`
- `seedance-2.0-image-to-video`
- `seedance-2.0-reference-to-video`

### Fast-модели

- `seedance-2.0-fast-text-to-video`
- `seedance-2.0-fast-image-to-video`
- `seedance-2.0-fast-reference-to-video`

## Быстрый старт

```bash
curl --request POST \
  --url https://api.evolink.ai/v1/videos/generations \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data '{
    "model": "seedance-2.0-text-to-video",
    "prompt": "Кинематографичный аэросъёмочный кадр футуристического города на рассвете, мягкие облака, отражающие небоскрёбы и плавное движение камеры",
    "duration": 5,
    "quality": "720p",
    "aspect_ratio": "16:9",
    "generate_audio": true
  }'
```

## Единый API-процесс

### 1. Создать задачу генерации

```http
POST https://api.evolink.ai/v1/videos/generations
```

### 2. Проверить статус задачи

```http
GET https://api.evolink.ai/v1/tasks/{task_id}
```

### 3. Получить результат

После завершения задача возвращает URL сгенерированного видео.

### 4. Необязательный callback

Если вы не хотите полагаться только на polling, передайте `callback_url`.

## Сравнение моделей

| Модель | Тип входа | Лучшее применение | Примечания |
|---|---|---|---|
| `seedance-2.0-text-to-video` | только текст | генерация видео по промпту | поддерживает опциональный web search |
| `seedance-2.0-image-to-video` | 1-2 изображения | анимация первого кадра или переход между первым и последним кадром | идеально для анимации изображений |
| `seedance-2.0-reference-to-video` | изображения, видео, аудио, текст | продвинутая мультимодальная генерация и редактирование | подходит для редактирования, продолжения и управляемой генерации |
| `seedance-2.0-fast-text-to-video` | только текст | более быстрая итерация промптов | тот же базовый паттерн, что и у стандартной модели |
| `seedance-2.0-fast-image-to-video` | 1-2 изображения | более быстрая анимация изображений | поддерживает больше форматов изображений |
| `seedance-2.0-fast-reference-to-video` | изображения, видео, аудио, текст | более быстрая мультимодальная генерация | хороший выбор для быстрой итерации |

## Основные параметры

| Параметр | Тип | Описание |
|---|---|---|
| `model` | string | выбирает модель Seedance 2.0 |
| `prompt` | string | промпт генерации |
| `duration` | integer | длительность результата, `4-15` секунд или `-1` для умной длины |
| `quality` | string | `480p` или `720p` |
| `aspect_ratio` | string | `16:9`, `9:16`, `1:1`, `4:3`, `3:4`, `21:9` или `adaptive` |
| `generate_audio` | boolean | нужно ли генерировать синхронное аудио |
| `callback_url` | string | необязательный HTTPS callback URL |

## Руководство по режимам

### Text to Video

Используйте `seedance-2.0-text-to-video` или `seedance-2.0-fast-text-to-video`, если хотите генерировать видео только из текста.

Ключевые моменты:
- не принимает image, video или audio на вход
- поддерживает `model_params.web_search`
- подходит для концептов и актуальных запросов

### Image to Video

Используйте `seedance-2.0-image-to-video` или `seedance-2.0-fast-image-to-video`, если хотите анимировать одно или два изображения.

Ключевые моменты:
- `image_urls` принимает 1-2 изображения
- 1 изображение = анимация первого кадра
- 2 изображения = переход от первого к последнему кадру

### Reference to Video

Используйте `seedance-2.0-reference-to-video` или `seedance-2.0-fast-reference-to-video`, если нужен максимальный контроль.

Ключевые моменты:
- поддерживает `image_urls`, `video_urls` и `audio_urls`
- может создавать новые результаты на основе мультимодальных референсов
- может продолжать, редактировать и перекомпоновывать видео
- длительность референс-видео влияет на стоимость

## Цена Seedance 2.0 Gateway Service

### Стоимость по выходу

```text
стоимость = длительность итогового видео × цена за разрешение
```

| Разрешение | Цена |
|---|---:|
| `480p` | 5.556 кредита / секунда |
| `720p` | 12.00 кредита / секунда |

### Стоимость для reference-to-video

```text
стоимость = (длительность референс-видео + длительность итогового видео) × цена за разрешение
```

### Дополнительно

- генерация аудио не оплачивается отдельно
- `web_search` стоит `0.04` кредита за каждый фактически выполненный поиск
- умная длина `-1` сначала резервирует 10 секунд, затем стоимость уточняется по фактической длине
- 1 кредит = 10,000 UC = ¥0.10

## Примеры запросов

### Пример text-to-video

```bash
curl --request POST \
  --url https://api.evolink.ai/v1/videos/generations \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data '{
    "model": "seedance-2.0-text-to-video",
    "prompt": "Макро-кадр стеклянной лягушки на зелёном листе, фокус на прозрачном теле и видимом бьющемся сердце",
    "duration": 8,
    "quality": "720p",
    "aspect_ratio": "16:9",
    "generate_audio": true
  }'
```

### Пример image-to-video

```bash
curl --request POST \
  --url https://api.evolink.ai/v1/videos/generations \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data '{
    "model": "seedance-2.0-image-to-video",
    "prompt": "Камера медленно приближается, а статичное изображение оживает",
    "image_urls": ["https://example.com/first-frame.jpg"],
    "duration": 5,
    "aspect_ratio": "adaptive"
  }'
```

### Пример reference-to-video

```bash
curl --request POST \
  --url https://api.evolink.ai/v1/videos/generations \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data '{
    "model": "seedance-2.0-reference-to-video",
    "prompt": "Используйте движение камеры из видео 1 и аудио 1 как фоновую музыку",
    "image_urls": ["https://example.com/ref1.jpg"],
    "video_urls": ["https://example.com/reference.mp4"],
    "audio_urls": ["https://example.com/bgm.mp3"],
    "duration": 10,
    "quality": "720p",
    "aspect_ratio": "16:9",
    "generate_audio": true
  }'
```

## Сценарии использования

- приложения для AI-генерации видео
- креативные инструменты и редакторские workflows
- пайплайны анимации изображений
- генерация видеорекламы
- создание контента для соцсетей
- продуктовые демо
- мультимодальное редактирование видео
- визуализация концептов

## FAQ

### Seedance 2.0 Gateway Service синхронный?
Нет. Seedance 2.0 использует асинхронный task-based workflow.

### В чём разница между стандартными и fast-моделями?
Fast-модели используют тот же паттерн запросов, но рассчитаны на более быструю итерацию.

### Можно ли генерировать видео только из текста?
Да. Используйте `seedance-2.0-text-to-video` или `seedance-2.0-fast-text-to-video`.

### Можно ли анимировать одно изображение или сделать переход между первым и последним кадром?
Да. Используйте image-to-video.

### Можно ли редактировать или продлевать существующее видео?
Да. Используйте reference-to-video с `video_urls`.

### Референсы влияют на цену?
Да. Для reference-to-video длительность референс-видео входит в стоимость.

### Сколько времени действуют URL результата?
URL сгенерированных видео действуют 24 часа.

## Структура репозитория

```text
Seedance-2.0-Gateway-Service/
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

## Связанные репозитории Seedance

- [Seedance 2.0 Gateway Service: Price and Guide](https://github.com/EvoLinkAI/Seedance-2.0-Gateway-Service)
- [Seedance 2 Video Gen Skill for OpenClaw](https://github.com/EvoLinkAI/seedance2-video-gen-skill-for-openclaw)
- [Awesome Seedance 2 Guide](https://github.com/EvoLinkAI/awesome-seedance-2-guide)

## Связанные ссылки

- [Seedance 2.0 Pricing](https://evolink.ai/seedance-2-0?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-api)
- [Get API Key](https://evolink.ai/signup?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-api)
- [EvoLink.ai](https://evolink.ai?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-api)

> Пожалуйста, ознакомьтесь с [Региональной доступностью](./docs/regional-availability.ru.md) перед интеграцией.

## Лицензия

MIT

---

> **Now Available:** Вы уже можете заранее подготовить интеграцию по документации. Как только Seedance Gateway Service будет официально открыт, мы уведомим пользователей Now Available.
