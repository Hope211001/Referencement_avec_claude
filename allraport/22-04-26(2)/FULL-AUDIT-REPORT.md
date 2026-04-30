# Rapport d'Audit SEO Complet — slayradio.ch

**Date :** 2026-04-21  
**Score global :** 49/100 (À améliorer)  
**Précédent score :** 42/100 (+7 pts depuis dernier audit)  
**Auditeur :** Claude SEO Skill — Audit LLM-first + scripts

---

## Résumé Exécutif

| Catégorie | Score | Poids | Points |
|-----------|-------|-------|--------|
| Technical SEO | 72/100 | 25% | 18.0 |
| Content Quality / E-E-A-T | 45/100 | 20% | 9.0 |
| On-Page SEO | 65/100 | 15% | 9.75 |
| Schema / Structured Data | 20/100 | 15% | 3.0 |
| Performance (CWV) | 40/100 | 10% | 4.0 |
| Image Optimization | 20/100 | 10% | 2.0 |
| AI Search Readiness (GEO) | 90/100 | 5% | 4.5 |
| **TOTAL** | **49/100** | 100% | **50.25** |

---

## Améliorations depuis le dernier audit (2026-04-21)

| Action | Statut |
|--------|--------|
| sitemap.evenements.xml créé (17 événements) | ✅ Fait |
| Sitemap index mis à jour | ✅ Fait |
| Titres de pages sur événements | ✅ Fait |

---

## Problèmes non résolus

| Action | Statut |
|--------|--------|
| /home/artiste — page toujours vide (placeholder) | ❌ Non fait |
| Lazy loading sur les images | ❌ Non fait |
| Meta descriptions pages internes | ❌ Non fait |
| JSON-LD MusicEvent sur événements | ❌ Non fait |
| Noms de fichiers images (Capture-d-ecran...) | ❌ Non fait |
| Dimensions width/height sur images | ❌ Non fait |
| Maillage interne vers événements | ❌ Non fait |

---

## 1. Technical SEO — 72/100

### 1.1 HTTPS & Sécurité
- **Finding:** HTTPS actif, HSTS configuré (max-age=31536000 + includeSubDomains)
- **Evidence:** `security_headers.py` → score 100/100, tous les headers présents (CSP, X-Frame-Options, X-Content-Type-Options, Referrer-Policy, Permissions-Policy)
- **Statut:** ✅ Pass

### 1.2 Redirections
- **Finding:** Aucune redirection, réponse directe 200 en 2060ms
- **Evidence:** `redirect_checker.py` → 0 hop, HTTP 200
- **Statut:** ✅ Pass

### 1.3 Robots.txt
- **Finding:** Bien configuré, tous les crawlers IA autorisés (GPTBot, ClaudeBot, PerplexityBot, Google-Extended, Applebot-Extended, Bytespider, CCBot, FacebookBot, Amazonbot)
- **Evidence:** `robots_checker.py` → 12 user-agents avec `Allow: /`
- **Statut:** ✅ Pass

### 1.4 Sitemap XML
- **Finding:** Sitemap index avec 2 fichiers. sitemap.evenements.xml = 17 événements (bien). Mais sitemap.static.xml ne couvre que 3 pages (/, /home/evenement, /apropos). Pages manquantes : /home/artiste, /home/podcast, /home/mix, /boutique.
- **Evidence:** sitemap.static.xml = 3 URLs | sitemap.evenements.xml = 17 URLs
- **Impact:** Pages /home/artiste, /home/podcast, /home/mix non indexables via sitemap
- **Statut:** ⚠️ Warning

### 1.5 Canonical
- **Finding:** Balise `<link rel="canonical">` non détectée sur la homepage
- **Evidence:** WebFetch homepage → canonical absente
- **Impact:** Risque de contenu dupliqué (www vs non-www, trailing slash)
- **Statut:** ⚠️ Warning

### 1.6 Liens internes
- **Finding:** 4 pages événements avec seulement 1 lien entrant chacune (quasi-orphelines)
- **Evidence:** `internal_links.py` → /client/evenement/5, /9, /10, /16 → 1 incoming link
- **Impact:** PageRank dilué, crawl budget moins efficace
- **Statut:** ⚠️ Warning

### 1.7 Liens cassés
- **Finding:** 0 lien cassé sur 19 liens vérifiés
- **Evidence:** `broken_links.py` → 19 healthy, 0 broken
- **Statut:** ✅ Pass

### 1.8 Rendu JavaScript
- **Finding:** Site SPA (React/Vue/Angular probable). Contenu artistes non rendu sans JS.
- **Evidence:** WebFetch /home/artiste → placeholder visible même en fetch statique
- **Impact:** Indexation retardée du contenu dynamique
- **Statut:** ⚠️ Warning

---

## 2. Content Quality / E-E-A-T — 45/100

### 2.1 Page /home/artiste — Thin Content Critique
- **Finding:** Page affiche toujours "De nouveaux artistes rejoignent bientôt la famille. Nos artistes sont en cours d'intégration."
- **Evidence:** WebFetch /home/artiste → placeholder confirmé, 0 profil artiste listé
- **Impact:** Thin content pénalisant — Google dévalorise les pages sans contenu substantiel
- **Statut:** 🔴 Critical

### 2.2 Page /apropos — E-E-A-T faible
- **Finding:** Sections Mission/Valeurs présentes mais sans date de fondation, sans équipe nommée, sans statistiques, sans mentions presse
- **Evidence:** WebFetch /apropos → aucun nom fondateur, aucune date, aucun chiffre
- **Impact:** Score E-E-A-T très bas — Google ne peut pas évaluer l'expertise
- **Statut:** ⚠️ Warning

### 2.3 Lisibilité Homepage
- **Finding:** Flesch 55.0 (difficile), paragraphes de 5.4 phrases en moyenne (cible : 2-4)
- **Evidence:** `readability.py` → Flesch 55.0, grade 10.5
- **Statut:** ⚠️ Warning

### 2.4 Contenu événements
- **Finding:** Les pages événements ont du contenu substantiel (titre, dates, description, artistes)
- **Evidence:** WebFetch /client/evenement/5 → contenu CARIBANA FESTIVAL présent
- **Statut:** ✅ Pass (minimum acceptable)

---

## 3. On-Page SEO — 65/100

### 3.1 Title Tags
- **Finding:** Présents et bien formatés sur toutes les pages vérifiées
  - Homepage: "Web radio suisse — Écoute Slay Radio en direct"
  - /home/artiste: "Artistes & DJs suisses — Slay Radio Suisse"
  - /client/evenement/5: "CARIBANA FESTIVAL (Crans) — Événement Slay Radio"
  - /apropos: "À propos de Slay Radio — Radio web suisse 100% musicale"
- **Statut:** ✅ Pass

### 3.2 Balises H1
- **Finding:** H1 unique présent sur toutes les pages vérifiées
- **Statut:** ✅ Pass

### 3.3 Meta Descriptions
- **Finding:** Absentes sur toutes les pages sauf la homepage (og:description)
  - /home/artiste, /client/evenement/*, /apropos : absentes
- **Evidence:** WebFetch pages internes → "Meta Description: Not provided"
- **Impact:** Google génère ses propres snippets → CTR potentiellement réduit
- **Statut:** ⚠️ Warning

### 3.4 Open Graph & Twitter Card
- **Finding:** Score 100/100 sur la homepage. og:locale fr_CH correct.
- **Evidence:** `social_meta.py` → 7/7 OG + 6/6 Twitter tags présents
- **Statut:** ✅ Pass (homepage)

### 3.5 Alt Text
- **Finding:** Alt text présent sur images principales, vide sur icônes réseaux sociaux
- **Evidence:** WebFetch → social_media_instagram.png et tiktok.png avec alt=""
- **Statut:** ⚠️ Warning

---

## 4. Schema / Structured Data — 20/100

### 4.1 JSON-LD Homepage
- **Finding:** Aucun JSON-LD détecté dans le HTML statique
- **Evidence:** WebFetch homepage → "Structured Data: None found"
- **Impact:** Pas d'éligibilité aux rich results RadioStation, pas de Knowledge Graph
- **Statut:** 🔴 Critical

### 4.2 JSON-LD Événements
- **Finding:** Aucun schema MusicEvent sur les pages événements
- **Evidence:** WebFetch /client/evenement/5 → "No JSON-LD or schema markup detected"
- **Impact:** Rich results manqués (calendrier Google, dates/lieu dans SERP)
- **Statut:** 🔴 Critical

### 4.3 JSON-LD Artistes
- **Finding:** Non vérifiable (rendu JS). Aucun schema Person/MusicGroup confirmé.
- **Statut:** ⚠️ Warning (hypothesis)

---

## 5. Performance (CWV) — 40/100

> Note : API PageSpeed Insights rate-limitée. Score estimé à partir des signaux HTML.

### 5.1 Lazy Loading
- **Finding:** Aucun attribut `loading="lazy"` sur les images
- **Evidence:** WebFetch → 8 images, 0 avec loading="lazy"
- **Impact:** LCP dégradé — toutes les images chargent simultanément au démarrage
- **Statut:** 🔴 Critical

### 5.2 Dimensions Images (CLS)
- **Finding:** 7 images sur 8 sans dimensions width/height
- **Evidence:** WebFetch → seule l'image Unsplash a width="600" height="450"
- **Impact:** CLS élevé — le layout se déplace pendant le chargement des images
- **Statut:** 🔴 Critical

### 5.3 Format WebP
- **Finding:** Toutes les images en PNG. Pas d'utilisation de WebP.
- **Evidence:** WebFetch → .png sur tous les uploads
- **Impact:** Poids 30-50% plus élevé qu'en WebP
- **Statut:** ⚠️ Warning

---

## 6. Image Optimization — 20/100

### 6.1 Noms de Fichiers
- **Finding:** 4 images avec noms auto-générés "Capture-d-ecran-YYYY-MM-DD-HHMMSS-[hash].png"
- **Evidence:** WebFetch → Capture-d-ecran-2026-04-17-094305-69e1e56d6d2ef.png, etc.
- **Impact:** Perte de signaux topicaux (nom = signal SEO faible mais réel)
- **Statut:** ⚠️ Warning

### 6.2 Alt Text Vide
- **Finding:** social_media_instagram.png et tiktok.png ont alt=""
- **Statut:** ⚠️ Warning

### 6.3 Image Externe (Unsplash)
- **Finding:** Image studio depuis Unsplash (externe), pas propriétaire
- **Impact:** Dépendance externe, pas de signal E-E-A-T visuel
- **Statut:** ℹ️ Info

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

## Tableau de Synthèse Global

| # | Finding | Sévérité | Catégorie | Impact Score |
|---|---------|----------|-----------|-------------|
| 1 | /home/artiste vide (thin content) | 🔴 Critical | Content | +6 pts |
| 2 | Aucun JSON-LD sur le site | 🔴 Critical | Schema | +8 pts |
| 3 | Pas de lazy loading images | 🔴 Critical | Performance | +3 pts |
| 4 | Pas de dimensions width/height | 🔴 Critical | Performance | +3 pts |
| 5 | Meta descriptions absentes (pages internes) | ⚠️ Warning | On-Page | +2 pts |
| 6 | sitemap.static.xml incomplet | ⚠️ Warning | Technical | +2 pts |
| 7 | Canonical absente | ⚠️ Warning | Technical | +1 pt |
| 8 | Noms fichiers images Capture-d-ecran | ⚠️ Warning | Images | +2 pts |
| 9 | /apropos sans E-E-A-T | ⚠️ Warning | Content | +5 pts |
| 10 | Maillage interne faible vers événements | ⚠️ Warning | Technical | +2 pts |
| 11 | Encodage corrompu llms.txt | ⚠️ Warning | GEO | +1 pt |
| 12 | Alt text vide sur icônes sociales | ⚠️ Warning | Images | +1 pt |
| 13 | Format PNG (pas WebP) | ⚠️ Warning | Images | +1 pt |
| 14 | Copyright © 2025 obsolète | ℹ️ Info | Content | +0 pt |

**Score potentiel si tout résolu : ~85/100**

---

## Limites de l'Audit

- **PageSpeed Insights :** rate-limited. CWV réels (LCP, INP, CLS) non disponibles. Findings performance basés sur l'analyse HTML.
- **JSON-LD :** WebFetch ne voit que le HTML statique. Si le schema est injecté par JS, il peut exister mais n'est pas confirmé.
- **Pages artistes (/artiste/*):** Non vérifiables sans rendu JavaScript.
