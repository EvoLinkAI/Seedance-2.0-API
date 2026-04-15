[English](./README.md) | [简体中文](./README.zh-CN.md) | [繁體中文](./README.zh-TW.md) | [Español](./README.es.md) | [Deutsch](./README.de.md) | [Français](./README.fr.md) | [日本語](./README.ja.md) | [한국어](./README.ko.md) | [Türkçe](./README.tr.md) | [Русский](./README.ru.md)

# Seedance 2.0 Gateway Service fiyat, modeller ve video üretim rehberi

<p align="center">
  <a href="https://evolink.ai/seedance-2-0?utm_source=github&utm_medium=banner&utm_campaign=seedance-2-api">
    <img src="./assets/banner.jpg" alt="Seedance 2.0 Human Face Now Available Try Now" width="100%" />
  </a>
</p>

<p align="center">
  <strong>Seedance 2.0<br>Human Face Now Available<br>Try Now</strong>
</p>

<p align="center">
  Seedance 2.0 Gateway Service fiyatı, modelleri, text-to-video, image-to-video ve reference-to-video tek bir rehberde.
</p>

<p align="left">
  <a href="https://evolink.ai/seedance-2-0?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-api">Seedance 2.0 fiyatlarını görüntüle</a> ·
  <a href="https://evolink.ai/signup?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-api">API anahtarı al</a> ·
  <a href="https://docs.evolink.ai?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-api">API belgelerini oku</a>
</p>

## Seedance 2.0 Gateway Service nedir?

Seedance 2.0 Gateway Service, metin istemleri, görseller ve çok modlu referanslar ile yapay zekâ videoları üretmek için kullanılan bir video üretim hizmetidir. EvoLink.ai üzerinden geliştiriciler, tutarlı bir iş akışıyla tüm Seedance 2.0 model ailesine erişebilir:

- bir üretim görevi oluştur
- hemen bir görev kimliği al
- durumu sorgula veya callback al
- nihai video sonucunu indir

Bu depo, şunları isteyen geliştiriciler için tasarlanmıştır:

- Seedance 2.0 Gateway Service fiyatını ve model farklarını anlamak
- text-to-video, image-to-video ve reference-to-video modlarını karşılaştırmak
- standart ve fast modeller arasındaki farkı görmek
- üretime hazır örnekleri kopyalamak
- entegrasyondan önce maliyeti tahmin etmek
- EvoLinkAI GitHub ekosistemindeki diğer Seedance kaynaklarını keşfetmek

## Desteklenen Seedance 2.0 modelleri

### Standart modeller

- `seedance-2.0-text-to-video`
- `seedance-2.0-image-to-video`
- `seedance-2.0-reference-to-video`

### Fast modeller

- `seedance-2.0-fast-text-to-video`
- `seedance-2.0-fast-image-to-video`
- `seedance-2.0-fast-reference-to-video`

## Hızlı başlangıç

```bash
curl --request POST \
  --url https://api.evolink.ai/v1/videos/generations \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data '{
    "model": "seedance-2.0-text-to-video",
    "prompt": "Gün doğumunda fütüristik bir şehrin sinematik hava çekimi, yumuşak bulutlar, yansıtıcı gökdelenler ve akıcı kamera hareketi",
    "duration": 5,
    "quality": "720p",
    "aspect_ratio": "16:9",
    "generate_audio": true
  }'
```

## Birleşik iş akışı

### 1. Üretim görevi oluştur

```http
POST https://api.evolink.ai/v1/videos/generations
```

### 2. Görev durumunu sorgula

```http
GET https://api.evolink.ai/v1/tasks/{task_id}
```

### 3. Sonuçları al

Görev tamamlandığında yanıt, üretilen video URL'lerini döndürür.

### 4. İsteğe bağlı callback

Sadece polling kullanmak istemiyorsan `callback_url` gönderebilirsin.

## Model karşılaştırması

| Model | Girdi türü | En uygun kullanım | Notlar |
|---|---|---|---|
| `seedance-2.0-text-to-video` | yalnızca metin | istem tabanlı video üretimi | isteğe bağlı web search destekler |
| `seedance-2.0-image-to-video` | 1-2 görsel | ilk kare animasyonu veya başlangıç/bitiş karesi geçişi | görsel animasyon iş akışları için ideal |
| `seedance-2.0-reference-to-video` | görsel, video, ses, metin | gelişmiş çok modlu üretim ve düzenleme | düzenleme, uzatma ve yönlendirilmiş üretim için ideal |
| `seedance-2.0-fast-text-to-video` | yalnızca metin | daha hızlı istem iterasyonu | standart modelle aynı temel desen |
| `seedance-2.0-fast-image-to-video` | 1-2 görsel | daha hızlı görsel animasyonu | daha fazla görsel formatını destekler |
| `seedance-2.0-fast-reference-to-video` | görsel, video, ses, metin | daha hızlı çok modlu üretim | hızlı iterasyon için güçlü bir seçim |

## Temel parametreler

| Parametre | Tür | Açıklama |
|---|---|---|
| `model` | string | Seedance 2.0 modelini seçer |
| `prompt` | string | üretim istemi |
| `duration` | integer | çıktı süresi, `4-15` saniye veya akıllı süre için `-1` |
| `quality` | string | `480p` veya `720p` |
| `aspect_ratio` | string | `16:9`, `9:16`, `1:1`, `4:3`, `3:4`, `21:9` veya `adaptive` |
| `generate_audio` | boolean | senkron ses üretilip üretilmeyeceği |
| `callback_url` | string | isteğe bağlı HTTPS callback URL'si |

## Moda göre rehber

### Text to Video

Yalnızca metinden video üretmek istiyorsan `seedance-2.0-text-to-video` veya `seedance-2.0-fast-text-to-video` kullan.

Temel noktalar:
- image, video veya audio girdisi almaz
- `model_params.web_search` destekler
- kavramsal üretim ve güncel içerikler için uygundur

### Image to Video

Bir veya iki görseli animasyona dönüştürmek istiyorsan `seedance-2.0-image-to-video` veya `seedance-2.0-fast-image-to-video` kullan.

Temel noktalar:
- `image_urls` 1-2 görsel kabul eder
- 1 görsel = ilk kare animasyonu
- 2 görsel = ilk kareden son kareye geçiş

### Reference to Video

En yüksek kontrol seviyesine ihtiyacın varsa `seedance-2.0-reference-to-video` veya `seedance-2.0-fast-reference-to-video` kullan.

Temel noktalar:
- `image_urls`, `video_urls` ve `audio_urls` destekler
- çok modlu referanslardan yeni çıktı oluşturabilir
- videoları uzatabilir, düzenleyebilir veya yeniden kurgulayabilir
- referans video süresi fiyatlandırmayı etkiler

## Seedance 2.0 Gateway Service fiyatı

### Çıktı fiyatlandırması

```text
maliyet = çıktı video süresi × çözünürlük fiyatı
```

| Çözünürlük | Fiyat |
|---|---:|
| `480p` | saniye başına 5.556 kredi |
| `720p` | saniye başına 12.00 kredi |

### Reference-to-video fiyatlandırması

```text
maliyet = (referans video süresi + çıktı video süresi) × çözünürlük fiyatı
```

### Ek notlar

- ses üretimi için ek ücret yoktur
- `web_search`, gerçek arama başına `0.04` kredi maliyet oluşturur
- akıllı süre `-1`, önce 10 saniye ayırır sonra gerçek süreye göre hesaplar
- 1 kredi = 10,000 UC = ¥0.10

## İstek örnekleri

### Text-to-video örneği

```bash
curl --request POST \
  --url https://api.evolink.ai/v1/videos/generations \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data '{
    "model": "seedance-2.0-text-to-video",
    "prompt": "Yeşil bir yaprak üzerindeki cam kurbağanın makro çekimi, saydam gövdesi ve atan kalbi vurgulanıyor",
    "duration": 8,
    "quality": "720p",
    "aspect_ratio": "16:9",
    "generate_audio": true
  }'
```

### Image-to-video örneği

```bash
curl --request POST \
  --url https://api.evolink.ai/v1/videos/generations \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data '{
    "model": "seedance-2.0-image-to-video",
    "prompt": "Kamera yavaşça yaklaşırken sabit görsel canlanmaya başlıyor",
    "image_urls": ["https://example.com/first-frame.jpg"],
    "duration": 5,
    "aspect_ratio": "adaptive"
  }'
```

### Reference-to-video örneği

```bash
curl --request POST \
  --url https://api.evolink.ai/v1/videos/generations \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data '{
    "model": "seedance-2.0-reference-to-video",
    "prompt": "Video 1'in kamera hareketini kullan ve audio 1'i arka plan müziği yap",
    "image_urls": ["https://example.com/ref1.jpg"],
    "video_urls": ["https://example.com/reference.mp4"],
    "audio_urls": ["https://example.com/bgm.mp3"],
    "duration": 10,
    "quality": "720p",
    "aspect_ratio": "16:9",
    "generate_audio": true
  }'
```

## Kullanım senaryoları

- AI video üretim uygulamaları
- yaratıcı araçlar ve düzenleme iş akışları
- görsel animasyon pipeline'ları
- video reklam üretimi
- sosyal medya içerik üretimi
- ürün demo videoları
- çok modlu video düzenleme iş akışları
- konsept görselleştirme

## SSS

### Seedance 2.0 Gateway Service senkron mu?
Hayır. Seedance 2.0 görev tabanlı asenkron bir akış kullanır.

### Standart modeller ile fast modeller arasındaki fark nedir?
Fast modeller aynı istek düzenini kullanır ancak daha hızlı iterasyon için tasarlanmıştır.

### Yalnızca metinle video üretebilir miyim?
Evet. `seedance-2.0-text-to-video` veya `seedance-2.0-fast-text-to-video` kullan.

### Tek bir görseli animasyon haline getirebilir veya başlangıç/bitiş karesi geçişi oluşturabilir miyim?
Evet. image-to-video kullan.

### Var olan bir videoyu düzenleyebilir veya uzatabilir miyim?
Evet. `video_urls` ile reference-to-video kullan.

### Referans girdileri fiyatı etkiler mi?
Evet. reference-to-video için referans video süresi fiyatlandırmaya dahildir.

### Sonuç URL'leri ne kadar süre geçerli?
Üretilen video URL'leri 24 saat boyunca geçerlidir.

## Depo yapısı

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

## İlgili Seedance depoları

- [Seedance 2.0 Gateway Service: Price and Guide](https://github.com/EvoLinkAI/Seedance-2.0-Gateway-Service)
- [Seedance 2 Video Gen Skill for OpenClaw](https://github.com/EvoLinkAI/seedance2-video-gen-skill-for-openclaw)
- [Awesome Seedance 2 Guide](https://github.com/EvoLinkAI/awesome-seedance-2-guide)

## İlgili bağlantılar

- [Seedance 2.0 Pricing](https://evolink.ai/seedance-2-0?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-api)
- [Get API Key](https://evolink.ai/signup?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-api)
- [EvoLink.ai](https://evolink.ai?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-api)

## Lisans

MIT

---

> ⚠️ Entegrasyondan önce lütfen [Bölgesel Kullanılabilirlik](./docs/regional-availability.tr.md) sayfasını inceleyin.

> **Now Available:** Dokümantasyona göre entegrasyonu şimdiden hazırlayabilirsiniz. Seedance Gateway Service resmi olarak açıldığında Now Available kullanıcılarına haber vereceğiz.
