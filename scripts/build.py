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
<meta name="theme-color" content="#140b0c">
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
      <img src="/images/logo-mark.webp" width="34" height="37" alt="">
      <span class="brand-name"><b>Riverstick</b><small>Industries · Est. 1968</small></span>
    </a>
    <nav class="nav" aria-label="Main navigation">
      <a href="/"{cur('home')}>Home</a>
      <a href="/#products"{cur('products')}>Products</a>
      <a href="/#about">About</a>
      <a href="/#contact">Contact</a>
      <a class="btn" href="tel:{PHONE_TEL}">{icon('phone')}Call Now</a>
    </nav>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="mobile-menu" aria-label="Open menu"><span></span></button>
  </div>
</header>
<div class="mobile-menu" id="mobile-menu">
  <nav aria-label="Mobile navigation">
    <a href="/">Home <small>01</small></a>
    <a href="/#products">Products <small>02</small></a>
    <a href="/#about">About <small>03</small></a>
    <a href="/#contact">Contact <small>04</small></a>
  </nav>
  <a class="btn" href="tel:{PHONE_TEL}">{icon('phone')}Call {PHONE_DISPLAY}</a>
  <p class="mm-meta">Mon to Fri, 9:00 to 17:30</p>
</div>
"""


def footer():
    plinks = "".join(f'<li><a href="/{p["slug"]}">{p["short"]}</a></li>' for p in PRODUCTS)
    return f"""<footer class="footer">
  <div class="wrap">
    <div class="footer-top">
      <div class="footer-brand">
        <img src="/images/logo-full.webp" width="150" height="227" alt="Riverstick Industries, established 1968" loading="lazy">
        <p>A trusted name in premium industrial materials for over five decades. Quality Irish materials with expert support.</p>
      </div>
      <div>
        <h4>Products</h4>
        <ul>{plinks}</ul>
      </div>
      <div>
        <h4>Quick Links</h4>
        <ul>
          <li><a href="/">Home</a></li>
          <li><a href="/#products">Products</a></li>
          <li><a href="/#about">About</a></li>
          <li><a href="/#contact">Contact</a></li>
          <li><a href="tel:{PHONE_TEL}">Call Now</a></li>
        </ul>
      </div>
      <div>
        <h4>Contact Info</h4>
        <a class="f-phone" href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>
        <address>{ADDRESS_HTML}</address>
        <p class="f-hours">Mon to Fri: 9:00 to 17:30<br>Sat and Sun: Closed</p>
      </div>
    </div>
  </div>
  <div class="footer-word" aria-hidden="true">Riverstick</div>
  <div class="wrap">
    <div class="footer-bottom">
      <span>© <span data-year>{datetime.date.today().year}</span> Riverstick Industries. All rights reserved.</span>
      <a href="https://donworthstudio.ie/" target="_blank" rel="noopener noreferrer"><img src="/images/donworth-d-emblem.svg" width="16" height="16" alt="">Designed &amp; Developed by Donworth Studio</a>
    </div>
  </div>
</footer>
<a class="fab" href="tel:{PHONE_TEL}" aria-label="Call Riverstick Industries on {PHONE_DISPLAY}">{icon('phone')}</a>
<script src="/js/site.js" defer></script>
</body>
</html>
"""


def picture(img, alt, eager=False, sizes="100vw", cls=""):
    load = 'fetchpriority="high" decoding="async"' if eager else 'loading="lazy" decoding="async"'
    c = f' class="{cls}"' if cls else ""
    return (f'<img{c} src="/images/{img}-1600.webp" srcset="/images/{img}-960.webp 960w, /images/{img}-1600.webp 1600w" '
            f'sizes="{sizes}" alt="{escape(alt)}" {load}>')


def product_card(p, i, small=False):
    h = "h3"
    return f"""<a class="p-card" href="/{p['slug']}" data-reveal style="--d:{(i % 2) * .08 if not small else i * .08:.2f}s">
      <div class="p-media">{picture(p['img'], p['name'], sizes='(max-width: 900px) 100vw, 50vw')}<span class="tag">{i + 1:02d}</span></div>
      <div class="p-body">
        <h3 class="{h}">{p['name']}</h3>
        {'' if small else f"<p>{p['card']}</p>"}
        <span class="link-arrow">More Info {icon('arrow')}</span>
      </div>
    </a>"""


def contact_section():
    return f"""<section class="section" id="contact" aria-labelledby="contact-title">
  <div class="wrap contact-grid">
    <div class="contact-copy" data-reveal>
      <span class="eyebrow">Get In Touch</span>
      <h2 class="h2" id="contact-title">Let's talk about <em>your project.</em></h2>
      <p class="lead">Ready to discuss your project? Our experienced team is here to help you find the perfect materials for your needs.</p>
      <a class="phone-big" href="tel:{PHONE_TEL}" aria-label="Call {PHONE_DISPLAY}"><span class="ic">{icon('phone')}</span>{PHONE_DISPLAY}</a>
      <div class="info-grid">
        <div class="info">
          <h3>Address</h3>
          <address>{ADDRESS_HTML}</address>
        </div>
        <div class="info">
          <h3>Opening Hours</h3>
          <dl class="hours">
            <dt>Mon to Fri</dt><dd>9:00 to 17:30</dd>
            <dt>Saturday</dt><dd>Closed</dd>
            <dt>Sunday</dt><dd>Closed</dd>
          </dl>
          <span class="status" data-open-status hidden></span>
        </div>
      </div>
      <div class="contact-ctas">
        <a class="btn btn-dark" href="tel:{PHONE_TEL}">{icon('phone')}Call Now for Quote</a>
        <a class="btn btn-line" href="{MAPS}" target="_blank" rel="noopener noreferrer">{icon('pin')}Get Directions</a>
      </div>
    </div>
    <div class="map-card" data-reveal style="--d:.12s">
      <div class="map-frame">
        <div class="map-fallback" aria-hidden="true"><span class="pin"></span><span>Curra, Riverstick, Co. Cork</span></div>
        <iframe title="Map showing Riverstick Industries, Curra, Riverstick, Co. Cork" src="{MAP_EMBED}" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
      </div>
      <div class="map-meta">
        <div>
          <h3>Find Us Here</h3>
          <address>Curra, Riverstick, Co. Cork, Ireland, P43 EY24</address>
        </div>
        <a class="btn" href="{MAPS}" target="_blank" rel="noopener noreferrer">Open in Google Maps {icon('arrow', ' class="arrow"')}</a>
      </div>
      <p class="map-note">Get precise directions and explore the area around our Riverstick location.</p>
    </div>
  </div>
</section>"""


def home():
    slides = "".join(
        f'<div class="hero-slide{" is-active" if i == 0 else ""}">{picture(p["img"], p["name"], eager=(i == 0))}</div>'
        for i, p in enumerate(PRODUCTS))
    rail = "".join(
        f'<li{" class=\"is-active\"" if i == 0 else ""}><button type="button" aria-label="Show {p["name"]}">'
        f'<span class="bar"><i></i></span><span class="num">{i + 1:02d}</span>'
        f'<span class="t">{p["name"]}</span><span class="d">{p["tagline"]}</span></button></li>'
        for i, p in enumerate(PRODUCTS))
    cards = "\n    ".join(product_card(p, i) for i, p in enumerate(PRODUCTS))
    sectors = ["Contractors", "Landscapers", "Facility Managers", "Garden Beds", "Stables &amp; Horse Walkers",
               "Gym Flooring", "Workshops", "Agriculture", "Patios &amp; Walkways", "Commercial Spaces"]
    marquee = "".join(f"<span>{s}</span>" for s in sectors) * 2
    return head("Riverstick Industries | Premium Industrial Materials | Cork, Ireland",
                "Premium bark mulch, rubber matting, horse walker matting and rubber bricks. Quality Irish industrial materials since 1968, with expert support and fast delivery across Cork.",
                "/", preload="bark-mulch") + header("home") + f"""
<main id="main">
<section class="hero" data-carousel aria-roledescription="carousel" aria-label="Our products">
  <div class="hero-slides">{slides}</div>
  <div class="hero-body">
    <div class="wrap">
      <div class="hero-copy">
        <span class="eyebrow light">Est. 1968 · Riverstick, Co. Cork</span>
        <h1 class="display">Premium industrial materials, <em>built to last.</em></h1>
        <p class="lead">Bark mulch, rubber matting, horse walker matting and rubber bricks for commercial, industrial and residential clients throughout Ireland and beyond.</p>
        <div class="hero-ctas">
          <a class="btn" href="tel:{PHONE_TEL}">{icon('phone')}Call to Order</a>
          <a class="btn btn-ghost" href="#products">Explore Products {icon('arrow', ' class="arrow"')}</a>
        </div>
      </div>
    </div>
  </div>
  <nav class="hero-rail" aria-label="Carousel navigation"><div class="wrap"><ol>{rail}</ol></div></nav>
</section>

<section class="trust" aria-label="Why Riverstick">
  <div class="wrap">
    <div class="trust-item"><span class="ic">{icon('award')}</span><span>Since 1968<small>Over five decades of trust</small></span></div>
    <div class="trust-item"><span class="ic">{icon('shield')}</span><span>Quality Guaranteed<small>Built to the highest standards</small></span></div>
    <div class="trust-item"><span class="ic">{icon('truck')}</span><span>Fast Delivery<small>Across Cork and beyond</small></span></div>
    <div class="trust-item"><span class="ic">{icon('support')}</span><span>Expert Support<small>Talk to our experienced team</small></span></div>
  </div>
</section>

<section class="section" id="products" aria-labelledby="products-title">
  <div class="wrap">
    <div class="section-head">
      <div data-reveal>
        <span class="eyebrow">Our Product Range</span>
        <h2 class="h2" id="products-title">Materials for every <em>surface and setting.</em></h2>
      </div>
      <p class="lead" data-reveal style="--d:.1s">Discover our comprehensive selection of premium industrial materials, each crafted to meet the highest standards of quality and durability.</p>
    </div>
    <div class="products">
    {cards}
    </div>
  </div>
</section>

<div class="marquee" aria-hidden="true"><div class="marquee-track">{marquee}</div></div>

<section class="section on-dark about" id="about" aria-labelledby="about-title">
  <div class="wrap">
    <div class="about-grid">
      <div class="about-copy" data-reveal>
        <span class="eyebrow">Our Story</span>
        <h2 class="h2" id="about-title">Industrial excellence <em>since 1968.</em></h2>
        <p>Riverstick Industries has been a trusted name in premium industrial materials for over five decades. We specialise in providing high-quality bark mulch, rubber matting, and specialised flooring solutions to commercial, industrial, and residential clients.</p>
        <p>Our commitment to quality, reliability, and customer service has made us the preferred choice for contractors, landscapers, and facility managers throughout Ireland and beyond.</p>
      </div>
      <div class="about-visual" data-reveal style="--d:.12s" aria-hidden="true">
        <span class="ring"></span>
        <img src="/images/logo-mark.webp" width="222" height="240" alt="" loading="lazy">
        <span class="year">1968</span>
      </div>
    </div>
    <div class="pillars">
      <div class="pillar" data-reveal><span class="ic">{icon('shield')}</span><h3>Quality Guaranteed</h3><p>Every material crafted to meet the highest standards of quality and durability.</p></div>
      <div class="pillar" data-reveal style="--d:.08s"><span class="ic">{icon('truck')}</span><h3>Fast Delivery</h3><p>Reliable delivery across Cork, with collection also available on bark mulch.</p></div>
      <div class="pillar" data-reveal style="--d:.16s"><span class="ic">{icon('support')}</span><h3>Expert Support</h3><p>An experienced team on hand to help you find the perfect materials for your needs.</p></div>
    </div>
  </div>
</section>

{contact_section()}
</main>
""" + footer()


def product_page(idx):
    p = PRODUCTS[idx]
    benefits = "".join(
        f'<div class="benefit" data-reveal style="--d:{(i % 2) * .08:.2f}s"><div class="top"><span class="ic">{icon("check")}</span>'
        f'<span class="n">{i + 1:02d}</span></div><h3>{b}</h3></div>' for i, b in enumerate(p["benefits"]))
    items = "".join(f"<li>{x}</li>" for x in p["list"])
    details = f'<div class="detail" data-reveal><h3>{p["list_title"]}</h3><ul>{items}</ul></div>'
    if p.get("delivery"):
        details += f'<div class="detail" data-reveal style="--d:.08s"><h3>Delivery &amp; Collection</h3><p>{p["delivery"]}</p></div>'
    if p.get("note"):
        details += (f'<div class="detail dark" data-reveal style="--d:.16s"><span class="leaf">{icon("leaf")}</span>'
                    f'<p>{p["note"]}</p></div>')
    others = "\n    ".join(product_card(o, j, small=True).replace(f'<span class="tag">{j + 1:02d}</span>', f'<span class="tag">{PRODUCTS.index(o) + 1:02d}</span>')
                           for j, o in enumerate([x for x in PRODUCTS if x is not p]))
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
<section class="p-hero">
  {picture(p['img'], p['name'], eager=True)}
  <div class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a>{icon('chev')}<a href="/#products">Products</a>{icon('chev')}<span aria-current="page">{p['short']}</span></nav>
    <div class="hero-copy">
      <span class="eyebrow light">{eyebrow}</span>
      <h1 class="display">{p['h1']}</h1>
      <span class="kicker">{p['kicker']}</span>
      <p class="lead">{p['lead']}</p>
      <div class="hero-ctas">
        <a class="btn" href="tel:{PHONE_TEL}">{icon('phone')}Call to Enquire</a>
        <a class="btn btn-ghost" href="#details">Learn More {icon('arrow', ' class="arrow"')}</a>
      </div>
    </div>
  </div>
  <span class="p-index" aria-hidden="true">{idx + 1:02d}</span>
</section>

<section class="section" id="details">
  <div class="wrap">
    <div class="benefits-grid">
      <div class="sticky" data-reveal>
        <span class="eyebrow">{p['short']}</span>
        <h2 class="h2">{p['benefits_title']}</h2>
        <p class="lead">{p['card']}</p>
      </div>
      <div class="benefits">{benefits}</div>
    </div>
    <div class="detail-grid">{details}</div>
  </div>
</section>

<section class="section on-dark cta-band" aria-labelledby="cta-title">
  <div class="wrap cta-inner">
    <div data-reveal>
      <span class="eyebrow">Call to Enquire</span>
      <h2 class="h2" id="cta-title">Ready to discuss <em>your project?</em></h2>
      <p class="lead">Our experienced team is here to help you find the perfect materials for your needs.</p>
    </div>
    <div class="cta-side" data-reveal style="--d:.1s">
      <a class="phone" href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>
      <small>Monday to Friday, 9:00 to 17:30 · Curra, Riverstick, Co. Cork</small>
      <a class="btn" href="tel:{PHONE_TEL}">{icon('phone')}Call Now for Quote</a>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="more-title">
  <div class="wrap">
    <div class="section-head">
      <div data-reveal>
        <span class="eyebrow">Our Product Range</span>
        <h2 class="h2" id="more-title">Explore the <em>full range.</em></h2>
      </div>
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
<main id="main" class="on-dark nf">
  <div>
    <span class="eyebrow">Error 404</span>
    <h1 class="display" style="margin-top:22px">This page has <em>moved on.</em></h1>
    <p class="lead">The page you were looking for doesn't exist. Head back home or give us a call and we'll point you in the right direction.</p>
    <div class="hero-ctas" style="justify-content:center">
      <a class="btn" href="/">Back to Home {icon('arrow', ' class="arrow"')}</a>
      <a class="btn btn-ghost" href="tel:{PHONE_TEL}">{icon('phone')}{PHONE_DISPLAY}</a>
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
