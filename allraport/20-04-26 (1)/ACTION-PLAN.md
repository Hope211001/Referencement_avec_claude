# Plan d'Action SEO — slayradio.ch

**Date :** 2026-04-20
**Score actuel :** 61/100 (Needs Improvement)
**Objectif à 30 jours :** 75/100 (Good)
**Précédent score :** 41/100 (2026-04-17) — **+20 pts gagnés ✅**

---

## ✅ Corrections Précédentes Validées

| Action | Résultat | Score impact |
|--------|----------|-------------|
| Lorem Ipsum supprimé | ✅ Confirmé absent | +10 pts contenu |
| Contenu 234 → 534 mots | ✅ Confirmé | +8 pts contenu |
| llms.txt créé (95/100) | ✅ Confirmé | +5 pts GEO |
| Alt text images (9/9) | ✅ Confirmé | +5 pts images |

---

## Résumé Priorités Actuelles

Quatre actions bloquent la progression :
1. **Schema logo/Facebook** — invalide dans RadioStation → penalise Knowledge Panel
2. **H1 pollué** — CTAs fusionnés dans le H1, signal on-page dégradé
3. **llms-full.txt manquant** — catalogue IA incomplet
4. **x-default hreflang absent** — signal géographique incomplet

Corriger ces quatre points peut faire passer le score à **70-75/100 en 1 semaine**.

---

## Phase 1 — Corrections Immédiates (Jour 1-2)

### P1-1 🔴 Corriger le Schema RadioStation — Logo
**Impact : Critique | Effort : Très faible | Délai : Jour 1**

**Problème :** `logo` pointe vers `favicon.svg`. Google exige ≥ 112×112px pour le Knowledge Panel.

```json
// AVANT (incorrect) :
"logo": "https://slayradio.ch/favicon.svg"

// APRÈS (correct) :
"logo": {
  "@type": "ImageObject",
  "url": "https://slayradio.ch/image/og-default.png",
  "width": 1200,
  "height": 630
}
```

---

### P1-2 🔴 Corriger le Schema RadioStation — Facebook
**Impact : Critique | Effort : Très faible | Délai : Jour 1**

**Problème :** `sameAs` contient `https://www.facebook.com/` sans page officielle.

```json
// AVANT (incorrect) :
"sameAs": ["https://www.facebook.com/", ...]

// APRÈS (correct) :
"sameAs": ["https://www.facebook.com/[votre-handle-officiel]", ...]
```

---

### P1-3 🔴 Nettoyer le H1 Homepage
**Impact : Élevé | Effort : Très faible | Délai : Jour 1**

```
Actuel : "Slay Radio —ÉCOUTE • VIBERÉSERVE TON DJ PRÉFÉRÉ"
Recommandé : "Slay Radio — La Web Radio Suisse 100% Musicale"
```

Modifier le composant hero dans le CMS/template pour extraire les CTAs hors du `<h1>` :
```html
<h1>Slay Radio — La Web Radio Suisse 100% Musicale</h1>
<p>Écoute • Vibe</p>
<a href="/booking">Réserve ton DJ préféré</a>
```

---

### P1-4 ⚠️ Ajouter hreflang x-default
**Impact : Moyen | Effort : Très faible | Délai : Jour 1**

```html
<!-- Dans <head> de toutes les pages — ajouter après le tag fr-CH existant -->
<link rel="alternate" hreflang="x-default" href="https://slayradio.ch/" />
```

---

## Phase 2 — Quick Wins (Semaine 1)

### P2-1 ⚠️ Créer llms-full.txt
**Impact : Moyen (GEO/IA) | Effort : Très faible | Délai : Jour 2-3**

```txt
# Fichier à créer : /llms-full.txt

# Slay Radio — Catalogue Complet
> Radio web suisse 100% musicale et digitale

## DJs et Artistes
- [Nom DJ] — [genre musical] — https://slayradio.ch/home/artiste/[slug]
- (liste complète des DJs résidents)

## Mix et Sets
- [Titre Mix] par [DJ] — [genre] — https://slayradio.ch/home/mix/[slug]

## Podcasts et Émissions
- [Nom émission] — [description 1 phrase] — https://slayradio.ch/home/podcast/[slug]

## Événements
- [Nom événement] — [date] — [lieu] — https://slayradio.ch/client/evenement/[id]

## Boutique
- https://slayradio.ch/boutique
```

---

### P2-2 ⚠️ Supprimer le contenu étranger ("Blues Rules")
**Impact : Élevé | Effort : Faible | Délai : Semaine 1**

**Problème :** Un texte sur un festival de blues du North Mississippi a été détecté dans la page. Ce contenu n'a aucun rapport avec Slay Radio.

**Actions :**
1. Chercher "Blues Rules" dans le CMS ou les fichiers templates
2. Identifier la section concernée (podcast ? article partenaire ?)
3. Supprimer ou remplacer par du contenu pertinent à Slay Radio

---

### P2-3 ⚠️ Corriger les pages orphelines — Événements
**Impact : Moyen | Effort : Faible | Délai : Semaine 1**

4 pages d'événements avec 1 seul lien entrant :
- `/client/evenement/9`, `/5`, `/10`, `/16`

**Actions :**
1. Ajouter des liens vers ces événements depuis la homepage (section "Événements à venir")
2. Ajouter un lien dans le footer ou la navigation secondaire vers `/home/evenement`
3. Ajouter des ancres descriptives (pas de texte vide)

---

### P2-4 ⚠️ Corriger H2 "Evenement disponible"
**Impact : Faible | Effort : Très faible | Délai : Semaine 1**

```
Actuel    : "Evenement disponible" (faute, sans accent)
Recommandé : "Événements musicaux en Suisse romande"
```

---

### P2-5 ⚠️ Améliorer la lisibilité du contenu
**Impact : Moyen | Effort : Faible | Délai : Semaine 1-2**

```
Flesch actuel : 54.0 (objectif ≥ 60)
Grade actuel  : 10.6 (objectif ≤ 8)
```

**Actions :**
1. Scinder les paragraphes de + de 4 phrases
2. Raccourcir les phrases > 25 mots
3. Remplacer les termes complexes par des synonymes simples

---

## Phase 3 — Améliorations Stratégiques (Semaine 2 — Mois 2)

### P3-1 ⚠️ Schema Organization complet
**Impact : Élevé (E-E-A-T + Knowledge Panel) | Effort : Faible | Délai : Semaine 2**

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Slay Radio",
  "url": "https://slayradio.ch/",
  "logo": {
    "@type": "ImageObject",
    "url": "https://slayradio.ch/image/og-default.png",
    "width": 1200,
    "height": 630
  },
  "foundingDate": "[YYYY]",
  "address": {
    "@type": "PostalAddress",
    "addressCountry": "CH",
    "addressRegion": "Suisse romande"
  },
  "contactPoint": {
    "@type": "ContactPoint",
    "contactType": "customer service",
    "email": "[email@slayradio.ch]"
  },
  "sameAs": [
    "https://www.facebook.com/[handle]",
    "https://www.instagram.com/slayradio1/",
    "https://www.youtube.com/channel/UCaD7SGkU6AI8liZdAKgm7nQ",
    "https://www.tiktok.com/@slayradio1"
  ]
}
</script>
```

---

### P3-2 ⚠️ BreadcrumbList sur les sous-pages
**Impact : Moyen | Effort : Faible | Délai : Semaine 2**

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

### P3-3 ⚠️ Réduire le TTFB (1583ms → < 800ms)
**Impact : Moyen | Effort : Moyen | Délai : Mois 1**

```
Options (ordre recommandé) :
1. Activer Cloudflare (CDN gratuit, cache statique, TTFB < 200ms possible)
2. Vérifier que l'hébergeur est en Europe / Suisse
3. Activer la compression brotli/gzip côté serveur
4. Mettre en cache les réponses API dynamiques
```

---

### P3-4 ⚠️ Schema MusicEvent sur les pages événements
**Impact : Moyen (rich results) | Effort : Moyen | Délai : Mois 1**

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

### P3-5 ⚠️ E-E-A-T : Enrichir /apropos et pages artiste
**Impact : Très élevé (long terme) | Effort : Élevé | Délai : Mois 2**

```
1. Page /apropos → 600+ mots :
   - Date de fondation, noms des fondateurs
   - Mission, valeurs, engagement local
   - Mentions presse suisse si disponibles

2. Pages artiste → chaque DJ :
   - Bio 200+ mots
   - Photo professionnelle (alt text inclus)
   - Genres, influences, liens Mixcloud/SoundCloud
   - Schema MusicGroup ou Person

3. Mesurer CWV avec clé API :
   export PAGESPEED_API_KEY=votre_cle
   python3 scripts/pagespeed.py https://slayradio.ch/ --strategy mobile
```

---

## Tableau de Bord Priorités

| Priorité | Action | Impact | Effort | Délai |
|----------|--------|--------|--------|-------|
| 🔴 P1 | Schema logo (favicon → image OG) | Critique | Très faible | Jour 1 |
| 🔴 P1 | Schema Facebook URL générique | Élevé | Très faible | Jour 1 |
| 🔴 P1 | Nettoyer H1 (séparer CTAs) | Élevé | Très faible | Jour 1 |
| ⚠️ P1 | Hreflang x-default | Moyen | Très faible | Jour 1 |
| ⚠️ P2 | Créer llms-full.txt | Moyen (GEO) | Très faible | Jour 2-3 |
| ⚠️ P2 | Supprimer contenu étranger (Blues Rules) | Élevé | Faible | Semaine 1 |
| ⚠️ P2 | Lier pages orphelines événements | Moyen | Faible | Semaine 1 |
| ⚠️ P2 | Corriger H2 "Evenement disponible" | Faible | Très faible | Semaine 1 |
| ⚠️ P2 | Améliorer lisibilité (Flesch 54 → 60+) | Moyen | Faible | Semaine 1-2 |
| ⚠️ P3 | Schema Organization complet | Élevé | Faible | Semaine 2 |
| ⚠️ P3 | BreadcrumbList sous-pages | Moyen | Faible | Semaine 2 |
| ⚠️ P3 | TTFB < 800ms (CDN/cache) | Moyen | Moyen | Mois 1 |
| ⚠️ P3 | Schema MusicEvent (événements) | Moyen | Moyen | Mois 1 |
| ⚠️ P3 | E-E-A-T : biographies + /apropos | Très élevé | Élevé | Mois 2 |

---

## Score Projeté après Phase 1+2

| Catégorie | Score actuel | Après P1+P2 | Gain estimé |
|-----------|-------------|-------------|-------------|
| Technique SEO | 75 | 80 | +5 |
| Qualité Contenu | 55 | 68 | +13 |
| On-Page SEO | 55 | 70 | +15 |
| Schema | 45 | 65 | +20 |
| Performance CWV | 40* | 40* | = |
| Images | 85 | 85 | = |
| Préparation IA | 75 | 85 | +10 |
| **Score Global** | **61** | **~74** | **+13** |

*Données CWV insuffisantes sans clé API PageSpeed

---

## Commandes de Vérification Post-Fix

```bash
cd d:\Fanantenana\SEO\Agentic-SEO-Skill-main
export PYTHONIOENCODING=utf-8

# Re-tester le schema après corrections
python3 scripts/fetch_page.py https://slayradio.ch/ --output page_v3.html
python3 scripts/validate_schema.py page_v3.html

# Re-tester hreflang
python3 scripts/hreflang_checker.py https://slayradio.ch/

# Vérifier llms-full.txt
python3 scripts/llms_txt_checker.py https://slayradio.ch/

# Mesurer CWV (avec clé API)
# export PAGESPEED_API_KEY=votre_cle
python3 scripts/pagespeed.py https://slayradio.ch/ --strategy mobile
python3 scripts/pagespeed.py https://slayradio.ch/ --strategy desktop

# Re-audit complet
python3 scripts/generate_report.py https://slayradio.ch/ --output SEO-REPORT-V3.html
```

---

*Plan généré par Agentic SEO Skill v1 — 2026-04-20*
