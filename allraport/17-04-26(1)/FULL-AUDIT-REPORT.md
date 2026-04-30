# Rapport d'Audit SEO Complet — slayradio.ch

**Date :** 2026-04-17 (mise à jour — audit précédent : 2026-04-16)
**URL :** https://slayradio.ch/
**Portée :** Audit page unique + vérifications techniques de base
**Type de site :** Radio web suisse — Publisher / Media, langue fr_CH
**Auditeur :** Agentic SEO Skill (Claude Sonnet 4.6)

---

## A) Résumé Exécutif

| Indicateur | Valeur | Δ vs audit précédent |
|---|---|---|
| Score SEO Global | **41 / 100 — Mauvais** | +9 (était 32) |
| Confiance du score | Moyenne (PageSpeed rate-limited) | — |
| Pages analysées | 9 | = |
| Liens internes | 65 | — |
| Liens brisés | 0 / 13 | = |
| HTTPS | ✅ Oui | = |
| Schema JSON-LD | ✅ RadioStation + WebSite | ↑ (était absent) |
| Lorem Ipsum | 🔴 Détecté | ↓ NEW |

### Top 3 Problèmes Critiques

1. 🔴 **Lorem Ipsum** — Texte fictif de remplacement visible publiquement sur la homepage (NOUVEAU)
2. 🔴 **H1 non pertinent** — "Listen • VibesBook Your Favorite DJ" (anglais, non localisé, non optimisé)
3. ⚠️ **Thin content** — 234 mots sur la homepage (seuil recommandé ≥ 500 mots)

### Top 3 Points Forts (confirmés)

1. ✅ **Sécurité exemplaire** — Headers de sécurité : 100/100 (HSTS, CSP, X-Frame-Options...)
2. ✅ **Social meta parfait** — Open Graph 7/7 + Twitter Card 6/6 : score 100/100
3. ✅ **Préparation IA avancée** — 11 crawlers IA explicitement autorisés, llms.txt 95/100

### Évolutions positives depuis le dernier audit

- Schema JSON-LD ajouté : RadioStation + WebSite avec SearchAction ✅
- Facebook URL dans sameAs toujours générique (à corriger)
- Rendu JS : le HTML de la homepage est maintenant servi avec contenu (pas de "Aucuns X trouvés")

---

## B) Tableau des Constats

| Domaine | Sévérité | Confiance | Constat | Preuve | Correction |
|---|---|---|---|---|---|
| Contenu | 🔴 Critique | Confirmé | Texte Lorem Ipsum présent sur la homepage | HTML : "Lorem Ipsum is simply dummy text of the printing and typesetting industry..." dans une section | Remplacer immédiatement par du contenu éditorial réel |
| On-Page | 🔴 Critique | Confirmé | H1 = "Listen • VibesBook Your Favorite DJ" — anglais, non pertinent | Extrait HTML `<h1>` | Réécrire : "Slay Radio — Votre Radio Web Suisse 100% Musicale" |
| Contenu | ⚠️ Warning | Confirmé | Thin content : 234 mots homepage (min requis ≥ 500) | readability.py : word_count=234 | Enrichir : mission, artistes, genres, émissions, valeur unique |
| Contenu | ⚠️ Warning | Confirmé | Lisibilité difficile : Flesch 44.7 / niveau 11,5 | readability.py : flesch_reading_ease=44.7, flesch_kincaid_grade=11.5 | Simplifier phrases ; viser Flesch ≥ 60 |
| Liens internes | ⚠️ Warning | Confirmé | 2 pages orphelines : /home/decouverte et /home/evenement (1 lien entrant chacune) | internal_links.py : "2 potential orphan pages" | Ajouter liens contextuels depuis navigation principale ou contenu connexe |
| Schema | ⚠️ Warning | Confirmé | sameAs Facebook générique : "https://www.facebook.com/" | JSON-LD RadioStation > sameAs[0] | Remplacer par l'URL exacte de la page Facebook Slay Radio |
| Schema | ⚠️ Warning | Confirmé | Logo schema pointe vers favicon.svg (trop petit) | JSON-LD : "logo": "https://slayradio.ch/favicon.svg" | Utiliser une image logo ≥ 112×112 px (PNG/JPG) |
| Schema | ⚠️ Warning | Confirmé | Pas de BreadcrumbList, pas d'Organization séparé ni d'Event schema | HTML : 1 bloc JSON-LD (tableau) | Ajouter Organization avec address, BreadcrumbList sur sous-pages, MusicEvent pour événements |
| Perf. | ⚠️ Warning | Likely | Temps de réponse 1384ms — lent | redirect_checker.py : 1384ms au TTFB | Activer CDN (Cloudflare), optimiser serveur origine |
| AI Search | ⚠️ Warning | Confirmé | llms-full.txt absent | llms_txt_checker.py : "llms-full.txt: Not found" | Créer /llms-full.txt avec catalogue étendu |
| Perf. CWV | ℹ️ Info | Hypothèse | PageSpeed non disponible (API rate-limited) | pagespeed.py : "Rate limited" | Relancer avec clé API Google PSI |
| Technique | ✅ Pass | Confirmé | HTTPS + tous en-têtes de sécurité présents (100/100) | security_headers.py : 100/100 | — |
| Technique | ✅ Pass | Confirmé | Canonical correctement défini | `<link rel="canonical" href="https://slayradio.ch/">` | — |
| Technique | ✅ Pass | Confirmé | robots.txt 200 OK + sitemap déclaré + 11 AI bots autorisés | robots_checker.py | — |
| Technique | ✅ Pass | Confirmé | 0 lien brisé sur 13 (12 sains, 1 redirigé) | broken_links.py | — |
| Images | ✅ Pass | Confirmé | 9 images — 0 sans attribut alt | BeautifulSoup parse HTML | — |
| Social | ✅ Pass | Confirmé | Open Graph 7/7 + Twitter Card 6/6 (og:locale fr_CH) | social_meta.py : 100/100 | — |
| Schema | ✅ Pass | Confirmé | JSON-LD RadioStation + WebSite avec SearchAction présents | HTML source — 1 bloc avec 2 objets | — |
| AI Search | ✅ Pass | Confirmé | llms.txt trouvé (200 OK), score 95/100, 4 sections, 9 liens | llms_txt_checker.py | — |

---

## C) Scores par Catégorie (méthode chaîne de pensée)

### Technique SEO — Score : 61/100 (Poids 25%)

**Positifs (5) :** HTTPS ✅ · Sécurité 100/100 ✅ · Canonical ✅ · robots.txt 200 ✅ · Sitemap ✅
**Déficits (2) :** Temps réponse 1384ms ⚠️ · SSL warnings urllib3 ⚠️
Base : 5/7 × 100 = 71 — Pénalités : −10 (2 Warning) → **Score : 61**

> "61 reflète une infrastructure de sécurité et de crawl exemplaire, pénalisé par un TTFB de 1384ms dépassant le seuil de 800ms."

### Qualité du Contenu — Score : 3/100 (Poids 20%)

**Positifs (2) :** Bonne meta description ✅ · OG/Twitter complet ✅
**Déficits (4) :** Lorem Ipsum 🔴 · Thin content 234 mots ⚠️ · Flesch 44.7 ⚠️ · H1 non optimisé ⚠️
Base : 2/6 × 100 = 33 — Pénalités : −15 (1 Critique) − 15 (3 Warning) → **Score : max(0, 3) = 3**

> "Score de 3 dominé par la présence de Lorem Ipsum (Critique, −15) aggravée par thin content, lisibilité difficile et H1 hors-sujet (3×Warning, −15)."

**Détail readability :**
```
word_count          : 234  (min requis : 500)
flesch_reading_ease : 44.7 → Difficile
flesch_kincaid_grade: 11.5 (lycée)
avg_sentence_len    : 18.0 mots
complex_words_%     : 19.2%
Texte détecté       : ⚠️ Lorem Ipsum (contenu fictif)
```

### On-Page SEO — Score : 25/100 (Poids 15%)

**Positifs (3) :** Titre bien écrit ✅ · Meta description ✅ · Canonical ✅
**Déficits (3) :** H1 non pertinent ⚠️ · 2 pages orphelines ⚠️ · Lorem Ipsum 🔴
Base : 50 — Pénalités : −15 −10 → **Score : 25**

**Titre et H1 actuel vs recommandé :**
| Élément | Actuel | Recommandé |
|---|---|---|
| `<title>` | "Slay Radio — Radio web 100% musicale, 100% digitale" | Conforme ✅ (51 car.) |
| `<h1>` | "Listen • VibesBook Your Favorite DJ" | "Slay Radio — Votre Radio Web Suisse 100% Musicale" |
| `<meta description>` | "Slay Radio, votre radio web digitale. Écoutez nos DJs en live, découvrez leurs mix, podcasts et réservez vos événements musicaux." | Conforme ✅ |

**H2 détectés :**
- "Mix Dj disponible", "Découvertes", "Podcast / Shows / Playlist Video", "Nos Produits", "Evenement disponible", "Prêt à vivre l'expérience Slay Radio ?"

### Schema / Données Structurées — Score : 35/100 (Poids 15%)

**Positifs (3) :** RadioStation JSON-LD ✅ · WebSite + SearchAction ✅ · Format JSON-LD correct ✅
**Déficits (3) :** sameAs Facebook générique ⚠️ · Logo = favicon.svg ⚠️ · Pas de BreadcrumbList ni Organization séparé ⚠️
Base : 50 — Pénalités : −15 (3 Warning) → **Score : 35**

**Schema actuel (extrait) :**
```json
[
  {
    "@type": "RadioStation",
    "name": "Slay Radio",
    "url": "https://slayradio.ch/",
    "logo": "https://slayradio.ch/favicon.svg",
    "sameAs": ["https://www.facebook.com/", "https://www.instagram.com/slayradio1/", ...]
  },
  {
    "@type": "WebSite",
    "name": "Slay Radio",
    "url": "https://slayradio.ch/",
    "potentialAction": { "@type": "SearchAction", "target": "...?q={search_term_string}" }
  }
]
```

**Améliorations prioritaires :**
- Corriger `sameAs[0]` Facebook : `"https://www.facebook.com/slayradio"` (ou URL exacte)
- Remplacer `"logo": "https://slayradio.ch/favicon.svg"` → `"logo": { "@type": "ImageObject", "url": "https://slayradio.ch/image/og-default.png" }`
- Ajouter BreadcrumbList sur toutes les sous-pages
- Ajouter MusicEvent pour les événements sur /home/evenement
- Ajouter MusicGroup/Person pour les artistes

### Performance (CWV) — Score : 50/100 (Poids 10%) — Confiance : Basse

PageSpeed API rate-limitée — données CWV non disponibles.
TTFB mesuré : 1384ms (seuil cible < 800ms).

### Images — Score : 80/100 (Poids 10%)

9 images, 0 sans attribut alt. Format/compression non vérifiés (parse_html error).

### Préparation IA (GEO/AEO) — Score : 70/100 (Poids 5%)

**Positifs (3) :** llms.txt 95/100 ✅ · 11 bots IA autorisés ✅ · HTTPS ✅
**Déficits (1) :** llms-full.txt absent ⚠️
Base : 75 — Pénalités : −5 → **Score : 70**

---

## Score Global Pondéré

| Catégorie | Poids | Score | Contribution |
|---|---|---|---|
| Technique SEO | 25% | 61 | 15.25 |
| Qualité Contenu | 20% | 3 | 0.60 |
| On-Page SEO | 15% | 25 | 3.75 |
| Schema | 15% | 35 | 5.25 |
| Performance CWV | 10% | 50* | 5.00 |
| Images | 10% | 80 | 8.00 |
| Préparation IA | 5% | 70 | 3.50 |
| **TOTAL** | | | **41 / 100 — Mauvais** |

*Données insuffisantes (API rate-limited) — score neutre appliqué

**Interprétation :** 41/100. La base technique est désormais solide (+9 vs hier grâce au schema). Le Lorem Ipsum et le thin content plombent massivement le score contenu. La remontée peut être rapide si le contenu est corrigé cette semaine.

---

## D) Inconnues et Suivis

| Vérification | Statut | Action requise |
|---|---|---|
| Core Web Vitals (LCP, INP, CLS) | ❌ Indisponible | Relancer avec clé API Google PSI |
| Compression images (WebP/AVIF) | ❓ Non vérifié | Inspecter avec DevTools réseau |
| Duplication de contenu | ❓ Non vérifié | Lancer `duplicate_content.py https://slayradio.ch/` |
| Profil de backlinks | ❓ Non vérifié | Lancer `link_profile.py https://slayradio.ch/` |
| Analyse visuelle mobile | ❓ Non vérifié | Installer Playwright → `capture_screenshot.py` |
| Google Search Console | ❓ Accès non configuré | Vérifier couverture d'indexation |
| Pages artiste (/home/artiste/[slug]) | ❓ Non vérifié | Tester quelques URLs artiste manuellement |

---

## E) Limitations Environnement

- **PageSpeed Insights** : Rate-limited (sans clé API). CWV non mesurés.
- **parse_html.py** : Erreur `AttributeError: 'list' object has no attribute 'get'` sur le bloc schema (type liste). Contenu vérifié via BeautifulSoup direct.
- **Playwright** : Non installé. Screenshots non capturés.
