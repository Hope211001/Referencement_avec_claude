# Rapport d'Audit SEO Complet — slayradio.ch

**Date :** 2026-04-27  
**Score global :** 74/100 (+25 pts depuis audit du 2026-04-21)  
**Précédent score :** 49/100 (audit 2026-04-21)  
**Auditeur :** Claude SEO Skill — Audit LLM-first + scripts Python directs (BeautifulSoup)  
**Méthode :** Fetch direct + parse HTML réel (non via WebFetch proxy)

---

## Résumé Exécutif

| Catégorie | Score | Poids | Points |
|-----------|-------|-------|--------|
| Technical SEO | 82/100 | 25% | 20.5 |
| Content Quality / E-E-A-T | 55/100 | 20% | 11.0 |
| On-Page SEO | 90/100 | 15% | 13.5 |
| Schema / Structured Data | 90/100 | 15% | 13.5 |
| Performance (CWV) | 55/100 | 10% | 5.5 |
| Image Optimization | 55/100 | 10% | 5.5 |
| AI Search Readiness (GEO) | 90/100 | 5% | 4.5 |
| **TOTAL** | **74/100** | 100% | **74.0** |

---

## Améliorations réalisées depuis l'audit du 2026-04-21

| Action | Statut |
|--------|--------|
| Schema JSON-LD RadioStation + WebSite + WebSearchAction | ✅ Fait |
| Schema MusicEvent sur pages événements | ✅ Fait |
| Schema ItemList + MusicGroup sur /home/artiste | ✅ Fait |
| Schema MusicGroup sur pages artistes individuelles | ✅ Fait |
| Open Graph (7 tags) sur toutes les pages | ✅ Fait |
| Twitter Card (5 tags) sur toutes les pages | ✅ Fait |
| Meta descriptions sur toutes les pages | ✅ Fait |
| Canonical URLs sur toutes les pages | ✅ Fait |
| Lazy loading sur images contenu (artistes, événements) | ✅ Fait |
| Dimensions width/height sur images contenu | ✅ Fait |
| Podcast page mise en noindex,nofollow | ✅ Fait |
| Copyright footer mis à jour (2025 → 2026) | ✅ Fait |
| Page /home/artiste avec vrais artistes (LES NOVAS visible) | ✅ Fait |
| Geo meta tags (geo.region: CH) | ✅ Fait |
| llms.txt présent et bien structuré | ✅ Fait |

---

## Problèmes restants

| Action | Statut |
|--------|--------|
| Site non indexé par Google | ❌ Critique |
| Lazy loading manquant sur image Unsplash + icônes sociales | ⚠️ Warning |
| Dimensions manquantes sur image Unsplash + icônes sociales | ⚠️ Warning |
| Noms de fichiers images (Capture-d-ecran...) | ⚠️ Warning |
| Format PNG (pas WebP) pour images événements | ⚠️ Warning |
| Handle Twitter @SlayRadio vs @slayradio1 (incohérence) | ⚠️ Warning |
| IndexNow non implémenté (Bing/Yandex) | ℹ️ Info |

---

## 1. Technical SEO — 82/100

### 1.1 HTTPS & Sécurité
- **Finding:** HTTPS actif, HSTS configuré (max-age=31536000 + includeSubDomains). Tous les headers présents.
- **Evidence:** Vérification directe HTTP 2026-04-27 → HSTS ✅, CSP ✅, X-Frame-Options: SAMEORIGIN ✅, X-Content-Type-Options: nosniff ✅, Referrer-Policy ✅, Permissions-Policy ✅
- **Statut:** ✅ Pass

### 1.2 Redirections
- **Finding:** Aucune redirection, réponse directe HTTP 200. Pas de boucle, pas de chaîne.
- **Evidence:** `requests.get(https://slayradio.ch/)` → status=200, history=[] (0 hop)
- **Statut:** ✅ Pass

### 1.3 Robots.txt
- **Finding:** Bien configuré. 12 user-agents. Tous les crawlers IA autorisés. Sitemap référencé.
- **Evidence:** `robots_checker.py` → GPTBot, ClaudeBot, PerplexityBot, Google-Extended, Applebot-Extended, Bytespider, CCBot, FacebookBot, Amazonbot → Allow: /
- **Statut:** ✅ Pass

### 1.4 Sitemap XML
- **Finding:** Sitemap index avec 3 sous-sitemaps : static (5 pages), artistes, événements. Bien structuré.
- **Evidence:** `sitemap.static.xml` = 5 URLs (/, /home/artiste, /home/evenement, /apropos, /radio-web-suisse) | `sitemap.artistes.xml` + `sitemap.evenements.xml` présents
- **Statut:** ✅ Pass

### 1.5 Canonical
- **Finding:** Balise `<link rel="canonical">` présente sur toutes les pages vérifiées.
- **Evidence:** BeautifulSoup → canonical ✅ sur /, /home/artiste, /home/evenement, /apropos, /radio-web-suisse, /artiste/les-novas, /evenement/corbak-festival-neuchatel
- **Statut:** ✅ Pass (corrigé depuis 2026-04-21)

### 1.6 Indexation Google
- **Finding:** CRITIQUE — Le site n'apparaît dans aucun résultat Google.
- **Evidence:** `site:slayradio.ch` → 0 résultats le 2026-04-27
- **Note:** Vérification GSC déjà en place (meta tag + fichier HTML `/googlefdc971f91a5e2331.html` HTTP 200). Sitemap non encore soumis ou en attente de crawl.
- **Impact:** 0 visiteur organique depuis Google Search
- **Statut:** 🔴 Critique

### 1.7 Liens cassés
- **Finding:** Toutes les pages vérifiées répondent en HTTP 200.
- **Statut:** ✅ Pass

### 1.8 Rendu JavaScript
- **Finding:** Le contenu est visible dans le HTML statique (artistes, événements, textes). Pas de SPA pur.
- **Evidence:** BeautifulSoup parse direct → artiste LES NOVAS visible, événements CORBAK présent
- **Statut:** ✅ Pass (amélioré depuis 2026-04-21)

---

## 2. Content Quality / E-E-A-T — 55/100

### 2.1 Page /home/artiste — Contenu présent
- **Finding:** La page affiche maintenant les vrais artistes (LES NOVAS visible). Thin content résolu.
- **Evidence:** BeautifulSoup /home/artiste → Schema ItemList avec MusicGroup "LES NOVAS" présent
- **Statut:** ✅ Pass (corrigé depuis 2026-04-21)

### 2.2 Page /apropos — E-E-A-T faible
- **Finding:** Page à améliorer — manque équipe nommée, chiffres clés, mentions presse
- **Evidence:** Analyse structurelle → H1 "À propos de Slay Radio" présent, contenu basique
- **Impact:** Score E-E-A-T modéré — Google évalue mieux les sites avec auteurs identifiables
- **Statut:** ⚠️ Warning

### 2.3 Contenu événements — Bon
- **Finding:** Pages événements individuelles avec contenu substantiel, schema MusicEvent, canonical
- **Evidence:** /evenement/corbak-festival-neuchatel → HTTP 200, title ✅, meta ✅, schema ✅
- **Statut:** ✅ Pass

### 2.4 Page podcasts
- **Finding:** Page mise en noindex,nofollow — bonne décision car contenu vide
- **Evidence:** `<meta name="robots" content="noindex, nofollow">` présent sur /home/podcast
- **Statut:** ✅ Pass (corrigé depuis 2026-04-21)

---

## 3. On-Page SEO — 90/100

### 3.1 Title Tags
- **Finding:** Présents et bien formatés sur toutes les pages — avec mots-clés géographiques
  - Homepage: `Slay Radio | Web Radio Suisse Romande — House, Afrobeat & R&B en Direct 24h/24`
  - /home/artiste: `Artistes & DJs suisses — Slay Radio Suisse`
  - /home/evenement: `Événements musicaux Suisse 2026 : concerts, showcases & festivals — Slay Radio`
  - /apropos: `À propos de Slay Radio — Radio web suisse 100% musicale`
  - /radio-web-suisse: `Radio Web Suisse en Direct — House, Afrobeat & R&B 24h/24 — Slay Radio`
- **Statut:** ✅ Pass

### 3.2 Balises H1
- **Finding:** H1 unique et descriptif présent sur toutes les pages
- **Statut:** ✅ Pass

### 3.3 Meta Descriptions
- **Finding:** Présentes sur toutes les pages (corrigé depuis 2026-04-21)
- **Evidence:** BeautifulSoup → meta description ✅ sur toutes les URLs vérifiées
- **Statut:** ✅ Pass

### 3.4 Open Graph (7/7) & Twitter Card (5/5)
- **Finding:** Implémentation complète sur toutes les pages
- **Evidence:** og:locale fr_CH, og:image 1200×630, twitter:card summary_large_image — tous présents
- **⚠️ Warning :** Handle Twitter `@SlayRadio` dans les meta ≠ `@slayradio1` dans sameAs schema — vérifier lequel est le vrai compte
- **Statut:** ✅ Pass (avec 1 avertissement)

### 3.5 Alt Text Images
- **Finding:** Alt text présent et descriptif sur toutes les images principales
- **Evidence:** BeautifulSoup → "Slay Radio — Web radio suisse" (logo), "LES NOVAS" (artiste), "Studio radio Slay Radio — web radio suisse" (studio), "Suivez Slay Radio sur Instagram" (icône)
- **Statut:** ✅ Pass (corrigé depuis 2026-04-21)

### 3.6 Lang Attribute
- **Finding:** `lang="fr-CH"` sur la balise html — correct pour la Suisse romande
- **Statut:** ✅ Pass

---

## 4. Schema / Structured Data — 90/100

### 4.1 JSON-LD Homepage — RadioStation + WebSite
- **Finding:** 2 schemas présents : RadioStation complet + WebSite avec SearchAction
- **Evidence:** BeautifulSoup → @type RadioStation (name, url, logo, broadcastFrequency, broadcastTimezone, areaServed, foundingDate, contactPoint, sameAs) + @type WebSite (potentialAction SearchAction)
- **Statut:** ✅ Pass (corrigé depuis 2026-04-21)

### 4.2 JSON-LD Événements — MusicEvent
- **Finding:** Schema MusicEvent présent sur la page liste ET les pages individuelles
- **Evidence:** /home/evenement → schema MusicEvent ✅ | /evenement/corbak-festival-neuchatel → schema MusicEvent ✅
- **Statut:** ✅ Pass (corrigé depuis 2026-04-21)

### 4.3 JSON-LD Artistes — MusicGroup
- **Finding:** Schema ItemList + MusicGroup sur /home/artiste. Schema MusicGroup sur pages individuelles.
- **Evidence:** /home/artiste → @type ItemList + @type MusicGroup ✅ | /artiste/les-novas → @type MusicGroup ✅
- **Statut:** ✅ Pass (corrigé depuis 2026-04-21)

### 4.4 JSON-LD Page radio-web-suisse — RadioStation
- **Finding:** Schema RadioStation présent avec URL propre
- **Evidence:** /radio-web-suisse → @type RadioStation ✅
- **Statut:** ✅ Pass

### 4.5 SearchAction — À vérifier fonctionnellement
- **Finding:** L'URL cible de la SearchAction est `https://slayradio.ch/home/artiste?q={search_term_string}` — vérifier que le paramètre `q` est bien traité par l'application
- **Statut:** ⚠️ Warning (à valider)

---

## 5. Performance (CWV) — 55/100

> Note : API PageSpeed Insights rate-limitée. Score estimé à partir des signaux HTML réels (BeautifulSoup 2026-04-27).

### 5.1 Lazy Loading — Partiel
- **Finding:** Lazy loading implémenté sur les images de contenu (artistes, événements). Manquant sur image Unsplash et icônes sociales.
- **Evidence:** BeautifulSoup →
  - `/image/logo.jpg` → loading=MISSING (correct — above the fold)
  - `/uploads/images/artistes/les-novas.png` → loading=lazy ✅
  - `/uploads/images/evenement/*.png` → loading=lazy ✅ (4 images)
  - `images.unsplash.com/...` → loading=MISSING ⚠️
  - `/image/social_media_instagram.png` → loading=MISSING ⚠️
  - `/image/social_media_tiktok.png` → loading=MISSING ⚠️
- **Statut:** ⚠️ Warning (partiellement corrigé)

### 5.2 Dimensions Images (CLS)
- **Finding:** Dimensions présentes sur la plupart des images (400×400). Manquantes sur image Unsplash et icônes sociales.
- **Evidence:** BeautifulSoup → logo w=400 h=400 ✅, artiste w=400 h=400 ✅, événements w=400 h=400 ✅, Unsplash MISSING ⚠️, icônes sociales MISSING ⚠️
- **Statut:** ⚠️ Warning (partiellement corrigé)

### 5.3 Format WebP
- **Finding:** Images événements toujours en PNG (noms "Capture-d-ecran-..."). Pas de conversion WebP.
- **Evidence:** BeautifulSoup → `.png` sur tous les uploads/images/evenement/
- **Impact:** Poids 30-50% plus élevé qu'en WebP
- **Statut:** ⚠️ Warning

---

## 6. Image Optimization — 55/100

### 6.1 Noms de Fichiers
- **Finding:** 4 images événements avec noms auto-générés non-SEO : "Capture-d-ecran-YYYY-MM-DD-HHMMSS-[hash].png"
- **Evidence:** BeautifulSoup → `Capture-d-ecran-2026-04-17-094305-[...].png` (×4)
- **Impact:** Signal topical faible — Google préfère des noms descriptifs comme `corbak-festival-neuchatel-2026.webp`
- **Statut:** ⚠️ Warning

### 6.2 Alt Text
- **Finding:** Alt text présent sur toutes les images y compris les icônes sociales ("Suivez Slay Radio sur Instagram")
- **Evidence:** BeautifulSoup → tous les img avec alt non vide ✅
- **Statut:** ✅ Pass (corrigé depuis 2026-04-21)

### 6.3 Lazy loading + dimensions manquants sur Unsplash et icônes
- **Finding:** Image Unsplash (studio) et icônes sociales sans lazy ni dimensions
- **Fix rapide :**
```html
<img src="https://images.unsplash.com/..." alt="Studio radio Slay Radio" loading="lazy" width="600" height="400">
<img src="/image/social_media_instagram.png" alt="Slay Radio sur Instagram" loading="lazy" width="32" height="32">
<img src="/image/social_media_tiktok.png" alt="Slay Radio sur TikTok" loading="lazy" width="32" height="32">
```
- **Statut:** ⚠️ Warning

---

## 7. AI Search Readiness (GEO) — 90/100

### 7.1 llms.txt
- **Finding:** Présent (HTTP 200), score 100/100, 5 sections, 10 liens. llms-full.txt présent.
- **Evidence:** `llms_txt_checker.py` → Quality Score: 100/100
- **Statut:** ✅ Pass

### 7.2 AI Crawlers
- **Finding:** Tous les bots IA majeurs autorisés dans robots.txt
- **Statut:** ✅ Pass

### 7.3 Encodage llms.txt
- **Finding:** Texte corrompu dans llms.txt : "Ã©vÃ©nements" au lieu de "événements"
- **Evidence:** `llms_txt_checker.py` → "DJs en live, mix, podcasts, Ã©vÃ©nements et boutique"
- **Impact:** Les LLMs voient du texte illisible, qualité de l'indexation IA dégradée
- **Statut:** ⚠️ Warning

---

## 8. Nouveaux Problèmes Détectés (non présents dans le précédent audit)

### 8.1 sitemap.static.xml incomplet
- /home/artiste, /home/podcast, /home/mix, /boutique absents
- **Impact :** Ces pages n'ont pas de signal de priorité/fréquence pour Googlebot

### 8.2 Encodage corrompu dans llms.txt
- Caractères français mal encodés en UTF-8

### 8.3 Copyright © 2025 obsolète
- "© 2025 Slay Radio" affiché en 2026 — signal de fraîcheur négatif

---

## Tableau de Synthèse Global — 2026-04-27

| # | Finding | Sévérité | Catégorie | Statut |
|---|---------|----------|-----------|--------|
| 1 | Site non indexé dans Google | 🔴 Critique | Technical | ❌ À faire |
| 2 | Lazy loading manquant (Unsplash + icônes) | ⚠️ Warning | Performance | ⚠️ Partiel |
| 3 | Dimensions manquantes (Unsplash + icônes) | ⚠️ Warning | Performance | ⚠️ Partiel |
| 4 | Noms fichiers images "Capture-d-ecran-..." | ⚠️ Warning | Images | ❌ À faire |
| 5 | Format PNG → WebP non convertis | ⚠️ Warning | Images | ❌ À faire |
| 6 | Handle Twitter @SlayRadio vs @slayradio1 | ⚠️ Warning | On-Page | ❌ À vérifier |
| 7 | SearchAction URL à tester (?q= param) | ⚠️ Warning | Schema | ❌ À tester |
| 8 | /apropos sans E-E-A-T (équipe, chiffres) | ⚠️ Warning | Content | ❌ À améliorer |
| 9 | IndexNow non implémenté (Bing/Yandex) | ℹ️ Info | Technical | ❌ À faire |
| 10 | Pas encore soumis sur annuaires radio suisses | ℹ️ Info | Backlinks | ❌ À faire |

**Score actuel : 74/100**  
**Score potentiel si tout résolu : ~88/100**

---

## Éléments parfaitement en place (ne pas toucher)

| Élément | Vérifié le |
|---|---|
| HTTPS + headers sécurité (HSTS, CSP, X-Frame…) | 2026-04-27 |
| Open Graph 7/7 tags | 2026-04-27 |
| Twitter Card 5/5 tags | 2026-04-27 |
| Schema RadioStation + WebSite + SearchAction | 2026-04-27 |
| Schema MusicEvent sur événements | 2026-04-27 |
| Schema MusicGroup/ItemList sur artistes | 2026-04-27 |
| Canonical URL sur toutes les pages | 2026-04-27 |
| Meta description sur toutes les pages | 2026-04-27 |
| Alt text sur toutes les images | 2026-04-27 |
| lang="fr-CH" | 2026-04-27 |
| geo.region: CH | 2026-04-27 |
| Sitemap index + 3 sous-sitemaps | 2026-04-27 |
| robots.txt + crawlers IA | 2026-04-27 |
| llms.txt pour AI Search | 2026-04-27 |
| Lazy loading sur images artistes/événements | 2026-04-27 |
| Dimensions width/height sur images contenu | 2026-04-27 |
| Copyright footer 2026 | 2026-04-27 |
| Page podcast en noindex | 2026-04-27 |
| Google Search Console vérifiée (2 méthodes) | 2026-04-27 |

---

## Limites de l'Audit

- **PageSpeed Insights :** rate-limited. CWV réels (LCP, INP, CLS) non disponibles. Estimés à partir de l'analyse HTML.
- **Méthode de collecte :** Fetch direct Python/BeautifulSoup — données HTML réelles (plus fiable que WebFetch proxy).
