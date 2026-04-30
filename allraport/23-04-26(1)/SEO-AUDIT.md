# Audit SEO — slayradio.ch
**Date :** 2026-04-23  
**Méthode :** WebFetch live (homepage, sitemap, robots, 8 pages internes)  
**Score estimé actuel :** 51/100  
**Score précédent (22-04-26) :** 49/100  
**Progression :** +2 pts (footer copyright corrigé + titles améliorés)

---

## 1. État par page

### Homepage — slayradio.ch/
| Élément | État | Valeur |
|---|---|---|
| Title | ✅ Bon | "Slay Radio \| Web Radio Suisse Romande — House, Afrobeat & R&B en Direct 24h/24" |
| Meta description | ❌ Absente | — |
| Canonical | ❌ Absent | — |
| Open Graph | ❌ Absent | — |
| Twitter Cards | ❌ Absent | — |
| JSON-LD | ❌ Absent | — |
| H1 | ✅ Bon | "Écoute la Web Radio Suisse Romande — House, Afrobeat & R&B 24h/24" |
| Images lazy loading | ❌ Absent | Aucun `loading="lazy"` |
| Images dimensions | ❌ Absent | Aucun width/height |
| Footer copyright | ✅ Corrigé | © 2026 Slay Radio |

### /home/artiste
| Élément | État | Valeur |
|---|---|---|
| Title | ✅ Bon | "Artistes & DJs suisses — Slay Radio Suisse" |
| Meta description | ❌ Absente | — |
| Canonical | ❌ Absent | — |
| JSON-LD | ❌ Absent | — |
| Contenu | ❌ Thin content | "De nouveaux artistes rejoignent bientôt la famille" |

### /home/podcast
| Élément | État | Valeur |
|---|---|---|
| Title | ✅ Bon | "Podcasts musicaux suisses — Émissions exclusives de DJs — Slay Radio" |
| Meta description | ❌ Absente | — |
| Canonical | ❌ Absent | — |
| JSON-LD | ❌ Absent | — |
| Contenu | ❌ Page vide | "De nouveaux podcasts arrivent bientôt" |

### /home/mix
| Élément | État | Valeur |
|---|---|---|
| Title | ✅ Bon | "Mix & Sets DJ suisses — House, Afrobeat, R&B — Slay Radio" |
| Meta description | ❌ Absente | — |
| Canonical | ❌ Absent | — |
| JSON-LD | ❌ Absent | — |
| Contenu | ❌ Page vide | "Les mixs arrivent bientôt" |

### /boutique
| Élément | État | Valeur |
|---|---|---|
| Title | ⚠️ Faible | "Boutique — Slay Radio" (trop court, pas de mots-clés) |
| Meta description | ❌ Absente | — |
| Canonical | ❌ Absent | — |
| JSON-LD | ❌ Absent | — |
| Contenu | ❌ Page vide | "De nouveaux produits arrivent bientôt" |

### /radio-web-suisse
| Élément | État | Valeur |
|---|---|---|
| Title | ⚠️ Faible | "Slay Radio — Radio web suisse en direct" (générique) |
| Meta description | ❌ Absente | — |
| Canonical | ❌ Absent | — |
| JSON-LD | ❌ Absent | — |
| Contenu | ✅ Bon | ~650-700 mots bien ciblés |

### /apropos
| Élément | État | Valeur |
|---|---|---|
| Title | ✅ Bon | "À propos de Slay Radio — Radio web suisse 100% musicale" |
| Meta description | ❌ Absente | — |
| Canonical | ❌ Absent | — |
| JSON-LD | ❌ Absent | — |
| Contenu | ⚠️ Maigre | 400-450 mots, 0 membre d'équipe, 0 statistique |

### /client/evenement/3 (CORBAK FESTIVAL)
| Élément | État | Valeur |
|---|---|---|
| Title | ✅ Bon | "CORBAK FESTIVAL (Neuchâtel) — Événement Slay Radio" |
| Meta description | ❌ Absente | — |
| Canonical | ❌ Absent | — |
| JSON-LD MusicEvent | ❌ Absent | — |
| Open Graph | ❌ Absent | — |
| Image alt | ✅ Présent | "CORBAK FESTIVAL (Neuchâtel)" |
| Image loading | ❌ Absent | Pas de lazy loading |
| Image dimensions | ❌ Absent | Pas de width/height |
| Image nom | ❌ Non-SEO | Capture-d-ecran-2026-04-17-094305-... |

---

## 2. Sitemap

### sitemap.static.xml — 4 pages indexées
| URL | lastmod | Priority |
|---|---|---|
| / | 2026-04-21 | 1.0 |
| /home/evenement | 2026-04-21 | 0.8 |
| /apropos | 2026-04-21 | 0.5 |
| /radio-web-suisse | 2026-04-21 | 0.7 |

**Manquants :** /home/artiste, /home/podcast, /home/mix, /boutique

### sitemap.evenements.xml — 17 événements
URLs au format `/client/evenement/[ID]` — toutes avec priority 0.7, weekly.

---

## 3. Robots.txt ✅
- Bloque : /admin/, /login, /register, /panier/, /commande/, /detail_artiste/
- Autorise : GPTBot, ClaudeBot, PerplexityBot, Bytespider et autres AI crawlers
- Sitemap référencé correctement

---

## 4. Récapitulatif des problèmes

| # | Problème | Criticité | Pages concernées |
|---|---|---|---|
| 1 | Zéro meta description | 🔴 Critique | Toutes (8/8 pages) |
| 2 | Zéro canonical | 🔴 Critique | Toutes (8/8 pages) |
| 3 | Zéro JSON-LD / Schema | 🔴 Critique | Toutes (8/8 pages) |
| 4 | Zéro Open Graph | 🔴 Critique | Toutes (8/8 pages) |
| 5 | Zéro lazy loading images | 🔴 Critique | Toutes |
| 6 | Zéro dimensions images | 🔴 Critique | Toutes |
| 7 | 4 pages thin/vide indexées | 🔴 Critique | artiste, podcast, mix, boutique |
| 8 | Sitemap incomplet (-4 pages) | ⚠️ High | sitemap.static.xml |
| 9 | URLs événements opaques | ⚠️ High | 17 événements |
| 10 | Images nommées "Capture-d-ecran-..." | ⚠️ Medium | événements |
| 11 | /boutique title trop court | ⚠️ Medium | boutique |
| 12 | /radio-web-suisse title générique | ⚠️ Low | radio-web-suisse |
| 13 | /apropos sans équipe ni stats | ⚠️ Low | apropos |
| 14 | llms.txt encoding UTF-8 | ⚠️ Low | llms.txt |

---

## 5. Ce qui fonctionne bien ✅

- Titles sur 6/8 pages bien optimisés
- H1 bien ciblé sur toutes les pages
- Sitemap index → 2 sitemaps enfants (structure correcte)
- robots.txt bien configuré avec AI crawlers
- 17 événements indexés
- /radio-web-suisse : bon contenu (~700 mots)
- Footer © 2026 (corrigé)
- Breadcrumbs sur les pages événements
