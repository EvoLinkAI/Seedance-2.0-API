[English](./README.md) | [简体中文](./README.zh-CN.md) | [繁體中文](./README.zh-TW.md) | [Español](./README.es.md) | [Deutsch](./README.de.md) | [Français](./README.fr.md) | [日本語](./README.ja.md) | [한국어](./README.ko.md) | [Türkçe](./README.tr.md) | [Русский](./README.ru.md)

# Seedance 2.0 Gateway Service 価格・モデル・動画生成ガイド

<p align="center">
  <a href="https://evolink.ai/seedance-2-0?utm_source=github&utm_medium=banner&utm_campaign=seedance-2-api">
    <img src="./assets/banner.jpg" alt="Seedance 2.0 Human Face Now Available Try Now" width="100%" />
  </a>
</p>

<p align="center">
  <strong>Seedance 2.0<br>Human Face Now Available<br>Try Now</strong>
</p>

<p align="center">
  Seedance 2.0 Gateway Service の価格、モデル、text-to-video、image-to-video、reference-to-video を 1 つのガイドにまとめました。
</p>

<p align="left">
  <a href="https://evolink.ai/seedance-2-0?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-api">Seedance 2.0 の価格を見る</a> ·
  <a href="https://evolink.ai/signup?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-api">API キーを取得</a> ·
  <a href="https://docs.evolink.ai?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-api">API ドキュメントを読む</a>
</p>

## Seedance 2.0 Gateway Service とは？

Seedance 2.0 Gateway Service は、テキストプロンプト、画像、マルチモーダル参照素材から AI 動画を生成するためのゲートウェイサービスです。EvoLink.ai を通じて、開発者は統一された API フローで Seedance 2.0 のモデル群全体にアクセスできます。

- 生成タスクを作成する
- タスク ID をすぐに受け取る
- ステータスをポーリングするかコールバックを受け取る
- 最終結果の動画をダウンロードする

このリポジトリは、次のような開発者向けです。

- Seedance 2.0 Gateway Service の価格とモデル差を理解したい
- text-to-video、image-to-video、reference-to-video を比較したい
- 標準モデルと fast モデルの違いを理解したい
- そのまま使える実運用向けサンプルを使いたい
- 導入前にコストを見積もりたい
- EvoLinkAI の GitHub エコシステム内にある関連 Seedance リソースも知りたい

## 対応している Seedance 2.0 モデル

### 標準モデル

- `seedance-2.0-text-to-video`
- `seedance-2.0-image-to-video`
- `seedance-2.0-reference-to-video`

### Fast モデル

- `seedance-2.0-fast-text-to-video`
- `seedance-2.0-fast-image-to-video`
- `seedance-2.0-fast-reference-to-video`

## クイックスタート

```bash
curl --request POST \
  --url https://api.evolink.ai/v1/videos/generations \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data '{
    "model": "seedance-2.0-text-to-video",
    "prompt": "未来都市の夜明けを映すシネマティックな空撮。柔らかな雲、反射する高層ビル、滑らかなカメラ移動",
    "duration": 5,
    "quality": "720p",
    "aspect_ratio": "16:9",
    "generate_audio": true
  }'
```

## 統一 API ワークフロー

### 1. 生成タスクを作成する

```http
POST https://api.evolink.ai/v1/videos/generations
```

### 2. タスク状態を取得する

```http
GET https://api.evolink.ai/v1/tasks/{task_id}
```

### 3. 結果を取得する

タスク完了後、レスポンスには生成された動画 URL が含まれます。

### 4. 任意のコールバック

ポーリングだけに頼りたくない場合は、`callback_url` を指定できます。

## モデル比較

| モデル | 入力タイプ | 向いている用途 | 備考 |
|---|---|---|---|
| `seedance-2.0-text-to-video` | テキストのみ | プロンプト中心の動画生成 | オプションの web search に対応 |
| `seedance-2.0-image-to-video` | 1〜2 枚の画像 | 先頭フレームのアニメーションや開始/終了フレーム遷移 | 画像アニメーション向け |
| `seedance-2.0-reference-to-video` | 画像、動画、音声、テキスト | 高度なマルチモーダル生成と編集 | 編集、延長、ガイド付き生成に最適 |
| `seedance-2.0-fast-text-to-video` | テキストのみ | より高速なプロンプト試行 | 標準モデルと同じ基本パターン |
| `seedance-2.0-fast-image-to-video` | 1〜2 枚の画像 | より高速な画像アニメーション | 対応画像形式が多い |
| `seedance-2.0-fast-reference-to-video` | 画像、動画、音声、テキスト | より高速なマルチモーダル生成 | 迅速な反復に向く |

## 主要パラメータ

| パラメータ | 型 | 説明 |
|---|---|---|
| `model` | string | Seedance 2.0 モデルを選択 |
| `prompt` | string | 生成プロンプト |
| `duration` | integer | 出力時間。`4-15` 秒、または `-1` でスマート長さ |
| `quality` | string | `480p` または `720p` |
| `aspect_ratio` | string | `16:9`、`9:16`、`1:1`、`4:3`、`3:4`、`21:9`、`adaptive` |
| `generate_audio` | boolean | 同期音声を生成するか |
| `callback_url` | string | 任意の HTTPS コールバック URL |

## モード別ガイド

### Text to Video

テキストだけで動画を生成したい場合は、`seedance-2.0-text-to-video` または `seedance-2.0-fast-text-to-video` を使います。

ポイント：
- image、video、audio 入力は受け付けない
- `model_params.web_search` に対応
- コンセプト生成や最新情報を含むプロンプトに向く

### Image to Video

1 枚または 2 枚の画像を動画化したい場合は、`seedance-2.0-image-to-video` または `seedance-2.0-fast-image-to-video` を使います。

ポイント：
- `image_urls` は 1〜2 枚を受け付ける
- 1 枚 = 先頭フレームアニメーション
- 2 枚 = 先頭フレームから最終フレームへの遷移

### Reference to Video

最大限の制御が必要な場合は、`seedance-2.0-reference-to-video` または `seedance-2.0-fast-reference-to-video` を使います。

ポイント：
- `image_urls`、`video_urls`、`audio_urls` をサポート
- マルチモーダル参照から新しい出力を生成できる
- 動画の延長、編集、再構成が可能
- 参照動画の長さは料金に影響する

## Seedance 2.0 Gateway Service の価格

### 出力料金

```text
料金 = 出力動画の長さ × 解像度単価
```

| 解像度 | 価格 |
|---|---:|
| `480p` | 5.556 クレジット / 秒 |
| `720p` | 12.00 クレジット / 秒 |

### Reference-to-video の料金

```text
料金 = (参照動画の長さ + 出力動画の長さ) × 解像度単価
```

### 補足

- 音声生成に追加料金はない
- `web_search` は実行された検索 1 回ごとに `0.04` クレジット
- スマート長さ `-1` は最初に 10 秒分を確保し、後で実際の長さに応じて調整
- 1 クレジット = 10,000 UC = ¥0.10

## リクエスト例

### Text-to-video 例

```bash
curl --request POST \
  --url https://api.evolink.ai/v1/videos/generations \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data '{
    "model": "seedance-2.0-text-to-video",
    "prompt": "緑の葉にいるグラスフロッグのマクロショット。透明な腹部と鼓動する心臓にフォーカスする",
    "duration": 8,
    "quality": "720p",
    "aspect_ratio": "16:9",
    "generate_audio": true
  }'
```

### Image-to-video 例

```bash
curl --request POST \
  --url https://api.evolink.ai/v1/videos/generations \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data '{
    "model": "seedance-2.0-image-to-video",
    "prompt": "カメラがゆっくり寄りながら静止画が動き出す",
    "image_urls": ["https://example.com/first-frame.jpg"],
    "duration": 5,
    "aspect_ratio": "adaptive"
  }'
```

### Reference-to-video 例

```bash
curl --request POST \
  --url https://api.evolink.ai/v1/videos/generations \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data '{
    "model": "seedance-2.0-reference-to-video",
    "prompt": "動画1のカメラ動作を使い、音声1をBGMとして使う",
    "image_urls": ["https://example.com/ref1.jpg"],
    "video_urls": ["https://example.com/reference.mp4"],
    "audio_urls": ["https://example.com/bgm.mp3"],
    "duration": 10,
    "quality": "720p",
    "aspect_ratio": "16:9",
    "generate_audio": true
  }'
```

## 主なユースケース

- AI 動画生成アプリ
- クリエイティブツールと編集ワークフロー
- 画像アニメーションパイプライン
- 動画広告生成
- SNS コンテンツ制作
- プロダクトデモ動画
- マルチモーダル動画編集
- コンセプト可視化

## FAQ

### Seedance 2.0 Gateway Service は同期型ですか？
いいえ。Seedance 2.0 は非同期タスクフローです。

### 標準モデルと fast モデルの違いは？
fast モデルは同じリクエスト形式ですが、より高速な反復のために最適化されています。

### テキストだけで動画を生成できますか？
はい。`seedance-2.0-text-to-video` または `seedance-2.0-fast-text-to-video` を使います。

### 画像 1 枚のアニメーションや開始/終了フレーム遷移はできますか？
はい。image-to-video を使います。

### 既存動画の編集や延長はできますか？
はい。`video_urls` を使って reference-to-video を使います。

### 参照素材は料金に影響しますか？
はい。reference-to-video では参照動画の長さが料金に含まれます。

### 結果 URL の有効期限は？
生成された動画 URL は 24 時間有効です。

## リポジトリ構成

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

## 関連する Seedance リポジトリ

- [Seedance 2.0 Gateway Service: Price and Guide](https://github.com/EvoLinkAI/Seedance-2.0-Gateway-Service)
- [Seedance 2 Video Gen Skill for OpenClaw](https://github.com/EvoLinkAI/seedance2-video-gen-skill-for-openclaw)
- [Awesome Seedance 2 Guide](https://github.com/EvoLinkAI/awesome-seedance-2-guide)

## 関連リンク

- [Seedance 2.0 Pricing](https://evolink.ai/seedance-2-0?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-api)
- [Get API Key](https://evolink.ai/signup?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-api)
- [EvoLink.ai](https://evolink.ai?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-api)

> 統合前に [地域別提供状況](./docs/regional-availability.ja.md) をご確認ください。

## ライセンス

MIT

---

> **Now Available：** 今のうちにドキュメントに沿って先に統合を進められます。Seedance Gateway Service の提供開始後、Now Available ユーザーへご案内します。
