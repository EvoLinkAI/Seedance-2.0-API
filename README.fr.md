[English](./README.md) | [简体中文](./README.zh-CN.md) | [繁體中文](./README.zh-TW.md) | [Español](./README.es.md) | [Deutsch](./README.de.md) | [Français](./README.fr.md) | [日本語](./README.ja.md) | [한국어](./README.ko.md) | [Türkçe](./README.tr.md) | [Русский](./README.ru.md)

# Guide des prix, modèles et de la génération vidéo avec le Seedance 2.0 Gateway Service

<p align="center">
  <a href="https://evolink.ai/seedance-2-0?utm_source=github&utm_medium=banner&utm_campaign=seedance-2-api">
    <img src="./assets/banner.jpg" alt="Seedance 2.0 Human Face Now Available Try Now" width="100%" />
  </a>
</p>

<p align="center">
  <strong>Seedance 2.0<br>Human Face Now Available<br>Try Now</strong>
</p>

<p align="center">
  Prix du Seedance 2.0 Gateway Service, modèles, text-to-video, image-to-video et reference-to-video dans un guide unique.
</p>

<p align="left">
  <a href="https://evolink.ai/seedance-2-0?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-api">Voir les prix de Seedance 2.0</a> ·
  <a href="https://evolink.ai/signup?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-api">Obtenir une API Key</a> ·
  <a href="https://docs.evolink.ai?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-api">Lire la documentation API</a>
</p>

## Qu’est-ce que le Seedance 2.0 Gateway Service ?

Seedance 2.0 Gateway Service est un service de génération vidéo pour créer des vidéos IA à partir de prompts texte, d’images et de références multimodales. Via EvoLink.ai, les développeurs peuvent accéder à toute la famille de modèles Seedance 2.0 avec un workflow API cohérent :

- créer une tâche de génération
- recevoir immédiatement un identifiant de tâche
- interroger le statut ou recevoir un callback
- télécharger le résultat final

Ce dépôt s’adresse aux développeurs qui veulent :

- comprendre le prix du Seedance 2.0 Gateway Service et les différences entre modèles
- comparer text-to-video, image-to-video et reference-to-video
- comprendre la différence entre les modèles standard et fast
- copier des exemples prêts pour la production
- estimer les coûts avant intégration
- découvrir d’autres ressources Seedance dans l’écosystème GitHub d’EvoLinkAI

## Modèles Seedance 2.0 pris en charge

### Modèles standard

- `seedance-2.0-text-to-video`
- `seedance-2.0-image-to-video`
- `seedance-2.0-reference-to-video`

### Modèles fast

- `seedance-2.0-fast-text-to-video`
- `seedance-2.0-fast-image-to-video`
- `seedance-2.0-fast-reference-to-video`

## Démarrage rapide

```bash
curl --request POST \
  --url https://api.evolink.ai/v1/videos/generations \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data '{
    "model": "seedance-2.0-text-to-video",
    "prompt": "Un plan aérien cinématographique d’une ville futuriste au lever du soleil, nuages doux, gratte-ciel réfléchissants et mouvement de caméra fluide",
    "duration": 5,
    "quality": "720p",
    "aspect_ratio": "16:9",
    "generate_audio": true
  }'
```

## Workflow API unifié

### 1. Créer une tâche de génération

```http
POST https://api.evolink.ai/v1/videos/generations
```

### 2. Interroger le statut de la tâche

```http
GET https://api.evolink.ai/v1/tasks/{task_id}
```

### 3. Récupérer les résultats

Une fois la tâche terminée, la réponse fournit les URL des vidéos générées.

### 4. Callback optionnel

Vous pouvez envoyer `callback_url` si vous ne voulez pas vous appuyer uniquement sur le polling.

## Comparaison des modèles

| Modèle | Type d’entrée | Idéal pour | Notes |
|---|---|---|---|
| `seedance-2.0-text-to-video` | texte בלבד | génération vidéo à partir de prompts | prend en charge `web_search` en option |
| `seedance-2.0-image-to-video` | 1-2 images | animation à partir de la première image ou transition début/fin | idéal pour l’animation d’images |
| `seedance-2.0-reference-to-video` | images, vidéos, audio, texte | génération et édition multimodales avancées | idéal pour l’édition, l’extension et le contrôle guidé |
| `seedance-2.0-fast-text-to-video` | texte בלבד | itération plus rapide | même schéma général que le modèle standard |
| `seedance-2.0-fast-image-to-video` | 1-2 images | animation plus rapide | prend en charge davantage de formats d’image |
| `seedance-2.0-fast-reference-to-video` | images, vidéos, audio, texte | génération multimodale plus rapide | bon choix pour l’itération rapide |

## Paramètres principaux

| Paramètre | Type | Description |
|---|---|---|
| `model` | string | sélectionne le modèle Seedance 2.0 |
| `prompt` | string | prompt de génération |
| `duration` | integer | durée de sortie, `4-15` secondes ou `-1` pour durée intelligente |
| `quality` | string | `480p` ou `720p` |
| `aspect_ratio` | string | `16:9`, `9:16`, `1:1`, `4:3`, `3:4`, `21:9` ou `adaptive` |
| `generate_audio` | boolean | indique si un audio synchronisé doit être généré |
| `callback_url` | string | URL de callback HTTPS optionnelle |

## Guide par mode

### Text to Video

Utilisez `seedance-2.0-text-to-video` ou `seedance-2.0-fast-text-to-video` pour générer une vidéo uniquement à partir d’un prompt texte.

Points clés :
- n’accepte ni image, ni vidéo, ni audio en entrée
- prend en charge `model_params.web_search`
- utile pour la génération conceptuelle et les contenus à jour

### Image to Video

Utilisez `seedance-2.0-image-to-video` ou `seedance-2.0-fast-image-to-video` pour animer une ou deux images.

Points clés :
- `image_urls` accepte 1 à 2 images
- 1 image = animation depuis la première image
- 2 images = transition de l’image de départ à l’image finale

### Reference to Video

Utilisez `seedance-2.0-reference-to-video` ou `seedance-2.0-fast-reference-to-video` si vous avez besoin d’un contrôle maximal.

Points clés :
- prend en charge `image_urls`, `video_urls` et `audio_urls`
- peut créer de nouvelles sorties à partir de références multimodales
- peut étendre, éditer ou recomposer des vidéos
- la durée des vidéos de référence affecte le prix

## Prix du Seedance 2.0 Gateway Service

### Prix de sortie

```text
coût = durée de la vidéo de sortie × prix par résolution
```

| Résolution | Prix |
|---|---:|
| `480p` | 5.556 crédits / seconde |
| `720p` | 12.00 crédits / seconde |

### Prix pour reference-to-video

```text
coût = (durée des vidéos de référence + durée de la vidéo de sortie) × prix par résolution
```

### Notes supplémentaires

- la génération audio n’a pas de coût supplémentaire
- `web_search` coûte `0.04` crédits par recherche réellement exécutée
- la durée intelligente `-1` réserve 10 secondes puis ajuste selon la durée réelle
- 1 crédit = 10,000 UC = ¥0.10

## Exemples de requêtes

### Exemple text-to-video

```bash
curl --request POST \
  --url https://api.evolink.ai/v1/videos/generations \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data '{
    "model": "seedance-2.0-text-to-video",
    "prompt": "Un plan macro d’une grenouille de verre sur une feuille verte, avec mise au point sur son corps transparent et son cœur battant visible",
    "duration": 8,
    "quality": "720p",
    "aspect_ratio": "16:9",
    "generate_audio": true
  }'
```

### Exemple image-to-video

```bash
curl --request POST \
  --url https://api.evolink.ai/v1/videos/generations \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data '{
    "model": "seedance-2.0-image-to-video",
    "prompt": "La caméra se rapproche lentement pendant que l’image fixe prend vie",
    "image_urls": ["https://example.com/first-frame.jpg"],
    "duration": 5,
    "aspect_ratio": "adaptive"
  }'
```

### Exemple reference-to-video

```bash
curl --request POST \
  --url https://api.evolink.ai/v1/videos/generations \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data '{
    "model": "seedance-2.0-reference-to-video",
    "prompt": "Utilisez le mouvement de caméra de la vidéo 1 et l’audio 1 comme musique de fond",
    "image_urls": ["https://example.com/ref1.jpg"],
    "video_urls": ["https://example.com/reference.mp4"],
    "audio_urls": ["https://example.com/bgm.mp3"],
    "duration": 10,
    "quality": "720p",
    "aspect_ratio": "16:9",
    "generate_audio": true
  }'
```

## Cas d’usage

- applications de génération vidéo IA
- outils créatifs et workflows d’édition
- animation d’images
- génération de publicités vidéo
- contenu pour réseaux sociaux
- démonstrations produit
- workflows d’édition vidéo multimodale
- visualisation de concepts

## FAQ

### Seedance 2.0 Gateway Service est-il synchrone ?
Non. Seedance 2.0 utilise un workflow asynchrone par tâches.

### Quelle est la différence entre les modèles standard et fast ?
Les modèles fast suivent le même schéma de requête, mais sont optimisés pour l’itération rapide.

### Puis-je générer une vidéo uniquement à partir de texte ?
Oui. Utilisez `seedance-2.0-text-to-video` ou `seedance-2.0-fast-text-to-video`.

### Puis-je animer une image ou créer une transition début/fin ?
Oui. Utilisez image-to-video.

### Puis-je éditer ou prolonger une vidéo existante ?
Oui. Utilisez reference-to-video avec `video_urls`.

### Les références influencent-elles le prix ?
Oui. La durée des vidéos de référence est comptabilisée pour reference-to-video.

### Combien de temps les URL de résultat restent-elles valides ?
Les URL des vidéos générées restent valides pendant 24 heures.

## Structure du dépôt

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

## Dépôts Seedance associés

- [Seedance 2.0 Gateway Service: Price and Guide](https://github.com/EvoLinkAI/Seedance-2.0-Gateway-Service)
- [Seedance 2 Video Gen Skill for OpenClaw](https://github.com/EvoLinkAI/seedance2-video-gen-skill-for-openclaw)
- [Awesome Seedance 2 Guide](https://github.com/EvoLinkAI/awesome-seedance-2-guide)

## Liens associés

- [Seedance 2.0 Pricing](https://evolink.ai/seedance-2-0?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-api)
- [Get API Key](https://evolink.ai/signup?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-api)
- [EvoLink.ai](https://evolink.ai?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-api)

> Veuillez consulter la [Disponibilité Régionale](./docs/regional-availability.fr.md) avant l'intégration.

## Licence

MIT

---

> **Now Available :** Vous pouvez intégrer le Gateway Service dès maintenant en vous appuyant sur la documentation. Dès que Seedance Gateway Service sera officiellement ouvert, nous informerons les utilisateurs Now Available.
