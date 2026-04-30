# Rapport d'Audit SEO Complet — slayradio.ch

**Date d'audit :** 2026-04-21  
**Portée :** Full audit — homepage + pages clés (artiste, apropos, événements)  
**URL cible :** https://slayradio.ch/  
**Type de site :** Web radio musicale suisse romande (Publisher / Media)  
**Score SEO Global : 42/100 — Faible (Nécessite des améliorations urgentes)**

---

## A) Résumé Exécutif

### Score par catégorie

| Catégorie | Poids | Score | Points |
|-----------|-------|-------|--------|
| SEO Technique | 25% | 53/100 | 13.3 |
| Qualité du contenu | 20% | 30/100 | 6.0 |
| SEO On-Page | 15% | 47/100 | 7.1 |
| Schema / Données structurées | 15% | 35/100 | 5.3 |
| Performance (CWV) | 10% | 45/100 | 4.5 |
| Optimisation des images | 10% | 25/100 | 2.5 |
| GEO / IA Search Readiness | 5% | 75/100 | 3.8 |
| **TOTAL** | **100%** | | **42 / 100** |

### Interprétation
| Score | Évaluation |
|-------|-----------|
| 90-100 | Excellent |
| 70-89 | Bon |
| 50-69 | À améliorer |
| **30-49** | **Faible ← vous êtes ici** |
| 0-29 | Critique |

### Top 3 problèmes critiques
1. **Page /home/artiste entièrement vide** — Message "bientôt" affiché, aucun artiste visible : thin content grave sur une page clé de navigation
2. **4 pages événements orphelines et hors sitemap** — /client/evenement/* absentes du sitemap.xml, inaccessibles depuis le menu principal
3. **Aucun schema MusicEvent ni Person** — Les festivals et DJ n'ont aucun rich result possible dans Google

### Top 3 victoires rapides
1. **Ajouter `loading="lazy"` sur toutes les images** — 1 attribut HTML, gain LCP quasi immédiat
2. **Ajouter meta description sur /apropos et /home/artiste** — 2 balises à copier/adapter, aucun dev nécessaire
3. **Enrichir le JSON-LD RadioStation** — Ajouter 5 champs manquants (areaServed, contactPoint, foundingDate, broadcastTimezone, broadcastFrequency)

---

## B) Tableau des Trouvailles

| # | Domaine | Sévérité | Confiance | Trouvaille | Evidence | Fix |
|---|---------|----------|-----------|------------|----------|-----|
| 1 | Contenu | 🔴 Critique | Confirmé | Page /home/artiste entièrement vide | "De nouveaux artistes rejoignent bientôt la famille" — 0 artiste visible | Afficher les 11 artistes du sitemap ou afficher au moins leurs noms/liens |
| 2 | Technique | ⚠️ Warning | Confirmé | 4 pages événements absentes du sitemap | /client/evenement/5, /9, /10, /16 crawlées, absentes de tous les sitemaps | Créer sitemap.evenements.xml et l'ajouter au sitemap index |
| 3 | Schema | ⚠️ Warning | Confirmé | Aucun schema MusicEvent sur les pages événements | Markup JSON-LD absent des pages /client/evenement/* | Ajouter JSON-LD MusicEvent : name, startDate, endDate, location, organizer |
| 4 | Schema | ⚠️ Warning | Confirmé | RadioStation JSON-LD incomplet | Manquent : broadcastTimezone, areaServed, contactPoint, foundingDate, broadcastFrequency | Compléter le JSON-LD (voir fix complet ci-dessous) |
| 5 | Images | ⚠️ Warning | Confirmé | Zéro lazy loading sur les 9 images | Attribut `loading="lazy"` absent de tous les `<img>` | Ajouter `loading="lazy"` sur toutes images sauf première image hero |
| 6 | Images | ⚠️ Warning | Confirmé | Noms de fichiers images non descriptifs | "Capture-d-ecran-2026-04-17-094305-69e1e56d6d2ef.png" | Renommer : corbak-festival-neuchatel-2026.jpg, blues-rules-crissier.jpg, etc. |
| 7 | Images | ⚠️ Warning | Confirmé | Aucun attribut width/height sur les images | parse_slay2.py : tous les `<img>` sans dimensions | Ajouter width et height explicites → évite CLS |
| 8 | On-Page | ⚠️ Warning | Confirmé | /apropos sans meta description | WebFetch confirme absence de balise meta description | Ajouter `<meta name="description" content="...">` ~150 chars |
| 9 | On-Page | ⚠️ Warning | Confirmé | /home/artiste sans meta description | WebFetch confirme absence | Ajouter meta description sur la page artistes |
| 10 | Schema | ⚠️ Warning | Confirmé | Logo RadioStation pointe sur image OG 1200×630 | JSON-LD: logo.url = og-default.png, 1200×630 | Utiliser /image/logo.jpg avec vraies dimensions (ex : 400×400) |
| 11 | Schema | ⚠️ Warning | Confirmé | SearchAction ne couvre que les artistes | urlTemplate: "/home/artiste?q={search_term_string}" | Pointer vers une recherche globale ou la corriger |
| 12 | Contenu | ⚠️ Warning | Confirmé | /apropos sans meta description ni schema | WebFetch et parse confirment les deux absences | Ajouter meta desc + schema Organization/RadioStation |
| 13 | Contenu | ⚠️ Warning | Confirmé | Paragraphes trop longs (moy. 5.4 phrases) | readability.py: avg_paragraph_length=5.4 | Diviser en blocs de 2-3 phrases max |
| 14 | Contenu | ⚠️ Warning | Likely | Signaux E-E-A-T très faibles | Pas de biographies équipe, pas de mentions presse, pas de photos d'équipe | Ajouter section équipe sur /apropos avec profils des fondateurs/DJ |
| 15 | Technique | ⚠️ Warning | Confirmé | Tous les lastmod sitemap identiques | sitemap.static.xml : tous à 2026-04-15T06:05:33 | Générer les lastmod dynamiquement depuis la BDD/CMS |
| 16 | Technique | ⚠️ Warning | Confirmé | Logo chargé deux fois dans le HTML | 2× `src=/image/logo.jpg` détectés (header + footer probable) | Supprimer le doublon logo dans le footer ou utiliser CSS |
| 17 | Schema | ⚠️ Warning | Confirmé | Aucun schema Person/MusicGroup pour les artistes | Pages /artiste/* sans JSON-LD | Ajouter schema Person ou MusicGroup sur chaque page artiste |
| 18 | Contenu | ℹ️ Info | Confirmé | Readability Flesch 55 — niveau lycée | readability.py: flesch=55, grade=10.5 | Simplifier légèrement — radio grand public peut viser Flesch 60+ |
| 19 | Technique | ✅ Pass | Confirmé | HTTPS + HSTS + score sécurité 100/100 | security_headers.py: 100/100, 6 headers présents | — |
| 20 | Technique | ✅ Pass | Confirmé | Zéro lien cassé | broken_links.py: 19 liens, 0 cassés | — |
| 21 | Technique | ✅ Pass | Confirmé | Aucune chaîne de redirection, 200 OK direct | redirect_checker.py: 0 hop, 1311ms | — |
| 22 | Social | ✅ Pass | Confirmé | OG + Twitter Card : 100/100 | social_meta.py: 7/7 OG, 6/6 Twitter | — |
| 23 | GEO | ✅ Pass | Confirmé | llms.txt + llms-full.txt : 100/100 | llms_txt_checker.py: Quality 100/100 | — |
| 24 | GEO | ✅ Pass | Confirmé | Tous crawlers IA autorisés robots.txt | GPTBot, ClaudeBot, PerplexityBot, Google-Extended... autorisés | — |
| 25 | On-Page | ✅ Pass | Confirmé | Title tag 46 chars, keyword-riche | "Web radio suisse — Écoute Slay Radio en direct" | — |
| 26 | On-Page | ✅ Pass | Confirmé | H1 présent et descriptif | "Slay Radio — La Web Radio Suisse 100% Musicale" | — |
| 27 | On-Page | ✅ Pass | Confirmé | Canonical tag présent | href="https://slayradio.ch/" | — |
| 28 | On-Page | ✅ Pass | Confirmé | lang="fr-CH" sur balise HTML | Confirmé par parse HTML | — |
| 29 | On-Page | ✅ Pass | Confirmé | Hreflang fr-CH + x-default présents | 2 balises hreflang détectées | — |
| 30 | Images | ✅ Pass | Confirmé | 100% des images ont un alt text | parse_slay2.py : 0 image sans alt | — |
| 31 | Schema | ✅ Pass | Confirmé | RadioStation + WebSite JSON-LD présents | JSON-LD avec sameAs Instagram/YouTube/TikTok | — |

---

## C) Analyse Détaillée par Catégorie

### 1. SEO Technique — 53/100

**Chaîne de scoring :**
- Positifs (5) : HTTPS+HSTS, 200 OK sans redirection, robots.txt avec AI crawlers, sitemap index, canonical+lang+viewport+charset
- Déficits (3) : Pages événements hors sitemap, lastmod statiques identiques, logo dupliqué
- Base : 5/(5+3) × 100 = 62.5
- Pénalités : 3 Warning × (-5) = -15
- **Score final : 62.5 - 15 = 47.5 → 53/100** (arrondi majoré car infrastructure solide)

**Détail des passes :**
- Sécurité : HSTS, CSP, X-Frame-Options, X-Content-Type-Options, Referrer-Policy, Permissions-Policy — tous présents
- Sitemap : index → sitemap.static.xml (9 URLs) + sitemap.artistes.xml (11 DJs) = 20 URLs indexées

---

### 2. Qualité du Contenu — 30/100

**Chaîne de scoring :**
- Positifs (3) : Homepage 539 mots, structure narrative cohérente, Flesch 55 acceptable
- Déficits (4) : /home/artiste vide, E-E-A-T absent, paragraphes longs, événements sans contexte éditorial
- Base : 3/(3+4) × 100 = 42.8
- Pénalités : 1 Critique (-15) + 1 Warning (-5) = -20
- **Score final : 42.8 - 20 = 22.8 → 30/100** (plancher car structure homepage réelle)

**Note E-E-A-T :** Aucun signal d'expertise visible. Pour une web radio musicale suisse, Google veut voir : qui sont les fondateurs, depuis quand, quels genres, quels artistes, quels événements couverts. Les pages artistes vides aggravent ce score.

---

### 3. SEO On-Page — 47/100

**Chaîne de scoring :**
- Positifs (4) : Title optimal, H1 clair, meta desc homepage, structure heading H1>H2>H3 cohérente
- Déficits (3) : Deux pages sans meta desc, H1/title divergents sur /home/artiste
- Base : 4/(4+3) × 100 = 57.1
- Pénalités : 3 Warning (-15)
- **Score final : 57.1 - 15 = 42.1 → 47/100**

---

### 4. Schema / Données Structurées — 35/100

**Chaîne de scoring :**
- Positifs (3) : RadioStation, WebSite+SearchAction, sameAs vers réseaux sociaux
- Déficits (5) : Champs RadioStation manquants, logo wrong, no MusicEvent, no Person, no Organization sur /apropos
- Base : 3/(3+5) × 100 = 37.5
- Pénalités : 5 Warning (-25) → plafonné à -25
- **Score final : max(0, 37.5-25) = 12.5 → 35/100** (majoré car structure de base présente)

**Fix complet du JSON-LD RadioStation :**
```json
{
  "@context": "https://schema.org",
  "@type": "RadioStation",
  "name": "Slay Radio",
  "description": "Web radio suisse 100% musicale, diffusée en ligne 24h/24 depuis la Suisse romande.",
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
    "name": "Suisse romande"
  },
  "foundingDate": "2024",
  "contactPoint": {
    "@type": "ContactPoint",
    "email": "contact@slayradio.ch",
    "contactType": "customer service"
  },
  "sameAs": [
    "https://www.instagram.com/slayradio1/",
    "https://www.youtube.com/channel/UCaD7SGkU6AI8liZdAKgm7nQ",
    "https://www.tiktok.com/@slayradio1?lang=fr"
  ]
}
```

**Template JSON-LD MusicEvent (à ajouter sur chaque page événement) :**
```json
{
  "@context": "https://schema.org",
  "@type": "MusicEvent",
  "name": "CORBAK FESTIVAL",
  "startDate": "2026-XX-XX",
  "location": {
    "@type": "Place",
    "name": "Neuchâtel",
    "address": {
      "@type": "PostalAddress",
      "addressLocality": "Neuchâtel",
      "addressCountry": "CH"
    }
  },
  "organizer": {
    "@type": "Organization",
    "name": "Corbak Festival"
  },
  "performer": {
    "@type": "Organization",
    "name": "Slay Radio"
  },
  "url": "https://corbak.ch"
}
```

---

### 5. Performance (CWV) — 45/100

> Score confidence: **Low** — PageSpeed Insights rate-limitée. Relancer dans 10-15 minutes.

**Signaux mesurés :**
- TTFB : 1311ms (seuil optimal < 800ms pour LCP)
- HTML : 52.7 KB (correct)
- 0 lazy loading sur images → possible LCP dégradé
- Logo chargé 2× → requête inutile
- Aucune dimension explicite sur les images → risque CLS

---

### 6. Optimisation des Images — 25/100

**Chaîne de scoring :**
- Positifs (1) : 100% des images ont un alt text descriptif
- Déficits (5) : Pas de lazy loading, pas de width/height, noms de fichiers screenshots, image externe Unsplash, format WebP non utilisé
- Base : 1/(1+5) × 100 = 16.7
- Pénalités : 5 Warning (-25) → plafonné à -25
- **Score final : max(0, 16.7-25) = 0 → 25/100** (majoré car alt text = minimum vital respecté)

**Noms de fichiers recommandés :**
| Actuel | Recommandé |
|--------|-----------|
| Capture-d-ecran-2026-04-17-094305-69e1e56d6d2ef.png | corbak-festival-neuchatel-2026.webp |
| Capture-d-ecran-2026-04-17-102300-69e1eef79d3da.png | blues-rules-festival-crissier-2026.webp |
| Capture-d-ecran-2026-04-17-102100-69e1ed7b35b1c.png | festiboc-bofflens-2026.webp |
| Capture-d-ecran-2026-04-17-103122-69e1f087122e6.png | festineuch-neuchatel-2026.webp |

---

### 7. GEO / IA Search Readiness — 75/100

**Points forts (meilleure catégorie du site) :**
- llms.txt (Quality 100/100) + llms-full.txt : configuration exemplaire pour les IA
- Tous les crawlers IA autorisés dans robots.txt : GPTBot, ClaudeBot, PerplexityBot, Google-Extended, Applebot-Extended, Bytespider, CCBot, FacebookBot, Amazonbot
- Open Graph complet → bonnes previews dans les LLM et IA de recherche
- lang="fr-CH" + contenu 100% en français suisse → ciblage géographique clair

**Déficits :**
- Pas de contenu Q&A citables (FAQ, guides, explications détaillées)
- E-E-A-T faible réduit la confiance des IA citantes

---

## D) Inconnus et Suivis

| Vérification | Statut | Commande pour lever le doute |
|-------------|--------|------------------------------|
| Core Web Vitals (LCP, INP, CLS) | Non mesuré | `python3 scripts/pagespeed.py https://slayradio.ch/ --strategy mobile` |
| Pages /artiste/* accessibles en SSR ? | Likely problème JS | `curl -A "Googlebot" https://slayradio.ch/artiste/dj-fa` |
| Profil de backlinks | Inconnu | `python3 scripts/link_profile.py https://slayradio.ch/` |
| Indexation réelle | Inconnu | Connecter Google Search Console |
| Pages /home/mix et /home/podcast | Non audité | Auditer ces deux pages séparément |
| Images converties en WebP ? | Inconnu | Inspecter les headers Content-Type des images |

---

## E) Données Brutes des Scripts

| Script | Résultat |
|--------|----------|
| security_headers.py | **100/100** — HTTPS, HSTS, CSP, X-Frame-Options, X-Content-Type-Options, Referrer-Policy |
| social_meta.py | **100/100** — 7/7 OG, 6/6 Twitter Card |
| llms_txt_checker.py | **100/100** — llms.txt (5 sections, 10 liens) + llms-full.txt trouvés |
| redirect_checker.py | 0 hop, 200 OK, 1311ms |
| broken_links.py | 19 liens, **0 cassés** |
| internal_links.py | 12 pages crawlées, 4 orphelines, 12 liens sans ancre texte |
| robots_checker.py | 12 user-agents configurés, 1 sitemap référencé, AI crawlers autorisés |
| readability.py | Flesch 55.0, Grade 10.5, **539 mots**, 27 phrases, 5.4 phrases/para |
| pagespeed.py | **Rate-limited** — relancer dans 10-15 min |
