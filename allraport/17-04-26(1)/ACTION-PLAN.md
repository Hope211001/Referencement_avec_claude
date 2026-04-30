# Plan d'Action SEO — slayradio.ch

**Date :** 2026-04-17
**Score actuel :** 41/100 (Mauvais)
**Objectif à 30 jours :** 65/100 (Needs Improvement → Good)

---

## Résumé Priorités

Trois actions bloquent la progression immédiate :
1. **Lorem Ipsum** — Contenu fictif visible sur la homepage → pénalité de contenu garantie
2. **H1 non optimisé** — Premier signal on-page pour Google, actuellement en anglais sans mot-clé
3. **Thin content** — 234 mots vs minimum 500 → pages jugées trop légères

Corriger ces trois points + améliorer le schema peut faire passer le score à **65-70/100 en 2 semaines**.

---

## Phase 1 — Corrections Immédiates (Jour 1-3)

### P1-1 🔴 Supprimer le Lorem Ipsum
**Impact : Critique | Effort : Très faible | Type : Blocage immédiat**

**Problème :** Texte Lorem Ipsum détecté sur la homepage dans une section du site. Google peut pénaliser les pages avec du contenu de remplacement non publié.

```
Texte détecté : "Lorem Ipsum is simply dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s..."

Localisation : Section à identifier dans le CMS/code source
```

**Actions :**
1. Identifier la section dans le CMS ou le code source (chercher "Lorem Ipsum" dans les fichiers templates)
2. Remplacer par un contenu éditorial réel décrivant Slay Radio
3. Republier la page et vérifier avec `curl https://slayradio.ch/ | grep -i "lorem"`

**Exemple de remplacement (100 mots) :**
```
Slay Radio est la première radio web suisse 100% digitale, dédiée aux DJs et artistes émergents
de la scène musicale helvétique. Depuis notre lancement, nous diffusons en continu des mix live,
des podcasts exclusifs et des sets House, Afrobeat, R&B et Hip-Hop sélectionnés par nos DJs résidents.
Notre mission : donner une voix aux talents musicaux suisses et créer un espace de découverte unique
pour les passionnés de musique électronique. Rejoignez notre communauté et vivez l'expérience Slay Radio.
```

---

### P1-2 🔴 Corriger le H1 homepage
**Impact : Élevé | Effort : Très faible | Type : Quick win**

```
Actuel    : "Listen • VibesBook Your Favorite DJ"
Recommandé : "Slay Radio — La Radio Web Suisse 100% Musicale"
```

Modifier le fichier template de la homepage (chercher `<h1>` dans le composant hero).

---

### P1-3 ⚠️ Corriger le schema RadioStation
**Impact : Moyen | Effort : Très faible | Type : Quick win**

**A. Corriger l'URL Facebook (sameAs) :**
```json
// Actuel (incorrect) :
"sameAs": ["https://www.facebook.com/", ...]

// Recommandé :
"sameAs": ["https://www.facebook.com/[votre-page-fb-officielle]", ...]
```

**B. Corriger le logo (trop petit — favicon) :**
```json
// Actuel :
"logo": "https://slayradio.ch/favicon.svg"

// Recommandé :
"logo": {
  "@type": "ImageObject",
  "url": "https://slayradio.ch/image/og-default.png",
  "width": 1200,
  "height": 630
}
```

---

## Phase 2 — Quick Wins (Semaine 1-2)

### P2-1 ⚠️ Enrichir le contenu homepage (234 → 500+ mots)
**Impact : Élevé | Effort : Faible | Type : Quick win**

**Structure recommandée pour atteindre 500 mots :**

```markdown
## Sections à ajouter / enrichir :

1. Hero — Proposition de valeur (~80 mots)
   "La première radio web suisse dédiée aux DJs émergents.
    Genres : House, Afrobeat, R&B, Hip-Hop, Dancehall."

2. "Notre Mission" (~100 mots)
   - Pourquoi Slay Radio existe
   - Engagement envers les artistes suisses locaux

3. "DJs à l'affiche" (~80 mots)
   - 3-4 DJs mis en avant avec courtes descriptions
   - Liens vers leurs pages artiste

4. "Émissions du moment" (~80 mots)
   - Mix récents, podcasts, lives planifiés

5. "Événements à venir" (~80 mots)
   - 2-3 prochains événements avec dates et lieux

6. "Rejoignez Slay Radio" (~80 mots)
   - CTA newsletter, réseaux sociaux, candidature DJ
```

**Objectif :** 500+ mots, Flesch > 60, grade level ≤ 8

---

### P2-2 ⚠️ Ajouter BreadcrumbList sur les sous-pages
**Impact : Moyen | Effort : Faible | Type : Quick win**

```html
<!-- Exemple pour /home/artiste -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Accueil", "item": "https://slayradio.ch"},
    {"@type": "ListItem", "position": 2, "name": "Artistes", "item": "https://slayradio.ch/home/artiste"}
  ]
}
</script>
```

---

### P2-3 ⚠️ Créer llms-full.txt
**Impact : Faible-Moyen (GEO) | Effort : Très faible | Type : Maintenance**

```txt
# Fichier à créer : /llms-full.txt

# Slay Radio — Catalogue Complet
> Radio web suisse 100% musicale et digitale

## DJs et Artistes
- [Nom DJ] — [genre musical] — https://slayradio.ch/home/artiste/[slug]
- [...]

## Mix et Sets
- [Titre Mix] par [DJ] — [genre] — [durée] — https://slayradio.ch/home/mix/[slug]
- [...]

## Podcasts et Émissions
- [Nom émission] — [description 1 phrase] — https://slayradio.ch/home/podcast/[slug]

## Événements
- [Nom événement] — [date] — [lieu] — https://slayradio.ch/home/evenement/[slug]

## Boutique
- https://slayradio.ch/boutique
```

---

### P2-4 ⚠️ Corriger les pages orphelines
**Impact : Moyen | Effort : Faible | Type : Quick win**

Ajouter des liens supplémentaires vers ces pages depuis la navigation ou le contenu contextuel :
- `/home/decouverte` — 1 seul lien entrant → ajouter dans homepage et /home/artiste
- `/home/evenement` — 1 seul lien entrant → ajouter dans homepage et footer

---

## Phase 3 — Améliorations Stratégiques (Semaine 3 — Mois 2)

### P3-1 ⚠️ E-E-A-T : Construire l'autorité
**Impact : Très élevé (long terme) | Effort : Élevé | Type : Strategic**

```
1. Page /apropos → enrichir à 600+ mots :
   - Date de fondation exacte
   - Noms des fondateurs et membres de l'équipe avec photos
   - Mission détaillée et valeurs
   - Mentions presse / médias suisses si disponibles

2. Pages artiste → chaque DJ doit avoir :
   - Bio 200+ mots
   - Photo professionnelle avec alt text
   - Genres, influences, liens Mixcloud/SoundCloud
   - Schema MusicGroup/Person

3. Ajouter schema Organization complet :
   - address (adresse suisse)
   - foundingDate
   - contactPoint avec email
```

---

### P3-2 ⚠️ Réduire le TTFB (1384ms → < 800ms)
**Impact : Moyen | Effort : Moyen | Type : Strategic**

```
Options (ordre recommandé) :
1. Activer Cloudflare (CDN + cache statique) — solution la plus rapide
2. Vérifier hébergement : serveur en Europe/Suisse ?
3. Activer compression gzip/brotli côté serveur
4. Mettre en cache les réponses API (si applicable)
```

---

### P3-3 ⚠️ Schema MusicEvent pour les événements
**Impact : Moyen (rich results) | Effort : Moyen | Type : Strategic**

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "MusicEvent",
  "name": "[Nom de l'événement]",
  "startDate": "[YYYY-MM-DDTHH:MM:SS+01:00]",
  "location": {
    "@type": "Place",
    "name": "[Lieu]",
    "address": { "@type": "PostalAddress", "addressCountry": "CH" }
  },
  "performer": { "@type": "MusicGroup", "name": "[DJ]" },
  "organizer": { "@type": "Organization", "name": "Slay Radio", "url": "https://slayradio.ch" }
}
</script>
```

---

### P3-4 ℹ️ Hreflang fr-CH
**Impact : Moyen (marché suisse francophone) | Effort : Faible | Type : Maintenance**

```html
<!-- Dans <head> de toutes les pages -->
<link rel="alternate" hreflang="fr-CH" href="https://slayradio.ch[/path]" />
<link rel="alternate" hreflang="x-default" href="https://slayradio.ch[/path]" />
```

---

## Tableau de Bord Priorités

| Priorité | Action | Impact | Effort | Délai cible |
|---|---|---|---|---|
| 🔴 P1 | Supprimer Lorem Ipsum | Critique | Très faible | Jour 1 |
| 🔴 P1 | Corriger H1 homepage | Élevé | Très faible | Jour 1 |
| 🔴 P1 | Corriger schema (Facebook URL + logo) | Moyen | Très faible | Jour 1-2 |
| ⚠️ P2 | Enrichir homepage (234 → 500+ mots) | Élevé | Faible | Semaine 1 |
| ⚠️ P2 | Ajouter BreadcrumbList sous-pages | Moyen | Faible | Semaine 1 |
| ⚠️ P2 | Créer llms-full.txt | Moyen (GEO) | Très faible | Semaine 1 |
| ⚠️ P2 | Corriger pages orphelines (liens internes) | Moyen | Faible | Semaine 2 |
| ⚠️ P3 | E-E-A-T : biographies équipe + artistes | Très élevé | Élevé | Mois 2 |
| ⚠️ P3 | TTFB < 800ms (CDN/cache) | Moyen | Moyen | Mois 2 |
| ⚠️ P3 | Schema MusicEvent (événements) | Moyen | Moyen | Mois 2 |
| ℹ️ P3 | Hreflang fr-CH | Moyen | Faible | Mois 2 |
| ℹ️ P3 | Mesurer CWV (clé API PSI) | Info | Très faible | Semaine 1 |

---

## Score Projeté après Phase 1+2

| Catégorie | Score actuel | Après P1+P2 | Gain estimé |
|---|---|---|---|
| Technique SEO | 61 | 65 | +4 |
| Qualité Contenu | 3 | 50 | +47 |
| On-Page SEO | 25 | 60 | +35 |
| Schema | 35 | 60 | +25 |
| Performance CWV | 50* | 50* | = |
| Images | 80 | 80 | = |
| Préparation IA | 70 | 78 | +8 |
| **Score Global** | **41** | **~64** | **+23** |

*Données insuffisantes

---

## Commandes de Vérification Post-Fix

```bash
# Re-tester après corrections (depuis d:\Fanantenana\SEO\Agentic-SEO-Skill-main)
export PYTHONIOENCODING=utf-8

# Vérifier contenu (Lorem Ipsum supprimé ?)
python3 scripts/fetch_page.py https://slayradio.ch/ --output /tmp/page_v2.html
python3 scripts/readability.py /tmp/page_v2.html --json

# Re-tester schema
python3 scripts/validate_schema.py /tmp/page_v2.html

# Re-tester social meta
python3 scripts/social_meta.py https://slayradio.ch/

# Mesurer CWV (avec clé API si disponible)
# export PAGESPEED_API_KEY=votre_cle
python3 scripts/pagespeed.py https://slayradio.ch/ --strategy mobile
python3 scripts/pagespeed.py https://slayradio.ch/ --strategy desktop

# Re-audit complet
python3 scripts/generate_report.py https://slayradio.ch/ --output SEO-REPORT-V2.html
```

---

*Plan généré par Agentic SEO Skill v1 — 2026-04-17*
