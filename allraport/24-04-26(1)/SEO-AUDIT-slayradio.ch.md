# Audit SEO — slayradio.ch
**Date :** 24 avril 2026  
**Auditeur :** Claude (Anthropic)  
**URL cible :** https://slayradio.ch/  
**Secteur :** Web radio / Streaming musical / Suisse Romande

---

## RÉSUMÉ EXÉCUTIF

Slay Radio est une web radio suisse émergente diffusant House, Afrobeat et R&B 24h/24. Le site est récent, bien structuré au niveau du contenu, mais présente **des lacunes techniques critiques** qui empêchent actuellement une indexation et un référencement efficaces sur Google. Le problème le plus urgent : **le site ne semble pas être indexé par Google** (`site:slayradio.ch` renvoie zéro résultat).

### Score global estimé : 38 / 100

| Catégorie | Score | Statut |
|-----------|-------|--------|
| Balises Meta (title, description, OG) | 6/20 | Critique |
| Contenu & mots-clés | 12/20 | Moyen |
| Structure technique | 8/20 | Critique |
| Indexation & Crawl | 5/15 | Critique |
| Autorité & backlinks | 2/15 | Critique |
| UX & Signaux sociaux | 5/10 | Moyen |

---

## 1. INDEXATION & CRAWLABILITÉ

### Résultats

| Élément | État | Détail |
|---------|------|--------|
| Indexation Google | CRITIQUE | `site:slayradio.ch` = 0 résultat |
| robots.txt | OK | Présent, bien configuré |
| Sitemap.xml | OK | Présent avec 2 sous-sitemaps |
| Sous-sitemap statique | OK | 4 URLs (/, /home/evenement, /apropos, /radio-web-suisse) |
| Sous-sitemap événements | OK | 17 URLs (/client/evenement/{id}) |
| Canonical tag | MANQUANT | Absent sur toutes les pages |
| Hreflang | N/A | Site monolangue (FR) — non requis |

### Problèmes identifiés

**P1 – Site non indexé (CRITIQUE)**  
La recherche `site:slayradio.ch` ne retourne aucun résultat. Causes possibles :
- Le site est trop récent et n'a pas encore été crawlé
- Google Search Console n'est pas configuré
- Absence de backlinks entrants
- Possible blocage involontaire (à vérifier avec Google Search Console)

**P2 – URLs d'événements non descriptives**  
Les URLs utilisent des IDs numériques : `/client/evenement/3`, `/client/evenement/7`…  
Ces URLs sont **inutilisables pour le SEO** — Google ne peut pas associer le contenu à des mots-clés.

```
ACTUEL :  /client/evenement/3
DEVRAIT ÊTRE : /evenement/corbak-festival-neuchatel-2026
```

### Actions prioritaires

1. **Configurer Google Search Console** et soumettre le sitemap manuellement
2. **Modifier les URLs événements** vers des slugs lisibles (ex: `/evenement/corbak-festival-neuchatel`)
3. Vérifier qu'aucune règle dans robots.txt ne bloque involontairement des sections

---

## 2. BALISES META

### Titre (Title Tag)

| Page | Titre actuel | Longueur | Évaluation |
|------|-------------|----------|------------|
| Accueil | `Slay Radio \| Web Radio Suisse Romande — House, Afrobeat & R&B en Direct 24h/24` | ~79 car. | BON (légèrement long) |
| /radio-web-suisse | `Slay Radio — Radio web suisse en direct` | ~40 car. | MOYEN (trop court) |
| /apropos | `À propos de Slay Radio — Radio web suisse 100% musicale` | ~55 car. | BON |

Le title de la page d'accueil est excellent. Les autres pages sont moins optimisées.

### Meta Description — CRITIQUE

**Aucune meta description trouvée sur aucune page.**  
C'est un problème majeur : Google génère alors ses propres snippets, souvent peu attractifs, et le CTR dans les SERP est significativement réduit.

### Open Graph & Twitter Cards — CRITIQUE

**Aucune balise Open Graph ni Twitter Card détectée.**  
Conséquence : lorsqu'un lien vers le site est partagé sur Instagram, Facebook, WhatsApp, Discord, Twitter/X — **aucun aperçu visuel ne s'affiche**. L'impact sur le partage social est nul.

### Structured Data / Schema.org — CRITIQUE

**Aucun balisage Schema.org détecté.** Pour une web radio, les types suivants sont essentiels :

- `RadioStation` — pour la station elle-même
- `Event` — pour chaque événement musical (très bon pour apparaître dans les résultats enrichis Google)
- `MusicGroup` / `Person` — pour les artistes
- `BroadcastService` — pour le flux live

### Canonical Tag

**Absent sur toutes les pages.** Sans canonical, Google peut considérer plusieurs versions d'une même URL comme du contenu dupliqué.

### Balises à implémenter en priorité

```html
<!-- META DESCRIPTION (exemple page d'accueil) -->
<meta name="description" content="Slay Radio, la web radio suisse romande qui diffuse House, Afrobeat et R&B 24h/24. 100% gratuit, sans inscription. Découvrez nos artistes et événements locaux.">

<!-- CANONICAL -->
<link rel="canonical" href="https://slayradio.ch/">

<!-- OPEN GRAPH -->
<meta property="og:title" content="Slay Radio | Web Radio Suisse Romande — House, Afrobeat & R&B">
<meta property="og:description" content="Web radio suisse en direct 24h/24. House, Afrobeat, R&B. 100% gratuit.">
<meta property="og:image" content="https://slayradio.ch/image/og-cover.jpg">
<meta property="og:url" content="https://slayradio.ch/">
<meta property="og:type" content="website">
<meta property="og:locale" content="fr_CH">

<!-- TWITTER CARD -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Slay Radio | Web Radio Suisse Romande">
<meta name="twitter:description" content="Web radio suisse en direct 24h/24. House, Afrobeat, R&B. 100% gratuit.">
<meta name="twitter:image" content="https://slayradio.ch/image/og-cover.jpg">

<!-- SCHEMA.ORG RadioStation -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "RadioStation",
  "name": "Slay Radio",
  "url": "https://slayradio.ch",
  "description": "Web radio suisse romande diffusant House, Afrobeat et R&B 24h/24.",
  "broadcastFrequency": "Internet",
  "broadcastTimezone": "Europe/Zurich",
  "areaServed": {
    "@type": "Country",
    "name": "Switzerland"
  },
  "inLanguage": "fr",
  "sameAs": [
    "https://www.instagram.com/slayradio1/",
    "https://www.tiktok.com/@slayradio1",
    "https://www.youtube.com/channel/UCaD7SGkU6AI8liZdAKgm7nQ"
  ]
}
</script>
```

---

## 3. CONTENU & MOTS-CLÉS

### Structure des headings (balises H)

**Page d'accueil :**
```
H1 : Écoute la Web Radio Suisse Romande — House, Afrobeat & R&B 24h/24  ✅
  H2 : Événements musicaux en Suisse romande  ✅
    H3 : CORBAK FESTIVAL (Neuchâtel)  ✅
    H3 : BLUES RULES FESTIVAL (Crissier)  ✅
    H3 : FESTIBOC (Bofflens)  ✅
    H3 : FESTI'NEUCH (Neuchâtel)  ✅
  H2 : Une radio née d'une passion pour la scène locale  ✅
  H2 : Ta radio digitale, 100% gratuite, sans inscription  ✅
  H2 : Tous nos genres musicaux  ✅
    H3 : House / Afrobeat / R&B & Soul / Hip-Hop / Électronique  ✅
  H2 : Prêt à vivre l'expérience Slay Radio ?  ✅
```

La structure H1→H2→H3 est **logique et bien hiérarchisée**. C'est un point positif.

### Analyse des mots-clés cibles

| Mot-clé | Volume estimé (CH/FR) | Difficulté | Présence sur le site |
|---------|----------------------|------------|---------------------|
| web radio suisse romande | Moyen | Faible | ✅ H1, H2, title |
| radio en ligne suisse | Moyen | Faible | ✅ Page /radio-web-suisse |
| house music suisse | Faible | Très faible | ⚠️ Mentionné mais pas ciblé |
| afrobeat suisse | Très faible | Très faible | ⚠️ Mentionné |
| radio gratuite suisse | Faible | Faible | ⚠️ Mentionné |
| festival musique neuchâtel | Faible | Faible | ✅ Via événements |
| écouter radio en direct | Moyen | Moyen | ⚠️ Pas assez ciblé |
| podcast musique suisse | Faible | Faible | ❌ Page podcast non indexée |

### Lacunes de contenu identifiées

1. **Pages Artistes, Podcasts, Mix** — Présentes dans la navigation mais **absentes du sitemap**. Google ne les crawle probablement pas.
2. **Descriptions des artistes** — Chaque artiste devrait avoir une page dédiée avec biographie, genres, mixes → contenu indexable.
3. **Blog / Actualités** — Absent. Une section blog (actualités musicales suisses, portraits d'artistes, guide des festivals) renforcerait massivement l'autorité thématique.
4. **Pages événements non optimisées** — Les pages `/client/evenement/{id}` ont des URLs numériques sans SEO value.
5. **Contenu trop court sur /apropos** — Moins de 500 mots estimés, peu de valeur pour le référencement.

### Qualité du contenu existant

- La page `/radio-web-suisse` (~1200 mots) est un bon exemple de page SEO longue forme. **À dupliquer** pour d'autres mots-clés cibles.
- Le contenu est rédigé en français correct, sans fautes apparentes.
- Les termes locaux (Genève, Lausanne, Zurich, Neuchâtel) sont bien présents.

---

## 4. ASPECTS TECHNIQUES

### Attributs d'images

| Image | Alt text | Évaluation |
|-------|----------|------------|
| /image/logo.jpg | "Slay Radio — Web radio suisse" | ✅ BON |
| Image CORBAK FESTIVAL | "CORBAK FESTIVAL (Neuchâtel)" | ✅ BON |
| Image Unsplash (studio) | "Studio radio Slay Radio — web radio suisse" | ✅ BON |
| /image/social_media_instagram.png | "Instagram icon" | ⚠️ Générique |
| /image/social_media_tiktok.png | "TikTok icon" | ⚠️ Générique |

Les alt texts des images principales sont bons. Les icônes sociales pourraient être améliorées (ex: "Suivez Slay Radio sur Instagram").

### Performance & Core Web Vitals

Non mesurable directement depuis cet audit. Points à vérifier :
- **LCP (Largest Contentful Paint)** : L'image Unsplash externe (`images.unsplash.com`) peut ralentir le chargement. Recommandation : héberger les images localement.
- **Images** : Les noms de fichiers d'événements contiennent des captures d'écran avec des noms aléatoires (ex: `Capture-d-ecran-2026-04-17-094305-69e1e56d6d2ef.png`). Ces noms ne contribuent pas au SEO.

### Recommandations techniques prioritaires

```
1. Renommer les images événements avec des noms descriptifs
   AVANT : Capture-d-ecran-2026-04-17-094305-69e1e56d6d2ef.png
   APRÈS : corbak-festival-neuchatel-2026.jpg

2. Compresser et héberger l'image Unsplash localement
   (actuellement chargée depuis images.unsplash.com)

3. Vérifier HTTPS et les redirections 301

4. Vérifier la vitesse de chargement via PageSpeed Insights
   → https://pagespeed.web.dev/?url=https://slayradio.ch/

5. Vérifier la compatibilité mobile (responsive design)
```

### Analytics & Tracking

**Aucun script de tracking détecté** lors de l'analyse (malgré la présence d'une bannière de consentement cookies). À vérifier :
- Google Analytics 4 (GA4) configuré ?
- Google Search Console lié ?
- Un outil comme Plausible ou Matomo ?

Sans données analytics, il est **impossible de mesurer les performances SEO** et d'ajuster la stratégie.

---

## 5. AUTORITÉ & BACKLINKS

### Situation actuelle

- **Backlinks entrants** : Quasi-inexistants. Le site est nouveau et peu mentionné sur le web.
- **Mentions trouvées** : Aucune référence directe à slayradio.ch dans les résultats de recherche.
- **Profil de liens sortants** : Liens vers des festivals suisses reconnus (corbak.ch, blues-rules.com, festiboc.ch, festineuch.ch) — bon signal de pertinence locale.

### Stratégie de netlinking recommandée

**Court terme (0-3 mois) :**
1. **Annuaires de radios** : Soumettre sur RadioFrance, myTuner Radio, TuneIn, Streema, Radio.fr, radio-en-ligne.fr
2. **Annuaires suisses** : suisseromande.com, 2222.ch, répertoires locaux
3. **Partenariats festivals** : Demander un lien depuis corbak.ch, festineuch.ch, festiboc.ch (déjà partenaires → demander un lien retour)
4. **Instagram/TikTok vers le site** : S'assurer que la bio contient le lien slayradio.ch

**Moyen terme (3-6 mois) :**
5. **Presse locale** : Contacter 24 Heures, Le Temps, ArcInfo, La Région (Neuchâtel) pour des articles de présentation
6. **Blogs musique** : Collaborer avec des blogueurs musique francophones
7. **Podcasts & interviews** : Apparaître sur d'autres podcasts suisses romands

---

## 6. PRÉSENCE SOCIALE & E-E-A-T

### Réseaux sociaux

| Plateforme | Compte | Lien |
|-----------|--------|------|
| Instagram | @slayradio1 | instagram.com/slayradio1/ |
| TikTok | @slayradio1 | tiktok.com/@slayradio1 |
| YouTube | Canal Slay Radio | youtube.com/channel/UCaD7SGkU6AI8liZdAKgm7nQ |

La présence sur 3 plateformes est un bon point. S'assurer que **chaque profil social** contient le lien vers slayradio.ch en bio.

### E-E-A-T (Experience, Expertise, Authoritativeness, Trustworthiness)

Google évalue la crédibilité des sources. Points actuels :
- ✅ Contact email présent (contact@slayradio.ch)
- ✅ Mentions de la Suisse romande (ancrage géographique)
- ❌ Pas de page "Équipe" avec photos/noms des fondateurs
- ❌ Pas de CGU, politique de confidentialité visible
- ❌ Pas de mentions presse
- ❌ Pas de date de création affichée

---

## 7. PLAN D'ACTION PRIORISÉ

### Semaine 1 — URGENT (corrections critiques)

- [ ] **Configurer Google Search Console** et soumettre le sitemap
- [ ] **Ajouter les meta descriptions** sur toutes les pages (accueil, /radio-web-suisse, /apropos, chaque événement)
- [ ] **Ajouter les balises Open Graph** sur toutes les pages
- [ ] **Ajouter le canonical tag** sur toutes les pages
- [ ] **Implémenter Schema.org RadioStation** sur la page d'accueil

### Semaine 2-3 — IMPORTANT

- [ ] **Soumettre le site** sur TuneIn, myTuner, Streema, radio.fr, suisseromande.com
- [ ] **Renommer les images** d'événements avec des noms descriptifs
- [ ] **Ajouter les pages** Artistes, Podcasts, Mix au sitemap
- [ ] **Implémenter Schema.org Event** sur chaque page événement
- [ ] **Configurer GA4** pour le suivi analytics

### Mois 2 — DÉVELOPPEMENT

- [ ] **Migrer les URLs** d'événements vers des slugs lisibles
- [ ] **Créer une page par artiste** avec contenu optimisé (biographie, genres, mixes)
- [ ] **Lancer une section Blog/Actualités** (2 articles/mois minimum)
- [ ] **Demander des liens** aux festivals partenaires

### Mois 3-6 — CROISSANCE

- [ ] **Stratégie de contenu** : guides, portraits d'artistes, chroniques de festivals
- [ ] **Relations presse** : contacter médias suisses romands
- [ ] **Optimiser Core Web Vitals** via PageSpeed Insights
- [ ] **Créer une page par genre musical** (house-suisse, afrobeat-suisse, rnb-suisse)

---

## 8. OPPORTUNITÉS SPÉCIFIQUES

### Mots-clés longue traîne à cibler

```
- "radio en ligne gratuite suisse romande"
- "écouter musique house suisse"
- "web radio afrobeat suisse"
- "festival musique electronique neuchâtel 2026"
- "festival musique lausanne 2026"
- "artiste dj suisse romande"
- "podcast musique suisse gratuit"
```

### Pages SEO à créer

1. `/radio-house-suisse` — cibler "house music suisse"
2. `/radio-afrobeat-suisse` — cibler "afrobeat suisse"
3. `/artistes-dj-suisse-romande` — index des artistes
4. `/festivals-musique-suisse-romande-2026` — guide des festivals

### Quick wins

1. Soumettre sur **TuneIn Radio** (gratuit, fort trafic, backlink .com de qualité)
2. Créer une fiche **Google Business Profile** (si applicable) 
3. Partager chaque événement sur Google via le compte GSC
4. Optimiser la bio YouTube avec le lien slayradio.ch

---

## ANNEXES

### Sitemap actuel

```
sitemap.xml
├── sitemap.static.xml
│   ├── / (priority: 1.0, daily)
│   ├── /home/evenement (priority: 0.8, weekly)
│   ├── /apropos (priority: 0.5, monthly)
│   └── /radio-web-suisse (priority: 0.7, monthly)
└── sitemap.evenements.xml
    └── /client/evenement/3 à /client/evenement/19 (17 URLs, priority: 0.7, weekly)
```

**Pages absentes du sitemap :**
- /home/artiste
- /home/podcast
- /home/mix
- /boutique

### robots.txt (résumé)

```
Disallow: /admin/
Disallow: /login
Disallow: /register
Disallow: /panier/
Disallow: /commande/
Disallow: /detail_artiste/

Sitemap: https://slayradio.ch/sitemap.xml
```

Note : `/detail_artiste/` est bloqué dans robots.txt, ce qui signifie que les pages artistes **ne peuvent pas être indexées** par Google. Si ces pages existent et ont du contenu, il faut supprimer cette règle.

---

*Rapport généré le 24 avril 2026 — Audit SEO automatisé*
