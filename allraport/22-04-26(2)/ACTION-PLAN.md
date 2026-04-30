# Plan d'Action SEO — slayradio.ch

**Date :** 2026-04-23  
**Analyse réalisée :** En direct sur le site (WebFetch + sitemap + robots.txt)  
**Score actuel estimé :** 49/100  
**Objectif à 30 jours :** 73/100  
**Objectif à 90 jours :** 82/100

---

## Résumé des problèmes détectés

| Catégorie | Statut | Détail |
|---|---|---|
| Meta description homepage | ✅ OK | Présente et pertinente |
| Meta descriptions autres pages | ❌ Absentes | 0 sur /radio-web-suisse, événements, artistes |
| Balise canonical | ❌ Absente | Aucune page |
| Schema.org JSON-LD | ❌ Absent | 0 sur tout le site |
| Images alt text | ❌ Manquant | Logo, events, studio, réseaux sociaux |
| Open Graph / Twitter Cards | ❌ Non confirmé | Non détecté |
| Lazy loading images | ❌ Absent | Aucun `loading="lazy"` |
| Dimensions width/height images | ❌ Absent | CLS non protégé |
| Sitemap | ✅ Présent | Index → 2 sitemaps enfants |
| robots.txt | ✅ Bon | Admin protégé, AI bots autorisés |
| Page podcasts | ❌ Vide | "Aucun podcast trouvé" — page vide indexée |
| URLs événements | ⚠️ Non-SEO | `/client/evenement/3` au lieu de slugs lisibles |
| Pages artistes | ⚠️ Thin content | Page affiche "bientôt" au lieu des vrais artistes |
| Breadcrumbs | ✅ Présents | Sur les pages événements |
| Page /radio-web-suisse | ✅ Bonne | ~550 mots, bien ciblée |

---

## PRIORITÉ 1 — IMMÉDIAT (cette semaine) — Bloqueurs critiques

### A1 — JSON-LD RadioStation + WebSite sur la homepage
**Impact :** Critique | **Effort :** Faible (copier-coller + 30 min)  
**Gain estimé :** +6 pts schema

Ajouter dans le `<head>` de la homepage :

```html
<script type="application/ld+json">
[
  {
    "@context": "https://schema.org",
    "@type": "RadioStation",
    "name": "Slay Radio",
    "description": "Web radio suisse 100% musicale, diffusée en ligne 24h/24 depuis la Suisse romande. Écoutez nos DJs en live, découvrez leurs mix house, afrobeat et R&B.",
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

### A2 — Corriger la page /home/artiste (thin content critique)
**Impact :** Critique | **Effort :** Faible si contenu en base  
**Gain estimé :** +6 pts SEO, indexation des artistes

La page affiche "De nouveaux artistes rejoignent bientôt la famille" alors que des artistes existent. Ce thin content pénalise l'ensemble du domaine.

**Actions :**
1. Connecter la page `/home/artiste` à la base de données artistes
2. Afficher au minimum : photo, nom, genre musical, lien vers profil
3. Si l'affichage dynamique n'est pas prêt → créer une liste statique temporaire

---

### A3 — Désindexer ou corriger la page podcasts vide
**Impact :** Critique | **Effort :** Très faible  
**Gain estimé :** +2 pts (supprimer signal négatif)

La page `/home/podcast` affiche actuellement **"Aucun podcast trouvé"** — une page vide indexée par Google envoie un signal de qualité négatif pour tout le domaine.

**Option A (rapide) :** Ajouter `<meta name="robots" content="noindex">` sur `/home/podcast` jusqu'à ce qu'il y ait du contenu.  
**Option B (mieux) :** Ajouter du contenu temporaire : description de la section, ce qui arrive, les genres couverts.

---

### A4 — Lazy loading + dimensions sur toutes les images
**Impact :** High (LCP + CLS) | **Effort :** Minimal (1-2h)  
**Gain estimé :** +6 pts performance

```html
<!-- Logo (PAS de lazy loading — above the fold) -->
<img src="/image/logo.jpg" alt="Slay Radio — Web radio suisse" width="180" height="50">

<!-- Images événements et contenu -->
<img src="/uploads/images/evenement/corbak.png"
     alt="CORBAK FESTIVAL Neuchâtel 2026"
     loading="lazy" width="600" height="400">

<!-- Icônes réseaux sociaux -->
<img src="/image/social_media_instagram.png" alt="Slay Radio sur Instagram" width="32" height="32" loading="lazy">
<img src="/image/social_media_tiktok.png" alt="Slay Radio sur TikTok" width="32" height="32" loading="lazy">
<img src="/image/social_media_youtube.png" alt="Slay Radio sur YouTube" width="32" height="32" loading="lazy">
```

**Règle :** Logo et première image hero → pas de lazy. Tout le reste → `loading="lazy"`.

---

### A5 — Ajouter les balises Open Graph et Twitter Cards
**Impact :** High (partage social + CTR) | **Effort :** Faible  
**Gain estimé :** +3 pts visibilité sociale

Ces balises ne sont pas détectées sur le site. Elles sont essentielles pour un site musical/radio qui mise sur les réseaux sociaux.

```html
<!-- Dans le <head> de chaque page -->
<meta property="og:type" content="website">
<meta property="og:title" content="Slay Radio — La Web Radio Suisse 100% Musicale">
<meta property="og:description" content="Web radio suisse 100% digitale, 24h/24 depuis la Suisse romande. House, afrobeat, R&B et sessions live.">
<meta property="og:image" content="https://slayradio.ch/image/og-cover.jpg">
<meta property="og:url" content="https://slayradio.ch/">
<meta property="og:locale" content="fr_CH">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Slay Radio — La Web Radio Suisse 100% Musicale">
<meta name="twitter:description" content="Web radio suisse 100% digitale, 24h/24 depuis la Suisse romande.">
<meta name="twitter:image" content="https://slayradio.ch/image/og-cover.jpg">
```

**À créer :** Une image `og-cover.jpg` de 1200×630 px avec le logo Slay Radio.

---

## PRIORITÉ 2 — COURT TERME (2 semaines) — Victoires rapides

### B1 — Meta descriptions sur toutes les pages internes
**Impact :** Medium | **Effort :** Très faible (30 min)  
**Gain estimé :** +3 pts on-page, +CTR dans Google

| Page | Meta description suggérée |
|------|--------------------------|
| `/radio-web-suisse` | "Slay Radio, la web radio suisse 100% musicale diffusée en ligne 24h/24. Découvrez la scène musicale romande : house, afrobeat, R&B et DJ sets live." |
| `/home/artiste` | "Découvrez les DJs et artistes de Slay Radio : house, afrobeat, R&B depuis la Suisse romande. Réservez un DJ pour votre événement musical." |
| `/home/podcast` | "Écoutez les podcasts de Slay Radio, la web radio suisse. Mix, sessions et émissions en replay, disponibles 24h/24." |
| `/home/mix` | "Explorez les mix exclusifs des DJs de Slay Radio. House, afrobeat, R&B et plus — diffusés depuis la Suisse romande." |
| `/apropos` | "Slay Radio, la web radio suisse née d'une passion pour la scène locale. Notre mission : connecter DJs et auditeurs en Suisse romande depuis 2024." |
| `/boutique` | "Boutique Slay Radio — merchandising officiel de la web radio suisse. Soutenez la scène musicale romande." |
| `/client/evenement/*` | Générer dynamiquement : "[Nom] à [Ville] le [Date] — Slay Radio couvre cet événement musical en Suisse romande." |

---

### B2 — Schema MusicEvent sur chaque page événement
**Impact :** High (rich results Google) | **Effort :** Moyen  
**Gain estimé :** +5 pts schema, éligibilité rich results

Pour chaque page `/client/evenement/*`, injecter dynamiquement depuis les données en base :

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "MusicEvent",
  "name": "[NOM ÉVÉNEMENT]",
  "startDate": "[DATE ISO 8601]",
  "endDate": "[DATE ISO 8601]",
  "eventStatus": "EventScheduled",
  "eventAttendanceMode": "OfflineEventAttendanceMode",
  "location": {
    "@type": "Place",
    "name": "[NOM LIEU]",
    "address": {
      "@type": "PostalAddress",
      "addressLocality": "[VILLE]",
      "addressCountry": "CH"
    }
  },
  "organizer": {
    "@type": "Organization",
    "name": "[NOM ORGANISATEUR]",
    "url": "[URL ORGANISATEUR]"
  },
  "image": "https://slayradio.ch/uploads/images/evenement/[NOM-FICHIER].webp",
  "performer": {
    "@type": "MusicGroup",
    "name": "[NOM ARTISTE PRINCIPAL]"
  }
}
</script>
```

---

### B3 — Ajouter la balise canonical sur toutes les pages
**Impact :** Medium | **Effort :** Très faible (5 min dev)  
**Gain estimé :** +2 pts technique

```html
<!-- Homepage -->
<link rel="canonical" href="https://slayradio.ch/">
<!-- Page artistes -->
<link rel="canonical" href="https://slayradio.ch/home/artiste">
<!-- Événement -->
<link rel="canonical" href="https://slayradio.ch/client/evenement/5">
<!-- Landing page -->
<link rel="canonical" href="https://slayradio.ch/radio-web-suisse">
```

---

### B4 — Compléter sitemap.static.xml
**Impact :** Medium | **Effort :** Très faible  
**Gain estimé :** +2 pts crawlabilité

Pages manquantes à ajouter dans `sitemap.static.xml` :

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

---

### B5 — Renommer et convertir les images événements en WebP
**Impact :** Medium (SEO images + performance) | **Effort :** Faible  
**Gain estimé :** +3 pts

| Fichier actuel | Nouveau nom SEO |
|----------------|-----------------|
| `Capture-d-ecran-2026-04-17-094305-69e1e56d6d2ef.png` | `corbak-festival-neuchatel-2026.webp` |
| `Capture-d-ecran-2026-04-17-102300-69e1eef79d3da.png` | `blues-rules-festival-crissier-2026.webp` |
| `Capture-d-ecran-2026-04-17-102100-69e1ed7b35b1c.png` | `festiboc-bofflens-2026.webp` |
| `Capture-d-ecran-2026-04-17-103122-69e1f087122e6.png` | `festineuch-neuchatel-2026.webp` |

```bash
# Conversion batch
for f in uploads/images/evenement/*.png; do
  cwebp -q 85 "$f" -o "${f%.png}.webp"
done
```

Mettre à jour les `src` HTML après conversion.

---

### B6 — Corriger l'encodage UTF-8 du fichier llms.txt
**Impact :** Low (GEO) | **Effort :** Très faible  
**Gain estimé :** +1 pt GEO

Le fichier contient du texte corrompu ("Ã©vÃ©nements" au lieu de "événements").

```bash
curl https://slayradio.ch/llms.txt | head -5
# Re-sauvegarder en UTF-8 strict (sans BOM) si caractères corrompus
```

---

### B7 — Corriger le copyright footer
**Impact :** Signal fraîcheur | **Effort :** 2 min  
**Gain estimé :** Signal positif de maintenance

Remplacer `© 2025 Slay Radio` → `© 2026 Slay Radio` dans le footer.

---

## PRIORITÉ 3 — MOYEN TERME (1 mois) — Stratégique

### C1 — Créer des pages artistes individuelles avec schema Person
**Impact :** High | **Effort :** Élevé  
**Gain estimé :** +8 pts contenu + E-E-A-T

Chaque DJ mérite une page dédiée. C'est une mine de mots-clés longue traîne ("DJ house Genève", "DJ afrobeat Lausanne").

Structure cible pour chaque page `/artiste/[slug-dj]` :
1. H1 : "DJ [Nom] — [Genre] depuis [Ville]"
2. Bio de 200+ mots (style, influences, parcours, événements joués)
3. Photo du DJ
4. Liens vers ses mix/podcasts sur le site
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

**Important :** S'assurer que ces pages sont rendues côté serveur (SSR) — Googlebot ne parse pas le JavaScript au premier passage.

---

### C2 — Corriger l'architecture des URLs événements
**Impact :** High (SEO longue traîne) | **Effort :** Élevé (redirections)  
**Gain estimé :** +4 pts structure

Les URLs actuelles `/client/evenement/3` sont opaques. Google ne peut pas déduire le sujet.

**Migration cible :**
```
Actuel  : /client/evenement/3
Cible   : /evenements/corbak-festival-neuchatel-2026

Actuel  : /home/evenement
Cible   : /evenements
```

**Obligatoire :** Mettre en place des redirections 301 des anciennes vers les nouvelles URLs avant toute migration.

---

### C3 — Enrichir /apropos avec signaux E-E-A-T
**Impact :** High | **Effort :** Moyen  
**Gain estimé :** +5 pts E-E-A-T

Contenu à ajouter :
1. **Section équipe** : Photos + prénoms des fondateurs/DJ principaux + rôles
2. **Histoire datée** : "Fondée en [année], Slay Radio a démarré avec..."
3. **Chiffres clés** : Nb d'auditeurs, nb de DJs, heures de diffusion
4. **Presse / mentions** : Tout article suisse ayant mentionné Slay Radio
5. **Schema Organization** :

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
    "https://www.youtube.com/channel/UCaD7SGkU6AI8liZdAKgm7nQ"
  ]
}
```

---

### C4 — Maillage interne vers les pages événements
**Impact :** Medium | **Effort :** Faible  
**Gain estimé :** +2 pts maillage

Les pages événements n'ont qu'un seul lien entrant depuis `/home/evenement`. Ajouter :
- Sur la homepage : lier chaque festival avec anchor text descriptif ("CORBAK FESTIVAL 2026 à Neuchâtel")
- Sur `/radio-web-suisse` : mentionner les événements à venir avec liens contextuels
- Sur les pages artistes (quand créées) : lier vers les événements où ils jouent

---

### C5 — Corriger les lastmod dynamiques dans le sitemap
**Impact :** Medium (crawl budget) | **Effort :** Moyen  
**Gain estimé :** +2 pts technique

Actuellement tous les `lastmod` sont identiques (2026-04-21). Le générateur doit utiliser la vraie date de modification depuis la base de données pour chaque entrée.

---

### C6 — Remplacer la photo Unsplash par une photo réelle du studio
**Impact :** Low (E-E-A-T) | **Effort :** Moyen (logistique photo)  
**Gain estimé :** +1 pt E-E-A-T

La photo de studio générique (Unsplash) nuit à l'authenticité. Une photo réelle du setup ou de l'équipe renforce la crédibilité aux yeux de Google et des visiteurs.

---

## Récapitulatif et Calendrier

| # | Action | Délai | Impact |
|---|--------|-------|--------|
| 🔴 A1 | JSON-LD RadioStation + WebSite homepage | Sem. 1 | +6 pts |
| 🔴 A2 | /home/artiste — afficher les artistes | Sem. 1 | +6 pts |
| 🔴 A3 | Désindexer / corriger page podcasts vide | Sem. 1 | +2 pts |
| 🔴 A4 | Lazy loading + dimensions images | Sem. 1 | +6 pts |
| 🔴 A5 | Open Graph + Twitter Cards | Sem. 1 | +3 pts |
| ⚠️ B1 | Meta descriptions toutes pages | Sem. 2 | +3 pts |
| ⚠️ B2 | Schema MusicEvent sur événements | Sem. 2 | +5 pts |
| ⚠️ B3 | Canonical tags | Sem. 2 | +2 pts |
| ⚠️ B4 | sitemap.static.xml complet | Sem. 2 | +2 pts |
| ⚠️ B5 | Renommer images → WebP | Sem. 2 | +3 pts |
| ⚠️ B6 | Encodage UTF-8 llms.txt | Sem. 2 | +1 pt |
| ⚠️ B7 | Copyright footer 2025 → 2026 | Sem. 2 | signal |
| 📅 C1 | Pages artistes individuelles SSR | Mois 1 | +8 pts |
| 📅 C2 | URLs événements → slugs + 301 | Mois 1 | +4 pts |
| 📅 C3 | /apropos E-E-A-T + équipe | Mois 1 | +5 pts |
| 📅 C4 | Maillage interne événements | Mois 1 | +2 pts |
| 📅 C5 | Lastmod dynamiques sitemap | Mois 1 | +2 pts |
| 📅 C6 | Photo studio propriétaire | Mois 1 | +1 pt |

**Score projeté après Priorité 1 (A) :** ~72/100  
**Score projeté après Priorité 1+2 (A+B) :** ~79/100  
**Score projeté après tout (A+B+C) :** ~87/100

---

## Scripts de vérification

```bash
# PageSpeed Insights mobile + desktop
python3 scripts/pagespeed.py https://slayradio.ch/ --strategy mobile
python3 scripts/pagespeed.py https://slayradio.ch/ --strategy desktop

# Vérifier rendu Googlebot sur pages artistes
curl -A "Googlebot/2.1" https://slayradio.ch/home/artiste

# Rapport HTML complet
python3 scripts/generate_report.py https://slayradio.ch/ --output SEO-REPORT.html

# Validation schema JSON-LD après implémentation
python3 scripts/validate_schema.py index.html

# Vérification sitemap + robots
PYTHONIOENCODING=utf-8 python3 scripts/robots_checker.py https://slayradio.ch/

# Vérifier encoding llms.txt
curl https://slayradio.ch/llms.txt | head -5
```
