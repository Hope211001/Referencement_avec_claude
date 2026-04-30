# Plan d'Action SEO — slayradio.ch

**Date :** 2026-04-21  
**Score actuel :** 49/100 (À améliorer)  
**Objectif à 30 jours :** 68/100 (Bon)  
**Objectif à 90 jours :** 82/100 (Très bon)

---

## Priorité 1 — IMMÉDIAT (cette semaine) — Bloqueurs critiques

### A1 — Corriger la page /home/artiste vide
**Impact :** Critique | **Effort :** Faible (contenu déjà en base)  
**Gain estimé :** +6 pts SEO, indexation des artistes

La page affiche toujours "De nouveaux artistes rejoignent bientôt la famille" alors que des artistes existent dans le sitemap (/artiste/dj-fa, /artiste/dj-max, etc.). Ce thin content pénalise l'ensemble du site.

**Actions concrètes :**
1. Connecter la page /home/artiste à la base de données artistes
2. Afficher au minimum : photo, nom, genre musical, lien vers profil pour chacun
3. Si l'affichage dynamique n'est pas prêt, créer manuellement une liste des artistes avec leurs liens

---

### A2 — Ajouter lazy loading sur toutes les images
**Impact :** High (LCP) | **Effort :** Minimal (1-2h)  
**Gain estimé :** +3 pts performance

Sur chaque `<img>`, ajouter `loading="lazy"` sauf la première image hero/logo.

```html
<!-- Avant -->
<img src="/uploads/images/evenement/corbak.png" alt="CORBAK FESTIVAL">

<!-- Après -->
<img src="/uploads/images/evenement/corbak.png" alt="CORBAK FESTIVAL" 
     loading="lazy" width="600" height="400">
```

**Règle :** Le logo en haut de page garde `loading="eager"` ou sans attribut. Toutes les autres → `loading="lazy"`.

---

### A3 — Ajouter dimensions width/height sur toutes les images
**Impact :** High (CLS) | **Effort :** Faible  
**Gain estimé :** +3 pts performance

```html
<img src="/image/logo.jpg" alt="Slay Radio" width="180" height="50">
<img src="/uploads/images/evenement/corbak.png" 
     alt="CORBAK FESTIVAL (Neuchâtel)" width="600" height="400" loading="lazy">
<img src="/image/social_media_instagram.png" alt="Instagram Slay Radio" width="32" height="32">
<img src="/image/social_media_tiktok.png" alt="TikTok Slay Radio" width="32" height="32">
```

---

### A4 — Ajouter le JSON-LD RadioStation + WebSite sur la homepage
**Impact :** Critique | **Effort :** Faible (copier-coller)  
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

## Priorité 2 — COURT TERME (2 semaines) — Victoires rapides

### B1 — Ajouter les meta descriptions sur toutes les pages internes
**Impact :** Medium | **Effort :** Très faible (30 min)  
**Gain estimé :** +2 pts on-page, +CTR dans Google

| Page | Meta description suggérée |
|------|--------------------------|
| /home/artiste | "Découvrez les DJs et artistes de Slay Radio : house, afrobeat, R&B depuis la Suisse romande. Réservez un DJ pour votre événement musical." |
| /home/podcast | "Écoutez les podcasts de Slay Radio, la web radio suisse. Mix, sessions et émissions en replay, disponibles 24h/24." |
| /home/mix | "Explorez les mix exclusifs des DJs de Slay Radio. House, afrobeat, R&B et plus — diffusés depuis la Suisse romande." |
| /apropos | "Découvrez l'histoire de Slay Radio, la web radio suisse 100% musicale née de la passion pour la scène locale. Notre mission : connecter DJs et auditeurs en Suisse romande." |
| /boutique | "Découvrez la boutique Slay Radio — merchandising officiel de la web radio suisse. Soutenez la scène musicale romande." |
| /client/evenement/* | Générer dynamiquement : "[Nom événement] à [Ville] le [Date] — Slay Radio vous invite à vivre cette expérience musicale en Suisse romande." |

---

### B2 — Ajouter schema MusicEvent sur chaque page événement
**Impact :** High (rich results) | **Effort :** Moyen  
**Gain estimé :** +5 pts schema, rich results événements

Pour chaque page `/client/evenement/*`, ajouter dynamiquement :

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

### B3 — Renommer les fichiers images des événements
**Impact :** Medium | **Effort :** Faible  
**Gain estimé :** +2 pts images

| Fichier actuel | Nouveau nom |
|----------------|-------------|
| Capture-d-ecran-2026-04-17-094305-69e1e56d6d2ef.png | corbak-festival-neuchatel-2026.webp |
| Capture-d-ecran-2026-04-17-102300-69e1eef79d3da.png | blues-rules-festival-crissier-2026.webp |
| Capture-d-ecran-2026-04-17-102100-69e1ed7b35b1c.png | festiboc-bofflens-2026.webp |
| Capture-d-ecran-2026-04-17-103122-69e1f087122e6.png | festineuch-neuchatel-2026.webp |

Après renommage : mettre à jour les `src` dans le HTML et convertir en WebP.

---

### B4 — Ajouter les pages manquantes dans sitemap.static.xml
**Impact :** Medium | **Effort :** Très faible (5 min)  
**Gain estimé :** +2 pts technique

Ajouter dans `sitemap.static.xml` :

```xml
<url>
  <loc>https://slayradio.ch/home/artiste</loc>
  <lastmod>2026-04-21T08:40:36+00:00</lastmod>
  <changefreq>weekly</changefreq>
  <priority>0.8</priority>
</url>
<url>
  <loc>https://slayradio.ch/home/podcast</loc>
  <lastmod>2026-04-21T08:40:36+00:00</lastmod>
  <changefreq>weekly</changefreq>
  <priority>0.7</priority>
</url>
<url>
  <loc>https://slayradio.ch/home/mix</loc>
  <lastmod>2026-04-21T08:40:36+00:00</lastmod>
  <changefreq>weekly</changefreq>
  <priority>0.7</priority>
</url>
<url>
  <loc>https://slayradio.ch/boutique</loc>
  <lastmod>2026-04-21T08:40:36+00:00</lastmod>
  <changefreq>monthly</changefreq>
  <priority>0.6</priority>
</url>
```

---

### B5 — Corriger l'encodage UTF-8 du fichier llms.txt
**Impact :** Low | **Effort :** Très faible (5 min)  
**Gain estimé :** +1 pt GEO

Le fichier llms.txt contient du texte corrompu ("Ã©vÃ©nements" au lieu de "événements").

**Action :** Re-sauvegarder le fichier llms.txt en encodage UTF-8 strict (sans BOM).

```bash
# Vérification
curl https://slayradio.ch/llms.txt | head -5
# Si caractères corrompus visibles, régénérer le fichier
```

---

### B6 — Ajouter balise canonical sur toutes les pages
**Impact :** Medium | **Effort :** Très faible  
**Gain estimé :** +1 pt technique

Dans le `<head>` de chaque page :
```html
<link rel="canonical" href="https://slayradio.ch/[chemin-page]">
```

Exemples :
```html
<!-- Homepage -->
<link rel="canonical" href="https://slayradio.ch/">
<!-- Artiste -->
<link rel="canonical" href="https://slayradio.ch/home/artiste">
<!-- Événement -->
<link rel="canonical" href="https://slayradio.ch/client/evenement/5">
```

---

### B7 — Corriger le copyright © 2025 → 2026
**Impact :** Info | **Effort :** Minimal (2 min)  
**Gain estimé :** signal fraîcheur positif

Dans le footer, remplacer `© 2025 Slay Radio` par `© 2026 Slay Radio`.

---

## Priorité 3 — MOYEN TERME (1 mois) — Améliorations stratégiques

### C1 — Créer des pages artistes complètes avec schema Person
**Impact :** High | **Effort :** Élevé  
**Gain estimé :** +8 pts contenu + E-E-A-T

Les pages /artiste/* existent dans le sitemap mais ne sont pas accessibles sans JavaScript. À faire :

1. Assurer le rendu SSR (Server-Side Rendering) des pages artistes pour Googlebot
2. Chaque page doit contenir :
   - Bio de 200+ mots (genre, histoire, influences, événements joués)
   - Photo du DJ
   - Liens vers mix/podcasts sur le site
   - JSON-LD Person ou MusicGroup

```json
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "DJ Fa",
  "jobTitle": "DJ",
  "url": "https://slayradio.ch/artiste/dj-fa",
  "worksFor": {
    "@type": "RadioStation",
    "name": "Slay Radio",
    "url": "https://slayradio.ch/"
  },
  "genre": ["House", "Afrobeat"]
}
```

---

### C2 — Enrichir /apropos avec signaux E-E-A-T
**Impact :** High | **Effort :** Moyen  
**Gain estimé :** +5 pts E-E-A-T

Contenu à ajouter :
1. **Section équipe** : Photos + prénoms des fondateurs/DJ principaux + rôles
2. **Histoire datée** : "Fondée en [année], Slay Radio a démarré avec..."
3. **Chiffres clés** : Nb d'auditeurs, nb de DJs, heures de diffusion
4. **Presse / mentions** : Si des articles suisses ont parlé de Slay Radio
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
  "areaServed": "Suisse romande"
}
```

---

### C3 — Maillage interne vers les pages événements
**Impact :** Medium | **Effort :** Faible  
**Gain estimé :** +2 pts maillage

Les 4 pages événements quasi-orphelines n'ont qu'un lien entrant :
- Sur la homepage : lier chaque festival avec anchor text descriptif ("CORBAK FESTIVAL 2026 à Neuchâtel")
- Sur /home/evenement : lier vers chaque /client/evenement/* avec contexte éditorial

---

### C4 — Corriger les lastmod dynamiques dans le sitemap
**Impact :** Medium | **Effort :** Moyen  
**Gain estimé :** +2 pts technique, meilleur crawl budget

Actuellement tous les lastmod sont identiques. Modifier le générateur de sitemap pour utiliser la vraie date de dernière modification de chaque contenu depuis la base de données.

---

### C5 — Convertir les images en WebP
**Impact :** Medium | **Effort :** Moyen  
**Gain estimé :** +2 pts performance

```bash
# Conversion batch (Linux/Mac)
for f in uploads/images/evenement/*.png; do
  cwebp -q 85 "$f" -o "${f%.png}.webp"
done
```

Mettre à jour les `src` des images après conversion.

---

### C6 — Remplacer l'image Unsplash par une photo propriétaire du studio
**Impact :** Low (E-E-A-T) | **Effort :** Moyen (logistique photo)  
**Gain estimé :** +1 pt E-E-A-T

Une photo réelle des studios/équipes Slay Radio renforce les signaux E-E-A-T. L'image Unsplash actuelle est générique.

---

## Récapitulatif et Calendrier

| Priorité | Action | Délai | Impact Score |
|----------|--------|-------|-------------|
| 🔴 A1 | /home/artiste — afficher les artistes | Semaine 1 | +6 pts |
| 🔴 A2 | Lazy loading images | Semaine 1 | +3 pts |
| 🔴 A3 | Dimensions width/height images | Semaine 1 | +3 pts |
| 🔴 A4 | JSON-LD RadioStation + WebSite | Semaine 1 | +6 pts |
| ⚠️ B1 | Meta descriptions pages internes | Semaine 2 | +2 pts |
| ⚠️ B2 | Schema MusicEvent événements | Semaine 2 | +5 pts |
| ⚠️ B3 | Renommer fichiers images → WebP | Semaine 2 | +2 pts |
| ⚠️ B4 | sitemap.static.xml complet | Semaine 2 | +2 pts |
| ⚠️ B5 | Encodage UTF-8 llms.txt | Semaine 2 | +1 pt |
| ⚠️ B6 | Balise canonical | Semaine 2 | +1 pt |
| ⚠️ B7 | Copyright 2025 → 2026 | Semaine 2 | +0 pt |
| 📅 C1 | Pages artistes SSR + schema Person | Mois 1 | +8 pts |
| 📅 C2 | /apropos E-E-A-T + équipe | Mois 1 | +5 pts |
| 📅 C3 | Maillage interne événements | Mois 1 | +2 pts |
| 📅 C4 | Lastmod dynamiques sitemap | Mois 1 | +2 pts |
| 📅 C5 | Conversion WebP | Mois 1 | +2 pts |

**Score projeté après Priorité 1 (A) :** ~67/100  
**Score projeté après Priorité 1+2 (A+B) :** ~73/100  
**Score projeté après Priorité 1+2+3 (A+B+C) :** ~82/100  

---

## Vérifications à Relancer

1. **PageSpeed Insights** (attendre 10 min puis relancer) :
   ```bash
   python3 scripts/pagespeed.py https://slayradio.ch/ --strategy mobile
   python3 scripts/pagespeed.py https://slayradio.ch/ --strategy desktop
   ```

2. **Pages artistes SSR** :
   ```bash
   curl -A "Googlebot/2.1" https://slayradio.ch/artiste/dj-fa
   ```

3. **Rapport HTML interactif** :
   ```bash
   python3 scripts/generate_report.py https://slayradio.ch/ --output SEO-REPORT.html
   ```

4. **Validation schema après implémentation** :
   ```bash
   python3 scripts/validate_schema.py index.html
   ```

5. **Vérification sitemap complet** :
   ```bash
   PYTHONIOENCODING=utf-8 python3 scripts/robots_checker.py https://slayradio.ch/
   ```
