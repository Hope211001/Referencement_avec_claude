# Plan d'Action SEO — slayradio.ch

**Date :** 2026-04-27  
**Analyse réalisée :** Fetch direct Python/BeautifulSoup — 9 pages + sitemap + robots.txt + headers HTTP  
**Score actuel :** 74/100 (+25 pts depuis audit 2026-04-21)  
**Objectif à 30 jours :** 82/100  
**Objectif à 90 jours :** 88/100

---

## Résumé de l'état actuel (2026-04-27)

| Catégorie | Statut | Détail |
|---|---|---|
| Meta descriptions | ✅ OK | Présentes sur toutes les pages |
| Canonical URLs | ✅ OK | Présentes sur toutes les pages |
| Schema JSON-LD | ✅ OK | RadioStation + WebSite + MusicEvent + MusicGroup |
| Open Graph (7 tags) | ✅ OK | Implémenté sur toutes les pages |
| Twitter Card (5 tags) | ✅ OK | Implémenté sur toutes les pages |
| Alt text images | ✅ OK | Présent sur toutes les images |
| Lazy loading images contenu | ✅ OK | Artistes + événements |
| Dimensions images contenu | ✅ OK | 400×400 sur artistes + événements |
| Page podcast | ✅ OK | Mise en noindex,nofollow |
| Copyright footer | ✅ OK | 2026 affiché |
| Sitemap | ✅ OK | Index + 3 sous-sitemaps |
| robots.txt | ✅ OK | Crawlers IA autorisés |
| llms.txt | ✅ OK | Présent et structuré |
| Headers sécurité | ✅ OK | HSTS, CSP, X-Frame, etc. |
| **Indexation Google** | **❌ Critique** | **0 résultat site:slayradio.ch** |
| Lazy loading (Unsplash + icônes) | ⚠️ Warning | Manquant sur 3 images |
| Dimensions (Unsplash + icônes) | ⚠️ Warning | Manquant sur 3 images |
| Noms fichiers images | ⚠️ Warning | "Capture-d-ecran-..." non SEO |
| Handle Twitter | ⚠️ Warning | @SlayRadio vs @slayradio1 |

---

## PRIORITÉ 1 — IMMÉDIAT (cette semaine) — Bloqueurs critiques

### A1 — Soumettre le Sitemap dans Google Search Console 🔴
**Impact :** Critique | **Effort :** 15 minutes  
**Gain estimé :** Indexation = +25 pts visibilité

Le site est vérifié dans Google Search Console (meta tag + fichier HTML), mais n'est pas encore indexé. Il faut soumettre le sitemap manuellement :

1. Aller sur https://search.google.com/search-console
2. Sélectionner la propriété `slayradio.ch`
3. Menu gauche → **"Sitemaps"**
4. Entrer `https://slayradio.ch/sitemap.xml` → **"Envoyer"**
5. Vérifier que le statut passe à **"Succès"**

### A2 — Demander l'indexation des pages clés 🔴
**Impact :** Critique | **Effort :** 20 minutes  
**Gain estimé :** Apparition dans Google en 1-14 jours

Dans Google Search Console → "Inspection d'URL" :

| URL | Action |
|---|---|
| `https://slayradio.ch/` | "Demander l'indexation" |
| `https://slayradio.ch/radio-web-suisse` | "Demander l'indexation" |
| `https://slayradio.ch/home/artiste` | "Demander l'indexation" |
| `https://slayradio.ch/home/evenement` | "Demander l'indexation" |
| `https://slayradio.ch/apropos` | "Demander l'indexation" |

### A3 — Corriger le handle Twitter ⚠️
**Impact :** Moyen | **Effort :** 5 minutes

Les balises Twitter Card affichent `@SlayRadio` mais les liens sameAs du schema pointent vers `@slayradio1`. Vérifier quel handle correspond au vrai compte et uniformiser :

```html
<!-- Si le vrai compte est @slayradio1 -->
<meta name="twitter:site" content="@slayradio1">
<meta name="twitter:creator" content="@slayradio1">
```

### ~~A1 ancien — JSON-LD RadioStation + WebSite sur la homepage~~
**DÉJÀ FAIT ✅** — Schema complet implémenté depuis 2026-04-21



---

### ~~A2 ancien — /home/artiste thin content~~
**DÉJÀ FAIT ✅** — Artistes affichés (LES NOVAS visible)

### ~~A3 ancien — Page podcasts vide~~
**DÉJÀ FAIT ✅** — Page mise en noindex,nofollow

### ~~A4 ancien — Lazy loading images~~
**PARTIELLEMENT FAIT ✅⚠️** — Voir action B1 pour finaliser

### ~~A5 ancien — Open Graph + Twitter Cards~~
**DÉJÀ FAIT ✅** — 7/7 OG + 5/5 Twitter Card implémentés

---

## PRIORITÉ 2 — COURT TERME (cette semaine) — Victoires rapides

### ~~B1 ancien — Meta descriptions~~
**DÉJÀ FAIT ✅** — Présentes sur toutes les pages

### ~~B2 ancien — Schema MusicEvent~~
**DÉJÀ FAIT ✅** — Présent sur événements et pages individuelles

### ~~B3 ancien — Canonical tags~~
**DÉJÀ FAIT ✅** — Présentes sur toutes les pages

### ~~B4 ancien — sitemap.static.xml~~
**DÉJÀ FAIT ✅** — 5 pages dans le sitemap static

---

### B1 — Finaliser lazy loading + dimensions (Unsplash + icônes)
**Impact :** Medium (CLS) | **Effort :** 15 minutes  
**Gain estimé :** +3 pts performance

```html
<!-- Image Unsplash studio (remplacer l'existant) -->
<img src="https://images.unsplash.com/photo-1516450360452-9312f5e86fc7"
     alt="Studio radio Slay Radio — web radio suisse"
     loading="lazy" width="600" height="400">

<!-- Icônes sociales (remplacer l'existant) -->
<img src="/image/social_media_instagram.png"
     alt="Suivez Slay Radio sur Instagram"
     loading="lazy" width="32" height="32">
<img src="/image/social_media_tiktok.png"
     alt="Suivez Slay Radio sur TikTok"
     loading="lazy" width="32" height="32">
```

---

### B2 — Renommer et convertir les images événements en WebP
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

### ~~B3 ancien — Encodage UTF-8 llms.txt~~
**DÉJÀ FAIT ✅** — llms.txt lisible et bien encodé (vérifié 2026-04-27)

### ~~B4 ancien — Copyright footer~~
**DÉJÀ FAIT ✅** — Affiche `© 2026 Slay Radio` (vérifié 2026-04-27)

---

## PRIORITÉ 3 — MOYEN TERME (1 mois) — Stratégique

### ~~C1 ancien — Pages artistes individuelles~~
**DÉJÀ FAIT ✅** — `/artiste/les-novas` existe avec schema MusicGroup (vérifié 2026-04-27). Continuer d'ajouter les autres artistes.

---

### ~~C2 ancien — URLs événements opaques /client/evenement/3~~
**DÉJÀ FAIT ✅** — URLs maintenant en `/evenement/corbak-festival-neuchatel` (slugs lisibles, vérifié 2026-04-27)

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

### C3 — Enrichir /apropos avec signaux E-E-A-T
**Impact :** High | **Effort :** Moyen  
**Gain estimé :** +5 pts E-E-A-T

Contenu à ajouter :
1. Section équipe avec photos + prénoms + rôles
2. Histoire datée : "Fondée en 2023, Slay Radio a démarré avec..."
3. Chiffres clés : nb auditeurs, nb DJs, heures de diffusion
4. Presse / mentions : tout article suisse ayant mentionné Slay Radio

---

### C4 — Soumettre sur les annuaires radio suisses
**Impact :** Medium (backlinks + visibilité directe) | **Effort :** 2h  
**Gain estimé :** +autorité de domaine

| Annuaire | URL |
|---|---|
| Online Radio Box | https://onlineradiobox.com/add |
| Radio.fr | https://www.radio.fr/add-radio |
| Streema | https://fr.streema.com/radios/add |
| Radios.ch | https://www.radios.ch |
| Broadcast.ch | https://www.broadcast.ch/fr |

---

### C5 — Implémenter IndexNow (Bing/Yandex)
**Impact :** Medium | **Effort :** 1h

```bash
# Envoyer notification à Bing à chaque publication
curl -X POST "https://api.indexnow.org/indexnow" \
  -H "Content-Type: application/json" \
  -d '{"host":"slayradio.ch","key":"VOTRE_CLE","urlList":["https://slayradio.ch/evenement/NOM"]}'
```

---

### C6 — Remplacer photo Unsplash par photo réelle
**Impact :** Low (E-E-A-T) | Photo réelle du studio → meilleure crédibilité

---

## Récapitulatif et Calendrier — 2026-04-27

| # | Action | Délai | Statut | Impact |
|---|--------|-------|--------|--------|
| 🔴 A1 | Soumettre sitemap dans GSC | Aujourd'hui | ❌ À faire | Indexation |
| 🔴 A2 | Demander indexation pages clés | Aujourd'hui | ❌ À faire | Indexation |
| ⚠️ A3 | Corriger handle Twitter @SlayRadio | Cette semaine | ❌ À faire | +1 pt |
| ⚠️ B1 | Lazy loading Unsplash + icônes | Cette semaine | ❌ À faire | +2 pts |
| ⚠️ B2 | Renommer images → WebP | Cette semaine | ❌ À faire | +3 pts |
| 📅 C3 | /apropos E-E-A-T + équipe | Mois 1 | ❌ À faire | +5 pts |
| 📅 C4 | Soumettre annuaires radio | Mois 1 | ❌ À faire | +autorité |
| 📅 C5 | IndexNow Bing/Yandex | Mois 1 | ❌ À faire | +2 pts |
| 📅 C6 | Photo studio propriétaire | Mois 2 | ❌ À faire | +1 pt |

**Score actuel : 74/100**  
**Score projeté après actions immédiates (A) :** ~80/100 (+ indexation)  
**Score projeté après tout (A+B+C) :** ~88/100

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
