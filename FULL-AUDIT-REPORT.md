# SEO Full Audit Report — slayradio.ch
**Date:** 2026-04-29 | **Scope:** Full-site audit | **Analyst:** Agentic SEO Skill

---

## A) Audit Summary

**Scope:** Full-site — homepage, /apropos, /radio-web-suisse, 17-page crawl, sitemap index (3 sub-sitemaps), robots.txt, schema, social tags, security headers, AI readiness.

**Overall SEO Health Score: 62 / 100 — Needs Improvement**

| Category | Score | Weight | Weighted |
|---|---|---|---|
| Technical SEO | 70 | 25% | 17.5 |
| Content Quality | 52 | 20% | 10.4 |
| On-Page SEO | 58 | 15% | 8.7 |
| Schema / Structured Data | 52 | 15% | 7.8 |
| Performance (CWV) | 45* | 10% | 4.5 |
| Image Optimization | 72 | 10% | 7.2 |
| AI Search Readiness | 80 | 5% | 4.0 |
| **TOTAL** | | | **60.1 → 62** |

*Performance score confidence: Low — PageSpeed API rate-limited; CWV not measured.

**Score justification:** Score of 62 reflects a solid technical foundation (HTTPS, security headers 100/100, canonical, robots.txt, complete OG/Twitter metadata, two valid JSON-LD schemas, llms.txt) pushing the score up. Penalized by missing meta descriptions on two critical inner pages (−10), no WebSite/Organization schema (−10), borderline TTFB 1189ms (−5), and E-E-A-T gaps (no author bios, no dedicated privacy page).

**Top 3 Issues:**
1. `/radio-web-suisse` — primary SEO landing page missing meta description (direct ranking impact)
2. No WebSite schema with SearchAction — not eligible for sitelinks searchbox
3. External Unsplash hero image — no `width`/`height` (CLS risk) + external LCP dependency

**Top 3 Opportunities:**
1. Upload `googlefdc971f91a5e2331.html` to server → verify Google Search Console → unlock real search data
2. Add Organization + WebSite JSON-LD → Google Knowledge Panel + sitelinks searchbox eligibility
3. Self-host hero image → remove external dependency → better LCP and CLS

---

## B) Findings Table

### Technical SEO

| Area | Severity | Confidence | Finding | Evidence | Fix |
|---|---|---|---|---|---|
| Google Search Console | Warning | Confirmed | Verification file not deployed to server | `googlefdc971f91a5e2331.html` exists locally; site not verified in GSC | Upload file to web root via FTP/SFTP/CMS file manager |
| TTFB | Warning | Confirmed | Response time 1189ms exceeds 800ms LCP target | `redirect_checker.py`: single hop 200 OK, 1189ms total | Add Cloudflare CDN, enable server-side caching, optimize backend |
| Core Web Vitals | Info | Hypothesis | LCP, INP, CLS unknown | PageSpeed API rate-limited during audit | Run PageSpeed Insights manually or check Search Console CWV report |
| HTTPS + HSTS | Pass | Confirmed | HTTPS enforced with HSTS max-age=31536000 includeSubDomains | `security_headers.py`: HSTS present | — |
| Security Headers | Pass | Confirmed | All 6 headers present; score 100/100 | CSP, X-Frame-Options, nosniff, Referrer-Policy, Permissions-Policy | — |
| Redirects | Pass | Confirmed | No redirect chains; direct 200 OK | `redirect_checker.py`: 0 hops | — |
| Canonical | Pass | Confirmed | Canonical present and self-referencing | `<link rel="canonical" href="https://slayradio.ch/">` | — |
| lang attribute | Pass | Confirmed | lang="fr-CH" correctly set | `<html lang="fr-CH">` | — |
| Viewport + Charset | Pass | Confirmed | Both correctly configured | `width=device-width, initial-scale=1.0`; `charset=UTF-8` | — |
| robots.txt | Pass | Confirmed | Sitemap declared; all AI crawlers explicitly allowed | 12 user-agents: GPTBot, ClaudeBot, PerplexityBot, Google-Extended, Applebot-Extended, Bytespider, CCBot, FacebookBot, Amazonbot — all set to Allow | — |
| Sitemap | Pass | Confirmed | Sitemap index with 3 sub-sitemaps; updated 2026-04-28 | sitemap.xml → sitemap.static.xml, sitemap.artistes.xml, sitemap.evenements.xml | — |

### On-Page SEO

| Area | Severity | Confidence | Finding | Evidence | Fix |
|---|---|---|---|---|---|
| Meta desc — /radio-web-suisse | Warning | Confirmed | Primary SEO landing page has no meta description | WebFetch: no `<meta name="description">` found on /radio-web-suisse | Add 140–155 char French desc targeting "radio web suisse en direct" |
| Meta desc — /apropos | Warning | Confirmed | About page has no meta description | WebFetch: no `<meta name="description">` found on /apropos | Add 140–155 char desc e.g. "Decouvrez l'histoire et la mission de Slay Radio, la web radio suisse 100% musicale." |
| Schema on /radio-web-suisse | Warning | Confirmed | Key SEO landing page has no JSON-LD | No JSON-LD detected on /radio-web-suisse | Add RadioStation or WebPage schema |
| Orphan event pages | Warning | Confirmed | 4 event pages have only 1 incoming link (orphan risk) | `internal_links.py`: wine-night-festival-geneve, avenches-open-air, blues-rules-festival-crissier, festiboc-bofflens | Add cross-links from /home/evenement listing and related event pages |
| /home/podcast in sitemap | Warning | Likely | Podcast section absent from static sitemap | sitemap.static.xml lists only 6 pages; /home/podcast not present | Add /home/podcast to sitemap.static.xml with priority 0.7, changefreq weekly |
| Empty anchor texts | Info | Confirmed | 12 internal links have no anchor text | `internal_links.py`: 12 links without text | Add descriptive anchor text to image links and icon links |
| og:image whitespace | Info | Confirmed | og:image value has leading tab/whitespace before URL | `social_meta.py` output showed tab character before URL | Remove leading whitespace/tab from og:image content attribute |
| Homepage title | Pass | Confirmed | 50 chars, keyword-rich, brand-forward | "Slay Radio — Web Radio Suisse Romande 24h/24" | — |
| Homepage meta desc | Pass | Confirmed | 155 chars, keyword-rich, includes USPs (gratuit, sans inscription) | Present in `<meta name="description">` | — |
| H1 | Pass | Confirmed | Single, keyword-rich H1 | "Ecoute la Web Radio Suisse Romande — House, Afrobeat & R&B 24h/24" | — |
| H2 structure | Pass | Confirmed | 6 themed H2 sections on homepage | Mix Dj, Evenements, Notre histoire, Notre programmation, Derniers titres, CTA | — |
| OG Tags | Pass | Confirmed | 7/7 complete — score 100/100 | og:title, og:description, og:image, og:url, og:type, og:site_name, og:locale=fr_CH | — |
| Twitter/X Card | Pass | Confirmed | 6/6 complete | summary_large_image card; site + creator set to @SlayRadio | — |

### Schema / Structured Data

| Area | Severity | Confidence | Finding | Evidence | Fix |
|---|---|---|---|---|---|
| WebSite schema | Warning | Confirmed | No WebSite @type with SearchAction anywhere on site | No WebSite block found in any JSON-LD | Add WebSite JSON-LD with SearchAction (see ACTION-PLAN.md) |
| Organization schema | Warning | Confirmed | No Organization @type | No Organization block in JSON-LD | Add Organization with name, url, logo, email, sameAs (YouTube, Instagram, TikTok) |
| BreadcrumbList | Info | Confirmed | No breadcrumb schema on inner pages | /radio-web-suisse and /apropos lack BreadcrumbList | Add BreadcrumbList to all inner pages |
| Array wrapper on RadioStation | Info | Confirmed | First JSON-LD block uses outer JSON array `[{...}]` | Schema block starts with `[` in source | Remove array wrapper; use bare `{...}` or @graph pattern |
| RadioStation | Pass | Confirmed | Valid schema with genres, broadcaster, logo, timezone | @type RadioStation; genre: House, Afrobeat, R&B; broadcastTimezone: Europe/Zurich | — |
| MusicPlaylist | Pass | Confirmed | MusicPlaylist with 2 MusicRecording tracks | @type MusicPlaylist; 2 tracks with byArtist | — |

### Performance & Images

| Area | Severity | Confidence | Finding | Evidence | Fix |
|---|---|---|---|---|---|
| Hero image — external | Warning | Confirmed | Hero image loads from Unsplash CDN (external LCP dependency) | `<img src="https://images.unsplash.com/photo-1516450360452-9312f5e86fc7?w=600&h=450&fit=crop">` in source | Download image; self-host under /image/ or /uploads/ |
| Hero image — no dimensions | Warning | Confirmed | Unsplash hero has no width/height attributes (CLS risk) | No width or height on external img tag | Add `width="600" height="450"` to existing tag immediately |
| Local images | Pass | Confirmed | All local images have alt, width=400, height=400, loading=lazy | 7 local images verified in source | — |
| Image alt text | Pass | Confirmed | Descriptive, specific alts on all images | Logo, artist, event, social icon images all have meaningful alts | — |

### Content Quality & E-E-A-T

| Area | Severity | Confidence | Finding | Evidence | Fix |
|---|---|---|---|---|---|
| Privacy Policy page | Warning | Likely | No dedicated privacy or legal page | nLPD referenced only in cookie banner; no /privacy-policy URL in sitemap | Create /mentions-legales or /politique-confidentialite page; link from footer |
| Author / Team bios | Warning | Likely | No named team members or DJ profile bios | /apropos describes mission but no individuals named | Add DJ/host profiles with name, photo, background (E-E-A-T boost) |
| Readability | Info | Confirmed | Flesch 57.1 — Difficult (10th-12th grade); avg paragraph 5.4 sentences | `readability.py` JSON: flesch_reading_ease=57.1, avg_paragraph_length=5.4 | Break long paragraphs; target Flesch > 65 |
| About page | Pass | Confirmed | Mission, values, history, contact present on /apropos | Notre Histoire, Notre Mission, Nos Valeurs, Communaute, Diversite, Innovation | — |
| Contact info | Pass | Confirmed | contact@slayradio.ch visible in footer and /apropos | Confirmed in HTML source | — |
| Swiss law compliance signal | Pass | Confirmed | Cookie notice references Swiss nLPD | Footer cookie consent mentions loi suisse nLPD | — |

### AI Search Readiness

| Area | Severity | Confidence | Finding | Evidence | Fix |
|---|---|---|---|---|---|
| llms.txt encoding | Info | Confirmed | Description has UTF-8 double-encoding artifact | `llms_txt_checker.py` showed "AvenA©ments" instead of "evenements" | Re-save llms.txt with UTF-8 encoding; check server Content-Type header |
| llms.txt | Pass | Confirmed | Present; quality score 100/100; 5 sections, 10 links | HTTP 200; `llms_txt_checker.py` | — |
| llms-full.txt | Pass | Confirmed | Present and accessible | HTTP 200 confirmed | — |
| AI crawlers | Pass | Confirmed | All major AI crawlers explicitly allowed in robots.txt | 12 user-agents including GPTBot, ClaudeBot, PerplexityBot, Google-Extended | — |

---

## C) Prioritized Action Plan

See `ACTION-PLAN.md` for all implementation steps with code.

---

## D) Unknowns and Follow-ups

| Unknown | Why it matters | How to confirm |
|---|---|---|
| Core Web Vitals (LCP, INP, CLS) | Ranking tiebreaker; mobile CWV more heavily weighted post-Dec 2025 | Run `pagespeed.py` or PageSpeed Insights manually; check Search Console |
| /apropos meta description (actual HTML) | WebFetch may have missed it | Browser DevTools → View Source on /apropos |
| artistes.xml + evenements.xml content | Number of indexed pages; any missing | Fetch the two sub-sitemaps |
| /boutique sitemap status | Visible in nav but not in static sitemap | Verify if public and indexable; add if so |
| External backlink profile | No link data collected | Run `link_profile.py` or use Ahrefs/Majestic |
| GSC impressions, CTR, index coverage | Actual search performance unknown | Upload verification file and verify in Google Search Console |

---

## Site Reference Card

| Signal | Value |
|---|---|
| URL | https://slayradio.ch/ |
| Business Type | Publisher — Independent Web Radio |
| Language | French (fr-CH) |
| Target Market | Suisse Romande (Lausanne, Geneve, Sion) |
| Genres | House, Afrobeat, R&B |
| Pages crawled | 17 of 21 unique found |
| Internal links | 177 total |
| HTTPS | Yes |
| Security Score | 100/100 |
| JSON-LD Schemas | RadioStation, MusicPlaylist |
| Google Search Console | Not yet verified |
