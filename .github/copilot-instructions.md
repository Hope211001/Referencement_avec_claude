---
name: agentic-seo-skill-workspace
description: >
  Workspace instructions for the Agentic SEO skill. Use this file to guide
  agent behavior, surface repository conventions, identify the available
  scripts and workflows, and orient the agent toward deterministic SEO audit
  outputs.
applyTo:
  - "**/*"
---

## What this repository is

This repo is an LLM-first SEO skill for agent IDEs, built around:
- `SKILL.md` for high-level orchestration and deterministic trigger mapping
- `resources/skills/` for sub-skill workflows such as `seo-audit`, `seo-page`, `seo-technical`, `seo-content`, `seo-schema`, `seo-github`, and others
- `resources/agents/` for specialist agent roles like technical SEO, content quality, performance, schema, sitemap, visual analysis, and GitHub SEO
- `scripts/` for evidence-gathering tools used by audits and specialist workflows

## Primary workflow rules

Use the repository as a reasoning-first SEO audit skill, not as a pure script runner.
- Prefer `read_url_content` or equivalent page content evidence first when the user asks for SEO analysis.
- Use scripts only to verify, enrich, and validate findings.
- Return structured findings with explicit `Finding`, `Evidence`, `Impact`, and `Fix` statements.
- Label confidence clearly: `Confirmed`, `Likely`, or `Hypothesis`.

## Core deliverables

For full audits and page audits, produce:
- `FULL-AUDIT-REPORT.md`
- `ACTION-PLAN.md`

If an HTML report is generated, include its exact saved path (for example `SEO-REPORT.html`).
If execution is blocked by environment constraints, still produce the markdown reports and document the limitation.

## Trigger phrases and commands

Treat these user intents as the main entry points:
- `perform seo analysis on <url>` → single-page full audit path
- `seo audit <url>` → full website audit
- `seo page <url>` → deep single-page analysis
- `seo technical <url>` → technical SEO checks
- `seo content <url>` → content quality and E-E-A-T
- `seo schema <url>` → schema markup validation/generation
- `seo sitemap <url>` → sitemap analysis
- `seo images <url>` → image optimization
- `seo geo <url>` → AI search / GEO readiness
- `seo aeo <url>` → answer engine optimization
- `seo github <repo_or_url>` → GitHub repository SEO
- `seo plan <url>` → strategic planning with the matching industry template

## Key files and directories

- `SKILL.md` — main skill orchestration guidance and deterministic trigger mapping
- `README.md` — install instructions, feature summary, example prompts, compatibility notes
- `resources/skills/` — workflow documents for each sub-skill
- `resources/agents/` — specialist agent prompts and context documents
- `resources/references/` — rubric and SEO reference data used by audits
- `resources/templates/` — industry strategy templates for `seo plan`
- `scripts/` — evidence-gathering and verification scripts

## Important repository-specific conventions

- The skill uses LLM-first analysis with script-backed verification.
- Always reference `resources/references/llm-audit-rubric.md` for mandatory report structure and confidence labels.
- Use `resources/references/*` as authoritative guidance for quality gates, Core Web Vitals, schema types, and E-E-A-T.
- The top-level `README.md` is the user-facing summary of capabilities and installation support.
- This repo is not a React/npm package, even though a `package-lock.json` file may exist. Do not install it with `npm install`.
- `install.sh` / `install.ps1` should target a separate IDE/project workspace, not the skill repo root.

## Installation and runtime

- Use `install.sh` or `install.ps1` to install the skill into your IDE environment:
  - On Windows PowerShell:
    `.\install.ps1 --target antigravity --project-dir C:\path\to\your\project`
  - On Linux/macOS:
    `bash install.sh --target antigravity --project-dir /path/to/your/project`
  - For Claude:
    `bash install.sh --target claude`
  - For Codex:
    `bash install.sh --target codex`
- For `--target antigravity`, set `--project-dir` to the destination project folder, not `D:\Fanantenana\SEO\Agentic-SEO-Skill-main` itself.
- For manual script usage inside this repo, create and activate a Python virtual environment in the repo root:
  - `python -m venv .venv`
  - `.\.venv\Scripts\Activate.ps1`
  - `pip install requests beautifulsoup4`
- Optionally install Playwright for visual analysis:
  - `pip install playwright`
  - `playwright install chromium`
- If the repo source and the target project are the same directory, the Antigravity installer may fail because it copies the repo into itself.

## Recommended script usage

If script execution is available, verify audit findings with these scripts:
- `python3 scripts/fetch_page.py <url> --output /tmp/page.html`
- `python3 scripts/parse_html.py /tmp/page.html --url <url> --json`
- `python3 scripts/robots_checker.py <url>`
- `python3 scripts/llms_txt_checker.py <url>`
- `python3 scripts/pagespeed.py <url> --strategy mobile`
- `python3 scripts/security_headers.py <url>`
- `python3 scripts/broken_links.py <url> --workers 5`
- `python3 scripts/redirect_checker.py <url>`
- `python3 scripts/readability.py /tmp/page.html --json`
- `python3 scripts/social_meta.py <url>`
- `python3 scripts/internal_links.py <url> --depth 1 --max-pages 20`
- `python3 scripts/article_seo.py <url> --json`

For GitHub SEO analysis, prefer the repository-specific scripts under `scripts/github_*`.

## Example prompts

Use these prompts to exercise the skill:
- "Run a full SEO audit on https://example.com and generate a prioritized action plan."
- "Analyze this page for schema, content, and Core Web Vitals issues."
- "Review GitHub SEO for owner/repo and produce GITHUB-SEO-REPORT.md plus a plan."
- "Create a strategic SEO plan for a SaaS landing page using the most relevant industry template."

## When not to use this repo

Do not treat this repository as a generic Python utility library.
This workspace is specifically designed for SEO/website/GitHub SEO auditing and planning with an agent-driven workflow.
