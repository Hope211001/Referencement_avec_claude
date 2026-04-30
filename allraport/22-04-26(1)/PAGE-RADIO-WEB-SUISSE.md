# Brief Page — /radio-web-suisse

**Date :** 2026-04-21  
**URL cible :** https://slayradio.ch/radio-web-suisse  
**Mot-clé principal :** radio web suisse / web radio suisse  
**Objectif :** Page de destination SEO visible + utile, intégrée dans la navigation

---

## 1. Positionnement dans la navigation

### Menu principal (à modifier)

**Avant :**
```
Accueil | Artistes | Podcasts | Mix | Boutique | Événements | À propos | Mon Panier
```

**Après (option recommandée — ajout dans menu) :**
```
Accueil | Écouter | Artistes | Podcasts | Mix | Boutique | Événements | À propos | Mon Panier
```
→ Le mot "Écouter" pointe vers `/radio-web-suisse`

**Alternative (sous-menu déroulant) :**
```
Accueil | Découvrir ▾ | Artistes | Podcasts | Mix | ...
                └── Radio web suisse
                └── Nos genres musicaux
```

### Footer (à enrichir)

**Ajouter dans le footer :**
```
Accueil | Radio web suisse | Mix | Artistes | Podcasts | À propos | Événements
```

### Maillage depuis la homepage

Dans l'intro de la homepage, ajouter ce lien :
```html
Découvrez notre <a href="/radio-web-suisse">radio web suisse</a> dédiée aux DJs 
et à la scène musicale romande.
```

Dans la section "Notre histoire" :
```html
Slay Radio est une <a href="/radio-web-suisse">radio web suisse</a> née d'une passion 
pour la scène locale — house, afrobeat, R&B depuis la Suisse romande.
```

---

## 2. Structure de la page `/radio-web-suisse`

### Métadonnées

```html
<title>Radio Web Suisse en Direct — Écoute Slay Radio 24h/24 | House, Afrobeat, R&B</title>

<meta name="description" content="Slay Radio est une radio web suisse 100% musicale, 
diffusée en ligne 24h/24 depuis la Suisse romande. Écoute gratuitement de la house, 
de l'afrobeat et du R&B — sans inscription.">

<link rel="canonical" href="https://slayradio.ch/radio-web-suisse">
```

### Balise Open Graph

```html
<meta property="og:title" content="Radio Web Suisse en Direct — Slay Radio">
<meta property="og:description" content="Écoute la radio web suisse 24h/24 : house, afrobeat, R&B depuis la Suisse romande. Gratuit, sans inscription.">
<meta property="og:url" content="https://slayradio.ch/radio-web-suisse">
<meta property="og:type" content="website">
<meta property="og:image" content="https://slayradio.ch/image/slay-radio-web-suisse.jpg">
```

---

## 3. Structure HTML de la page (squelette)

```html
<!-- SECTION 1 — Hero / Player -->
<section class="hero">
  <h1>La Radio Web Suisse 100% Musicale — En Direct 24h/24</h1>
  <p>
    Écoute Slay Radio, ta radio web suisse indépendante depuis la Suisse romande. 
    House, afrobeat, R&B — en direct, gratuit, sans inscription.
  </p>
  <!-- Player audio ici -->
  <button>▶ Écouter maintenant</button>
</section>

<!-- SECTION 2 — Qu'est-ce qu'une radio web suisse ? -->
<section>
  <h2>Qu'est-ce qu'une radio web suisse ?</h2>
  <p>
    Une radio web suisse est une station de radio diffusée exclusivement en ligne, 
    accessible depuis n'importe quel appareil connecté à internet. 
    Contrairement aux radios FM traditionnelles, elle ne nécessite ni antenne ni abonnement.
  </p>
  <p>
    Slay Radio est l'une des rares radio web suisse romande 100% indépendante, 
    dédiée à la house, l'afrobeat et le R&B. 
    Nos DJs diffusent en direct depuis la Suisse, 24h sur 24, 7j sur 7.
  </p>
</section>

<!-- SECTION 3 — Pourquoi choisir Slay Radio -->
<section>
  <h2>Pourquoi écouter Slay Radio, ta radio web suisse ?</h2>
  <ul>
    <li>
      <strong>100% gratuite</strong> — Aucun abonnement, aucune inscription requise
    </li>
    <li>
      <strong>En direct 24h/24</strong> — Diffusion continue sans interruption
    </li>
    <li>
      <strong>Indépendante et locale</strong> — Née en Suisse romande, pour la scène romande
    </li>
    <li>
      <strong>Genres variés</strong> — House, afrobeat, R&B et plus encore
    </li>
    <li>
      <strong>DJs locaux</strong> — Découvrez des artistes suisses talentueux
    </li>
  </ul>
</section>

<!-- SECTION 4 — Nos genres musicaux -->
<section>
  <h2>Les genres de notre radio web suisse</h2>

  <article>
    <h3>House</h3>
    <p>
      De la house profonde à l'afro house en passant par la tech house, 
      nos DJs suisses mixent les meilleurs sons du moment. 
      Une radio web suisse qui fait vivre la scène house européenne depuis Genève et Lausanne.
    </p>
  </article>

  <article>
    <h3>Afrobeat & Afrobeats</h3>
    <p>
      Rythmes africains, sons urban et tropical : l'afrobeat prend une place unique 
      sur notre antenne. Une radio web suisse ouverte sur le monde, 
      qui célèbre la diversité musicale de la Suisse romande.
    </p>
  </article>

  <article>
    <h3>R&B & Soul</h3>
    <p>
      Voix, émotion et groove — le R&B a toujours sa place sur Slay Radio. 
      Notre radio web suisse diffuse les classiques et les nouveautés R&B, 
      soul et urban 24h/24.
    </p>
  </article>
</section>

<!-- SECTION 5 — Comment écouter -->
<section>
  <h2>Comment écouter notre radio web suisse ?</h2>
  <ol>
    <li>Clique sur le bouton <strong>"Écouter maintenant"</strong> ci-dessus</li>
    <li>Le player démarre instantanément — aucun téléchargement nécessaire</li>
    <li>Écoute depuis ton téléphone, ta tablette ou ton ordinateur</li>
    <li>Compatible avec tous les navigateurs modernes</li>
  </ol>
  <p>
    Notre radio web suisse fonctionne partout en Suisse et dans le monde entier, 
    24h/24, 7j/7.
  </p>
</section>

<!-- SECTION 6 — CTA Artistes / Mix / Podcasts -->
<section>
  <h2>Explore tout le contenu de ta radio web suisse</h2>
  <div class="cards">
    <a href="/home/artiste">
      <h3>Nos DJs suisses</h3>
      <p>Découvrez les artistes de Slay Radio et réservez un DJ pour votre événement.</p>
    </a>
    <a href="/home/mix">
      <h3>Mix & DJ Sets</h3>
      <p>Replay des meilleurs mix de notre radio web suisse — disponibles à tout moment.</p>
    </a>
    <a href="/home/podcast">
      <h3>Podcasts musicaux</h3>
      <p>Émissions et podcasts de Slay Radio, en replay 24h/24.</p>
    </a>
  </div>
</section>

<!-- SECTION 7 — JSON-LD Schema -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "RadioStation",
  "name": "Slay Radio",
  "description": "Radio web suisse 100% musicale, diffusée en ligne 24h/24 depuis la Suisse romande. House, afrobeat, R&B — gratuit et sans inscription.",
  "url": "https://slayradio.ch/radio-web-suisse",
  "broadcastFrequency": "Online",
  "broadcastTimezone": "Europe/Zurich",
  "genre": ["House", "Afrobeat", "R&B"],
  "areaServed": {
    "@type": "Place",
    "name": "Suisse romande",
    "address": {
      "@type": "PostalAddress",
      "addressCountry": "CH"
    }
  },
  "potentialAction": {
    "@type": "ListenAction",
    "target": "https://slayradio.ch/radio-web-suisse"
  }
}
</script>
```

---

## 4. Contenu textuel final optimisé (prêt à copier-coller)

### H1
```
La Radio Web Suisse 100% Musicale — En Direct 24h/24
```

### Paragraphe d'introduction (zone critique SEO — 150 premiers mots)
```
Écoute Slay Radio, ta radio web suisse indépendante depuis la Suisse romande. 
House, afrobeat, R&B — en direct, gratuit, sans inscription. 
Diffusée 24h/24 depuis la Suisse, notre radio web suisse est accessible 
depuis n'importe quel appareil connecté, sans téléchargement ni abonnement.

Découvrez les mix exclusifs de nos DJs suisses, plongez dans nos podcasts musicaux 
en replay, et laissez-vous guider par une programmation musicale 100% indépendante, 
née d'une passion pour la scène romande.
```

### H2 — Section principale
```
Qu'est-ce qu'une radio web suisse ?
Pourquoi écouter Slay Radio, ta radio web suisse ?
Les genres de notre radio web suisse
Comment écouter notre radio web suisse ?
Explore tout le contenu de ta radio web suisse
```

---

## 5. Densité de mots-clés cible

| Mot-clé | Occurrences recommandées | Répartition |
|---------|-------------------------|-------------|
| radio web suisse | 6–8 fois | H1, H2 x2, intro, corps x3 |
| web radio suisse | 2–3 fois | Intro, corps |
| suisse romande | 3–4 fois | Intro, section histoire, corps |
| house afrobeat r&b | 1–2 fois par genre | Section genres |
| écouter radio en ligne | 2–3 fois | Intro, CTA, corps |
| 24h/24 | 2–3 fois | H1, intro, corps |

**Règle :** Ne jamais répéter le même mot-clé exact dans 2 phrases consécutives. Varier entre "radio web suisse", "web radio suisse", "notre radio suisse", "radio en ligne".

---

## 6. Longueur recommandée

| Section | Mots |
|---------|------|
| Hero + intro | 120–150 mots |
| Définition "radio web suisse" | 100–150 mots |
| Pourquoi Slay Radio | 80–100 mots |
| Section genres (3 x H3) | 60–80 mots chacun |
| Comment écouter | 60–80 mots |
| CTA cards | 30–40 mots chacun |
| **Total page** | **700–1000 mots** |

→ 700–1000 mots = seuil minimal pour qu'une page de niche soit prise au sérieux par Google.

---

## 7. Maillage interne complet

### Liens sortants depuis `/radio-web-suisse`

| Texte d'ancre | URL cible |
|--------------|-----------|
| "DJs suisses" | /home/artiste |
| "mix exclusifs" | /home/mix |
| "podcasts musicaux" | /home/podcast |
| "événements en Suisse romande" | /home/evenement |
| "réservez un DJ" | /home/artiste (ou page booking) |

### Liens entrants vers `/radio-web-suisse`

| Page source | Texte d'ancre recommandé |
|-------------|--------------------------|
| Homepage | "radio web suisse" (dans l'intro) |
| /apropos | "notre radio web suisse" |
| Footer | "Radio web suisse" |
| Menu principal | "Écouter" ou "Radio" |
| /home/artiste | "sur notre radio web suisse" |

---

## 8. Checklist avant mise en ligne

- [ ] URL : `/radio-web-suisse` (tirets, pas underscores)
- [ ] Title ≤ 80 caractères avec mot-clé principal
- [ ] Meta description ≤ 160 caractères
- [ ] H1 unique sur la page, différent du Title
- [ ] H2 présents (minimum 3)
- [ ] Player audio intégré et fonctionnel
- [ ] JSON-LD RadioStation ajouté dans le `<head>`
- [ ] Balise canonical pointant vers elle-même
- [ ] Lien dans le menu principal
- [ ] Lien dans le footer
- [ ] Lien depuis la homepage (ancre textuelle)
- [ ] Lien depuis /apropos
- [ ] Page ajoutée dans sitemap.xml avec `<priority>0.9</priority>`
- [ ] Page non bloquée dans robots.txt
- [ ] Images avec alt text contenant "radio web suisse"
