# Plan d'Action SEO — slayradio.ch
**Date:** 2026-04-29 | **Score actuel: 62/100** | **Cible: 80+/100**

---

## ETAPE 0 — Google Search Console (Faire en premier)

**Action:** Uploader le fichier de verification Google sur le serveur web.

Le fichier `googlefdc971f91a5e2331.html` est deja dans ce dossier. Il doit etre accessible a l'URL:
```
https://slayradio.ch/googlefdc971f91a5e2331.html
```

**Comment faire:**
1. Connectez-vous au gestionnaire de fichiers de votre hebergeur (cPanel, FTP, SFTP...)
2. Uploadez `googlefdc971f91a5e2331.html` a la racine du site web (meme dossier que `index.php` ou `public/`)
3. Verifiez que https://slayradio.ch/googlefdc971f91a5e2331.html retourne le contenu: `google-site-verification: googlefdc971f91a5e2331.html`
4. Dans Google Search Console → cliquez "Verifier"

**Pourquoi:** Sans GSC verifie, vous n'avez pas de donnees sur vos positions, CTR, pages indexees, ni erreurs de crawl.

---

## IMMEDIAT — Semaine 1 (Impact critique)

### 1. Ajouter une meta description a `/radio-web-suisse`

Cette page cible le mot-cle "radio web suisse" — elle n'a pas de meta description. C'est une opportunite directe de CTR.

Ajoutez dans le `<head>` de la page `/radio-web-suisse`:
```html
<meta name="description" content="Ecoutez la radio web suisse en direct — House, Afrobeat et R&B 24h/24 sur Slay Radio. Streaming gratuit, sans inscription, depuis la Suisse romande.">
```
(147 caracteres — ideal entre 140-155)

---

### 2. Ajouter une meta description a `/apropos`

```html
<meta name="description" content="Decouvrez l'histoire et la mission de Slay Radio, la web radio suisse 100% musicale. DJs, mix exclusifs et evenements depuis la Suisse romande.">
```
(148 caracteres)

---

### 3. Ajouter un schema WebSite avec SearchAction

Dans le `<head>` de la page d'accueil uniquement, ajoutez:
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "Slay Radio",
  "url": "https://slayradio.ch/",
  "potentialAction": {
    "@type": "SearchAction",
    "target": {
      "@type": "EntryPoint",
      "urlTemplate": "https://slayradio.ch/home/artiste?q={search_term_string}"
    },
    "query-input": "required name=search_term_string"
  }
}
</script>
```

---

### 4. Ajouter un schema Organization

Dans le `<head>` de la page d'accueil:
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Slay Radio",
  "url": "https://slayradio.ch/",
  "logo": {
    "@type": "ImageObject",
    "url": "https://slayradio.ch/image/logo.jpg",
    "width": 400,
    "height": 400
  },
  "email": "contact@slayradio.ch",
  "description": "Web radio suisse 100% musicale, diffusee en ligne 24h/24 depuis la Suisse romande.",
  "sameAs": [
    "https://www.instagram.com/slayradio1/",
    "https://www.tiktok.com/@slayradio1",
    "https://www.youtube.com/channel/UCaD7SGkU6AI8liZdAKgm7nQ"
  ],
  "areaServed": {
    "@type": "GeoCircle",
    "geoMidpoint": {
      "@type": "GeoCoordinates",
      "latitude": 46.8182,
      "longitude": 8.2275
    },
    "geoRadius": "200000"
  }
}
</script>
```

---

### 5. Corriger l'image hero Unsplash

**Etape A (immediat):** Ajouter les dimensions manquantes pour eviter le CLS:
```html
<!-- Avant: -->
<img src="https://images.unsplash.com/photo-1516450360452-9312f5e86fc7?w=600&h=450&fit=crop"
     alt="Studio radio Slay Radio — web radio suisse"
     class="rounded-2xl shadow-2xl w-full h-auto object-cover relative z-10">

<!-- Apres: -->
<img src="https://images.unsplash.com/photo-1516450360452-9312f5e86fc7?w=600&h=450&fit=crop"
     alt="Studio radio Slay Radio — web radio suisse"
     width="600" height="450"
     class="rounded-2xl shadow-2xl w-full h-auto object-cover relative z-10">
```

**Etape B (strategique):** Telechargez l'image et hebergez-la localement:
```
/image/studio-radio-slay.jpg
```
Puis remplacez l'URL Unsplash par: `src="/image/studio-radio-slay.jpg"`. Cela elimine une dependance externe et ameliore le LCP.

---

## RAPIDE — Dans les 2 semaines (Impact fort, effort faible)

### 6. Corriger le schema RadioStation (retirer le tableau JSON)

Actuellement la schema RadioStation est enveloppee dans un tableau `[{...}]`. Corrigez:
```json
// Avant (avec tableau):
[
  {
    "@context": "https://schema.org",
    "@type": "RadioStation",
    ...
  }
]

// Apres (objet direct):
{
  "@context": "https://schema.org",
  "@type": "RadioStation",
  ...
}
```

---

### 7. Ajouter un schema RadioStation sur `/radio-web-suisse`

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "RadioStation",
  "name": "Slay Radio",
  "broadcastDisplayName": "Slay Radio",
  "genre": ["House", "Afrobeat", "R&B"],
  "description": "Radio web suisse en direct — House, Afrobeat et R&B 24h/24 depuis la Suisse romande.",
  "url": "https://slayradio.ch/radio-web-suisse",
  "broadcastFrequency": "Online",
  "broadcastTimezone": "Europe/Zurich"
}
</script>
```

---

### 8. Corriger l'espace dans og:image

Dans votre template HTML, trouvez la balise og:image:
```html
<!-- Avant (espace/tabulation avant l'URL): -->
<meta property="og:image" content="	https://slayradio.ch/image/og-default.png">

<!-- Apres (URL propre): -->
<meta property="og:image" content="https://slayradio.ch/image/og-default.png">
```

---

### 9. Corriger l'encodage de llms.txt

Ouvrez `llms.txt` dans un editeur (VS Code), verifiez que l'encodage est **UTF-8** (sans BOM), et re-sauvegardez. Les caracteres accentues comme "evenements" apparaissent corrompus via le script de verification.

---

### 10. Ajouter `/home/podcast` au sitemap

Dans `sitemap.static.xml`, ajoutez:
```xml
<url>
  <loc>https://slayradio.ch/home/podcast</loc>
  <lastmod>2026-04-29</lastmod>
  <changefreq>weekly</changefreq>
  <priority>0.7</priority>
</url>
```

---

## MOYEN TERME — Dans le mois (Impact important)

### 11. Creer une page Mentions Legales / Politique de confidentialite

Creez `/mentions-legales` ou `/politique-confidentialite` avec:
- Responsable du traitement (Slay Radio)
- Donnees collectees et finalites
- Droits des utilisateurs (acces, rectification, suppression)
- Contact: contact@slayradio.ch
- Reference a la loi suisse nLPD

Ajoutez le lien dans le footer a cote du copyright.

**Pourquoi:** Requis par la nLPD suisse (en vigueur depuis sept. 2023). Signal de confiance fort pour E-E-A-T.

---

### 12. Ajouter des bios DJ / equipe sur /apropos

Pour chaque DJ/animateur principal, ajoutez une section avec:
- Nom complet
- Photo (avec alt descriptif)
- Genres de predilection
- Annees d'experience / parcours
- Liens reseaux sociaux

Exemple de schema JSON-LD a ajouter pour chaque profil:
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "DJ BENDO",
  "url": "https://slayradio.ch/artiste/dj-bendo",
  "image": "https://slayradio.ch/uploads/images/artistes/dj-bendo-ea4ea2.jpg",
  "jobTitle": "DJ & Animateur",
  "worksFor": {
    "@type": "Organization",
    "name": "Slay Radio"
  }
}
</script>
```

---

### 13. Ajouter BreadcrumbList sur les pages internes

Pour `/apropos`:
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Accueil",
      "item": "https://slayradio.ch/"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "A propos",
      "item": "https://slayradio.ch/apropos"
    }
  ]
}
</script>
```

Pour `/radio-web-suisse`:
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Accueil",
      "item": "https://slayradio.ch/"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Radio Web Suisse",
      "item": "https://slayradio.ch/radio-web-suisse"
    }
  ]
}
</script>
```

---

### 14. Corriger les 4 pages evenements orphelines

Ces pages n'ont qu'un seul lien interne:
- `/evenement/wine-night-festival-geneve`
- `/evenement/avenches-open-air`
- `/evenement/blues-rules-festival-crissier`
- `/evenement/festiboc-bofflens`

**Solution:** Sur la page `/home/evenement`, ajoutez un lien vers chacune. Sur chaque page d'evenement, ajoutez des liens "Voir aussi" vers d'autres evenements proches.

---

### 15. Verifier et ajouter /boutique au sitemap

Si `/boutique` est publique et indexable, ajoutez-la a `sitemap.static.xml`:
```xml
<url>
  <loc>https://slayradio.ch/boutique</loc>
  <lastmod>2026-04-29</lastmod>
  <changefreq>weekly</changefreq>
  <priority>0.6</priority>
</url>
```

---

## STRATEGIQUE — 1 a 3 mois

### 16. Optimiser les Core Web Vitals

Une fois le fichier GSC uploade et verifie:
1. Consultez le rapport "Signaux Web" dans Google Search Console
2. Identifiez les pages avec LCP > 2.5s ou CLS > 0.1
3. Executez: `python scripts/pagespeed.py https://slayradio.ch/ --strategy mobile`
4. Priorites typiques:
   - LCP: heberger l'image hero en local, precharger avec `<link rel="preload">`
   - CLS: verifier que tous les elements d'image ont `width` et `height`
   - TTFB: activer la mise en cache Cloudflare ou optimiser la BDD

---

### 17. Reduire le TTFB sous 800ms

Avec un TTFB de 1189ms, l'hebergement actuel est lent. Options:
1. Activer Cloudflare (gratuit) en mode proxy — reduit le TTFB de 40-60%
2. Activer OPcache PHP sur le serveur
3. Mettre en cache les requetes base de donnees (Redis/Memcached)
4. Utiliser un CDN pour les assets statiques (images, JS, CSS)

---

### 18. Construire un cluster de contenu autour de "radio web suisse"

La page `/radio-web-suisse` est un bon debut. Elargissez avec:
- `/radio-house-suisse` — focus sur le genre house
- `/radio-afrobeat-suisse` — focus sur l'afrobeat
- `/djs-suisse-romande` — listing DJs locaux
- `/evenements-musicaux-suisse` — hub evenements

Reliez toutes ces pages entre elles et depuis la page pilier `/radio-web-suisse`.

---

### 19. Obtenir des mentions externes

- Soumettez Slay Radio aux annuaires de radios suisses (Radio.net, TuneIn, Swiss-Radios.ch)
- Contactez les blogs musique suisses romands pour des articles
- Proposez des partenariats avec les festivals listes sur le site (Balelec, Corbak)
- Demandez a etre liste dans les articles "meilleures web radios suisses"

---

## Recapitulatif des priorites

| Priorite | Action | Impact | Effort |
|---|---|---|---|
| 0 | Uploader googlefdc971f91a5e2331.html | Debloquer GSC | 5 min |
| 1 | Meta desc /radio-web-suisse | CTR + ranking | 5 min |
| 2 | Meta desc /apropos | CTR | 5 min |
| 3 | Schema WebSite + Organization | Rich results | 15 min |
| 4 | Dimensions image hero (width/height) | CLS | 2 min |
| 5 | Heberger image hero localement | LCP | 30 min |
| 6 | Corriger schema array wrapper | Validite | 5 min |
| 7 | Schema sur /radio-web-suisse | Rich results | 10 min |
| 8 | Corriger og:image whitespace | Social preview | 2 min |
| 9 | Corriger encodage llms.txt | AI crawlers | 5 min |
| 10 | Ajouter /home/podcast au sitemap | Indexation | 5 min |
| 11 | Page mentions legales | E-E-A-T + conformite | 2h |
| 12 | Bios DJ/equipe | E-E-A-T | 3h |
| 13 | BreadcrumbList inner pages | Navigation + rich results | 30 min |
| 14 | Liens vers pages orphelines | Architecture | 30 min |
| 15 | Optimiser CWV | Performance ranking | 4-8h |
| 16 | Reduire TTFB | LCP, performance | 2-4h |
| 17 | Cluster contenu | Trafic organique | Ongoing |
| 18 | Mentions externes | Autorite | Ongoing |

**Score cible apres actions 0-9:** ~72/100
**Score cible apres toutes les actions:** 82-88/100
