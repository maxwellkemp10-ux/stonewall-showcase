# Deployment Integrations: Vercel, Cloudflare, Replit, Railway

This repository now includes first-class deployment configuration for all four requested platforms.

## Shared runtime surface

The repository has two deployment modes:

1) **Python static server mode** (Replit):

- `python3 scripts/serve_static.py --directory docs`

2) **Edge static assets mode** (Vercel + Cloudflare):

- `docs/` is served directly by platform routing/asset bindings.

Shared behavior:

- Root route resolves to `docs/index.html`
- `docs/portal/` remains available at `/portal`
- `PORT` env var is honored by the Python server when provided

## Vercel

Files:

- `vercel.json`

Usage:

1. Connect the repo in Vercel.
2. Framework preset: **Other**.
3. Build command: none.
4. Output directory: none.
5. Deploy.

`vercel.json` rewrites root and portal routes to `docs/` content.

## Cloudflare

Files:

- `wrangler.toml`
- `_worker.js`

Usage (Cloudflare Workers static assets):

1. `npm i -g wrangler` (or local wrangler tooling)
2. `wrangler login`
3. `wrangler deploy`

The worker serves static content from `docs/` through Cloudflare assets and falls back unknown paths to `/`.

## Replit

Files:

- `.replit`
- `replit.nix`

Usage:

1. Import repo into Replit.
2. Replit reads `.replit` and starts:
   - `python3 scripts/serve_static.py --host 0.0.0.0 --directory docs`
3. Open the web preview.

## Railway

Usage:

Railway is commonly used for long-running worker/bot processes in Stonewall (for example, Telegram bot services). To avoid overriding an existing bot start command, this repo intentionally does **not** pin a `railway.json` start command.

Recommended approach:

1. Keep your bot service command configured in Railway service settings.
2. Use Vercel/Cloudflare/Replit for static web surfaces from this repo.
3. If you later want a separate Railway static service, configure that service command directly in Railway UI (instead of a repo-wide override).

## Local verification

- `make serve` to run local web surface
- `make smoke` to validate script + integration surfaces
