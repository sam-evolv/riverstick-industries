# riverstickindustries.ie

Static site. No framework, no npm, no build step needed to deploy.

## Structure
- `index.html`, `bark-mulch.html`, `rubber-matting.html`, `horse-walker-matting.html`, `rubber-bricks.html`, `404.html`: generated pages
- `scripts/build.py`: all copy and templates live here
- `css/site.css`, `js/site.js`: styles and behaviour
- `fonts/`: self-hosted Instrument Serif + Inter (no Google requests)
- `images/`: optimised webp (960w and 1600w per product), logo, icons, og-image
- `vercel.json`: clean URLs (`/bark-mulch` serves `bark-mulch.html`), security headers, caching

## Edit copy
1. Change text in `scripts/build.py`
2. `python3 scripts/build.py`
3. Commit the regenerated `.html` files

## Preview locally
`python3 -m http.server 8000` then open http://localhost:8000/ (product pages: /bark-mulch.html locally; clean URLs work on Vercel)

## Rollback
The previous React build is in git history: `git revert <merge-commit>` or redeploy the previous production deployment in Vercel.
