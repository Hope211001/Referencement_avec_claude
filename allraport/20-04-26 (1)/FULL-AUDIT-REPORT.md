# Rapport d'Audit SEO Complet — slayradio.ch

**Date :** 2026-04-20
**Auditeur :** Agentic SEO Skill v1
**Score SEO Global : 61/100** *(Amélioration : +20 pts vs audit précédent 41/100)*
**Précédent audit :** 2026-04-17

---

## Résumé Exécutif

| Catégorie | Score | Poids | Contribution | Évolution |
|-----------|-------|-------|--------------|-----------|
| Technique SEO | 75/100 | 25% | 18.75 | ↑ +14 |
| Qualité Contenu | 55/100 | 20% | 11.00 | ↑ +52 |
| On-Page SEO | 55/100 | 15% | 8.25 | ↑ +30 |
| Schema / Données Structurées | 45/100 | 15% | 6.75 | ↑ +10 |
| Performance (CWV) | 40/100 | 10% | 4.00 | = (données insuffisantes) |
| Images | 85/100 | 10% | 8.50 | ↑ +5 |
| Préparation IA (GEO) | 75/100 | 5% | 3.75 | ↑ +5 |
| **TOTAL** | **61/100** | 100% | **61.00** | **↑ +20** |

**Interprétation :** Needs Improvement — objectif 75/100 à 30 jours.

---

## Top 5 Problèmes Critiques

1. 🔴 **Schema RadioStation : logo = favicon.svg** — Google exige une image ≥ 112×112px pour le Knowledge Panel
2. 🔴 **Schema RadioStation : URL Facebook générique** — `https://www.facebook.com/` sans page officielle Slay Radio
3. ⚠️ **H1 non optimisé** — contenu éditorial et CTAs fusionnés, aucun mot-clé cible clair
4. ⚠️ **4 pages événement orphelines** — `/client/evenement/5,9,10,16` avec seulement 1 lien entrant chacune
5. ⚠️ **llms-full.txt absent** — llms.txt présent (95/100) mais catalogue complet manquant pour les LLMs

---

## Top 5 Quick Wins

1. ✅ Corriger `logo` dans schema RadioStation → utiliser l'image OG existante (1200×630)
2. ✅ Corriger URL Facebook dans `sameAs` → page officielle Slay Radio
3. ✅ Ajouter `<link rel="alternate" hreflang="x-default" href="https://slayradio.ch/" />` dans `<head>`
4. ✅ Créer `/llms-full.txt` avec catalogue DJs, mix, podcasts, événements
5. ✅ Nettoyer le H1 — séparer le contenu éditorial des CTAs

---

## Progrès Confirmés (depuis audit 2026-04-17)

| Action | Statut |
|--------|--------|
| Supprimer Lorem Ipsum | ✅ CORRIGÉ |
| Contenu homepage 234 → 500+ mots | ✅ CORRIGÉ (534 mots) |
| llms.txt créé | ✅ PRÉSENT (95/100) |
| Images — alt text | ✅ 9/9 images avec alt |
| H1 partiellement amélioré | ⚠️ Encore perfectible |
| Schema logo / Facebook | 🔴 NON CORRIGÉ |
| llms-full.txt | 🔴 NON CRÉÉ |
| Pages orphelines événements | ⚠️ Toujours 4 orphelines |

---

## 1. Technique SEO — 75/100

### 1.1 Robots.txt ✅ PASS (Confirmé)
```
Status          : 200 OK
Sitemap déclaré : https://slayradio.ch/sitemap.xml
Crawlers IA     : GPTBot, ClaudeBot, PerplexityBot, Google-Extended, Applebot-Extended,
                  Bytespider, CCBot, anthropic-ai, FacebookBot, Amazonbot — tous autorisés
Disallows       : 6 règles pour *
```
Gestion exemplaire des crawlers IA. Aucune action requise.

### 1.2 HTTPS & Sécurité ✅ PASS (Confirmé)
```
Score sécurité  : 100/100
HSTS            : max-age=31536000; includeSubDomains ✅
CSP             : Présent ✅
X-Frame-Options : SAMEORIGIN ✅
X-Content-Type  : nosniff ✅
Referrer-Policy : strict-origin-when-cross-origin ✅
Permissions-Policy : Présent ✅
```

### 1.3 Redirections ✅ PASS — TTFB ⚠️ WARNING (Confirmé)
```
Statut : 200 OK direct — aucune redirection inutile
TTFB   : 1583ms (objectif < 800ms)
```
**Finding :** TTFB 1583ms dépasse la recommandation Google de 800ms.
**Impact :** Pénalise le LCP et le score global Core Web Vitals.
**Fix :** Activer Cloudflare (CDN gratuit) ou optimiser le cache serveur côté hébergeur.
**Confidence :** Confirmé

### 1.4 Liens Brisés ✅ PASS (Confirmé)
```
Total vérifié : 19 liens
Brisés (4xx)  : 0
Timeouts      : 0
```
Note : warnings SSL (certificat non vérifié côté client) — sans impact SEO réel.

### 1.5 Liens Internes ⚠️ WARNING (Confirmé)
```
Pages crawlées   : 12
Pages uniques    : 16
Liens internes   : 108
Ancres vides     : 12 liens sans texte d'ancre
Orphelines       : 4 pages événements (≤ 1 lien entrant)
  → /client/evenement/9
  → /client/evenement/5
  → /client/evenement/10
  → /client/evenement/16
```
**Impact :** PageRank mal distribué vers les pages événements. Sous-indexation probable.
**Fix :** Ajouter des liens contextuels vers ces événements depuis homepage et /home/evenement.
**Confidence :** Confirmé

### 1.6 Hreflang ⚠️ WARNING (Confirmé)
```
Tags trouvés : 1
  ✅ fr-CH → https://slayradio.ch/
  ❌ x-default → ABSENT
Sitemap hreflang : Non trouvé
```
**Fix :**
```html
<link rel="alternate" hreflang="x-default" href="https://slayradio.ch/" />
```
**Confidence :** Confirmé

---

## 2. Qualité du Contenu — 55/100

### 2.1 Volume de Contenu ✅ PASS (Confirmé — Amélioré)
```
Mots        : 534 (objectif ≥ 500) ✅
Lorem Ipsum : ABSENT ✅ (corrigé depuis 2026-04-17)
```

### 2.2 Lisibilité ⚠️ WARNING (Confirmé)
```
Flesch Reading Ease   : 54.0 (objectif ≥ 60)
Flesch-Kincaid Grade  : 10.6 (objectif ≤ 8)
Niveau               : 9e–12e année (difficile)
Mots complexes        : 87 (16.3%)
Longueur para. moy.   : 5.4 phrases (objectif 2-4)
```
**Impact :** Taux de rebond potentiellement plus élevé. Score E-E-A-T réduit.
**Fix :** Raccourcir les phrases > 25 mots, scinder les longs paragraphes.
**Confidence :** Confirmé

### 2.3 Contenu Étranger Détecté ⚠️ WARNING (Likely)
```
Phrase détectée : "Blues Rules s'est alors employé avec assiduité à promouvoir
le blues du North Mississippi Hill Country à travers son festival..."
```
**Finding :** Un texte sur un festival de blues américain semble présent dans la page — étranger à l'identité de Slay Radio.
**Impact :** Contenu dilué, confusion thématique pour Google.
**Fix :** Identifier la section dans le CMS (podcasts ? événements ?) et supprimer ou remplacer.
**Confidence :** Likely (vérification visuelle recommandée)

### 2.4 E-E-A-T ⚠️ WARNING (Likely)
```
✅ H2 "Une radio née d'une passion pour la scène locale" — signal expérience
✅ H2 "Slay Radio, votre web radio suisse indépendante" — signal identité
❌ Page /apropos : non enrichie (biographies manquantes)
❌ Schema Organization : sans address CH, foundingDate, contactPoint
❌ Biographies DJs : non vérifiées
```
**Fix :** Enrichir /apropos + ajouter schema Organization complet.
**Confidence :** Likely

---

## 3. On-Page SEO — 55/100

### 3.1 Title Tag ✅ PASS (Confirmé)
```
Valeur   : "Web radio suisse — Écoute Slay Radio en direct"
Longueur : 46 caractères ✅
Mot-clé  : "web radio suisse" en tête ✅
```

### 3.2 Meta Description ✅ PASS (Confirmé)
```
Valeur   : "Slay Radio est une web radio suisse 100% musicale, diffusée en ligne
            24h/24. Écoute nos DJs en live, découvre leurs mix house, afrobeat et
            R&B, et suis les événements musicaux en Suisse romande."
Longueur : 194 caractères ✅
CTA      : "Écoute", "découvre", "suis" ✅
```

### 3.3 H1 🔴 CRITICAL (Confirmé)
```
Valeur extraite : "Slay Radio —ÉCOUTE • VIBERÉSERVE TON DJ PRÉFÉRÉ"
Problème        : Plusieurs spans fusionnés — CTAs inclus dans le H1
```
**Impact :** Signal on-page principal de Google dégradé. Le H1 ne communique pas de mot-clé cible.
**Fix :**
```html
<h1>Slay Radio — La Web Radio Suisse 100% Musicale</h1>
<!-- Déplacer ÉCOUTE • VIBE et RÉSERVE TON DJ PRÉFÉRÉ dans des <p> ou <span> -->
```
**Confidence :** Confirmé

### 3.4 Structure H2 ⚠️ MIXED (Confirmé)
```
H2-1 : "Evenement disponible" — Faible (faute, pas de mot-clé)
H2-2 : "Une radio née d'une passion pour la scène locale" ✅
H2-3 : "Slay Radio, votre web radio suisse indépendante" ✅
H2-4 : "Prêt à vivre l'expérience Slay Radio ?" — CTA acceptable
```
**Fix H2-1 :** Renommer en "Événements musicaux en Suisse romande".

### 3.5 URL & Canonical ✅ PASS (Confirmé)
```
Canonical : https://slayradio.ch/ — correct ✅
URLs sous-pages : /client/evenement/[id] — numériques, peu descriptifs
```
**Suggestion long terme :** Migrer vers `/evenements/[slug-titre]`.

---

## 4. Schema / Données Structurées — 45/100

### 4.1 RadioStation ⚠️ ISSUES (Confirmé)
```json
{
  "@type": "RadioStation",
  "name": "Slay Radio",
  "description": "Web radio suisse 100% musicale..." ✅,
  "url": "https://slayradio.ch/" ✅,
  "logo": "https://slayradio.ch/favicon.svg" 🔴,
  "sameAs": [
    "https://www.facebook.com/" 🔴,
    "https://www.instagram.com/slayradio1/" ✅,
    "https://www.youtube.com/channel/UCaD7SGkU6AI8liZdAKgm7nQ" ✅,
    "https://www.tiktok.com/@slayradio1?lang=fr" ✅
  ]
}
```
**Fix logo :**
```json
"logo": {
  "@type": "ImageObject",
  "url": "https://slayradio.ch/image/og-default.png",
  "width": 1200,
  "height": 630
}
```
**Fix Facebook :**
```json
"https://www.facebook.com/[handle-officiel-slay-radio]"
```

### 4.2 WebSite avec SearchAction ✅ PASS (Confirmé)
```json
{
  "@type": "WebSite",
  "potentialAction": {
    "@type": "SearchAction",
    "target": { "urlTemplate": "https://slayradio.ch/home/artiste?q={search_term_string}" }
  }
}
```
Sitelinks Searchbox potentiellement éligible dans les SERPs. ✅

### 4.3 Manques Identifiés ⚠️ WARNING (Hypothèse)
```
❌ BreadcrumbList — absent sur les sous-pages
❌ MusicEvent — absent sur les pages d'événements
❌ Organization — absent (address CH, foundingDate, contactPoint)
❌ MusicGroup/Person — absent sur les pages artiste
```
**Confidence :** Likely (vérification des sous-pages non exhaustive)

---

## 5. Performance (CWV) — 40/100

### 5.1 PageSpeed Insights ℹ️ INFO (Données insuffisantes)
```
Status : Rate-limited par l'API Google (sans clé API PSI)
```
**Limitation environnement :** CWV non mesurables. Utiliser :
```bash
export PAGESPEED_API_KEY=votre_cle
python3 scripts/pagespeed.py https://slayradio.ch/ --strategy mobile
```

### 5.2 TTFB ⚠️ WARNING (Confirmé)
```
TTFB mesuré : 1583ms (objectif < 800ms)
```
**Impact :** TTFB élevé pénalise directement le LCP.
**Options :** Cloudflare CDN > cache brotli/gzip > hébergement Europe.

---

## 6. Images — 85/100

### 6.1 Alt Text ✅ PASS (Confirmé)
```
Images totales : 9
Alt manquants  : 0 (100% couverts) ✅
```

### 6.2 Format & Compression ℹ️ INFO (Hypothèse)
```
Recommandation : Utiliser WebP/AVIF pour économiser 25-50% de poids
Confidence     : Hypothèse (nécessite PageSpeed pour confirmation)
```

---

## 7. Préparation IA (GEO) — 75/100

### 7.1 llms.txt ✅ PASS (Confirmé)
```
Status        : HTTP 200 ✅
Titre         : Slay Radio
Description   : "Radio web suisse 100% musicale, 100% digitale"
Sections      : 4
Liens         : 9
Score qualité : 95/100
```

### 7.2 llms-full.txt 🔴 MISSING (Confirmé)
```
Status : HTTP 404 — Non créé
```
**Impact :** Les LLMs (ChatGPT, Perplexity, Claude) ne peuvent pas accéder au catalogue complet des DJs, mix et podcasts.
**Fix :** Créer `/llms-full.txt` (voir ACTION-PLAN.md § P2-3).
**Confidence :** Confirmé

### 7.3 Crawlers IA ✅ PASS (Confirmé)
```
Tous les crawlers IA majeurs autorisés dans robots.txt ✅
```

---

## Annexe — Scripts Exécutés

| Script | Résultat |
|--------|----------|
| `fetch_page.py` | ✅ 200 OK |
| `robots_checker.py` | ✅ Complet — 12 crawlers gérés |
| `security_headers.py` | ✅ 100/100 |
| `redirect_checker.py` | ✅ 0 redirection — TTFB 1583ms |
| `social_meta.py` | ✅ 100/100 |
| `readability.py` | ✅ Flesch 54.0, grade 10.6 |
| `llms_txt_checker.py` | ✅ 95/100 — llms-full.txt absent |
| `internal_links.py` | ✅ 4 pages orphelines |
| `broken_links.py` | ✅ 0 lien brisé |
| `hreflang_checker.py` | ✅ x-default manquant |
| `validate_schema.py` | ⚠️ Erreur parse (schema sous forme de liste JSON) |
| `pagespeed.py` | ❌ Rate limited (sans clé API) |
| `article_seo.py` | ❌ Erreur parse (même cause) |

---

*Rapport généré par Agentic SEO Skill v1 — 2026-04-20*
