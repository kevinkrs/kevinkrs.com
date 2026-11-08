# kevinkrs.com

Personal site of Kevin Kraus. Built with [Astro](https://astro.build), deployed to GitHub Pages.

## Edit content
Everything on the homepage is in `src/data/site.ts`.

## Develop
```bash
npm install
npm run dev
```

## Deploy
Pushing to `main` builds and deploys via `.github/workflows/deploy.yml`.
One-time setup: repo Settings → Pages → Source: **GitHub Actions**, custom domain `kevinkrs.com`.
DNS at your registrar: `A` records for `kevinkrs.com` → 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153, and `CNAME` `www` → `<your-github-username>.github.io`.

## Before going live
- Replace placeholder rows in `src/data/site.ts` (experience, education).
- Fill in `src/pages/impressum/index.astro`.
