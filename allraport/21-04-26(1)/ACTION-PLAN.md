# Plan d'Action SEO — slayradio.ch

**Date :** 2026-04-21  
**Score actuel :** 42/100 (Faible)  
**Objectif à 30 jours :** 65/100 (À améliorer)  
**Objectif à 90 jours :** 78/100 (Bon)

---

## Priorité 1 — IMMÉDIAT (cette semaine) — Bloqueurs

### A1 — Corriger la page /home/artiste vide
**Impact :** Critique | **Effort :** Faible (contenu déjà en base)  
**Gain estimé :** +6 pts SEO, indexation de 11 artistes  

La page affiche "De nouveaux artistes rejoignent bientôt la famille" alors que 11 artistes existent dans le sitemap (/artiste/dj-fa, /artiste/dj-max, etc.). Ce thin content pénalise l'ensemble du site.

**Actions concrètes :**
1. Connecter la page /home/artiste à la base de données des artistes existants
2. Afficher au minimum : photo, nom, genre musical, lien vers profil pour chacun
3. Si l'affichage dynamique n'est pas prêt, créer manuellement une liste des artistes avec leurs liens

---

### A2 — Ajouter les pages événements au sitemap
**Impact :** High | **Effort :** Très faible  
**Gain estimé :** +3 pts technique, 4 pages indexées  

Les URLs /client/evenement/5, /9, /10, /16 existent mais sont absentes du sitemap.xml.

**Actions concrètes :**
1. Créer `https://slayradio.ch/sitemap.evenements.xml` :
```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://slayradio.ch/client/evenement/5</loc>
    <changefreq>weekly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://slayradio.ch/client/evenement/9</loc>
    <changefreq>weekly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://slayradio.ch/client/evenement/10</loc>
    <changefreq>weekly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://slayradio.ch/client/evenement/16</loc>
    <changefreq>weekly</changefreq>
    <priority>0.7</priority>
  </url>
</urlset>
```
2. Ajouter dans le sitemap index :
```xml
<sitemap>
  <loc>https://slayradio.ch/sitemap.evenements.xml</loc>
  <lastmod>2026-04-21T00:00:00+00:00</lastmod>
</sitemap>
```
3. Soumettre le sitemap dans Google Search Console

---

### A3 — Ajouter lazy loading sur toutes les images
**Impact :** High (LCP) | **Effort :** Minimal  
**Gain estimé :** +3 pts performance  

Sur chaque `<img>`, ajouter `loading="lazy"` sauf la première image hero/logo.

```html
<!-- Avant -->
<img src="/uploads/images/evenement/corbak.png" alt="CORBAK FESTIVAL">

<!-- Après -->
<img src="/uploads/images/evenement/corbak.png" alt="CORBAK FESTIVAL" 
     loading="lazy" width="600" height="400">
```

**Règle :** Le logo en haut de page (above the fold) garde `loading="eager"` ou pas d'attribut. Toutes les autres images → `loading="lazy"`.

---

## Priorité 2 — COURT TERME (2 semaines) — Victoires rapides

### B1 — Ajouter meta description sur toutes les pages internes
**Impact :** Medium | **Effort :** Très faible  
**Gain estimé :** +2 pts on-page, +CTR dans Google  

Pages concernées (méta absente confirmée) :

| Page | Meta description suggérée |
|------|--------------------------|
| /apropos | "Découvrez l'histoire de Slay Radio, la web radio suisse 100% musicale née de la passion pour la scène locale. Notre mission : connecter DJs et auditeurs en Suisse romande." |
| /home/artiste | "Découvrez les DJs et artistes de Slay Radio : house, afrobeat, R&B depuis la Suisse romande. Réservez un DJ pour votre événement." |
| /home/podcast | "Écoutez les podcasts de Slay Radio, la web radio suisse. Mix, sessions et émissions en replay, disponibles 24h/24." |
| /home/mix | "Explorez les mix exclusifs des DJs de Slay Radio. House, afrobeat, R&B et plus — diffusés depuis la Suisse romande." |

---

### B2 — Enrichir le JSON-LD RadioStation
**Impact :** Medium | **Effort :** Faible  
**Gain estimé :** +4 pts schema, éligibilité rich results  

Remplacer le JSON-LD actuel par :

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

### B3 — Renommer les fichiers images des événements
**Impact :** Medium | **Effort :** Faible  
**Gain estimé :** +2 pts images, signaux topicaux  

| Fichier actuel | Nouveau nom |
|----------------|-------------|
| Capture-d-ecran-2026-04-17-094305-69e1e56d6d2ef.png | corbak-festival-neuchatel-2026.webp |
| Capture-d-ecran-2026-04-17-102300-69e1eef79d3da.png | blues-rules-festival-crissier-2026.webp |
| Capture-d-ecran-2026-04-17-102100-69e1ed7b35b1c.png | festiboc-bofflens-2026.webp |
| Capture-d-ecran-2026-04-17-103122-69e1f087122e6.png | festineuch-neuchatel-2026.webp |

**Après renommage :** Mettre à jour les `src` dans le HTML et les `lastmod` dans le sitemap.

**Bonus :** Convertir en format WebP (compression ~30% meilleure que PNG/JPG).

---

### B4 — Ajouter dimensions width/height sur toutes les images
**Impact :** Medium (CLS) | **Effort :** Faible  
**Gain estimé :** +2 pts performance (CLS)  

Mesurer les dimensions réelles de chaque image et les ajouter :
```html
<img src="/image/logo.jpg" alt="Slay Radio" width="180" height="50">
<img src="/uploads/images/evenement/corbak-festival-neuchatel-2026.webp" 
     alt="CORBAK FESTIVAL (Neuchâtel)" width="600" height="400" loading="lazy">
```

---

### B5 — Ajouter schema MusicEvent sur chaque page événement
**Impact :** High (rich results) | **Effort :** Moyen  
**Gain estimé :** +5 pts schema, rich results événements  

Pour chaque page /client/evenement/*, ajouter :
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "MusicEvent",
  "name": "CORBAK FESTIVAL",
  "startDate": "2026-XX-XX",
  "endDate": "2026-XX-XX",
  "eventStatus": "EventScheduled",
  "eventAttendanceMode": "OfflineEventAttendanceMode",
  "location": {
    "@type": "Place",
    "name": "Corbak Festival",
    "address": {
      "@type": "PostalAddress",
      "addressLocality": "Neuchâtel",
      "addressCountry": "CH"
    }
  },
  "organizer": {
    "@type": "Organization",
    "name": "Corbak Festival",
    "url": "https://corbak.ch"
  },
  "image": "https://slayradio.ch/uploads/images/evenement/corbak-festival-neuchatel-2026.webp"
}
</script>
```

---

## Priorité 3 — MOYEN TERME (1 mois) — Améliorations stratégiques

### C1 — Créer des pages artistes complètes avec schema Person
**Impact :** High | **Effort :** Élevé  
**Gain estimé :** +8 pts contenu + E-E-A-T  

Les 11 artistes dans le sitemap ont des pages (/artiste/dj-fa etc.) mais elles semblent inaccessibles sans JavaScript. À faire :

1. Assurer le rendu côté serveur (SSR) des pages artistes pour Googlebot
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

### C2 — Enrichir la page /apropos avec signaux E-E-A-T
**Impact :** High | **Effort :** Moyen  
**Gain estimé :** +5 pts E-E-A-T  

La page /apropos a le contenu de base mais sans signaux de confiance. À ajouter :

1. **Section équipe** : Photos + prénoms des fondateurs/DJ principaux + rôles
2. **Histoire datée** : "Fondée en [année], Slay Radio a démarré avec..."
3. **Chiffres clés** : Nb d'auditeurs, nb de DJs, heures de diffusion
4. **Presse / mentions** : Si des articles suisses ont parlé de Slay Radio
5. **Schema Organization** sur /apropos :

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

### C3 — Corriger les lastmod dynamiques dans le sitemap
**Impact :** Medium | **Effort :** Moyen  
**Gain estimé :** +2 pts technique, meilleur crawl budget  

Actuellement : tous les lastmod sont identiques (2026-04-15T06:05:33). Modifier le générateur de sitemap pour utiliser la vraie date de dernière modification de chaque page/contenu depuis la base de données.

---

### C4 — Ajouter liens internes vers les pages événements
**Impact :** Medium | **Effort :** Faible  
**Gain estimé :** +2 pts maillage interne  

Les 4 pages événements n'ont qu'un seul lien entrant chacune. Ajouter :
- Sur la homepage, lier chaque festival avec un anchor text descriptif (ex: "CORBAK FESTIVAL 2026 à Neuchâtel")
- Sur /home/evenement, lier vers chaque /client/evenement/* avec contexte éditorial

---

### C5 — Diviser les paragraphes trop longs
**Impact :** Low (UX) | **Effort :** Faible  
**Gain estimé :** +1 pt readability  

Sur la homepage et /apropos, diviser les blocs texte de plus de 4 phrases en paragraphes de 2-3 phrases. Cible : Flesch 60+ (actuellement 55).

---

## Récapitulatif et Calendrier

| Priorité | Action | Délai | Impact Score |
|----------|--------|-------|-------------|
| 🔴 A1 | Afficher artistes sur /home/artiste | Semaine 1 | +6 pts |
| 🔴 A2 | Événements dans le sitemap | Semaine 1 | +3 pts |
| 🔴 A3 | Lazy loading images | Semaine 1 | +3 pts |
| ⚠️ B1 | Meta descriptions pages internes | Semaine 2 | +2 pts |
| ⚠️ B2 | Enrichir JSON-LD RadioStation | Semaine 2 | +4 pts |
| ⚠️ B3 | Renommer fichiers images | Semaine 2 | +2 pts |
| ⚠️ B4 | Dimensions width/height images | Semaine 2 | +2 pts |
| ⚠️ B5 | Schema MusicEvent événements | Semaine 2 | +5 pts |
| 📅 C1 | Pages artistes SSR + schema | Mois 1 | +8 pts |
| 📅 C2 | /apropos E-E-A-T + team | Mois 1 | +5 pts |
| 📅 C3 | Lastmod dynamiques sitemap | Mois 1 | +2 pts |
| 📅 C4 | Maillage interne événements | Mois 1 | +2 pts |

**Score projeté après Priorité 1+2 :** ~58/100  
**Score projeté après Priorité 1+2+3 :** ~75/100  

---

## Vérifications à Relancer

1. **PageSpeed Insights** (dans 15 min) :
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

4. **Profil de backlinks** :
   ```bash
   python3 scripts/link_profile.py https://slayradio.ch/
   ```
