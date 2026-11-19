from pathlib import Path
from html import escape as e
import json
BASE='https://www.riverstickindustries.ie'
TEL='tel:+353214771362'
MAP='https://www.google.com/maps/search/?api=1&query=Curra,+Riverstick,+Co.+Cork,+Ireland+P43+EY24'
P=[
('bark-mulch','Bark mulch','Landscaping','bark-mulch','A natural finish for outdoor spaces.','Natural wood-based bark mulch for landscaping, garden beds and erosion control. Available in fine and medium grades.',['Retains soil moisture','Helps to suppress weeds naturally','Protects plant roots','Breaks down naturally','Brings a neat, natural finish'],['Fine bark mulch','Medium bark mulch'],'Delivery is available for a minimum of 10 cubic metres. Collection is also available. Our bark is sustainably sourced, locally processed and free from dyes or harsh chemicals.','A landscaped bed of rich bark mulch and low planting'),
('rubber-matting','Industrial rubber matting','Industrial & agricultural','rubber-matting','Flooring built for hard work.','Durable, recycled rubber matting for commercial, industrial and everyday spaces.',['Slip-resistant surface','Shock-absorbing comfort','Built for heavy use','Low maintenance','Reduces noise and vibration'],['Stable and horse mats','Gym flooring','Industrial and workshop matting','Agricultural matting','Entrance and anti-slip mats'],'','Close-up of textured rubber drainage mats'),
('horse-walker-matting','Horse walker matting','Equestrian','horse-walker','Built for hooves in motion.','Durable, non-slip rubber flooring for horse walkers and equestrian areas, with excellent grip and comfort that helps reduce bedding and maintenance costs.',['Slip-resistant surface','Shock-absorbing comfort for joints','Easy to clean and hose down','Custom sizes available'],['Horse walkers','Training rings','Equine rehabilitation areas'],'','Outdoor horse walker in an equestrian setting'),
('rubber-bricks','Rubber bricks','Interlocking surfaces','rubber-bricks','Interlocking strength for everyday spaces.','Durable interlocking rubber brick flooring for patios, walkways and commercial spaces. Easy to install and designed to last.',['Slip-resistant surface','Shock-absorbing','Fast interlocking installation','Suitable for wet and dry environments'],['Patios and paths','Commercial walkways','Stables and farm lanes','Industrial floor safety zones'],'','Pattern of interlocking charcoal rubber bricks')]
def a(h,t,cls=''):
 return f'<a class="{cls}" href="{e(h,quote=True)}">{t}</a>'
def tag(t):return f'<p class="eyebrow">{t}</p>'
def brand():
 return '<a href="/" class="brand" aria-label="Riverstick Industries home"><span class="mark" aria-hidden="true">R<span>.</span></span><span>RIVERSTICK<small>INDUSTRIES</small></span></a>'
def shell(title,description,route,body,img,product=None):
 url=BASE+route
 schema={'@context':'https://schema.org','@type':'LocalBusiness','@id':BASE+'/#business','name':'Riverstick Industries','url':BASE+'/','telephone':'+353214771362','foundingDate':'1968','image':BASE+'/images/riverstick_industries_logo_transparent.png','address':{'@type':'PostalAddress','streetAddress':'Curra, Riverstick','addressRegion':'Co. Cork','postalCode':'P43 EY24','addressCountry':'IE'},'openingHours':'Mo-Fr 09:00-17:30'}
 if product:
  schema={'@context':'https://schema.org','@graph':[schema,{'@type':'Product','name':product,'url':url,'image':BASE+img,'description':description,'brand':{'@id':BASE+'/#business'}}]}
 return f'''<!doctype html>
<html lang="en-IE">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title><meta name="description" content="{e(description)}">
<link rel="canonical" href="{url}">
<meta property="og:site_name" content="Riverstick Industries"><meta property="og:type" content="website">
<meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(description)}">
<meta property="og:url" content="{url}"><meta property="og:image" content="{BASE+img}">
<link rel="icon" href="/favicon.png"><link rel="stylesheet" href="/refurb.css">
<script type="application/ld+json">{json.dumps(schema,ensure_ascii=False)}</script>
</head><body>
<a class="skip" href="#main">Skip to content</a>
<div class="topline"><div class="wrap topinner"><span>RIVERSTICK, COUNTY CORK</span><span>ESTABLISHED 1968</span></div></div>
<header class="mast"><div class="wrap mastinner">{brand()}<nav aria-label="Main navigation">{a('/#products','Products')}{a('/#about','About')}{a('/#contact','Contact')}</nav>{a(TEL,'021 477 1362 <span aria-hidden="true">↗</span>','mastcall')}</div></header>
{body}
<footer><div class="wrap foot"><div>{brand()}<p>Materials for landscapes, workplaces and equestrian spaces.</p></div><div class="footlinks">{a('/#products','Products')}{a('/#about','About')}{a('/#contact','Contact')}</div><a class="credit" href="https://donworthstudio.ie"><img src="/images/donworth-d-emblem.svg" width="21" height="21" alt=""> Donworth Studio</a></div><div class="wrap legal">© Riverstick Industries <span>CURRA · RIVERSTICK · CORK</span></div></footer>
</body></html>
'''
def card(i,p):
 slug,title,cat,img,_,desc,*_=p
 return f'''<a class="material" href="/{slug}"><div class="materialshot"><img loading="lazy" src="/images/{img}-hero.webp" alt=""></div><div class="cardcopy">{tag(f'<span>0{i}</span> / {cat}')}<h3>{title}</h3><p>{desc}</p><span class="card-arrow" aria-hidden="true">↗</span></div></a>'''
def contact():
 return f'''<section class="contact" id="contact"><div class="wrap contactgrid"><div>{tag('03 / CONTACT')}<h2>Let’s talk<br>materials.</h2><p>Tell us what you’re working on and we’ll help you choose the right material for the job.</p>{a(TEL,'Call 021 477 1362 <span aria-hidden="true">↗</span>','button primary')}</div><div class="info"><div>{tag('FIND US')}<address>Curra, Riverstick<br>Co. Cork, Ireland<br>P43 EY24</address>{a(MAP,'Get directions ↗','textlink')}</div><div>{tag('OPENING HOURS')}<p>Monday to Friday<br>9:00 am – 5:30 pm</p><p>Saturday &amp; Sunday<br>Closed</p></div></div></div></section>'''
def home():
 hero=f'''<main id="main"><section class="hero"><div class="wrap hero-grid"><div class="herocopy">{tag('MATERIALS SUPPLIER / COUNTY CORK')}<h1>The groundwork<br>for better <em>spaces.</em></h1><p>Bark mulch, rubber matting and specialised flooring for landscaping, industry and equestrian spaces.</p><div class="actions">{a('#products','Explore materials <span aria-hidden="true">↓</span>','button primary')}{a('#contact','Talk to us <span aria-hidden="true">↗</span>','button quiet')}</div></div><figure class="heroshot"><picture><source media="(max-width:650px)" srcset="/images/bark-mulch-hero-mobile.webp"><img src="/images/bark-mulch-hero.webp" alt="Bark mulch framing a planted garden" fetchpriority="high"></picture><figcaption><span>01 / LANDSCAPING</span><span>BARK MULCH</span></figcaption></figure></div></section>
<section class="strip"><div class="wrap stripgrid"><span>01 <b>Quality guaranteed</b></span><span>02 <b>Fast delivery</b></span><span>03 <b>Expert support</b></span></div></section>
<section class="range wrap" id="products"><div class="sectionhead"><div>{tag('01 / PRODUCT RANGE')}<h2>Find your<br><em>surface.</em></h2></div><p>Four ranges for gardens, workplaces and equestrian facilities. Browse the options or give us a call for advice.</p></div><div class="materialgrid">{''.join(card(i,p) for i,p in enumerate(P,1))}</div></section>
<section class="about" id="about"><div class="wrap aboutgrid"><div class="heritage" aria-hidden="true"><span>ESTABLISHED</span><strong>1968</strong><span>RIVERSTICK · COUNTY CORK</span></div><div>{tag('02 / ABOUT RIVERSTICK')}<h2>Grounded<br>in <em>Cork.</em></h2><p>Riverstick Industries has supplied materials from Cork since 1968. We work with contractors, landscapers and facility managers, as well as homeowners, across commercial, industrial and residential projects.</p><p>Our focus is straightforward: reliable materials and practical advice for the job in front of you.</p></div></div></section>{contact()}</main>'''
 return shell('Riverstick Industries | Bark Mulch & Rubber Matting, Cork','Cork supplier of bark mulch, industrial rubber matting, horse walker flooring and rubber bricks. Based in Riverstick since 1968.','/',hero,'/images/bark-mulch-hero.webp')
def product(i,p):
 slug,t,cat,img,headline,desc,features,uses,extra,alt=p
 lists=lambda vs: ''.join(f'<li>{e(v)}</li>' for v in vs)
 body=f'''<main id="main"><section class="product-hero wrap"><a class="crumb" href="/#products">← All materials</a><div class="productgrid"><div>{tag(f'0{i} / {cat}')}<h1>{e(t)}</h1><p class="standfirst">{headline}</p><p>{desc}</p>{a(TEL,'Call to enquire <span aria-hidden="true">↗</span>','button primary')}</div><figure class="productshot"><img src="/images/{img}-hero.webp" alt="{alt}" fetchpriority="high"><figcaption><span>0{i} / MATERIALS</span><span>{t}</span></figcaption></figure></div></section>
<section class="spec"><div class="wrap specgrid"><div>{tag('THE MATERIAL')}<h2>Key features.</h2><ul>{lists(features)}</ul></div><div>{tag('THE APPLICATION')}<h2>{'Grades available.' if i==1 else 'Where it works.'}</h2><ul>{lists(uses)}</ul></div></div>{f'<div class="wrap delivery">{tag("DELIVERY &amp; COLLECTION")}<p>{e(extra)}</p></div>' if extra else ''}</section>
<section class="wrap related"><div class="sectionhead"><div>{tag('THE RANGE')}<h2>Other <em>materials.</em></h2></div>{a('/#products','See all materials ↗','textlink')}</div><div class="materialgrid">{''.join(card(j,q) for j,q in enumerate(P,1) if j!=i)}</div></section>{contact()}</main>'''
 return shell(f'{t} | Riverstick Industries, Cork',desc,'/'+slug,body,f'/images/{img}-hero.webp',t)
Path('index.html').write_text(home())
for i,p in enumerate(P,1): Path(p[0]+'.html').write_text(product(i,p))
Path('sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f'  <url><loc>{BASE}{r}</loc></url>\n' for r in ['/',*('/'+v[0] for v in P)])+'</urlset>\n')
Path('robots.txt').write_text('User-agent: *\nAllow: /\n\nSitemap: '+BASE+'/sitemap.xml\n')
