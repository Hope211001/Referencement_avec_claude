# Plan d'Action SEO — slayradio.ch

**Date :** 2026-04-23  
**Analyse réalisée :** En direct sur le site (WebFetch live — 8 pages + sitemap + robots.txt)  
**Score actuel estimé :** 51/100  
**Objectif à 30 jours :** 75/100  
**Objectif à 90 jours :** 85/100

---

## Statut des actions précédentes

| Action | Statut |
|---|---|
| B7 — Copyright footer 2025 → 2026 | ✅ FAIT |
| Titles optimisés sur les pages | ✅ FAIT (partiel) |
| A1 — JSON-LD RadioStation + WebSite | ❌ Non fait |
| A2 — /home/artiste contenu | ❌ Non fait |
| A3 — Podcasts vides noindex | ❌ Non fait |
| A4 — Lazy loading + dimensions | ❌ Non fait |
| A5 — Open Graph + Twitter Cards | ❌ Non fait |
| B1 — Meta descriptions | ❌ Non fait |
| B2 — Schema MusicEvent événements | ❌ Non fait |
| B3 — Canonical tags | ❌ Non fait |
| B4 — Sitemap.static.xml complet | ❌ Non fait |

---

## PRIORITÉ 1 — IMMÉDIAT (cette semaine) — Impact maximum

### A1 — Meta descriptions sur TOUTES les pages
**Impact :** Critique | **Effort :** 30 min  
**Gain estimé :** +8 pts (CTR Google + signal on-page)

Aucune page du site n'a de meta description. C'est le problème le plus simple à corriger avec le gain le plus immédiat.

| Page | Meta description à implémenter |
|------|-------------------------------|
| `/` | `Slay Radio, la web radio suisse 100% musicale diffusée 24h/24 depuis la Suisse romande. House, Afrobeat, R&B — écoutez nos DJs en direct, gratuitement.` |
| `/home/artiste` | `Découvrez les DJs et artistes de Slay Radio : house, afrobeat, R&B depuis la Suisse romande. Réservez un DJ pour votre prochain événement musical.` |
| `/home/podcast` | `Écoutez les podcasts de Slay Radio, la web radio suisse. Mix, sessions et émissions de vos DJs préférés, disponibles en replay 24h/24.` |
| `/home/mix` | `Explorez les mix exclusifs des DJs de Slay Radio. House, afrobeat, R&B et plus — enregistrés et diffusés depuis la Suisse romande.` |
| `/boutique` | `Boutique officielle Slay Radio — vêtements et accessoires de la web radio suisse. Soutenez la scène musicale romande.` |
| `/radio-web-suisse` | `Slay Radio, la web radio suisse en direct 24h/24. Streaming gratuit de house, afrobeat et R&B depuis la Suisse romande — sur tous vos appareils.` |
| `/apropos` | `Découvrez l'histoire de Slay Radio, web radio suisse née d'une passion pour la scène musicale romande. Notre mission : connecter DJs et auditeurs depuis 2024.` |
| `/client/evenement/*` | Générer dynamiquement : `[NOM ÉVÉNEMENT] à [VILLE] — [DATE]. Retrouvez cet événement musical en Suisse romande sur Slay Radio.` |

```html
<!-- Exemple implementation dans <head> -->
<meta name="description" content="Slay Radio, la web radio suisse 100% musicale diffusée 24h/24 depuis la Suisse romande. House, Afrobeat, R&B — écoutez nos DJs en direct, gratuitement.">
```

---

### A2 — Balises canonical sur toutes les pages
**Impact :** Critique | **Effort :** 5 min dev  
**Gain estimé :** +4 pts (évite duplicate content)

```html
<!-- Homepage -->
<link rel="canonical" href="https://slayradio.ch/">

<!-- Pages internes — utiliser l'URL exacte de chaque page -->
<link rel="canonical" href="https://slayradio.ch/home/artiste">
<link rel="canonical" href="https://slayradio.ch/home/podcast">
<link rel="canonical" href="https://slayradio.ch/home/mix">
<link rel="canonical" href="https://slayradio.ch/boutique">
<link rel="canonical" href="https://slayradio.ch/radio-web-suisse">
<link rel="canonical" href="https://slayradio.ch/apropos">

<!-- Événements — utiliser l'URL réelle de la page -->
<link rel="canonical" href="https://slayradio.ch/client/evenement/3">
```

---

### A3 — JSON-LD RadioStation + WebSite sur la homepage
**Impact :** Critique | **Effort :** 30 min (copier-coller)  
**Gain estimé :** +6 pts schema

Ajouter dans le `<head>` de la homepage uniquement :

```html
<script type="application/ld+json">
[
  {
    "@context": "https://schema.org",
    "@type": "RadioStation",
    "name": "Slay Radio",
    "description": "Web radio suisse 100% musicale, diffusée en ligne 24h/24 depuis la Suisse romande. House, afrobeat et R&B.",
    "url": "https://slayradio.ch/",
    "logo": {
      "@type": "ImageObject",
      "url": "https://slayradio.ch/image/logo.jpg",
      "width": 400,
      "height": 400
    },
    "broadcastFrequency": "Online",
    "broadcastTimezone": "Europe/Zurich",
    "areaServed": {
      "@type": "Place",
      "name": "Suisse romande",
      "address": {
        "@type": "PostalAddress",
        "addressCountry": "CH"
      }
    },
    "foundingDate": "2024",
    "contactPoint": {
      "@type": "ContactPoint",
      "email": "contact@slayradio.ch",
      "contactType": "customer service",
      "availableLanguage": "French"
    },
    "sameAs": [
      "https://www.instagram.com/slayradio1/",
      "https://www.youtube.com/channel/UCaD7SGkU6AI8liZdAKgm7nQ",
      "https://www.tiktok.com/@slayradio1?lang=fr"
    ]
  },
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
]
</script>
```

---

### A4 — Open Graph + Twitter Cards sur toutes les pages
**Impact :** Critique | **Effort :** 30 min  
**Gain estimé :** +4 pts (partage social + CTR)

```html
<!-- Dans le <head> de chaque page — adapter title, description et url -->
<meta property="og:type" content="website">
<meta property="og:site_name" content="Slay Radio">
<meta property="og:locale" content="fr_CH">
<meta property="og:title" content="Slay Radio — La Web Radio Suisse 100% Musicale">
<meta property="og:description" content="Web radio suisse 100% digitale, 24h/24 depuis la Suisse romande. House, afrobeat, R&B et sessions live.">
<meta property="og:image" content="https://slayradio.ch/image/og-cover.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:url" content="https://slayradio.ch/">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Slay Radio — La Web Radio Suisse 100% Musicale">
<meta name="twitter:description" content="Web radio suisse 100% digitale, 24h/24 depuis la Suisse romande.">
<meta name="twitter:image" content="https://slayradio.ch/image/og-cover.jpg">
```

**À créer :** image `og-cover.jpg` 1200×630 px avec logo Slay Radio sur fond coloré.

Pour les pages événements, adapter dynamiquement :
```html
<meta property="og:type" content="event">
<meta property="og:title" content="CORBAK FESTIVAL (Neuchâtel) — Slay Radio">
<meta property="og:image" content="https://slayradio.ch/uploads/images/evenement/corbak-festival-neuchatel-2026.webp">
```

---

### A5 — Lazy loading + dimensions sur toutes les images
**Impact :** High (LCP + CLS) | **Effort :** 1-2h  
**Gain estimé :** +6 pts performance

```html
<!-- Logo homepage — PAS de lazy (above the fold) -->
<img src="/image/logo.jpg"
     alt="Slay Radio — Web radio suisse"
     width="180" height="50">

<!-- Image hero homepage — PAS de lazy -->
<img src="/image/hero.jpg"
     alt="Web radio suisse Slay Radio en direct"
     width="1200" height="600">

<!-- Images événements — lazy loading obligatoire -->
<img src="/uploads/images/evenement/corbak-festival-neuchatel-2026.webp"
     alt="CORBAK FESTIVAL Neuchâtel 2026 — 30ème édition"
     loading="lazy" width="600" height="400">

<!-- Icônes réseaux sociaux -->
<img src="/image/social_media_instagram.png"
     alt="Slay Radio sur Instagram"
     width="32" height="32" loading="lazy">
<img src="/image/social_media_tiktok.png"
     alt="Slay Radio sur TikTok"
     width="32" height="32" loading="lazy">
<img src="/image/social_media_youtube.png"
     alt="Slay Radio sur YouTube"
     width="32" height="32" loading="lazy">
```

**Règle générale :**
- Above the fold (logo, hero) → pas de lazy
- Tout le reste → `loading="lazy"` + `width` + `height` obligatoires

---

### A6 — Désindexer les 4 pages vides
**Impact :** Critique | **Effort :** Très faible (10 min)  
**Gain estimé :** +3 pts (supprimer signaux négatifs)

Ces 4 pages sont vides et indexées. Elles envoient un signal de mauvaise qualité à Google :
- `/home/artiste` — "Bientôt disponible"
- `/home/podcast` — "Bientôt disponible"
- `/home/mix` — "Bientôt disponible"
- `/boutique` — "Bientôt disponible"

**Solution rapide :** Ajouter `<meta name="robots" content="noindex, follow">` sur chacune jusqu'à ce qu'elles aient du contenu réel.

```html
<!-- Sur chaque page vide, dans <head> -->
<meta name="robots" content="noindex, follow">
```

**Alternative (mieux à long terme) :** Ajouter du contenu textuel provisoire décrivant ce qui arrive, les genres couverts, les DJs impliqués — même sans les médias réels.

---

## PRIORITÉ 2 — COURT TERME (2 semaines)

### B1 — Schema MusicEvent sur chaque page événement
**Impact :** High (rich results Google) | **Effort :** Moyen  
**Gain estimé :** +5 pts (éligibilité aux résultats enrichis)

Pour chaque `/client/evenement/[ID]`, injecter depuis la base de données :

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "MusicEvent",
  "name": "CORBAK FESTIVAL",
  "startDate": "2026-05-21T18:00:00+01:00",
  "endDate": "2026-05-23T23:00:00+01:00",
  "eventStatus": "https://schema.org/EventScheduled",
  "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
  "location": {
    "@type": "Place",
    "name": "Neuchâtel",
    "address": {
      "@type": "PostalAddress",
      "addressLocality": "Neuchâtel",
      "addressCountry": "CH"
    }
  },
  "image": "https://slayradio.ch/uploads/images/evenement/corbak-festival-neuchatel-2026.webp",
  "organizer": {
    "@type": "Organization",
    "name": "Slay Radio",
    "url": "https://slayradio.ch/"
  },
  "performer": {
    "@type": "MusicGroup",
    "name": "CORBAK"
  }
}
</script>
```

---

### B2 — Compléter sitemap.static.xml
**Impact :** Medium | **Effort :** Très faible (5 min)  
**Gain estimé :** +2 pts crawlabilité

Pages manquantes à ajouter :

```xml
<url>
  <loc>https://slayradio.ch/home/artiste</loc>
  <lastmod>2026-04-23T00:00:00+00:00</lastmod>
  <changefreq>weekly</changefreq>
  <priority>0.8</priority>
</url>
<url>
  <loc>https://slayradio.ch/home/podcast</loc>
  <lastmod>2026-04-23T00:00:00+00:00</lastmod>
  <changefreq>weekly</changefreq>
  <priority>0.7</priority>
</url>
<url>
  <loc>https://slayradio.ch/home/mix</loc>
  <lastmod>2026-04-23T00:00:00+00:00</lastmod>
  <changefreq>weekly</changefreq>
  <priority>0.7</priority>
</url>
<url>
  <loc>https://slayradio.ch/boutique</loc>
  <lastmod>2026-04-23T00:00:00+00:00</lastmod>
  <changefreq>monthly</changefreq>
  <priority>0.6</priority>
</url>
```

**Note :** Si les pages vides sont en `noindex`, ne pas les inclure dans le sitemap non plus — les deux doivent être cohérents.

---

### B3 — Améliorer les titles faibles
**Impact :** Medium | **Effort :** 10 min  
**Gain estimé :** +2 pts

| Page | Title actuel | Title optimisé |
|------|-------------|----------------|
| `/boutique` | "Boutique — Slay Radio" | "Boutique Slay Radio — Merchandising Web Radio Suisse" |
| `/radio-web-suisse` | "Slay Radio — Radio web suisse en direct" | "Radio Web Suisse en Direct 24h/24 — Slay Radio \| House, Afrobeat, R&B" |

---

### B4 — Renommer et convertir les images événements en WebP
**Impact :** Medium (SEO images + performance) | **Effort :** Faible  
**Gain estimé :** +3 pts

| Fichier actuel | Nouveau nom SEO |
|----------------|-----------------|
| `Capture-d-ecran-2026-04-17-094305-69e1e56d6d2ef.png` | `corbak-festival-neuchatel-2026.webp` |
| `Capture-d-ecran-2026-04-17-102300-69e1eef79d3da.png` | `blues-rules-festival-crissier-2026.webp` |
| `Capture-d-ecran-2026-04-17-102100-69e1ed7b35b1c.png` | `festiboc-bofflens-2026.webp` |
| `Capture-d-ecran-2026-04-17-103122-69e1f087122e6.png` | `festineuch-neuchatel-2026.webp` |

```bash
# Conversion batch (nécessite cwebp installé)
for f in uploads/images/evenement/*.png; do
  cwebp -q 85 "$f" -o "${f%.png}.webp"
done
```

Mettre à jour les `src` dans le HTML + les chemins dans la base de données après conversion.

---

## PRIORITÉ 3 — MOYEN TERME (1 mois)

### C1 — Pages artistes individuelles avec schema Person
**Impact :** High | **Effort :** Élevé  
**Gain estimé :** +8 pts contenu + E-E-A-T

Structure cible pour `/artiste/[slug-dj]` :
1. H1 : "DJ [Nom] — [Genre] depuis [Ville]"
2. Bio 200+ mots
3. Photo du DJ
4. Mix/podcasts du DJ sur le site
5. JSON-LD Person :

```json
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "DJ [Nom]",
  "jobTitle": "DJ",
  "url": "https://slayradio.ch/artiste/[slug]",
  "worksFor": {
    "@type": "RadioStation",
    "name": "Slay Radio",
    "url": "https://slayradio.ch/"
  },
  "genre": ["House", "Afrobeat"]
}
```

**Obligatoire :** Rendu SSR (Server-Side Rendering) — Googlebot ne parse pas le JavaScript.

---

### C2 — URLs événements → slugs + redirections 301
**Impact :** High | **Effort :** Élevé  
**Gain estimé :** +4 pts structure

```
Actuel  : /client/evenement/3
Cible   : /evenements/corbak-festival-neuchatel-2026

Actuel  : /home/evenement
Cible   : /evenements
```

**Important :** Mettre en place les redirections 301 avant la migration.

---

### C3 — Enrichir /apropos avec E-E-A-T
**Impact :** High | **Effort :** Moyen  
**Gain estimé :** +5 pts

La page a 400-450 mots mais ZÉRO mention d'équipe, ZÉRO statistique, ZÉRO preuve d'autorité.

À ajouter :
1. Photos + prénoms des fondateurs/DJs principaux
2. Chiffres clés : nb auditeurs, nb DJs, heures de diffusion
3. Date de création précise
4. Mentions presse (si existantes)
5. Schema Organization :

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Slay Radio",
  "url": "https://slayradio.ch/",
  "email": "contact@slayradio.ch",
  "foundingDate": "2024",
  "description": "Web radio suisse 100% musicale depuis la Suisse romande.",
  "areaServed": "Suisse romande",
  "sameAs": [
    "https://www.instagram.com/slayradio1/",
    "https://www.youtube.com/channel/UCaD7SGkU6AI8liZdAKgm7nQ",
    "https://www.tiktok.com/@slayradio1?lang=fr"
  ]
}
```

---

### C4 — Maillage interne vers les événements
**Impact :** Medium | **Effort :** Faible  
**Gain estimé :** +2 pts

- Homepage : lier chaque festival avec anchor text descriptif
- /radio-web-suisse : mentionner les événements à venir avec liens
- Pages artistes (quand créées) : lier vers les événements

---

### C5 — Corriger l'encoding UTF-8 de llms.txt
**Impact :** Low (GEO) | **Effort :** Très faible  
**Gain estimé :** +1 pt

Vérifier et re-sauvegarder en UTF-8 strict (sans BOM).

---

## Récapitulatif et Calendrier

| # | Action | Délai | Gain |
|---|--------|-------|------|
| ✅ B7 | Footer copyright | FAIT | signal |
| 🔴 A1 | Meta descriptions toutes pages | Sem. 1 | +8 pts |
| 🔴 A2 | Canonical toutes pages | Sem. 1 | +4 pts |
| 🔴 A3 | JSON-LD RadioStation + WebSite | Sem. 1 | +6 pts |
| 🔴 A4 | Open Graph + Twitter Cards | Sem. 1 | +4 pts |
| 🔴 A5 | Lazy loading + dimensions images | Sem. 1 | +6 pts |
| 🔴 A6 | Noindex pages vides (artiste/podcast/mix/boutique) | Sem. 1 | +3 pts |
| ⚠️ B1 | Schema MusicEvent sur événements | Sem. 2 | +5 pts |
| ⚠️ B2 | Sitemap.static.xml complet | Sem. 2 | +2 pts |
| ⚠️ B3 | Titles boutique + radio-web-suisse | Sem. 2 | +2 pts |
| ⚠️ B4 | Images WebP renommées | Sem. 2 | +3 pts |
| 📅 C1 | Pages artistes individuelles SSR | Mois 1 | +8 pts |
| 📅 C2 | URLs événements slugs + 301 | Mois 1 | +4 pts |
| 📅 C3 | /apropos E-E-A-T + équipe | Mois 1 | +5 pts |
| 📅 C4 | Maillage interne | Mois 1 | +2 pts |
| 📅 C5 | UTF-8 llms.txt | Mois 1 | +1 pt |

**Score actuel :** 51/100  
**Score après Semaine 1 (A1-A6) :** ~82/100 (+31 pts)  
**Score après Semaine 2 (A+B) :** ~94/100 (+12 pts supplémentaires)  
**Score après Mois 1 (A+B+C) :** ~97/100

---

## Scripts de vérification

```bash
# PageSpeed Insights
python3 scripts/pagespeed.py https://slayradio.ch/ --strategy mobile
python3 scripts/pagespeed.py https://slayradio.ch/ --strategy desktop

# Rendu Googlebot
curl -A "Googlebot/2.1" https://slayradio.ch/home/artiste

# Rapport HTML complet
python3 scripts/generate_report.py https://slayradio.ch/ --output SEO-REPORT.html

# Validation JSON-LD
python3 scripts/validate_schema.py index.html

# Sitemap + robots
PYTHONIOENCODING=utf-8 python3 scripts/robots_checker.py https://slayradio.ch/

# Encoding llms.txt
curl https://slayradio.ch/llms.txt | head -5
```
