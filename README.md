# Riverstick Industries — Website

Marketing site for **Riverstick Industries**, a Cork-based supplier of premium
industrial and landscaping materials (established 1968): bark mulch, rubber
matting, horse walker matting and rubber bricks.

This is a **static site** — plain HTML, CSS and a little vanilla JavaScript, with
no build step or framework. It can be hosted on any static host (Netlify,
Cloudflare Pages, GitHub Pages, Vercel, etc.) by serving this folder as-is.

## Structure

```
.
├── index.html                 # Home (hero, products, about, contact)
├── bark-mulch/index.html      # Product page  →  /bark-mulch/
├── rubber-matting/index.html  #               →  /rubber-matting/
├── horse-walker-matting/…     #               →  /horse-walker-matting/
├── rubber-bricks/index.html   #               →  /rubber-bricks/
├── 404.html                   # Friendly not-found page
├── css/styles.css             # All styling (design tokens at the top)
├── js/main.js                 # Nav, hero carousel, scroll reveal
├── images/                    # Optimised .webp photos + logo/favicons
├── favicon.png, sitemap.xml, robots.txt, _headers
```

## Branding

Tokens live at the top of `css/styles.css` (`:root`):

- **Burgundy** `#5f0000` · **Gold** `#e2b43d`
- Headings: **Fraunces** (serif) · Body: **Inter** (sans) — loaded from Google Fonts
- Logo: `images/logo.png` (full lockup) and `images/logo-mark.png` (the "R" monogram, used in the header)

## Editing common things

- **Phone number** — search the repo for `+353 21 477 1362` / `tel:+353214771362`.
- **Address / opening hours** — in the contact section of `index.html` and in the footer of every page.
- **Product copy** — each product page is self-contained in its `index.html`.
- **Adding a product** — duplicate a product folder, update the content, then add
  it to the homepage product grid, the footer "Products" list and `sitemap.xml`.

## Local preview

No build needed. From this folder:

```bash
python3 -m http.server 8000
# then open http://localhost:8000
```

(Use a server rather than opening files directly so that the absolute `/…` paths
and the clean folder URLs resolve correctly.)

## Deploying

Upload the contents of this folder to any static host. `_headers` sets sensible
security and caching headers on Netlify / Cloudflare Pages; other hosts can apply
the equivalent. Update the domain in `sitemap.xml`, `robots.txt` and the
`canonical` / `og:url` tags if it ever changes from `riverstickindustries.ie`.

---

Designed & developed by [EvolvAi](https://evolvai.ie).
