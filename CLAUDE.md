# CLAUDE.md

## Project purpose

VyOS community website (community.vyos.net). A static site built by the [soupault](https://soupault.app) static-site generator from HTML pages plus SASS-built CSS. Deployed via AWS Amplify (`amplify.yml` present).

## Tech stack

- Static-site generator: soupault (OCaml).
- HTML templates under `templates/`, content under `site/`.
- Sass for stylesheets (`sass/main.sass` → `build/main.css`).
- Soupault plugins under `plugins/` (Lua).
- AWS Amplify deploy spec: `amplify.yml`.
- `release-status.toml` for the per-train release banner data.
- `mergify.yml` present (single-rule conflicts label).

## Build / test / run

```
# Site
soupault                    # → build/
# CSS
sass -I sass/ sass/main.sass > build/main.css
# Combined
make all
```

## Repository layout

- `templates/` — page skeletons including `main.html`; soupault inserts page content into `div#content`.
- `site/` — actual page content (Markdown + HTML).
- `sass/` — SASS sources.
- `fonts/` — static assets.
- `plugins/` — soupault Lua plugins.
- `scripts/` — helper scripts.
- `soupault.toml` — site config; markdown extensions, strict mode, etc.
- `amplify.yml` — Amplify build pipeline (likely calls `make all`).
- `release-status.toml` — release-train metadata feed for the site.

## Cross-repo context

Static site, independent of the VyOS image build. Sibling corporate web properties live under `sentrium/*` (`next-js-vyos` is the main vyos.io site on Next.js + DatoCMS + Vercel; `community.vyos.net` is the older soupault-based community site). May be consumed by `vyos/amplify-build-status` (also in this chunk) for build-status gating.

## Conventions

- Commit / PR title format: `component: T12345: description` (Phorge task ID mandatory). Enforced by `vyos/.github` reusable workflows where consumed.
- **Branch model differs:** `main` is the staging branch (auto-deployed to staging.vyos.net); `production` is the production branch.
- `mergify.yml` adds a `conflicts` label to conflicting PRs (byte-identical to other VyOS repos with this file).

## Mirror relationship

Mirror twin: `VyOS-Networks/community.vyos.net`. Canonical side is **here** (`vyos/community.vyos.net`).

## Notes for future contributors

- This repo's branch model is `main` (staging) → `production` (live), **not** the `current`/`sagitta`/`circinus` train naming used by VyOS image repos.
- soupault is the build dependency, not Hugo or Jekyll. Install from soupault.app.
- License: see `LICENSE` (none committed; treat as VyOS-default).
