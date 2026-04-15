[English](./README.md) | [简体中文](./README.zh-CN.md) | [繁體中文](./README.zh-TW.md) | [Español](./README.es.md) | [Deutsch](./README.de.md) | [Français](./README.fr.md) | [日本語](./README.ja.md) | [한국어](./README.ko.md) | [Türkçe](./README.tr.md) | [Русский](./README.ru.md)

# Seedance 2.0 Gateway Service 가격, 모델, 비디오 생성 가이드

<p align="center">
  <a href="https://evolink.ai/seedance-2-0?utm_source=github&utm_medium=banner&utm_campaign=seedance-2-api">
    <img src="./assets/banner.jpg" alt="Seedance 2.0 Human Face Now Available Try Now" width="100%" />
  </a>
</p>

<p align="center">
  <strong>Seedance 2.0<br>Human Face Now Available<br>Try Now</strong>
</p>

<p align="center">
  Seedance 2.0 Gateway Service 가격, 모델, text-to-video, image-to-video, reference-to-video를 하나의 가이드로 정리했습니다.
</p>

<p align="left">
  <a href="https://evolink.ai/seedance-2-0?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-api">Seedance 2.0 가격 보기</a> ·
  <a href="https://evolink.ai/signup?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-api">API 키 받기</a> ·
  <a href="https://docs.evolink.ai?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-api">API 문서 읽기</a>
</p>

## Seedance 2.0 Gateway Service란?

Seedance 2.0 Gateway Service는 텍스트 프롬프트, 이미지, 멀티모달 레퍼런스를 기반으로 AI 비디오를 생성하는 게이트웨이 서비스입니다. EvoLink.ai를 통해 개발자는 통일된 API 흐름으로 Seedance 2.0 모델 전체를 사용할 수 있습니다.

- 생성 작업 만들기
- 즉시 작업 ID 받기
- 상태를 폴링하거나 콜백 받기
- 최종 비디오 결과 다운로드하기

이 저장소는 다음과 같은 개발자에게 적합합니다.

- Seedance 2.0 Gateway Service 가격과 모델 차이를 이해하고 싶은 경우
- text-to-video, image-to-video, reference-to-video를 비교하고 싶은 경우
- 표준 모델과 fast 모델의 차이를 이해하고 싶은 경우
- 바로 쓸 수 있는 실전 예제를 원할 경우
- 도입 전에 비용을 추산하고 싶은 경우
- EvoLinkAI GitHub 생태계 내의 관련 Seedance 리소스도 함께 보고 싶은 경우

## 지원되는 Seedance 2.0 모델

### 표준 모델

- `seedance-2.0-text-to-video`
- `seedance-2.0-image-to-video`
- `seedance-2.0-reference-to-video`

### Fast 모델

- `seedance-2.0-fast-text-to-video`
- `seedance-2.0-fast-image-to-video`
- `seedance-2.0-fast-reference-to-video`

## 빠른 시작

```bash
curl --request POST \
  --url https://api.evolink.ai/v1/videos/generations \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data '{
    "model": "seedance-2.0-text-to-video",
    "prompt": "미래 도시의 새벽을 담은 시네마틱 항공 샷, 부드러운 구름, 반사되는 초고층 빌딩, 매끄러운 카메라 무빙",
    "duration": 5,
    "quality": "720p",
    "aspect_ratio": "16:9",
    "generate_audio": true
  }'
```

## 통합 API 워크플로

### 1. 생성 작업 만들기

```http
POST https://api.evolink.ai/v1/videos/generations
```

### 2. 작업 상태 조회

```http
GET https://api.evolink.ai/v1/tasks/{task_id}
```

### 3. 결과 받기

작업이 완료되면 응답에 생성된 비디오 URL이 포함됩니다.

### 4. 선택적 콜백

폴링만 사용하고 싶지 않다면 `callback_url`을 전달할 수 있습니다.

## 모델 비교

| 모델 | 입력 유형 | 적합한 용도 | 비고 |
|---|---|---|---|
| `seedance-2.0-text-to-video` | 텍스트만 | 프롬프트 중심 비디오 생성 | 선택적 web search 지원 |
| `seedance-2.0-image-to-video` | 이미지 1-2장 | 첫 프레임 애니메이션 또는 시작/종료 프레임 전환 | 이미지 애니메이션 워크플로에 적합 |
| `seedance-2.0-reference-to-video` | 이미지, 비디오, 오디오, 텍스트 | 고급 멀티모달 생성 및 편집 | 편집, 연장, 가이드 생성에 적합 |
| `seedance-2.0-fast-text-to-video` | 텍스트만 | 더 빠른 프롬프트 반복 | 표준 모델과 같은 기본 패턴 |
| `seedance-2.0-fast-image-to-video` | 이미지 1-2장 | 더 빠른 이미지 애니메이션 | 더 많은 이미지 포맷 지원 |
| `seedance-2.0-fast-reference-to-video` | 이미지, 비디오, 오디오, 텍스트 | 더 빠른 멀티모달 생성 | 빠른 반복 작업에 적합 |

## 핵심 파라미터

| 파라미터 | 타입 | 설명 |
|---|---|---|
| `model` | string | Seedance 2.0 모델 선택 |
| `prompt` | string | 생성 프롬프트 |
| `duration` | integer | 출력 길이, `4-15`초 또는 `-1` 스마트 길이 |
| `quality` | string | `480p` 또는 `720p` |
| `aspect_ratio` | string | `16:9`, `9:16`, `1:1`, `4:3`, `3:4`, `21:9`, `adaptive` |
| `generate_audio` | boolean | 동기화된 오디오 생성 여부 |
| `callback_url` | string | 선택적 HTTPS 콜백 URL |

## 모드별 가이드

### Text to Video

텍스트만으로 비디오를 생성하려면 `seedance-2.0-text-to-video` 또는 `seedance-2.0-fast-text-to-video`를 사용합니다.

핵심 포인트:
- 이미지, 비디오, 오디오 입력 불가
- `model_params.web_search` 지원
- 콘셉트 생성과 최신성 있는 프롬프트에 적합

### Image to Video

한 장 또는 두 장의 이미지를 애니메이션화하려면 `seedance-2.0-image-to-video` 또는 `seedance-2.0-fast-image-to-video`를 사용합니다.

핵심 포인트:
- `image_urls`는 1-2장의 이미지를 받음
- 이미지 1장 = 첫 프레임 애니메이션
- 이미지 2장 = 첫 프레임에서 마지막 프레임으로 전환

### Reference to Video

최대한의 제어가 필요하면 `seedance-2.0-reference-to-video` 또는 `seedance-2.0-fast-reference-to-video`를 사용합니다.

핵심 포인트:
- `image_urls`, `video_urls`, `audio_urls` 지원
- 멀티모달 레퍼런스로 새 결과 생성 가능
- 비디오 연장, 편집, 재구성 가능
- 레퍼런스 비디오 길이가 요금에 반영됨

## Seedance 2.0 Gateway Service 가격

### 출력 기준 요금

```text
비용 = 출력 비디오 길이 × 해상도 단가
```

| 해상도 | 가격 |
|---|---:|
| `480p` | 5.556 크레딧 / 초 |
| `720p` | 12.00 크레딧 / 초 |

### Reference-to-video 요금

```text
비용 = (레퍼런스 비디오 길이 + 출력 비디오 길이) × 해상도 단가
```

### 추가 메모

- 오디오 생성은 추가 요금이 없음
- `web_search`는 실제 검색 1회당 `0.04` 크레딧
- 스마트 길이 `-1`은 먼저 10초를 예약하고 실제 길이에 맞게 정산
- 1 크레딧 = 10,000 UC = ¥0.10

## 요청 예제

### Text-to-video 예제

```bash
curl --request POST \
  --url https://api.evolink.ai/v1/videos/generations \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data '{
    "model": "seedance-2.0-text-to-video",
    "prompt": "초록 잎 위에 있는 유리개구리의 매크로 샷, 투명한 몸과 뛰는 심장을 강조",
    "duration": 8,
    "quality": "720p",
    "aspect_ratio": "16:9",
    "generate_audio": true
  }'
```

### Image-to-video 예제

```bash
curl --request POST \
  --url https://api.evolink.ai/v1/videos/generations \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data '{
    "model": "seedance-2.0-image-to-video",
    "prompt": "카메라가 천천히 다가가면서 정지 이미지가 살아난다",
    "image_urls": ["https://example.com/first-frame.jpg"],
    "duration": 5,
    "aspect_ratio": "adaptive"
  }'
```

### Reference-to-video 예제

```bash
curl --request POST \
  --url https://api.evolink.ai/v1/videos/generations \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data '{
    "model": "seedance-2.0-reference-to-video",
    "prompt": "비디오 1의 카메라 무빙을 사용하고 오디오 1을 배경음악으로 사용",
    "image_urls": ["https://example.com/ref1.jpg"],
    "video_urls": ["https://example.com/reference.mp4"],
    "audio_urls": ["https://example.com/bgm.mp3"],
    "duration": 10,
    "quality": "720p",
    "aspect_ratio": "16:9",
    "generate_audio": true
  }'
```

## 활용 사례

- AI 비디오 생성 앱
- 크리에이티브 툴 및 편집 워크플로
- 이미지 애니메이션 파이프라인
- 비디오 광고 생성
- 소셜 미디어 콘텐츠 제작
- 제품 데모 영상
- 멀티모달 비디오 편집 워크플로
- 콘셉트 시각화

## FAQ

### Seedance 2.0 Gateway Service는 동기식인가요?
아니요. Seedance 2.0은 비동기 작업 기반 워크플로를 사용합니다.

### 표준 모델과 fast 모델의 차이는 무엇인가요?
fast 모델은 같은 요청 패턴을 따르지만 더 빠른 반복 작업에 맞춰져 있습니다.

### 텍스트만으로 비디오를 만들 수 있나요?
네. `seedance-2.0-text-to-video` 또는 `seedance-2.0-fast-text-to-video`를 사용하세요.

### 이미지 한 장 애니메이션이나 시작/끝 프레임 전환이 가능한가요?
네. image-to-video를 사용하면 됩니다.

### 기존 비디오를 편집하거나 연장할 수 있나요?
네. `video_urls`와 함께 reference-to-video를 사용하세요.

### 레퍼런스 입력이 가격에 영향을 주나요?
네. reference-to-video에서는 레퍼런스 비디오 길이가 가격에 포함됩니다.

### 결과 URL은 얼마나 유효한가요?
생성된 비디오 URL은 24시간 유효합니다.

## 저장소 구조

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

## 관련 Seedance 저장소

- [Seedance 2.0 Gateway Service: Price and Guide](https://github.com/EvoLinkAI/Seedance-2.0-Gateway-Service)
- [Seedance 2 Video Gen Skill for OpenClaw](https://github.com/EvoLinkAI/seedance2-video-gen-skill-for-openclaw)
- [Awesome Seedance 2 Guide](https://github.com/EvoLinkAI/awesome-seedance-2-guide)

## 관련 링크

- [Seedance 2.0 Pricing](https://evolink.ai/seedance-2-0?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-api)
- [Get API Key](https://evolink.ai/signup?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-api)
- [EvoLink.ai](https://evolink.ai?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-api)

> 통합 전에 [지역별 제공 현황](./docs/regional-availability.ko.md)을 확인해 주세요.

## 라이선스

MIT

---

> **Now Available:** 지금 문서를 기준으로 먼저 연동을 진행할 수 있습니다. Seedance Gateway Service가 정식으로 열리면 Now Available 사용자에게 안내드리겠습니다.
