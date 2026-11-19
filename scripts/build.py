#!/usr/bin/env python3
"""Generate the static Riverstick Industries site.

All copy lives in this file. Edit it, then run:  python3 scripts/build.py
Outputs index.html, one .html page per product, 404.html and sitemap.xml at the repo root.
"""
from html import escape
from pathlib import Path
import json
import datetime

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://www.riverstickindustries.ie"
PHONE_DISPLAY = "021 477 1362"
PHONE_TEL = "+353214771362"
MAPS = "https://www.google.com/maps/search/?api=1&query=Curra,+Riverstick,+Co.+Cork,+Ireland+P43+EY24"
MAP_EMBED = "https://maps.google.com/maps?q=Curra%2C%20Riverstick%2C%20Co.%20Cork%2C%20P43%20EY24&z=12&output=embed"
ADDRESS_HTML = "Curra, Riverstick<br>Co. Cork, Ireland<br>P43 EY24"

ICONS = {
    "phone": '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.8 19.8 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.12 4.18 2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.9.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/>',
    "arrow": '<path d="M5 12h14"/><path d="m12 5 7 7-7 7"/>',
    "chev": '<path d="m9 18 6-6-6-6"/>',
    "check": '<path d="M20 6 9 17l-5-5"/>',
    "pin": '<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/>',
    "clock": '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
    "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/>',
    "truck": '<path d="M14 18V6a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2v11a1 1 0 0 0 1 1h2"/><path d="M15 18H9"/><path d="M19 18h2a1 1 0 0 0 1-1v-3.65a1 1 0 0 0-.22-.62L18.3 9.38a1 1 0 0 0-.78-.38H14"/><circle cx="17" cy="18" r="2"/><circle cx="7" cy="18" r="2"/>',
    "support": '<path d="M3 14h3a2 2 0 0 1 2 2v3a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-7a9 9 0 0 1 18 0v7a2 2 0 0 1-2 2h-1a2 2 0 0 1-2-2v-3a2 2 0 0 1 2-2h3"/>',
    "award": '<circle cx="12" cy="8" r="6"/><path d="M15.48 12.89 17 22l-5-3-5 3 1.52-9.11"/>',
    "leaf": '<path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19 2c1 2 2 4.18 2 8 0 5.5-4.78 10-10 10Z"/><path d="M2 21c0-3 1.85-5.36 5.08-6C9.5 14.52 12 13 13 12"/>',
}


def icon(name, extra=""):
    return (f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"{extra}>{ICONS[name]}</svg>')


PRODUCTS = [
    {
        "slug": "bark-mulch",
        "img": "bark-mulch",
        "name": "Premium Bark Mulch",
        "short": "Bark Mulch",
        "tagline": "Professional landscaping materials for every project",
        "card": "Natural wood-based mulch perfect for landscaping, garden beds, and erosion control. Available in various sizes and colours.",
        "meta": "Premium bark mulch for landscaping, garden beds, and erosion control. Natural wood-based mulch available in various sizes and colours. Expert support in Cork, Ireland.",
        "h1": "Bark Mulch",
        "kicker": "Nature's finishing touch for your garden.",
        "lead": "Bark mulch is more than just a decorative ground cover. It's a simple, beautiful way to protect your soil, nurture your plants, and bring a polished, natural look to your outdoor spaces.",
        "benefits_title": "Why use bark mulch?",
        "benefits": ["Keeps Soil Moist", "Blocks Weeds Naturally", "Protects Plant Roots", "Breaks Down Beautifully", "Brings Instant Beauty"],
        "list_title": "Types we offer",
        "list": ["Fine Bark Mulch", "Medium Bark Mulch"],
        "delivery": "<b>Delivery:</b> minimum 10 cubic metres. Collection also available.",
        "note": "Sustainably sourced, locally processed, and free from dyes or harsh chemicals.",
    },
    {
        "slug": "rubber-matting",
        "img": "rubber-matting",
        "name": "Industrial Rubber Matting",
        "short": "Rubber Matting",
        "tagline": "Durable flooring solutions for commercial spaces",
        "card": "High-quality rubber flooring solutions for commercial and industrial applications. Slip-resistant and durable.",
        "meta": "High-quality industrial rubber matting for commercial and industrial applications. Slip-resistant, durable flooring solutions with expert support in Cork, Ireland.",
        "h1": "Built to perform. Designed to last.",
        "eyebrow": "Industrial Rubber Matting",
        "kicker": "Premium rubber matting for work, wellness and the everyday.",
        "lead": "High-quality rubber flooring solutions for commercial and industrial applications. Slip-resistant and durable.",
        "benefits_title": "Why rubber matting?",
        "benefits": ["Slip-Resistant", "Shock-Absorbing Comfort", "Built for Heavy Use", "Low Maintenance", "Noise + Vibration Control"],
        "list_title": "Matting types",
        "list": ["Stable &amp; Horse Mats", "Gym Flooring", "Industrial &amp; Workshop Matting", "Agricultural Matting", "Entrance &amp; Anti-Slip Mats"],
        "note": "Crafted from recycled rubber. Tough on the job, gentle on the planet.",
    },
    {
        "slug": "horse-walker-matting",
        "img": "horse-walker",
        "name": "Horse Walker Matting",
        "short": "Horse Walker Matting",
        "tagline": "Specialised equestrian solutions for training facilities",
        "card": "Specialised equestrian flooring designed for horse walkers and training facilities. Provides excellent grip and comfort.",
        "meta": "Specialised equestrian horse walker matting for stables and training facilities. Professional flooring solutions with excellent grip and comfort in Cork, Ireland.",
        "h1": "Horse Walker Matting",
        "kicker": "Built for hooves in motion.",
        "lead": "Durable, non-slip rubber flooring designed for horse walkers and equestrian areas. Provides excellent grip and comfort while reducing bedding and maintenance costs.",
        "benefits_title": "Key features",
        "benefits": ["Slip-resistant surface", "Shock-absorbing comfort for joints", "Easy to clean and hose down", "Custom sizes available"],
        "list_title": "Ideal for",
        "list": ["Horse walkers", "Training rings", "Equine rehabilitation areas"],
    },
    {
        "slug": "rubber-bricks",
        "img": "rubber-bricks",
        "name": "Rubber Bricks",
        "short": "Rubber Bricks",
        "tagline": "Interlocking rubber brick flooring for versatile applications",
        "card": "Interlocking rubber brick flooring system perfect for patios, walkways, and commercial spaces. Durable, slip-resistant, and easy to install.",
        "meta": "Interlocking rubber brick flooring systems perfect for patios, walkways, and commercial spaces. Durable, slip-resistant, and easy to install in Cork, Ireland.",
        "h1": "Rubber Bricks",
        "kicker": "Interlocking strength, everyday practicality.",
        "lead": "Interlocking rubber brick flooring system perfect for patios, walkways, and commercial spaces. Durable, easy to install, and designed to last.",
        "benefits_title": "Key features",
        "benefits": ["Slip-resistant surface", "Shock-absorbing", "Fast interlocking installation", "Suitable for wet and dry environments"],
        "list_title": "Use cases",
        "list": ["Patios and paths", "Commercial walkways", "Stables and farm lanes", "Industrial floor safety zones"],
    },
]

FONTS = ('<link rel="preload" href="/fonts/instrument-serif-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>'
         '<link rel="preload" href="/fonts/inter-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>')

LOCAL_BUSINESS = {
    "@context": "https://schema.org",
    "@type": "LocalBusiness",
    "@id": SITE + "/#business",
    "name": "Riverstick Industries",
    "description": "Premium industrial materials including bark mulch, rubber matting, horse walker matting, and rubber bricks.",
    "url": SITE + "/",
    "logo": SITE + "/images/logo-full.png",
    "image": SITE + "/images/og-image.jpg",
    "telephone": PHONE_TEL,
    "foundingDate": "1968",
    "address": {"@type": "PostalAddress", "streetAddress": "Curra, Riverstick", "addressLocality": "Cork",
                "addressRegion": "Co. Cork", "postalCode": "P43 EY24", "addressCountry": "IE"},
    "openingHoursSpecification": [{"@type": "OpeningHoursSpecification",
                                   "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
                                   "opens": "09:00", "closes": "17:30"}],
    "hasMap": MAPS,
}


def head(title, desc, path, preload=None, extra_ld=None):
    url = SITE + path
    ld = [LOCAL_BUSINESS] + (extra_ld or [])
    pre = ""
    if preload:
        pre = (f'<link rel="preload" as="image" href="/images/{preload}-960.webp" media="(max-width: 960px)" fetchpriority="high">'
               f'<link rel="preload" as="image" href="/images/{preload}-1600.webp" media="(min-width: 961px)" fetchpriority="high">')
    return f"""<!DOCTYPE html>
<html lang="en-IE">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{escape(title)}</title>
<meta name="description" content="{escape(desc)}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#f7f5f1">
<link rel="icon" type="image/png" href="/favicon.png">
<link rel="apple-touch-icon" href="/images/apple-touch-icon.png">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Riverstick Industries">
<meta property="og:title" content="{escape(title)}">
<meta property="og:description" content="{escape(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/images/og-image.jpg">
<meta property="og:locale" content="en_IE">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{escape(title)}">
<meta name="twitter:description" content="{escape(desc)}">
<meta name="twitter:image" content="{SITE}/images/og-image.jpg">
{pre}
{FONTS}
<link rel="stylesheet" href="/css/site.css">
<script>document.documentElement.classList.add('js')</script>
<script type="application/ld+json">{json.dumps(ld if len(ld) > 1 else ld[0], separators=(',', ':'))}</script>
</head>"""


def header(active=None):
    def cur(k):
        return ' aria-current="page"' if active == k else ""
    return f"""<body>
<a class="skip" href="#main">Skip to content</a>
<header class="header">
  <div class="wrap header-inner">
    <a class="brand" href="/" aria-label="Riverstick Industries home">
      <img src="/images/logo-mark.webp" width="26" height="28" alt="">
      <span>Riverstick Industries</span>
    </a>
    <nav class="nav" aria-label="Main navigation">
      <a href="/#products"{cur('products')}>Products</a>
      <a href="/#about">About</a>
      <a href="/#contact">Contact</a>
      <a class="btn btn-sm" href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a>
    </nav>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="mobile-menu" aria-label="Open menu"><span></span></button>
  </div>
</header>
<div class="mobile-menu" id="mobile-menu">
  <nav aria-label="Mobile navigation">
    <a href="/">Home</a>
    <a href="/#products">Products</a>
    <a href="/#about">About</a>
    <a href="/#contact">Contact</a>
  </nav>
  <a class="btn" href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a>
  <p class="mm-meta">Monday to Friday, 9:00 to 17:30</p>
</div>
"""


def footer():
    plinks = "".join(f'<li><a href="/{p["slug"]}">{p["short"]}</a></li>' for p in PRODUCTS)
    return f"""<footer class="footer">
  <div class="wrap">
    <div class="footer-top">
      <div class="footer-brand">
        <img src="/images/logo-full.webp" width="84" height="127" alt="Riverstick Industries, established 1968" loading="lazy">
      </div>
      <div>
        <h4>Products</h4>
        <ul>{plinks}</ul>
      </div>
      <div>
        <h4>Company</h4>
        <ul>
          <li><a href="/">Home</a></li>
          <li><a href="/#about">About</a></li>
          <li><a href="/#contact">Contact</a></li>
        </ul>
      </div>
      <div>
        <h4>Contact</h4>
        <ul>
          <li><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></li>
          <li><address>{ADDRESS_HTML}</address></li>
          <li class="muted">Mon to Fri, 9:00 to 17:30<br>Sat and Sun, Closed</li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© <span data-year>{datetime.date.today().year}</span> Riverstick Industries. All rights reserved.</span>
      <a href="https://donworthstudio.ie/" target="_blank" rel="noopener noreferrer">Designed &amp; Developed by Donworth Studio</a>
    </div>
  </div>
</footer>
<a class="fab" href="tel:{PHONE_TEL}" aria-label="Call Riverstick Industries on {PHONE_DISPLAY}">{icon('phone')}</a>
<script src="/js/site.js" defer></script>
</body>
</html>
"""


def picture(img, alt, eager=False, sizes="100vw"):
    load = 'fetchpriority="high" decoding="async"' if eager else 'loading="lazy" decoding="async"'
    return (f'<img src="/images/{img}-1600.webp" srcset="/images/{img}-960.webp 960w, /images/{img}-1600.webp 1600w" '
            f'sizes="{sizes}" alt="{escape(alt)}" {load}>')


def product_card(p, short=False, sizes="(max-width: 900px) 100vw, 50vw"):
    desc = "" if short else f"<p>{p['card']}</p>"
    return f"""<a class="p-card" href="/{p['slug']}" data-reveal>
      <div class="p-media">{picture(p['img'], p['name'], sizes=sizes)}</div>
      <div class="p-body">
        <div class="p-title"><h3>{p['name']}</h3>{icon('arrow')}</div>
        {desc}
      </div>
    </a>"""


def contact_section():
    return f"""<section class="section" id="contact" aria-labelledby="contact-title">
  <div class="wrap"><div class="contact-grid">
    <div class="contact-copy" data-reveal>
      <p class="eyebrow">Get in touch</p>
      <h2 class="h2" id="contact-title">Talk to us about your project.</h2>
      <p class="lead">Ready to discuss your project? Our experienced team is here to help you find the perfect materials for your needs.</p>
      <dl class="info">
        <div><dt>Phone</dt><dd><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></dd></div>
        <div><dt>Address</dt><dd><address>{ADDRESS_HTML}</address></dd></div>
        <div><dt>Hours</dt><dd>Monday to Friday, 9:00 to 17:30<br>Saturday and Sunday, Closed<span class="status" data-open-status hidden></span></dd></div>
      </dl>
      <div class="actions">
        <a class="btn" href="tel:{PHONE_TEL}">Call Now for Quote</a>
        <a class="btn btn-quiet" href="{MAPS}" target="_blank" rel="noopener noreferrer">Open in Google Maps</a>
      </div>
    </div>
    <figure class="map" data-reveal>
      <div class="map-frame">
        <iframe title="Map showing Riverstick Industries, Curra, Riverstick, Co. Cork" src="{MAP_EMBED}" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
      </div>
      <figcaption>Find us at Curra, Riverstick, Co. Cork, P43 EY24. <a href="{MAPS}" target="_blank" rel="noopener noreferrer">Get directions</a></figcaption>
    </figure>
  </div></div>
</section>"""


def home():
    slides = "".join(
        f'<figure class="hero-slide{" is-active" if i == 0 else ""}">{picture(p["img"], p["name"], eager=(i == 0))}'
        f'<figcaption>{p["name"]}<span>{p["tagline"]}</span></figcaption></figure>'
        for i, p in enumerate(PRODUCTS))
    dots = "".join(f'<button type="button" aria-label="Show {p["name"]}"{" class=\"is-active\"" if i == 0 else ""}></button>' for i, p in enumerate(PRODUCTS))
    cards = "\n    ".join(product_card(p) for p in PRODUCTS)
    return head("Riverstick Industries | Premium Industrial Materials | Cork, Ireland",
                "Premium bark mulch, rubber matting, horse walker matting and rubber bricks. Quality Irish industrial materials since 1968, with expert support and fast delivery across Cork.",
                "/", preload="bark-mulch") + header("home") + f"""
<main id="main">
<section class="intro">
  <div class="wrap">
    <div class="intro-grid">
      <h1 class="display">Premium industrial materials, made to last.</h1>
      <div class="intro-side">
        <p class="lead">Bark mulch, rubber matting, horse walker matting and rubber bricks for commercial, industrial and residential clients. Supplied from Riverstick, Co. Cork since 1968.</p>
        <div class="actions">
          <a class="btn" href="tel:{PHONE_TEL}">Call to Order</a>
          <a class="btn btn-quiet" href="#products">View products</a>
        </div>
      </div>
    </div>
  </div>
  <div class="wrap">
    <div class="hero" data-carousel aria-roledescription="carousel" aria-label="Our products">
      {slides}
      <div class="dots" role="group" aria-label="Carousel navigation">{dots}</div>
    </div>
  </div>
</section>

<section class="facts" aria-label="Why Riverstick">
  <div class="wrap">
    <ul>
      <li><b>Since 1968</b><span>Over five decades in business</span></li>
      <li><b>Quality Guaranteed</b><span>Built to the highest standards</span></li>
      <li><b>Fast Delivery</b><span>Across Cork and beyond</span></li>
      <li><b>Expert Support</b><span>An experienced team on hand</span></li>
    </ul>
  </div>
</section>

<section class="section" id="products" aria-labelledby="products-title">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <p class="eyebrow">Our product range</p>
      <h2 class="h2" id="products-title">Four materials, one standard.</h2>
      <p class="lead">Discover our comprehensive selection of premium industrial materials, each crafted to meet the highest standards of quality and durability.</p>
    </div>
    <div class="products">
    {cards}
    </div>
  </div>
</section>

<section class="section about" id="about" aria-labelledby="about-title">
  <div class="wrap"><div class="about-grid">
    <div data-reveal>
      <p class="eyebrow">Our story</p>
      <h2 class="h2" id="about-title">Industrial excellence since 1968.</h2>
    </div>
    <div class="about-copy" data-reveal>
      <p>Riverstick Industries has been a trusted name in premium industrial materials for over five decades. We specialise in providing high-quality bark mulch, rubber matting, and specialised flooring solutions to commercial, industrial, and residential clients.</p>
      <p>Our commitment to quality, reliability, and customer service has made us the preferred choice for contractors, landscapers, and facility managers throughout Ireland and beyond.</p>
    </div>
  </div></div>
</section>

{contact_section()}
</main>
""" + footer()


def product_page(idx):
    p = PRODUCTS[idx]
    benefits = "".join(f'<li>{icon("check")}<span>{b}</span></li>' for b in p["benefits"])
    cols = f'<div class="spec"><h3>{p["list_title"]}</h3><ul>{"".join(f"<li>{x}</li>" for x in p["list"])}</ul></div>'
    if p.get("delivery"):
        cols += f'<div class="spec"><h3>Delivery &amp; collection</h3><p>{p["delivery"]}</p></div>'
    if p.get("note"):
        cols += f'<div class="spec"><h3>Materials</h3><p>{p["note"]}</p></div>'
    others = "\n    ".join(product_card(o, short=True, sizes="(max-width: 900px) 100vw, 33vw") for o in PRODUCTS if o is not p)
    eyebrow = p.get("eyebrow", p["name"])
    crumbs_ld = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": "Products", "item": SITE + "/#products"},
        {"@type": "ListItem", "position": 3, "name": p["name"], "item": f"{SITE}/{p['slug']}"}]}
    product_ld = {"@context": "https://schema.org", "@type": "Product", "name": p["name"], "description": p["meta"],
                  "image": f"{SITE}/images/{p['img']}-1600.webp", "brand": {"@type": "Brand", "name": "Riverstick Industries"},
                  "manufacturer": {"@id": SITE + "/#business"}}
    title = f"{p['name']} | Riverstick Industries, Cork"
    return head(title, p["meta"], f"/{p['slug']}", preload=p["img"], extra_ld=[crumbs_ld, product_ld]) + header("products") + f"""
<main id="main">
<section class="intro">
  <div class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a><span>/</span><a href="/#products">Products</a><span>/</span><span aria-current="page">{p['short']}</span></nav>
    <div class="intro-grid">
      <div>
        <p class="eyebrow">{eyebrow}</p>
        <h1 class="display">{p['h1']}</h1>
      </div>
      <div class="intro-side">
        <p class="kicker">{p['kicker']}</p>
        <p class="lead">{p['lead']}</p>
        <div class="actions">
          <a class="btn" href="tel:{PHONE_TEL}">Call to Enquire</a>
          <a class="btn btn-quiet" href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>
        </div>
      </div>
    </div>
  </div>
  <div class="wrap">
    <div class="hero hero-static">{picture(p['img'], p['name'], eager=True)}</div>
  </div>
</section>

<section class="section">
  <div class="wrap detail-grid">
    <div data-reveal>
      <h2 class="h2">{p['benefits_title']}</h2>
    </div>
    <div data-reveal>
      <ul class="benefits">{benefits}</ul>
      <div class="specs">{cols}</div>
    </div>
  </div>
</section>

<section class="section cta" aria-labelledby="cta-title">
  <div class="wrap"><div class="cta-inner" data-reveal>
    <div>
      <h2 class="h2" id="cta-title">Ready to discuss your project?</h2>
      <p class="lead">Our experienced team is here to help you find the perfect materials for your needs.</p>
    </div>
    <div class="actions">
      <a class="btn" href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a>
      <span class="muted small">Monday to Friday, 9:00 to 17:30</span>
    </div>
  </div></div>
</section>

<section class="section section-tight" aria-labelledby="more-title">
  <div class="wrap">
    <div class="row-head" data-reveal>
      <h2 class="h3" id="more-title">Also from Riverstick</h2>
      <a class="text-link" href="/#products">All products</a>
    </div>
    <div class="more-grid">
    {others}
    </div>
  </div>
</section>
</main>
""" + footer()


def not_found():
    return head("Page not found | Riverstick Industries", "The page you were looking for could not be found.", "/404") + header() + f"""
<main id="main" class="nf">
  <div class="wrap">
    <p class="eyebrow">404</p>
    <h1 class="display">This page could not be found.</h1>
    <p class="lead">Head back home, or give us a call and we'll point you in the right direction.</p>
    <div class="actions">
      <a class="btn" href="/">Back to home</a>
      <a class="btn btn-quiet" href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>
    </div>
  </div>
</main>
""" + footer()


def sitemap():
    today = datetime.date.today().isoformat()
    urls = [("/", "1.0")] + [(f"/{p['slug']}", "0.8") for p in PRODUCTS]
    body = "".join(f"  <url><loc>{SITE}{u}</loc><lastmod>{today}</lastmod><priority>{pr}</priority></url>\n" for u, pr in urls)
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{body}</urlset>\n'


if __name__ == "__main__":
    (ROOT / "index.html").write_text(home())
    for i, p in enumerate(PRODUCTS):
        (ROOT / f"{p['slug']}.html").write_text(product_page(i))
    (ROOT / "404.html").write_text(not_found())
    (ROOT / "sitemap.xml").write_text(sitemap())
    print("Built:", ", ".join(["index.html"] + [p["slug"] + ".html" for p in PRODUCTS] + ["404.html", "sitemap.xml"]))
