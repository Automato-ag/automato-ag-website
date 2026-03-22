import os

# ── STRIPE PAYMENT LINKS ──────────────────────────────────────────────────────
# Replace these with your real Stripe Payment Link URLs from your Stripe dashboard.
# In Stripe: Dashboard → Payment Links → + New → set product name & price → copy URL
STRIPE_BRAIN_BOARD  = 'https://buy.stripe.com/dRm4gyalU1zi2n28yl5os01'   # $25
STRIPE_SENSOR_BOARD = 'https://buy.stripe.com/14A5kCgKidi0aTy7uh5os02'  # $30
STRIPE_RELAY_BOARD  = 'https://buy.stripe.com/fZu00i3Xw5Pyf9O8yl5os03'   # $32

# ── FORMSPREE ENDPOINT ────────────────────────────────────────────────────────
# Steps to get your endpoint (free, ~2 min):
#   1. Go to https://formspree.io and sign up with automato.llc@gmail.com
#   2. Click "+ New Form", name it "Automato Contact"
#   3. Copy the endpoint URL — looks like https://formspree.io/f/xabcdefg
#   4. Paste it below, replacing the placeholder
FORMSPREE_ENDPOINT  = 'https://formspree.io/f/mgonzogn'

shared_css = """/* shared styles — automato.ag */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
:root {
  --cream: #fdf8f0; --cream-mid: #f5f0e4; --cream-dark: #f0ede4;
  --card-bg: #fffdf8; --border: #e2d8c4; --border-soft: #ede4d0;
  --green: #3d6b2c; --green-light: #5a9a3a; --green-pale: #eaf5de; --green-tag: #c0dca0;
  --amber: #c47a2a; --amber-pale: #fdf0dc; --amber-tag: #e8cc9a;
  --text-dark: #1e2e14; --text-body: #5a4a30; --text-mid: #6a5a40; --text-muted: #7a6a50; --text-light: #a08060;
  --footer-bg: #2a1e0e; --footer-text: #c8d8b0; --footer-muted: #6a5a3a;
}
html { scroll-behavior: smooth; }
body { font-family: 'DM Sans', sans-serif; background: var(--cream); color: var(--text-dark); font-size: 16px; line-height: 1.6; }
a { color: inherit; text-decoration: none; }
.mono { font-family: 'DM Mono', monospace; }
.container { max-width: 1100px; margin: 0 auto; padding: 0 2.5rem; }
.section { padding: 4.5rem 0; }
hr.divider { border: none; border-top: 1px solid var(--border); }
.section-label { font-family: 'DM Mono', monospace; font-size: 11px; color: var(--amber); letter-spacing: .15em; text-transform: uppercase; margin-bottom: .5rem; }
.section-title { font-size: 32px; font-weight: 700; color: var(--text-dark); margin-bottom: .4rem; }
.section-sub { font-size: 15px; color: var(--text-muted); margin-bottom: 2.5rem; line-height: 1.65; }
.btn-primary { background: var(--green); color: #fff; font-family: 'DM Sans',sans-serif; font-weight: 600; font-size: 14px; padding: 13px 26px; border-radius: 24px; border: none; cursor: pointer; display: inline-block; }
.btn-primary:hover { background: #4a8035; }
.btn-ghost { background: transparent; color: var(--green); font-family: 'DM Sans',sans-serif; font-weight: 600; font-size: 14px; padding: 12px 26px; border-radius: 24px; border: 2px solid var(--green-tag); cursor: pointer; display: inline-block; }
.btn-ghost:hover { background: var(--green-pale); }
.btn-amber { background: var(--amber); color: #fff; font-family: 'DM Sans',sans-serif; font-weight: 600; font-size: 14px; padding: 13px 26px; border-radius: 24px; border: none; cursor: pointer; display: inline-block; }
.btn-amber:hover { background: #b06820; }
.nav { position: sticky; top: 0; z-index: 100; background: var(--card-bg); border-bottom: 1px solid var(--border); padding: 1rem 2.5rem; display: flex; align-items: center; justify-content: space-between; }
.nav-logo { font-size: 20px; font-weight: 700; color: var(--green); letter-spacing: .04em; }
.nav-logo span { color: var(--amber); }
.nav-links { display: flex; gap: 2rem; }
.nav-links a { font-size: 14px; color: var(--text-muted); transition: color .15s; }
.nav-links a:hover, .nav-links a.active { color: var(--green); font-weight: 600; }
.nav-cta { background: var(--green); color: #fff; font-family: 'DM Sans',sans-serif; font-weight: 600; font-size: 13px; padding: 9px 20px; border-radius: 20px; border: none; cursor: pointer; }
.nav-cta:hover { background: #4a8035; }
.nav-toggle { display: none; background: none; border: none; cursor: pointer; flex-direction: column; gap: 5px; padding: 4px; }
.nav-toggle span { display: block; width: 22px; height: 2px; background: var(--text-muted); border-radius: 2px; }
.footer-wrap { background: var(--footer-bg); }
.footer { padding: 2.5rem; display: flex; justify-content: space-between; align-items: center; max-width: 1100px; margin: 0 auto; flex-wrap: wrap; gap: 1rem; }
.footer-logo { font-size: 17px; font-weight: 700; color: var(--footer-text); }
.footer-logo span { color: #e8a84a; }
.footer-links { display: flex; gap: 1.5rem; flex-wrap: wrap; }
.footer-links a { font-size: 13px; color: #8a7a5a; transition: color .12s; }
.footer-links a:hover { color: var(--footer-text); }
.footer-copy { font-family: 'DM Mono', monospace; font-size: 11px; color: var(--footer-muted); }
.product-card { background: var(--card-bg); border: 1.5px solid var(--border); border-radius: 16px; overflow: hidden; position: relative; display: flex; flex-direction: column; }
.product-card.featured { border-color: var(--green-light); box-shadow: 0 0 0 3px #e8f5dc; }
.card-badge { position: absolute; top: 14px; right: 14px; background: var(--green); color: #fff; font-size: 10px; font-weight: 700; padding: 4px 12px; border-radius: 20px; letter-spacing: .06em; text-transform: uppercase; }
.card-image { width: 100%; aspect-ratio: 1.2; background: var(--cream-mid); display: flex; align-items: center; justify-content: center; border-bottom: 1.5px solid var(--border); }
.card-body { padding: 1.3rem 1.4rem; flex: 1; display: flex; flex-direction: column; }
.card-body h3 { font-size: 17px; font-weight: 700; margin-bottom: .4rem; }
.card-desc { font-size: 13px; color: var(--text-muted); line-height: 1.65; margin-bottom: 1rem; flex: 1; }
.card-specs { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 1.2rem; }
.spec-tag { font-family: 'DM Mono', monospace; font-size: 10px; color: var(--green); background: var(--green-pale); border: 1px solid var(--green-tag); padding: 3px 9px; border-radius: 20px; }
.card-footer { display: flex; align-items: center; justify-content: space-between; padding-top: 1rem; border-top: 1px solid var(--border-soft); }
.card-price { font-family: 'DM Mono', monospace; font-size: 26px; font-weight: 500; color: var(--green); }
.card-btn { background: var(--green); color: #fff; font-family: 'DM Sans',sans-serif; font-size: 13px; font-weight: 600; padding: 9px 18px; border-radius: 20px; border: none; cursor: pointer; }
.card-btn:hover { background: #4a8035; }
.card-btn-ghost { background: transparent; color: #5a7a44; font-family: 'DM Sans',sans-serif; font-size: 13px; font-weight: 600; padding: 9px 18px; border-radius: 20px; border: 1.5px solid var(--green-tag); cursor: pointer; }
.card-btn-ghost:hover { background: var(--green-pale); }
@media (max-width: 600px) {
  .nav-links, .nav-cta { display: none; }
  .nav-toggle { display: flex; }
  .nav-links.open { display: flex; flex-direction: column; position: absolute; top: 60px; left: 0; right: 0; background: var(--card-bg); border-bottom: 1px solid var(--border); padding: 1rem 2rem; gap: 1rem; z-index: 99; }
  .container { padding: 0 1.2rem; }
  .nav { padding: 1rem 1.2rem; }
  .section-title { font-size: 26px; }
}
"""

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet">'

def nav(active, prefix=''):
    links = [
        ('products.html', 'Products'),
        ('docs.html', 'Docs'),
        ('github.html', 'GitHub'),
        ('planting-calendar.html', 'Planting Calendar'),
        ('about.html', 'About'),
        ('contact.html', 'Contact'),
    ]
    items = ''
    for href, label in links:
        cls = ' class="active"' if label == active else ''
        items += f'<a href="{prefix}{href}"{cls}>{label}</a>'
    return f'''<nav class="nav">
  <a href="{prefix}index.html" class="nav-logo">Automato<span>.ag</span></a>
  <div class="nav-links" id="nav-links">{items}</div>
  <a class="nav-cta" href="{prefix}products.html">Shop now</a>
  <button class="nav-toggle" id="nav-toggle" aria-label="Menu"><span></span><span></span><span></span></button>
</nav>'''

def footer(prefix=''):
    return f'''<footer class="footer-wrap">
  <div class="footer">
    <a href="{prefix}index.html" class="footer-logo">Automato<span>.ag</span></a>
    <nav class="footer-links">
      <a href="{prefix}products.html">Products</a>
      <a href="{prefix}docs.html">Docs</a>
      <a href="{prefix}github.html">GitHub</a>
      <a href="{prefix}planting-calendar.html">Planting Calendar</a>
      <a href="{prefix}about.html">About</a>
      <a href="{prefix}contact.html">Contact</a>
    </nav>
    <p class="footer-copy">© 2026 Automato.ag</p>
  </div>
</footer>'''

def nav_script():
    return '''<script>
const t=document.getElementById('nav-toggle'),n=document.getElementById('nav-links');
t.addEventListener('click',()=>n.classList.toggle('open'));
n.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>n.classList.remove('open')));
</script>'''

def page(title, active, body, extra_css='', prefix=''):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{title} — Automato.ag</title>
{FONTS}
<style>
{shared_css}
{extra_css}
</style>
</head>
<body>
{nav(active, prefix)}
{body}
{footer(prefix)}
{nav_script()}
</body>
</html>'''

# ─── SVGs ──────────────────────────────────────────────────────────────────

brain_svg = '''<svg width="72%" viewBox="0 0 200 165" xmlns="http://www.w3.org/2000/svg">
  <rect width="200" height="165" fill="#f0ede4"/>
  <rect x="25" y="22" width="150" height="120" rx="10" fill="#fffdf8" stroke="#c8bc9a" stroke-width="2"/>
  <rect x="68" y="50" width="64" height="52" rx="6" fill="#eaf5de" stroke="#9acd7a" stroke-width="1.5"/>
  <text x="100" y="78" text-anchor="middle" font-family="monospace" font-size="8" fill="#3a7a2a">ESP32-C6</text>
  <text x="100" y="90" text-anchor="middle" font-family="monospace" font-size="6" fill="#6aaa4a">RISC-V WiFi 6</text>
  <rect x="36" y="40" width="24" height="18" rx="3" fill="#fdf0dc" stroke="#e0bc7a" stroke-width="1"/>
  <text x="48" y="52" text-anchor="middle" font-family="monospace" font-size="6" fill="#c47a2a">SHTC3</text>
  <rect x="140" y="40" width="30" height="18" rx="3" fill="#fdf0dc" stroke="#e0bc7a" stroke-width="1"/>
  <text x="155" y="52" text-anchor="middle" font-family="monospace" font-size="5.5" fill="#c47a2a">TSL2591</text>
  <rect x="36" y="108" width="24" height="16" rx="3" fill="#eaf5de" stroke="#9acd7a" stroke-width="1"/>
  <text x="48" y="119" text-anchor="middle" font-family="monospace" font-size="5.5" fill="#3a7a2a">Qwiic</text>
  <rect x="144" y="108" width="24" height="16" rx="3" fill="#eaf5de" stroke="#9acd7a" stroke-width="1"/>
  <text x="156" y="119" text-anchor="middle" font-family="monospace" font-size="5.5" fill="#3a7a2a">Qwiic</text>
  <circle cx="48" cy="142" r="5" fill="#5aaa3a"/><circle cx="65" cy="142" r="5" fill="#c47a2a"/><circle cx="82" cy="142" r="5" fill="#1a6a1a"/>
  <rect x="100" y="136" width="60" height="14" rx="3" fill="#eaf5de" stroke="#9acd7a"/>
  <text x="130" y="146" text-anchor="middle" font-family="monospace" font-size="6" fill="#3a7a2a">USB-C</text>
</svg>'''

sensor_svg = '''<svg width="72%" viewBox="0 0 200 165" xmlns="http://www.w3.org/2000/svg">
  <rect width="200" height="165" fill="#f0ede4"/>
  <rect x="25" y="22" width="150" height="120" rx="10" fill="#fffdf8" stroke="#c8bc9a" stroke-width="2"/>
  <rect x="62" y="38" width="76" height="56" rx="5" fill="#e8f0e0" stroke="#a0b888" stroke-width="1.5"/>
  <text x="100" y="62" text-anchor="middle" font-family="monospace" font-size="7.5" fill="#4a6a38">ESP32</text>
  <text x="100" y="74" text-anchor="middle" font-family="monospace" font-size="5.5" fill="#7a9a62">WROOM-DA</text>
  <rect x="148" y="42" width="22" height="36" rx="3" fill="#fdf0dc" stroke="#e0bc7a" stroke-width="1"/>
  <text x="159" y="63" text-anchor="middle" font-family="monospace" font-size="5.5" fill="#c47a2a">LoRa</text>
  <rect x="34" y="42" width="24" height="36" rx="3" fill="#f5f0e4" stroke="#d4c8a8" stroke-width="1"/>
  <line x1="34" y1="53" x2="58" y2="53" stroke="#e0d8c4" stroke-width="1"/>
  <line x1="34" y1="62" x2="58" y2="62" stroke="#e0d8c4" stroke-width="1"/>
  <line x1="34" y1="71" x2="58" y2="71" stroke="#e0d8c4" stroke-width="1"/>
  <text x="46" y="83" text-anchor="middle" font-family="monospace" font-size="5" fill="#8a9a7a">14x I/O</text>
  <rect x="38" y="105" width="60" height="24" rx="4" fill="#e8f0e0" stroke="#a0c888" stroke-width="1.5"/>
  <rect x="42" y="109" width="52" height="16" rx="2" fill="#c8e4c0"/>
  <text x="68" y="120" text-anchor="middle" font-family="monospace" font-size="6" fill="#2a5a1a">display</text>
  <rect x="108" y="105" width="22" height="12" rx="3" fill="#fdf0dc" stroke="#e0bc7a" stroke-width="1"/>
  <text x="119" y="114" text-anchor="middle" font-family="monospace" font-size="5" fill="#c47a2a">SD</text>
  <rect x="134" y="105" width="30" height="12" rx="3" fill="#eaf5de" stroke="#9acd7a" stroke-width="1"/>
  <text x="149" y="114" text-anchor="middle" font-family="monospace" font-size="5" fill="#3a7a2a">LiPo</text>
  <circle cx="44" cy="142" r="5" fill="#5aaa3a"/><circle cx="60" cy="142" r="5" fill="#c47a2a"/>
</svg>'''

relay_svg = '''<svg width="72%" viewBox="0 0 200 165" xmlns="http://www.w3.org/2000/svg">
  <rect width="200" height="165" fill="#f0ede4"/>
  <rect x="25" y="22" width="150" height="120" rx="10" fill="#fffdf8" stroke="#c8bc9a" stroke-width="2"/>
  <rect x="34" y="36" width="132" height="22" rx="4" fill="#f5f0e4" stroke="#d4c8a8" stroke-width="1"/>
  <text x="100" y="51" text-anchor="middle" font-family="monospace" font-size="6.5" fill="#8a7a5a">AC/DC — HLK-PM03</text>
  <rect x="42" y="70" width="28" height="44" rx="4" fill="#fdf0dc" stroke="#e0bc7a" stroke-width="1.5"/>
  <circle cx="56" cy="92" r="10" fill="#fff8f0" stroke="#e0bc7a"/><circle cx="56" cy="92" r="5" fill="#f0d8a0"/>
  <rect x="78" y="70" width="28" height="44" rx="4" fill="#fdf0dc" stroke="#e0bc7a" stroke-width="1.5"/>
  <circle cx="92" cy="92" r="10" fill="#fff8f0" stroke="#e0bc7a"/><circle cx="92" cy="92" r="5" fill="#f0d8a0"/>
  <rect x="114" y="70" width="28" height="44" rx="4" fill="#eaf5de" stroke="#9acd7a" stroke-width="1.5"/>
  <circle cx="128" cy="92" r="10" fill="#f4fbed" stroke="#9acd7a"/><circle cx="128" cy="92" r="5" fill="#b0e090"/>
  <rect x="148" y="70" width="22" height="44" rx="4" fill="#eaf5de" stroke="#9acd7a" stroke-width="1.5"/>
  <circle cx="159" cy="92" r="8" fill="#f4fbed" stroke="#9acd7a"/><circle cx="159" cy="92" r="4" fill="#b0e090"/>
  <rect x="50" y="126" width="100" height="10" rx="3" fill="#f5f0e4" stroke="#d4c8a8"/>
  <text x="100" y="134" text-anchor="middle" font-family="monospace" font-size="5.5" fill="#8a7a5a">4x relay — mains rated</text>
</svg>'''

# ─── HERO SVG ───────────────────────────────────────────────────────────────
hero_svg = '''<svg width="88%" viewBox="0 0 340 320" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="320" fill="#f0ede4"/>
  <ellipse cx="200" cy="285" rx="110" ry="24" fill="#e0d8c4" opacity="0.4"/>
  <rect x="90" y="80" width="160" height="130" rx="12" fill="#fffdf8" stroke="#c8bc9a" stroke-width="2"/>
  <rect x="110" y="100" width="70" height="55" rx="6" fill="#eaf5de" stroke="#9acd7a" stroke-width="1.5"/>
  <text x="145" y="128" text-anchor="middle" font-family="monospace" font-size="8" fill="#3a7a2a">ESP32-C6</text>
  <text x="145" y="141" text-anchor="middle" font-family="monospace" font-size="6" fill="#6aaa4a">BRAIN BOARD</text>
  <rect x="188" y="100" width="44" height="20" rx="4" fill="#fdf0dc" stroke="#e0bc7a" stroke-width="1"/>
  <text x="210" y="114" text-anchor="middle" font-family="monospace" font-size="7" fill="#c47a2a">SHTC3</text>
  <rect x="188" y="128" width="44" height="20" rx="4" fill="#fdf0dc" stroke="#e0bc7a" stroke-width="1"/>
  <text x="210" y="142" text-anchor="middle" font-family="monospace" font-size="7" fill="#c47a2a">TSL2591</text>
  <rect x="96" y="165" width="18" height="14" rx="3" fill="#fdf0dc" stroke="#e0bc7a" stroke-width="1"/>
  <rect x="120" y="165" width="18" height="14" rx="3" fill="#fdf0dc" stroke="#e0bc7a" stroke-width="1"/>
  <circle cx="220" cy="172" r="7" fill="#eaf5de" stroke="#9acd7a" stroke-width="1.5"/>
  <circle cx="220" cy="172" r="3.5" fill="#5aaa3a"/>
  <circle cx="234" cy="172" r="7" fill="#fdf0dc" stroke="#e0bc7a" stroke-width="1.5"/>
  <circle cx="234" cy="172" r="3.5" fill="#c4841a"/>
  <line x1="170" y1="210" x2="170" y2="240" stroke="#b8d090" stroke-width="2" stroke-dasharray="4,3"/>
  <rect x="130" y="240" width="80" height="48" rx="10" fill="#eaf5de" stroke="#9acd7a" stroke-width="1.5"/>
  <text x="170" y="260" text-anchor="middle" font-family="monospace" font-size="7" fill="#3a7a2a">Relay Board</text>
  <rect x="144" y="268" width="14" height="10" rx="2" fill="#fffdf8" stroke="#9acd7a"/>
  <rect x="163" y="268" width="14" height="10" rx="2" fill="#fffdf8" stroke="#9acd7a"/>
  <rect x="182" y="268" width="14" height="10" rx="2" fill="#c8e8b0" stroke="#7ab87a"/>
  <line x1="90" y1="145" x2="50" y2="145" stroke="#d4c8a8" stroke-width="1.5" stroke-dasharray="3,3"/>
  <rect x="18" y="120" width="36" height="50" rx="6" fill="#fffdf8" stroke="#d4c8a8" stroke-width="1.5"/>
  <text x="36" y="145" text-anchor="middle" font-family="monospace" font-size="6" fill="#8a9a7a">Qwiic</text>
  <text x="36" y="156" text-anchor="middle" font-family="monospace" font-size="6" fill="#8a9a7a">sensor</text>
  <line x1="250" y1="145" x2="290" y2="145" stroke="#d4c8a8" stroke-width="1.5" stroke-dasharray="3,3"/>
  <rect x="286" y="120" width="36" height="50" rx="6" fill="#fffdf8" stroke="#d4c8a8" stroke-width="1.5"/>
  <text x="304" y="145" text-anchor="middle" font-family="monospace" font-size="6" fill="#8a9a7a">WiFi</text>
  <text x="304" y="156" text-anchor="middle" font-family="monospace" font-size="6" fill="#8a9a7a">cloud</text>
</svg>'''

# ──────────────────────────────────────────────────────────────────────────────
# index.html
# ──────────────────────────────────────────────────────────────────────────────
index_css = '''
.hero { display:grid; grid-template-columns:1fr 1fr; gap:4rem; align-items:center; padding:5rem 0 4rem; }
.hero-tag { font-family:'DM Mono',monospace; font-size:11px; color:var(--amber); letter-spacing:.14em; text-transform:uppercase; background:var(--amber-pale); display:inline-block; padding:4px 12px; border-radius:20px; border:1px solid var(--amber-tag); margin-bottom:1rem; }
.hero h1 { font-size:50px; font-weight:700; line-height:1.08; color:var(--text-dark); margin-bottom:1.2rem; }
.hero h1 em { font-style:normal; color:var(--green); }
.hero p { font-size:16px; line-height:1.75; color:var(--text-mid); margin-bottom:2rem; }
.hero-btns { display:flex; gap:1rem; flex-wrap:wrap; }
.hero-graphic { background:var(--cream-dark); border-radius:20px; border:1px solid var(--border); aspect-ratio:1.05; display:flex; align-items:center; justify-content:center; overflow:hidden; }
.products-grid { display:grid; grid-template-columns:repeat(3,1fr); gap:1.5rem; }
.usecases-grid { display:grid; grid-template-columns:1fr 1fr; gap:3rem; align-items:center; }
.usecase-list { display:flex; flex-direction:column; gap:.8rem; }
.usecase-item { display:flex; gap:1rem; padding:1rem 1.2rem; border:1.5px solid var(--border); border-radius:12px; background:var(--card-bg); align-items:flex-start; }
.usecase-item.active { border-color:var(--green-light); background:#f4fbed; }
.usecase-item h4 { font-size:14px; font-weight:700; color:#2a3e1a; margin-bottom:3px; }
.usecase-item p { font-size:12px; color:var(--text-muted); line-height:1.55; }
.dash-mock { background:var(--card-bg); border:1.5px solid var(--border); border-radius:16px; padding:1.2rem; }
.dash-hdr { font-family:'DM Mono',monospace; font-size:10px; color:var(--amber); letter-spacing:.1em; margin-bottom:1rem; display:flex; align-items:center; gap:6px; }
.dash-dot { width:7px; height:7px; border-radius:50%; background:var(--green-light); display:inline-block; }
.dash-metrics { display:grid; grid-template-columns:1fr 1fr; gap:8px; margin-bottom:1rem; }
.dash-m { background:var(--cream-mid); border:1px solid var(--border); border-radius:10px; padding:10px 12px; }
.dash-m-lbl { font-family:'DM Mono',monospace; font-size:9px; color:var(--text-light); letter-spacing:.08em; text-transform:uppercase; margin-bottom:4px; }
.dash-m-val { font-family:'DM Mono',monospace; font-size:22px; font-weight:500; color:var(--green); }
.dash-m-unit { font-size:11px; color:var(--text-light); }
.relay-row { display:flex; align-items:center; justify-content:space-between; padding:7px 0; border-bottom:1px solid var(--border-soft); font-family:'DM Mono',monospace; font-size:10px; color:var(--text-muted); }
.relay-on { background:var(--green-pale); color:var(--green); padding:3px 10px; border-radius:20px; font-size:10px; font-weight:500; }
.relay-off { background:var(--cream-mid); color:var(--text-light); padding:3px 10px; border-radius:20px; font-size:10px; }
.features-grid { display:grid; grid-template-columns:repeat(3,1fr); gap:1.5rem; }
.feature-card { background:var(--card-bg); border:1.5px solid var(--border); border-radius:14px; padding:1.5rem; }
.feature-card h4 { font-size:15px; font-weight:700; margin-bottom:.5rem; }
.feature-card p { font-size:13px; color:var(--text-muted); line-height:1.65; }
@media(max-width:900px){.hero,.usecases-grid{grid-template-columns:1fr;gap:2.5rem;} .hero h1{font-size:36px;} .products-grid{grid-template-columns:1fr 1fr;} .features-grid{grid-template-columns:1fr 1fr;}}
@media(max-width:600px){.products-grid,.features-grid{grid-template-columns:1fr;}}
'''

index_body = f'''<main>
<div class="container">
  <div class="hero">
    <div>
      <div class="hero-tag">Open-source agricultural IoT</div>
      <h1>Grow smarter,<br><em>automate anything.</em></h1>
      <p>Affordable DIY sensor hardware and open firmware for home growers, hobbyists, and researchers. Monitor your plants, automate your pumps, and keep your grow running — even when you&rsquo;re not there.</p>
      <div class="hero-btns">
        <a class="btn-primary" href="products.html">Shop hardware</a>
        <a class="btn-ghost" href="github.html">View on GitHub</a>
      </div>
    </div>
    <div class="hero-graphic">{hero_svg}</div>
  </div>
</div>

<hr class="divider"/>

<section class="section">
  <div class="container">
    <p class="section-label">Hardware</p>
    <h2 class="section-title">Everything you need to get started</h2>
    <p class="section-sub">All boards are open-source hardware. KiCad files and firmware are free on GitHub.</p>
    <div class="products-grid">
      <div class="product-card featured">
        <span class="card-badge">New</span>
        <div class="card-image">{brain_svg}</div>
        <div class="card-body">
          <h3>Brain Board V2.0</h3>
          <p class="card-desc">Our newest node. Onboard temp, humidity, and light sensors. Wireless mesh via ESP-NOW. Expand with any Qwiic sensor.</p>
          <div class="card-specs"><span class="spec-tag">ESP32-C6</span><span class="spec-tag">WiFi 6</span><span class="spec-tag">ESP-NOW LR</span><span class="spec-tag">SHTC3</span><span class="spec-tag">TSL2591</span><span class="spec-tag">Qwiic</span></div>
          <div class="card-footer"><span class="card-price">$25</span><a class="card-btn" href="products/brain-board.html">Learn more</a></div>
        </div>
      </div>
      <div class="product-card">
        <div class="card-image">{sensor_svg}</div>
        <div class="card-body">
          <h3>Sensor Board</h3>
          <p class="card-desc">The original Automato node. ESP32 + LoRa radio, built-in display, 14-channel I/O, LiPo charging, and microSD logging.</p>
          <div class="card-specs"><span class="spec-tag">ESP32</span><span class="spec-tag">LoRa</span><span class="spec-tag">Display</span><span class="spec-tag">14x I/O</span><span class="spec-tag">LiPo</span><span class="spec-tag">microSD</span></div>
          <div class="card-footer"><span class="card-price">$30</span><a class="card-btn-ghost" href="products/sensor-board.html">Learn more</a></div>
        </div>
      </div>
      <div class="product-card">
        <div class="card-image">{relay_svg}</div>
        <div class="card-body">
          <h3>Relay Board</h3>
          <p class="card-desc">4-channel relay controller with mains-rated contacts and onboard AC/DC power supply. Pairs with any Automato node.</p>
          <div class="card-specs"><span class="spec-tag">4x relay</span><span class="spec-tag">AC/DC PSU</span><span class="spec-tag">Mains-rated</span><span class="spec-tag">Optoisolated</span></div>
          <div class="card-footer"><span class="card-price">$32</span><a class="card-btn-ghost" href="products/relay-board.html">Learn more</a></div>
        </div>
      </div>
    </div>
  </div>
</section>

<hr class="divider"/>

<section class="section">
  <div class="container">
    <p class="section-label">What you can build</p>
    <h2 class="section-title">Made for home growers &amp; tinkerers</h2>
    <p class="section-sub">Whether you&rsquo;re growing tomatoes, mushrooms, or fish &mdash; Automato has you covered.</p>
    <div class="usecases-grid">
      <div class="usecase-list">
        <div class="usecase-item active"><span style="font-size:20px;min-width:28px;">🌱</span><div><h4>Hydroponics &amp; aquaculture</h4><p>Monitor EC, pH, dissolved oxygen, and temperature. Automate pumps, dosing, and lighting on a schedule or threshold.</p></div></div>
        <div class="usecase-item"><span style="font-size:20px;min-width:28px;">🍄</span><div><h4>Indoor grows &amp; mycology</h4><p>Precise humidity and CO₂ control for fruiting chambers. Get notified when conditions drift out of range.</p></div></div>
        <div class="usecase-item"><span style="font-size:20px;min-width:28px;">🌿</span><div><h4>Greenhouse &amp; garden</h4><p>Multi-node mesh networks across large areas. Works outdoors with solar power and deep-sleep modes.</p></div></div>
        <div class="usecase-item"><span style="font-size:20px;min-width:28px;">🔬</span><div><h4>Research &amp; prototyping</h4><p>Open firmware, open hardware. Connect any I2C sensor and log to SD or push to your own server.</p></div></div>
      </div>
      <div class="dash-mock">
        <div class="dash-hdr"><span class="dash-dot"></span> LIVE DASHBOARD &nbsp;&middot;&nbsp; BRAIN BOARD</div>
        <div class="dash-metrics">
          <div class="dash-m"><div class="dash-m-lbl">Temperature</div><div><span class="dash-m-val">24.3</span><span class="dash-m-unit"> &deg;C</span></div></div>
          <div class="dash-m"><div class="dash-m-lbl">Humidity</div><div><span class="dash-m-val">68</span><span class="dash-m-unit"> %RH</span></div></div>
          <div class="dash-m"><div class="dash-m-lbl">Light</div><div><span class="dash-m-val">4120</span><span class="dash-m-unit"> lux</span></div></div>
          <div class="dash-m"><div class="dash-m-lbl">VPD</div><div><span class="dash-m-val">1.14</span><span class="dash-m-unit"> kPa</span></div></div>
        </div>
        <div style="font-family:'DM Mono',monospace;font-size:9px;color:var(--text-light);letter-spacing:.08em;margin-bottom:6px;">RELAY CHANNELS</div>
        <div class="relay-row">Pump <span class="relay-on">ON</span></div>
        <div class="relay-row">Lights <span class="relay-off">off</span></div>
        <div class="relay-row">Fan <span class="relay-off">off</span></div>
        <div style="font-family:'DM Mono',monospace;font-size:9px;color:var(--text-light);margin-top:10px;display:flex;align-items:center;gap:5px;"><span class="dash-dot"></span> ESP-NOW link active &nbsp;&middot;&nbsp; 2 nodes online</div>
      </div>
    </div>
  </div>
</section>

<hr class="divider"/>

<section class="section">
  <div class="container">
    <p class="section-label">Why Automato</p>
    <h2 class="section-title">Open, hackable, and yours</h2>
    <p class="section-sub">No subscriptions. No lock-in. Everything runs on your own hardware.</p>
    <div class="features-grid">
      <div class="feature-card"><div style="margin-bottom:.8rem"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#3d6b2c" stroke-width="1.8"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg></div><h4>100% open source</h4><p>All firmware is MIT-licensed and on GitHub. Full access to every line of code on your hardware.</p></div>
      <div class="feature-card"><div style="margin-bottom:.8rem"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#3d6b2c" stroke-width="1.8"><path d="M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"/><path d="M3 3v5h5"/></svg></div><h4>Works without the cloud</h4><p>The live dashboard runs from the board itself. ESP-NOW mesh works even without WiFi.</p></div>
      <div class="feature-card"><div style="margin-bottom:.8rem"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#3d6b2c" stroke-width="1.8"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg></div><h4>Expandable with Qwiic</h4><p>Plug in hundreds of I2C sensors with a standard Qwiic/STEMMA QT cable. No soldering required.</p></div>
    </div>
  </div>
</section>
</main>'''

with open('./index.html', 'w', encoding='utf-8') as f:
    f.write(page('Home', '', index_body, index_css))
print("index.html done")

# ──────────────────────────────────────────────────────────────────────────────
# products.html
# ──────────────────────────────────────────────────────────────────────────────
products_css = '''
.products-grid { display:grid; grid-template-columns:repeat(3,1fr); gap:1.5rem; }
.compare-table { width:100%; border-collapse:collapse; margin-top:3rem; font-size:14px; }
.compare-table th { background:var(--cream-mid); font-weight:600; padding:12px 16px; text-align:left; border-bottom:2px solid var(--border); }
.compare-table td { padding:11px 16px; border-bottom:1px solid var(--border-soft); color:var(--text-body); vertical-align:top; }
.compare-table tr:hover td { background:var(--green-pale); }
.compare-table .check { color:var(--green); font-weight:700; }
.compare-table .dash { color:var(--text-light); }
@media(max-width:900px){.products-grid{grid-template-columns:1fr 1fr;}}
@media(max-width:600px){.products-grid{grid-template-columns:1fr;} .compare-table{font-size:12px;} .compare-table th,.compare-table td{padding:8px 10px;}}
'''

products_body = f'''<main>
<section class="section">
  <div class="container">
    <p class="section-label">Hardware</p>
    <h2 class="section-title">Our boards</h2>
    <p class="section-sub">All Automato hardware is open-source. KiCad files and firmware are free on GitHub. Click any board to see full specs and documentation.</p>
    <div class="products-grid">
      <div class="product-card featured">
        <span class="card-badge">New</span>
        <div class="card-image">{brain_svg}</div>
        <div class="card-body">
          <h3>Brain Board V2.0</h3>
          <p class="card-desc">Our newest node. Onboard temp, humidity, and light sensors. Wireless mesh via ESP-NOW. Expand with any Qwiic sensor.</p>
          <div class="card-specs"><span class="spec-tag">ESP32-C6</span><span class="spec-tag">WiFi 6</span><span class="spec-tag">ESP-NOW LR</span><span class="spec-tag">SHTC3</span><span class="spec-tag">TSL2591</span><span class="spec-tag">Qwiic</span></div>
          <div class="card-footer"><span class="card-price">$25</span>
            <div style="display:flex;gap:8px;">
              <a class="card-btn-ghost" href="products/brain-board.html">Details</a>
              <a class="card-btn" href="{STRIPE_BRAIN_BOARD}" target="_blank">Buy — $25</a>
            </div>
          </div>
        </div>
      </div>
      <div class="product-card">
        <div class="card-image">{sensor_svg}</div>
        <div class="card-body">
          <h3>Sensor Board</h3>
          <p class="card-desc">The original Automato node. ESP32 + LoRa radio, built-in display, 14-channel I/O, LiPo charging, and microSD logging.</p>
          <div class="card-specs"><span class="spec-tag">ESP32</span><span class="spec-tag">LoRa</span><span class="spec-tag">Display</span><span class="spec-tag">14x I/O</span><span class="spec-tag">LiPo</span><span class="spec-tag">microSD</span></div>
          <div class="card-footer"><span class="card-price">$30</span>
            <div style="display:flex;gap:8px;">
              <a class="card-btn-ghost" href="products/sensor-board.html">Details</a>
              <a class="card-btn" href="{STRIPE_SENSOR_BOARD}" target="_blank">Buy — $30</a>
            </div>
          </div>
        </div>
      </div>
      <div class="product-card">
        <div class="card-image">{relay_svg}</div>
        <div class="card-body">
          <h3>Relay Board</h3>
          <p class="card-desc">4-channel relay controller with mains-rated contacts and onboard AC/DC power supply. Pairs with any Automato node.</p>
          <div class="card-specs"><span class="spec-tag">4x relay</span><span class="spec-tag">AC/DC PSU</span><span class="spec-tag">Mains-rated</span><span class="spec-tag">Optoisolated</span></div>
          <div class="card-footer"><span class="card-price">$32</span>
            <div style="display:flex;gap:8px;">
              <a class="card-btn-ghost" href="products/relay-board.html">Details</a>
              <a class="card-btn" href="{STRIPE_RELAY_BOARD}" target="_blank">Buy — $32</a>
            </div>
          </div>
        </div>
      </div>
    </div>

    <hr class="divider" style="margin:3rem 0 2rem;">
    <p class="section-label">Compare</p>
    <h2 class="section-title" style="margin-bottom:1rem;">Side by side</h2>
    <table class="compare-table">
      <thead>
        <tr><th>Feature</th><th>Brain Board V2.0</th><th>Sensor Board</th><th>Relay Board</th></tr>
      </thead>
      <tbody>
        <tr><td>Price</td><td><strong>$25</strong></td><td><strong>$30</strong></td><td><strong>$32</strong></td></tr>
        <tr><td>Microcontroller</td><td>ESP32-C6 (RISC-V, 160 MHz)</td><td>ESP32-WROOM-DA (Xtensa, 240 MHz)</td><td>None (peripheral board)</td></tr>
        <tr><td>WiFi</td><td class="check">✓ WiFi 6 (802.11ax)</td><td class="check">✓ WiFi 4 (802.11b/g/n)</td><td class="dash">—</td></tr>
        <tr><td>Wireless mesh</td><td class="check">✓ ESP-NOW Long Range</td><td class="check">✓ LoRa (RFM95W)</td><td class="dash">—</td></tr>
        <tr><td>Onboard sensors</td><td>SHTC3 (temp/humidity), TSL2591 (light)</td><td class="dash">— (connect via I/O)</td><td class="dash">—</td></tr>
        <tr><td>Display</td><td class="dash">—</td><td class="check">✓ Built-in display</td><td class="dash">—</td></tr>
        <tr><td>I/O expansion</td><td>2× Qwiic (I2C)</td><td>14-channel screw terminal</td><td class="dash">—</td></tr>
        <tr><td>Relay control</td><td class="dash">— (via Qwiic GPIO expander)</td><td class="check">✓ USB-C cable or GPIO pin</td><td class="dash">— (is the relay controller)</td></tr>
        <tr><td>Power input</td><td>USB-C</td><td>USB-C + LiPo</td><td>AC mains (onboard PSU)</td></tr>
        <tr><td>Data logging</td><td class="dash">— (WiFi / push to server)</td><td class="check">✓ microSD card</td><td class="dash">—</td></tr>
        <tr><td>Open source</td><td class="check">✓ MIT license</td><td class="check">✓ MIT license</td><td class="check">✓ MIT license</td></tr>
      </tbody>
    </table>
  </div>
</section>
</main>'''

with open('./products.html', 'w', encoding='utf-8') as f:
    f.write(page('Products', 'Products', products_body, products_css))
print("products.html done")

# ──────────────────────────────────────────────────────────────────────────────
# docs.html
# ──────────────────────────────────────────────────────────────────────────────
docs_css = '''
.docs-grid { display:grid; grid-template-columns:repeat(3,1fr); gap:1.2rem; }
.doc-card { background:var(--card-bg); border:1.5px solid var(--border); border-radius:14px; padding:1.4rem; transition:border-color .15s; }
.doc-card:hover { border-color:var(--green-light); }
.doc-icon { font-size:26px; margin-bottom:.8rem; }
.doc-card h4 { font-size:15px; font-weight:700; margin-bottom:.4rem; }
.doc-card > p { font-size:12px; color:var(--text-muted); line-height:1.6; margin-bottom:1rem; }
.doc-links { display:flex; flex-direction:column; gap:5px; }
.doc-link { font-family:'DM Mono',monospace; font-size:11px; color:var(--green); display:flex; align-items:center; gap:5px; }
.doc-link:hover { color:#2a4e1c; }
.doc-link::before { content:'→'; font-size:10px; }
.search-bar { display:flex; gap:.8rem; margin-bottom:2.5rem; }
.search-bar input { flex:1; padding:12px 16px; border:1.5px solid var(--border); border-radius:10px; font-family:'DM Sans',sans-serif; font-size:15px; background:var(--card-bg); color:var(--text-dark); outline:none; }
.search-bar input:focus { border-color:var(--green); }
@media(max-width:900px){.docs-grid{grid-template-columns:1fr 1fr;}}
@media(max-width:600px){.docs-grid{grid-template-columns:1fr;}}
'''

docs_body = '''<main>
<section class="section">
  <div class="container">
    <p class="section-label">Documentation</p>
    <h2 class="section-title">Everything you need to build</h2>
    <p class="section-sub">Guides, references, and setup walkthroughs &mdash; from first boot to full automation.</p>
    <div class="search-bar">
      <input type="text" placeholder="Search docs&hellip;" oninput="filterDocs(this.value)"/>
    </div>
    <div class="docs-grid" id="docs-grid">
      <div class="doc-card" data-tags="getting started quick start flash arduino install board package relay">
        <div class="doc-icon">🚀</div><h4>Getting started</h4>
        <p>Flash your first board and get sensor data on your screen in under 10 minutes.</p>
        <div class="doc-links">
          <a class="doc-link" href="#">Brain Board quick start</a>
          <a class="doc-link" href="#">Sensor Board quick start</a>
          <a class="doc-link" href="#">Installing the Arduino board package</a>
          <a class="doc-link" href="#">Your first relay automation</a>
        </div>
      </div>
      <div class="doc-card" data-tags="firmware api code library reference pin relay esp-now">
        <div class="doc-icon">📖</div><h4>Code &amp; API reference</h4>
        <p>Full firmware documentation, library APIs, and hardware pin references.</p>
        <div class="doc-links">
          <a class="doc-link" href="#">Brain Board firmware reference</a>
          <a class="doc-link" href="#">Sensor Board firmware reference</a>
          <a class="doc-link" href="#">Relay control API</a>
          <a class="doc-link" href="#">ESP-NOW mesh networking</a>
        </div>
      </div>
      <div class="doc-card" data-tags="hydroponics pump pH EC aquaculture dosing nutrient lighting schedule">
        <div class="doc-icon">🌱</div><h4>Hydroponics setup</h4>
        <p>Monitor and automate a hydroponic system from sensor wiring to threshold rules.</p>
        <div class="doc-links">
          <a class="doc-link" href="#">Nutrient dosing automation</a>
          <a class="doc-link" href="#">pH &amp; EC sensor wiring</a>
          <a class="doc-link" href="#">Pump &amp; lighting schedules</a>
          <a class="doc-link" href="#">Multi-zone setup guide</a>
        </div>
      </div>
      <div class="doc-card" data-tags="mycology mushroom fruiting chamber humidity CO2 FAE fan alert">
        <div class="doc-icon">🍄</div><h4>Mycology &amp; indoor grows</h4>
        <p>Dial in humidity, temperature, and fresh air exchange for fruiting chambers.</p>
        <div class="doc-links">
          <a class="doc-link" href="#">Fruiting chamber setup</a>
          <a class="doc-link" href="#">Humidity &amp; CO₂ control</a>
          <a class="doc-link" href="#">FAE fan automation</a>
          <a class="doc-link" href="#">Alert thresholds guide</a>
        </div>
      </div>
      <div class="doc-card" data-tags="greenhouse outdoor solar battery LoRa irrigation mesh multi-node">
        <div class="doc-icon">🌿</div><h4>Greenhouse &amp; outdoor</h4>
        <p>Deploy multi-node networks across large spaces with solar power and long-range radio.</p>
        <div class="doc-links">
          <a class="doc-link" href="#">Multi-node ESP-NOW mesh</a>
          <a class="doc-link" href="#">Solar &amp; battery power</a>
          <a class="doc-link" href="#">Irrigation automation</a>
          <a class="doc-link" href="#">LoRa long-range setup</a>
        </div>
      </div>
      <div class="doc-card" data-tags="hardware schematic BOM kicad qwiic relay wiring safety expansion">
        <div class="doc-icon">🔧</div><h4>Hardware &amp; expansion</h4>
        <p>Schematics, BOM, Qwiic sensor compatibility, and custom hardware guides.</p>
        <div class="doc-links">
          <a class="doc-link" href="#">Brain Board hardware reference</a>
          <a class="doc-link" href="#">Qwiic sensor compatibility</a>
          <a class="doc-link" href="#">Relay wiring &amp; safety</a>
          <a class="doc-link" href="https://github.com/Automato-ag" target="_blank">KiCad files on GitHub ↗</a>
        </div>
      </div>
    </div>
  </div>
</section>
</main>
<script>
function filterDocs(q) {
  q = q.toLowerCase();
  document.querySelectorAll('#docs-grid .doc-card').forEach(card => {
    const text = (card.innerText + card.dataset.tags).toLowerCase();
    card.style.display = text.includes(q) ? '' : 'none';
  });
}
</script>'''

with open('./docs.html', 'w', encoding='utf-8') as f:
    f.write(page('Docs', 'Docs', docs_body, docs_css))
print("docs.html done")

# ──────────────────────────────────────────────────────────────────────────────
# github.html
# ──────────────────────────────────────────────────────────────────────────────
github_css = '''
.repo-grid { display:grid; grid-template-columns:repeat(2,1fr); gap:1.2rem; }
.repo-card { background:var(--card-bg); border:1.5px solid var(--border); border-radius:14px; padding:1.5rem; display:flex; flex-direction:column; gap:.8rem; }
.repo-card:hover { border-color:var(--green-light); }
.repo-header { display:flex; align-items:center; gap:.8rem; }
.repo-icon { font-size:22px; }
.repo-card h3 { font-size:16px; font-weight:700; margin:0; }
.repo-card p { font-size:13px; color:var(--text-muted); line-height:1.6; flex:1; }
.repo-tags { display:flex; flex-wrap:wrap; gap:6px; }
.repo-tag { font-family:'DM Mono',monospace; font-size:10px; color:var(--amber); background:var(--amber-pale); border:1px solid var(--amber-tag); padding:2px 8px; border-radius:20px; }
.repo-link { font-family:'DM Mono',monospace; font-size:11px; color:var(--green); display:inline-flex; align-items:center; gap:5px; margin-top:.2rem; }
.repo-link::before { content:'→'; }
.gh-hero { background:var(--cream-dark); border-radius:20px; border:1px solid var(--border); padding:3rem 2.5rem; margin-bottom:3rem; display:flex; align-items:center; gap:2rem; flex-wrap:wrap; }
.gh-hero-text h2 { font-size:28px; font-weight:700; margin-bottom:.6rem; }
.gh-hero-text p { font-size:15px; color:var(--text-mid); line-height:1.7; max-width:520px; }
.gh-hero-btns { display:flex; gap:1rem; margin-top:1.4rem; flex-wrap:wrap; }
@media(max-width:700px){.repo-grid{grid-template-columns:1fr;}}
'''

github_body = '''<main>
<section class="section">
  <div class="container">
    <div class="gh-hero">
      <svg width="60" height="60" viewBox="0 0 98 96" xmlns="http://www.w3.org/2000/svg" style="min-width:60px">
        <path fill="#3d6b2c" fill-rule="evenodd" clip-rule="evenodd" d="M49 0C21.9 0 0 22.4 0 50c0 22.1 14.3 40.8 34.2 47.4 2.5.5 3.4-1.1 3.4-2.4 0-1.2-.05-4.3-.07-8.4-13.9 3-16.8-6.7-16.8-6.7-2.3-5.8-5.5-7.3-5.5-7.3-4.5-3.1.34-3 .34-3 5 .35 7.6 5.1 7.6 5.1 4.4 7.6 11.6 5.4 14.4 4.1.44-3.2 1.7-5.4 3.1-6.6-11.1-1.3-22.7-5.5-22.7-24.7 0-5.5 1.9-9.9 5.1-13.4-.51-1.3-2.2-6.3.48-13.2 0 0 4.1-1.3 13.5 5 3.9-1.1 8.1-1.6 12.3-1.6 4.2 0 8.4.56 12.3 1.6 9.4-6.4 13.5-5 13.5-5 2.7 6.9.99 12 .48 13.2 3.2 3.5 5.1 8 5.1 13.4 0 19.2-11.7 23.4-22.8 24.6 1.8 1.5 3.4 4.6 3.4 9.3 0 6.7-.06 12.1-.06 13.7 0 1.3.87 2.9 3.4 2.4C83.7 90.8 98 72.1 98 50 98 22.4 76.1 0 49 0z"/>
      </svg>
      <div class="gh-hero-text">
        <h2>Open source, always</h2>
        <p>All Automato hardware designs and firmware are freely available on GitHub under the MIT license. Fork it, modify it, contribute back — it belongs to the community.</p>
        <div class="gh-hero-btns">
          <a class="btn-primary" href="https://github.com/Automato-ag" target="_blank">Automato-ag on GitHub ↗</a>
          <a class="btn-ghost" href="https://github.com/InterstitialTech" target="_blank">Legacy: InterstitialTech ↗</a>
        </div>
      </div>
    </div>

    <p class="section-label">Repositories</p>
    <h2 class="section-title">All projects</h2>
    <p class="section-sub" style="margin-bottom:2rem;">Firmware, hardware designs, and server infrastructure — all in one place.</p>

    <div class="repo-grid">
      <div class="repo-card">
        <div class="repo-header"><span class="repo-icon">🧠</span><h3>Brain-Board</h3></div>
        <p>Firmware (Arduino), hardware reference, quick start guides, and relay automation docs for the Brain Board V2.0.</p>
        <div class="repo-tags"><span class="repo-tag">Arduino</span><span class="repo-tag">ESP32-C6</span><span class="repo-tag">WiFi</span><span class="repo-tag">ESP-NOW</span></div>
        <a class="repo-link" href="https://github.com/Automato-ag/Brain-Board" target="_blank">github.com/Automato-ag/Brain-Board</a>
      </div>
      <div class="repo-card">
        <div class="repo-header"><span class="repo-icon">📡</span><h3>automato-sensor</h3></div>
        <p>KiCad hardware design files, BOM, and schematic for the original Automato Sensor Board with ESP32 + LoRa.</p>
        <div class="repo-tags"><span class="repo-tag">KiCad</span><span class="repo-tag">ESP32</span><span class="repo-tag">LoRa</span><span class="repo-tag">Hardware</span></div>
        <a class="repo-link" href="https://github.com/InterstitialTech/automato-sensor" target="_blank">github.com/InterstitialTech/automato-sensor</a>
      </div>
      <div class="repo-card">
        <div class="repo-header"><span class="repo-icon">⚡</span><h3>automato-relay</h3></div>
        <p>KiCad hardware design files, BOM, and schematic for the Relay Board — 4-channel, mains-rated, optoisolated.</p>
        <div class="repo-tags"><span class="repo-tag">KiCad</span><span class="repo-tag">Relay</span><span class="repo-tag">AC/DC</span><span class="repo-tag">Hardware</span></div>
        <a class="repo-link" href="https://github.com/InterstitialTech/automato-relay" target="_blank">github.com/InterstitialTech/automato-relay</a>
      </div>
      <div class="repo-card">
        <div class="repo-header"><span class="repo-icon">🦀</span><h3>automato-etc</h3></div>
        <p>Rust + Actix-web server infrastructure, serial command CLI (matomsg), and Elm frontend for the desktop dashboard.</p>
        <div class="repo-tags"><span class="repo-tag">Rust</span><span class="repo-tag">Actix-web</span><span class="repo-tag">Elm</span><span class="repo-tag">Server</span></div>
        <a class="repo-link" href="https://github.com/InterstitialTech/automato-etc" target="_blank">github.com/InterstitialTech/automato-etc</a>
      </div>
      <div class="repo-card">
        <div class="repo-header"><span class="repo-icon">📋</span><h3>automato-sketches</h3></div>
        <p>Example Arduino sketches and code samples for the Sensor Board, demonstrating sensors, LoRa, and I/O usage.</p>
        <div class="repo-tags"><span class="repo-tag">Arduino</span><span class="repo-tag">Examples</span><span class="repo-tag">Sensor Board</span></div>
        <a class="repo-link" href="https://github.com/InterstitialTech/automato-sketches" target="_blank">github.com/InterstitialTech/automato-sketches</a>
      </div>
      <div class="repo-card">
        <div class="repo-header"><span class="repo-icon">📦</span><h3>automato-arduino</h3></div>
        <p>Arduino board package for both the Sensor Board and Brain Board. Install via the Arduino Board Manager URL.</p>
        <div class="repo-tags"><span class="repo-tag">Arduino</span><span class="repo-tag">Board package</span><span class="repo-tag">ESP32-C6</span></div>
        <a class="repo-link" href="https://github.com/InterstitialTech/automato-arduino" target="_blank">github.com/InterstitialTech/automato-arduino</a>
      </div>
    </div>

    <div style="background:var(--green-pale);border:1.5px solid var(--green-tag);border-radius:14px;padding:2rem;margin-top:3rem;display:flex;gap:1.5rem;align-items:flex-start;flex-wrap:wrap;">
      <div style="font-size:28px;">🤝</div>
      <div>
        <h3 style="font-size:17px;font-weight:700;margin-bottom:.4rem;">Want to contribute?</h3>
        <p style="font-size:14px;color:var(--text-body);line-height:1.7;margin-bottom:1rem;">Found a bug? Have an improvement? We welcome issues and pull requests on all repos. If you build something with Automato hardware, let us know &mdash; we&rsquo;d love to feature it.</p>
        <a class="btn-ghost" href="https://github.com/Automato-ag" target="_blank" style="font-size:13px;padding:9px 18px;">Open an issue on GitHub ↗</a>
      </div>
    </div>
  </div>
</section>
</main>'''

with open('./github.html', 'w', encoding='utf-8') as f:
    f.write(page('GitHub', 'GitHub', github_body, github_css))
print("github.html done")

# ──────────────────────────────────────────────────────────────────────────────
# about.html
# ──────────────────────────────────────────────────────────────────────────────
about_css = '''
.about-hero { display:grid; grid-template-columns:1fr 1fr; gap:4rem; align-items:center; margin-bottom:4rem; }
.about-img { background:var(--cream-dark); border-radius:20px; border:1px solid var(--border); aspect-ratio:1.1; display:flex; align-items:center; justify-content:center; overflow:hidden; }
.about-pull { font-size:20px; font-weight:700; color:var(--green); line-height:1.4; border-left:4px solid var(--green-tag); padding-left:1.2rem; margin-bottom:1.5rem; }
.about-body p { font-size:15px; line-height:1.8; color:var(--text-body); margin-bottom:1.1rem; }
.about-btns { display:flex; gap:1rem; flex-wrap:wrap; margin-top:1.8rem; }
.values-grid { display:grid; grid-template-columns:repeat(3,1fr); gap:1.5rem; }
.value-card { background:var(--card-bg); border:1.5px solid var(--border); border-radius:14px; padding:1.5rem; }
.value-card h4 { font-size:15px; font-weight:700; margin-bottom:.5rem; }
.value-card p { font-size:13px; color:var(--text-muted); line-height:1.65; }
@media(max-width:900px){.about-hero{grid-template-columns:1fr;gap:2.5rem;} .values-grid{grid-template-columns:1fr 1fr;}}
@media(max-width:600px){.values-grid{grid-template-columns:1fr;}}
'''

about_svg = '''<svg width="85%" viewBox="0 0 300 270" xmlns="http://www.w3.org/2000/svg">
  <rect width="300" height="270" fill="#f0ede4"/>
  <ellipse cx="150" cy="230" rx="100" ry="18" fill="#ddd4bc" opacity="0.5"/>
  <rect x="80" y="60" width="140" height="110" rx="8" fill="#fffdf8" stroke="#c8bc9a" stroke-width="1.5"/>
  <rect x="95" y="75" width="110" height="70" rx="5" fill="#c8e4c0" stroke="#9acd7a" stroke-width="1"/>
  <text x="150" y="108" text-anchor="middle" font-family="monospace" font-size="8" fill="#2a5a1a">Sensor data</text>
  <text x="150" y="121" text-anchor="middle" font-family="monospace" font-size="7" fill="#4a8a3a">24.3&deg;C  68%RH</text>
  <text x="150" y="133" text-anchor="middle" font-family="monospace" font-size="7" fill="#4a8a3a">4120 lux  VPD 1.14</text>
  <line x1="100" y1="170" x2="100" y2="200" stroke="#b8bc98" stroke-width="8" stroke-linecap="round"/>
  <line x1="150" y1="170" x2="150" y2="190" stroke="#8aaa68" stroke-width="8" stroke-linecap="round"/>
  <line x1="200" y1="170" x2="200" y2="210" stroke="#6a9a48" stroke-width="8" stroke-linecap="round"/>
  <ellipse cx="100" cy="200" rx="14" ry="8" fill="#7ab85a"/><ellipse cx="100" cy="196" rx="10" ry="6" fill="#8acc68"/>
  <ellipse cx="150" cy="190" rx="18" ry="10" fill="#5aa83a"/><ellipse cx="150" cy="185" rx="13" ry="8" fill="#6aba4a"/>
  <ellipse cx="200" cy="210" rx="16" ry="9" fill="#4a9830"/><ellipse cx="200" cy="205" rx="11" ry="7" fill="#5aaa3a"/>
</svg>'''

about_body = f'''<main>
<section class="section">
  <div class="container">
    <p class="section-label">About</p>
    <h2 class="section-title">Built by growers, for growers</h2>
    <div style="height:1.5rem"></div>
    <div class="about-hero">
      <div class="about-img">{about_svg}</div>
      <div class="about-body">
        <p class="about-pull">&ldquo;We wanted automation tools that were affordable, hackable, and didn&rsquo;t require a subscription to a cloud you don&rsquo;t control.&rdquo;</p>
        <p>Automato started as a personal project &mdash; a need for affordable, reliable automation in a small hydroponic setup. Off-the-shelf solutions were either too expensive, too locked-down, or just not designed for the kind of DIY tinkering that makes growing fun.</p>
        <p>So we built our own. The Sensor Board was the first result: an open-source ESP32 node with LoRa radio, a display, and enough I/O to connect almost anything. The Brain Board V2.0 is the next generation &mdash; smaller, faster, and wireless out of the box.</p>
        <p>Everything we make is open-source hardware and software. The KiCad files, firmware, and docs are all on GitHub. If you find a bug, open an issue. If you build something cool, we&rsquo;d love to hear about it.</p>
        <div class="about-btns">
          <a class="btn-primary" href="https://github.com/Automato-ag" target="_blank">View on GitHub</a>
          <a class="btn-ghost" href="contact.html">Get in touch</a>
        </div>
      </div>
    </div>

    <hr class="divider" style="margin:1rem 0 3rem"/>
    <p class="section-label">Our values</p>
    <h2 class="section-title" style="margin-bottom:1rem;">What we believe in</h2>
    <div class="values-grid">
      <div class="value-card">
        <div style="font-size:24px;margin-bottom:.8rem;">🌱</div>
        <h4>Accessible technology</h4>
        <p>Growing automation shouldn&rsquo;t cost a fortune. We keep our hardware affordable and our software free so anyone can build with it.</p>
      </div>
      <div class="value-card">
        <div style="font-size:24px;margin-bottom:.8rem;">🔓</div>
        <h4>Radical openness</h4>
        <p>Every schematic, every line of firmware, every footprint &mdash; all public, all MIT-licensed. No black boxes, ever.</p>
      </div>
      <div class="value-card">
        <div style="font-size:24px;margin-bottom:.8rem;">🏠</div>
        <h4>Local-first</h4>
        <p>Your data lives on your hardware. The dashboard runs on your board. You don&rsquo;t need our servers running to keep your plants watered.</p>
      </div>
      <div class="value-card">
        <div style="font-size:24px;margin-bottom:.8rem;">🤝</div>
        <h4>Community-driven</h4>
        <p>We build what the community needs. Open issues, pull requests, and forum threads shape the roadmap as much as anything we plan ourselves.</p>
      </div>
      <div class="value-card">
        <div style="font-size:24px;margin-bottom:.8rem;">🔧</div>
        <h4>Hackable by design</h4>
        <p>Standard connectors, documented APIs, open firmware. Everything is designed to be modified, extended, and repurposed.</p>
      </div>
      <div class="value-card">
        <div style="font-size:24px;margin-bottom:.8rem;">🌍</div>
        <h4>Practical sustainability</h4>
        <p>Efficient hardware with deep-sleep modes, solar-friendly power budgets, and long hardware lifespans reduce the footprint of automation.</p>
      </div>
    </div>
  </div>
</section>
</main>'''

with open('./about.html', 'w', encoding='utf-8') as f:
    f.write(page('About', 'About', about_body, about_css))
print("about.html done")

# ──────────────────────────────────────────────────────────────────────────────
# contact.html
# ──────────────────────────────────────────────────────────────────────────────
contact_css = '''
.contact-grid { display:grid; grid-template-columns:1fr 1fr; gap:4rem; align-items:start; }
.contact-form { display:flex; flex-direction:column; gap:1rem; }
.contact-form input, .contact-form textarea, .contact-form select {
  padding:12px 16px; border:1.5px solid var(--border); border-radius:10px;
  font-family:'DM Sans',sans-serif; font-size:15px; background:var(--card-bg); color:var(--text-dark); outline:none; width:100%;
}
.contact-form input:focus, .contact-form textarea:focus, .contact-form select:focus { border-color:var(--green); }
.contact-form label { font-size:13px; font-weight:600; color:var(--text-body); margin-bottom:-4px; }
.contact-info { display:flex; flex-direction:column; gap:1.5rem; }
.contact-info-item { display:flex; gap:1rem; align-items:flex-start; }
.contact-info-item h4 { font-size:14px; font-weight:700; margin-bottom:3px; }
.contact-info-item p { font-size:13px; color:var(--text-muted); line-height:1.6; }
.contact-info-icon { font-size:22px; min-width:32px; }
@media(max-width:800px){.contact-grid{grid-template-columns:1fr;gap:2.5rem;}}
'''

contact_body = f'''<main>
<section class="section">
  <div class="container" style="max-width:900px;">
    <p class="section-label">Contact</p>
    <h2 class="section-title">Get in touch</h2>
    <p class="section-sub">Questions about hardware, firmware, a project you&rsquo;re building, or just want to say hi?</p>
    <div class="contact-grid">
      <div>
        <form class="contact-form" id="contact-form">
          <div><label for="name">Your name</label><input id="name" name="name" type="text" placeholder="Jane Smith" required/></div>
          <div><label for="email">Email address</label><input id="email" name="email" type="email" placeholder="jane@example.com" required/></div>
          <div><label for="topic">Topic</label>
            <select id="topic" name="topic">
              <option value="">Select a topic&hellip;</option>
              <option>Hardware question</option>
              <option>Firmware / software</option>
              <option>Order / shipping</option>
              <option>Bug report</option>
              <option>Feature request</option>
              <option>Just saying hi</option>
            </select>
          </div>
          <div><label for="msg">Message</label><textarea id="msg" name="message" rows="5" placeholder="Tell us what you&rsquo;re working on&hellip;" required></textarea></div>
          <button type="submit" id="submit-btn" class="btn-primary" style="align-self:flex-start;">Send message</button>
          <p id="form-success" style="display:none;color:var(--green);font-size:14px;font-weight:600;">&#10003; Message sent! We&rsquo;ll get back to you soon.</p>
          <p id="form-error" style="display:none;color:#c44;font-size:13px;">Something went wrong &mdash; please email us directly at <a href="mailto:automato.llc@gmail.com" style="color:#c44;">automato.llc@gmail.com</a></p>
        </form>
      </div>
      <div class="contact-info">
        <div style="background:var(--green-pale);border:1.5px solid var(--green-tag);border-radius:14px;padding:1.5rem;margin-bottom:.5rem;">
          <p style="font-size:14px;color:var(--text-body);line-height:1.7;">The fastest way to reach us for technical issues is to <strong><a href="https://github.com/Automato-ag" target="_blank" style="color:var(--green);">open a GitHub issue</a></strong> on the relevant repo. For everything else, use the form.</p>
        </div>
        <div class="contact-info-item">
          <span class="contact-info-icon">✉️</span>
          <div><h4>Email us directly</h4><p><a href="mailto:automato.llc@gmail.com" style="color:var(--green);font-family:'DM Mono',monospace;">automato.llc@gmail.com</a><br>We aim to reply within 2 business days.</p></div>
        </div>
        <div class="contact-info-item">
          <span class="contact-info-icon">🐛</span>
          <div><h4>Bug reports</h4><p>Open an issue on GitHub with your board version, firmware version, and steps to reproduce.</p></div>
        </div>
        <div class="contact-info-item">
          <span class="contact-info-icon">💡</span>
          <div><h4>Feature requests</h4><p>We track feature requests as GitHub issues. Label yours &ldquo;enhancement&rdquo; so we can find it.</p></div>
        </div>
        <div class="contact-info-item">
          <span class="contact-info-icon">📦</span>
          <div><h4>Orders &amp; shipping</h4><p>For order questions, use the contact form with topic &ldquo;Order / shipping&rdquo; and your order number.</p></div>
        </div>
        <div class="contact-info-item">
          <span class="contact-info-icon">🌱</span>
          <div><h4>Show us your build</h4><p>Built something with Automato hardware? We&rsquo;d love to see it &mdash; send a photo and a short description.</p></div>
        </div>
      </div>
    </div>
  </div>
</section>
</main>
<script>
document.getElementById('contact-form').addEventListener('submit', async function(e) {{
  e.preventDefault();
  const btn = document.getElementById('submit-btn');
  btn.disabled = true;
  btn.textContent = 'Sending\u2026';
  try {{
    const res = await fetch('__FORMSPREE__', {{
      method: 'POST',
      headers: {{ 'Accept': 'application/json' }},
      body: new FormData(this)
    }});
    if (res.ok) {{
      document.getElementById('form-success').style.display = 'block';
      this.reset();
    }} else {{
      throw new Error('non-ok');
    }}
  }} catch(err) {{
    btn.disabled = false;
    btn.textContent = 'Send message';
    document.getElementById('form-error').style.display = 'block';
  }}
}});
</script>'''

with open('./contact.html', 'w', encoding='utf-8') as f:
    f.write(page('Contact', 'Contact', contact_body, contact_css).replace('__FORMSPREE__', FORMSPREE_ENDPOINT))
print("contact.html done")

# ──────────────────────────────────────────────────────────────────────────────
# Product detail pages — shared CSS
# ──────────────────────────────────────────────────────────────────────────────
product_detail_css = '''
.pd-hero { display:grid; grid-template-columns:1fr 1fr; gap:4rem; align-items:center; padding:3rem 0 2.5rem; }
.pd-image { background:var(--cream-dark); border-radius:20px; border:1px solid var(--border); aspect-ratio:1.1; display:flex; align-items:center; justify-content:center; overflow:hidden; }
.pd-badge { font-family:'DM Mono',monospace; font-size:10px; color:var(--green); background:var(--green-pale); border:1px solid var(--green-tag); padding:3px 10px; border-radius:20px; display:inline-block; margin-bottom:.8rem; }
.pd-hero h1 { font-size:38px; font-weight:700; line-height:1.1; margin-bottom:.6rem; }
.pd-price { font-family:'DM Mono',monospace; font-size:36px; font-weight:500; color:var(--green); margin:.8rem 0 1.2rem; }
.pd-desc { font-size:15px; line-height:1.8; color:var(--text-body); margin-bottom:1.5rem; }
.pd-specs-inline { display:flex; flex-wrap:wrap; gap:6px; margin-bottom:1.8rem; }
.pd-btns { display:flex; gap:1rem; flex-wrap:wrap; }
.pd-tabs { display:flex; gap:0; border-bottom:2px solid var(--border); margin-bottom:2rem; }
.pd-tab { padding:.8rem 1.4rem; font-size:14px; font-weight:600; color:var(--text-muted); cursor:pointer; border-bottom:2px solid transparent; margin-bottom:-2px; background:none; border-top:none; border-left:none; border-right:none; font-family:'DM Sans',sans-serif; }
.pd-tab.active { color:var(--green); border-bottom-color:var(--green); }
.pd-tab:hover { color:var(--green); }
.pd-panel { display:none; }
.pd-panel.active { display:block; }
.spec-table { width:100%; border-collapse:collapse; font-size:14px; }
.spec-table tr { border-bottom:1px solid var(--border-soft); }
.spec-table tr:last-child { border-bottom:none; }
.spec-table td { padding:11px 0; vertical-align:top; }
.spec-table td:first-child { font-weight:600; color:var(--text-dark); width:38%; }
.spec-table td:last-child { color:var(--text-body); }
.pin-table { width:100%; border-collapse:collapse; font-size:13px; }
.pin-table th { background:var(--cream-mid); font-weight:600; padding:10px 14px; text-align:left; border-bottom:2px solid var(--border); }
.pin-table td { padding:9px 14px; border-bottom:1px solid var(--border-soft); color:var(--text-body); }
.pin-table tr:hover td { background:var(--green-pale); }
.link-card { background:var(--card-bg); border:1.5px solid var(--border); border-radius:12px; padding:1.2rem 1.4rem; display:flex; align-items:center; gap:1rem; transition:border-color .15s; }
.link-card:hover { border-color:var(--green-light); }
.link-card-icon { font-size:24px; min-width:36px; }
.link-card h4 { font-size:14px; font-weight:700; margin-bottom:2px; }
.link-card p { font-size:12px; color:var(--text-muted); }
.link-card .arrow { margin-left:auto; color:var(--green); font-size:18px; }
.links-grid { display:grid; grid-template-columns:1fr 1fr; gap:1rem; }
.breadcrumb { font-size:13px; color:var(--text-muted); margin-bottom:1.5rem; display:flex; align-items:center; gap:.5rem; flex-wrap:wrap; }
.breadcrumb a { color:var(--green); }
.breadcrumb span { color:var(--text-light); }
@media(max-width:900px){.pd-hero{grid-template-columns:1fr;gap:2rem;} .pd-hero h1{font-size:30px;} .links-grid{grid-template-columns:1fr;}}
'''

def product_detail(title, badge, name, price, desc, svg_content, specs_tags, specs_table_rows, pins_rows, docs_links, github_url, stripe_url, active_page='Products', prefix='../'):
    body = f'''<main>
<section class="section">
<div class="container">
  <div class="breadcrumb">
    <a href="{prefix}index.html">Home</a><span>/</span>
    <a href="{prefix}products.html">Products</a><span>/</span>
    <span style="color:var(--text-dark)">{name}</span>
  </div>
  <div class="pd-hero">
    <div class="pd-image">{svg_content}</div>
    <div>
      <span class="pd-badge">{badge}</span>
      <h1>{name}</h1>
      <div class="pd-price">{price}</div>
      <p class="pd-desc">{desc}</p>
      <div class="pd-specs-inline">{specs_tags}</div>
      <div class="pd-btns">
        <a class="btn-primary" href="{stripe_url}" target="_blank">Buy — {price}</a>
        <a class="btn-ghost" href="{github_url}" target="_blank">View on GitHub ↗</a>
      </div>
    </div>
  </div>

  <div style="background:var(--cream-dark);border-radius:12px;padding:.8rem 1.2rem;margin:1rem 0 2.5rem;display:flex;gap:1rem;flex-wrap:wrap;align-items:center;">
    <span style="font-size:13px;color:var(--text-muted);">Open-source hardware &amp; firmware &nbsp;&middot;&nbsp; MIT License &nbsp;&middot;&nbsp; KiCad design files available</span>
  </div>

  <div class="pd-tabs">
    <button class="pd-tab active" onclick="showTab(this,'overview')">Overview</button>
    <button class="pd-tab" onclick="showTab(this,'specs')">Full specs</button>
    <button class="pd-tab" onclick="showTab(this,'pinout')">Pinout</button>
    <button class="pd-tab" onclick="showTab(this,'links')">Docs &amp; links</button>
  </div>

  <div class="pd-panel active" id="tab-overview">
    {docs_links['overview']}
  </div>

  <div class="pd-panel" id="tab-specs">
    <table class="spec-table">
      <tbody>{specs_table_rows}</tbody>
    </table>
  </div>

  <div class="pd-panel" id="tab-pinout">
    <table class="pin-table">
      <thead><tr><th>Pin / Label</th><th>GPIO</th><th>Function</th></tr></thead>
      <tbody>{pins_rows}</tbody>
    </table>
  </div>

  <div class="pd-panel" id="tab-links">
    <div class="links-grid">
      {docs_links['links']}
    </div>
  </div>
</div>
</section>
</main>
<script>
function showTab(btn, id) {{
  document.querySelectorAll('.pd-tab').forEach(t=>t.classList.remove('active'));
  document.querySelectorAll('.pd-panel').forEach(p=>p.classList.remove('active'));
  btn.classList.add('active');
  document.getElementById('tab-'+id).classList.add('active');
}}
</script>'''
    return page(title, active_page, body, product_detail_css, prefix)

# ── BRAIN BOARD ──────────────────────────────────────────────────────────────
bb_specs_tags = '''<span class="spec-tag">ESP32-C6</span><span class="spec-tag">WiFi 6</span><span class="spec-tag">ESP-NOW LR</span>
<span class="spec-tag">SHTC3</span><span class="spec-tag">TSL2591</span><span class="spec-tag">Qwiic ×2</span>
<span class="spec-tag">USB-C</span><span class="spec-tag">3× LED</span><span class="spec-tag">Open source</span>'''

bb_specs_rows = '''
<tr><td>Microcontroller</td><td>ESP32-C6-MINI-1-N4 (RISC-V HP core 160 MHz + LP core 20 MHz, 4 MB flash)</td></tr>
<tr><td>Wireless</td><td>WiFi 6 (802.11ax), Bluetooth 5 LE, IEEE 802.15.4 (Zigbee/Thread), ESP-NOW Long Range</td></tr>
<tr><td>Temperature / humidity</td><td>Sensirion SHTC3-TR — ±0.2°C, ±2% RH, I2C address 0x70</td></tr>
<tr><td>Ambient light</td><td>ams-OSRAM TSL25911FN (TSL2591) — lux + infrared channel, I2C address 0x29</td></tr>
<tr><td>I2C bus</td><td>SDA = IO6, SCL = IO7 (shared between sensors and both Qwiic connectors)</td></tr>
<tr><td>Expansion connectors</td><td>2× Qwiic / STEMMA QT (JST SM04B-SRSS-TB, 1 mm pitch)</td></tr>
<tr><td>USB</td><td>USB-C (native USB-CDC, no UART chip) — right-angle Switchcraft RAHUC31AUTR</td></tr>
<tr><td>Power regulator</td><td>Diodes Inc. AP2112K-3.3 LDO, 600 mA max</td></tr>
<tr><td>LEDs</td><td>Green (IO?), Red (IO?), Blue / LED_BUILTIN (IO23) — Kingbright 0402</td></tr>
<tr><td>Buttons</td><td>RESET (EN) and BOOT (IO9) — tactile SMD</td></tr>
<tr><td>Reverse-polarity protection</td><td>BAT20J Schottky diode</td></tr>
<tr><td>Castellated pads</td><td>2× 1×10 (DNP) exposing IO0–IO5, IO14, IO15, IO18–IO23, TX, RX, USB</td></tr>
<tr><td>Arduino board package</td><td>automato-arduino v0.1.2, requires arduino-esp32 v3.3.0</td></tr>
<tr><td>Bootloader offset</td><td>0x0 (ESP32-C6 native)</td></tr>
<tr><td>Dimensions</td><td>See KiCad files for exact dimensions</td></tr>
<tr><td>License</td><td>MIT (hardware &amp; firmware)</td></tr>'''

bb_pins_rows = '''
<tr><td>LED_BUILTIN / Blue LED</td><td>IO23</td><td>Digital output — onboard blue LED</td></tr>
<tr><td>SDA</td><td>IO6</td><td>I2C data — shared with sensors + Qwiic</td></tr>
<tr><td>SCL</td><td>IO7</td><td>I2C clock — shared with sensors + Qwiic</td></tr>
<tr><td>TX</td><td>IO16</td><td>UART transmit</td></tr>
<tr><td>RX</td><td>IO17</td><td>UART receive</td></tr>
<tr><td>SS</td><td>IO2</td><td>SPI chip select</td></tr>
<tr><td>MOSI</td><td>IO3</td><td>SPI data out</td></tr>
<tr><td>MISO</td><td>IO4</td><td>SPI data in</td></tr>
<tr><td>SCK</td><td>IO5</td><td>SPI clock</td></tr>
<tr><td>BOOT</td><td>IO9</td><td>Boot button — hold at power-on for flash mode</td></tr>'''

bb_overview = '''<div style="display:grid;grid-template-columns:1fr 1fr;gap:2rem;margin-bottom:2rem;">
  <div>
    <h3 style="font-size:17px;font-weight:700;margin-bottom:.8rem;">What it does</h3>
    <p style="font-size:14px;color:var(--text-body);line-height:1.8;">The Brain Board V2.0 is a compact wireless sensor node designed for DIY agricultural automation. It ships with onboard temperature, humidity, and ambient light sensors, and connects to a host node or WiFi network right out of the box.</p>
    <p style="font-size:14px;color:var(--text-body);line-height:1.8;margin-top:.8rem;">Using the ESP-NOW Long Range protocol, multiple Brain Boards can form a wireless mesh — one acts as the Host (serving a live web dashboard), others act as Remote nodes sending readings every few seconds.</p>
  </div>
  <div>
    <h3 style="font-size:17px;font-weight:700;margin-bottom:.8rem;">What&rsquo;s in the box</h3>
    <ul style="font-size:14px;color:var(--text-body);line-height:2;padding-left:1.2rem;">
      <li>1× Brain Board V2.0 (assembled)</li>
      <li>Onboard SHTC3 temp/humidity sensor</li>
      <li>Onboard TSL2591 ambient light sensor</li>
      <li>2× Qwiic connectors for expansion</li>
    </ul>
    <p style="font-size:12px;color:var(--text-muted);margin-top:.8rem;">USB-C cable and Qwiic sensors sold separately.</p>
  </div>
</div>
<div style="background:var(--amber-pale);border:1.5px solid var(--amber-tag);border-radius:12px;padding:1.2rem 1.4rem;">
  <p style="font-size:13px;color:var(--text-body);line-height:1.7;"><strong>New to Automato?</strong> Start with the <a href="../docs.html" style="color:var(--green);">Brain Board quick start guide</a> — you&rsquo;ll have live sensor data in your browser in under 10 minutes.</p>
</div>'''

bb_links = '''
<a class="link-card" href="../docs.html"><div class="link-card-icon">🚀</div><div><h4>Quick start guide</h4><p>First boot to live dashboard in 10 minutes</p></div><span class="arrow">→</span></a>
<a class="link-card" href="../docs.html"><div class="link-card-icon">📖</div><div><h4>Firmware reference</h4><p>Full API, endpoints, and configuration</p></div><span class="arrow">→</span></a>
<a class="link-card" href="https://github.com/Automato-ag/Brain-Board" target="_blank"><div class="link-card-icon">💻</div><div><h4>GitHub repository</h4><p>Firmware, hardware reference, docs</p></div><span class="arrow">↗</span></a>
<a class="link-card" href="../docs.html"><div class="link-card-icon">⚡</div><div><h4>Relay control guide</h4><p>Connecting and automating the Relay Board</p></div><span class="arrow">→</span></a>
<a class="link-card" href="../docs.html"><div class="link-card-icon">📡</div><div><h4>ESP-NOW mesh setup</h4><p>Multi-node wireless sensor networks</p></div><span class="arrow">→</span></a>
<a class="link-card" href="../docs.html"><div class="link-card-icon">🔧</div><div><h4>Hardware reference</h4><p>Schematics, BOM, and pin map</p></div><span class="arrow">→</span></a>'''

bb_docs = {'overview': bb_overview, 'links': bb_links}

bb_svg_large = brain_svg.replace('width="72%"', 'width="78%"')

with open('./products/brain-board.html', 'w', encoding='utf-8') as f:
    f.write(product_detail(
        'Brain Board V2.0', 'New — ESP32-C6', 'Brain Board V2.0', '$25',
        'Our newest wireless sensor node. Onboard temperature, humidity, and ambient light sensors. WiFi 6 and ESP-NOW Long Range mesh networking. Expand with any Qwiic I2C sensor — no soldering required.',
        bb_svg_large, bb_specs_tags, bb_specs_rows, bb_pins_rows, bb_docs,
        'https://github.com/Automato-ag/Brain-Board',
        STRIPE_BRAIN_BOARD
    ))
print("brain-board.html done")

# ── SENSOR BOARD ─────────────────────────────────────────────────────────────
sb_specs_tags = '''<span class="spec-tag">ESP32</span><span class="spec-tag">LoRa</span><span class="spec-tag">Display</span>
<span class="spec-tag">14x I/O</span><span class="spec-tag">LiPo</span><span class="spec-tag">microSD</span>
<span class="spec-tag">USB-C</span><span class="spec-tag">Open source</span>'''

sb_specs_rows = '''
<tr><td>Microcontroller</td><td>ESP32-WROOM-DA-N4 (Xtensa dual-core 240 MHz, 4 MB flash, dual antenna)</td></tr>
<tr><td>Wireless</td><td>LoRa (RFM95W-868S2), WiFi 802.11 b/g/n, Bluetooth 4.2</td></tr>
<tr><td>Display</td><td>Built-in display (see KiCad files for exact part)</td></tr>
<tr><td>I/O terminal</td><td>14-channel Phoenix Contact screw terminal (3.5 mm pitch) — analog + digital</td></tr>
<tr><td>USB</td><td>2× USB-C (Amphenol 12401610E4-2A) — one for power/programming, one for data</td></tr>
<tr><td>Battery</td><td>LiPo connector (JST PH 2-pin), MCP73831T charge controller, P-ch MOSFET power path</td></tr>
<tr><td>Power regulation</td><td>Diodes Inc. AP2112K-3.3 LDO (3.3V), Monolithic Power MP2452DD buck regulator</td></tr>
<tr><td>USB-UART</td><td>Silicon Labs CP2104-F03 bridge</td></tr>
<tr><td>Data storage</td><td>microSD (Hirose DM3D-SF connector)</td></tr>
<tr><td>SMA connector</td><td>Right-angle edge-mount SMA for external LoRa antenna</td></tr>
<tr><td>Switches</td><td>RESET, BOOT (tactile), power SPDT (C&amp;K L102021ML04Q)</td></tr>
<tr><td>LEDs</td><td>Yellow, Green, Red status LEDs</td></tr>
<tr><td>Relay Board control</td><td>Via USB-C cable (planned addition to Relay Board schematic) or direct GPIO pin via 14-ch I/O terminal → Relay Board SPI header</td></tr>
<tr><td>License</td><td>MIT (hardware &amp; firmware)</td></tr>'''

sb_pins_rows = '''
<tr><td>I/O Terminal CH1–CH14</td><td>Various</td><td>3.5 mm screw terminal — analog/digital I/O, power, GND. Any channel can drive Relay Board SPI control.</td></tr>
<tr><td>Qwiic</td><td>IO21 (SDA), IO22 (SCL)</td><td>I2C expansion via JST 1 mm 4-pin connector</td></tr>
<tr><td>SMA</td><td>—</td><td>External LoRa antenna connector</td></tr>
<tr><td>LiPo</td><td>—</td><td>JST PH 2-pin battery connector</td></tr>
<tr><td>microSD</td><td>SPI bus</td><td>Data logging storage</td></tr>
<tr><td>BOOT</td><td>IO0</td><td>Boot button — hold at power-on for flash mode</td></tr>
<tr><td>RESET</td><td>EN</td><td>Hard reset</td></tr>'''

sb_overview = '''<div style="display:grid;grid-template-columns:1fr 1fr;gap:2rem;margin-bottom:2rem;">
  <div>
    <h3 style="font-size:17px;font-weight:700;margin-bottom:.8rem;">The original Automato node</h3>
    <p style="font-size:14px;color:var(--text-body);line-height:1.8;">The Sensor Board is a fully-featured ESP32 sensor and control node with a built-in display, 14 screw-terminal I/O channels, LoRa radio for long-range mesh, LiPo battery support, and microSD data logging — all in one board.</p>
    <p style="font-size:14px;color:var(--text-body);line-height:1.8;margin-top:.8rem;">It&rsquo;s designed for installations where you need lots of wired I/O — connecting existing analog sensors, relays, solenoids, and meters to a single central node.</p>
  </div>
  <div>
    <h3 style="font-size:17px;font-weight:700;margin-bottom:.8rem;">Controlling the Relay Board</h3>
    <p style="font-size:14px;color:var(--text-body);line-height:1.8;">The Sensor Board can control the Relay Board in two ways:</p>
    <ul style="font-size:14px;color:var(--text-body);line-height:2.1;padding-left:1.2rem;margin-top:.5rem;">
      <li><strong>USB-C cable</strong> — direct plug-and-play connection between the two boards <em>(planned addition — not in current Relay Board schematic)</em></li>
      <li><strong>GPIO pin</strong> — wire a GPIO pin from the 14-channel I/O terminal directly to the Relay Board&rsquo;s SPI control header</li>
    </ul>
    <p style="font-size:12px;color:var(--text-muted);margin-top:.8rem;">USB-C cable, LiPo battery, LoRa antenna, and sensors sold separately.</p>
  </div>
</div>
<div style="background:var(--amber-pale);border:1.5px solid var(--amber-tag);border-radius:12px;padding:1.2rem 1.4rem;">
  <p style="font-size:13px;color:var(--text-body);line-height:1.7;"><strong>Comparing boards?</strong> The Brain Board V2.0 is our newer, more compact node with onboard sensors and WiFi 6. The Sensor Board is better when you need lots of wired I/O, long-range LoRa mesh, or direct USB-C relay control.</p>
</div>'''

sb_links = '''
<a class="link-card" href="../docs.html"><div class="link-card-icon">🚀</div><div><h4>Quick start guide</h4><p>Flash firmware and connect sensors</p></div><span class="arrow">→</span></a>
<a class="link-card" href="../docs.html"><div class="link-card-icon">📖</div><div><h4>Firmware reference</h4><p>Full API and I/O configuration</p></div><span class="arrow">→</span></a>
<a class="link-card" href="https://github.com/InterstitialTech/automato-sensor" target="_blank"><div class="link-card-icon">💻</div><div><h4>Hardware files on GitHub</h4><p>KiCad schematics, BOM, PCB layout</p></div><span class="arrow">↗</span></a>
<a class="link-card" href="https://github.com/InterstitialTech/automato-sketches" target="_blank"><div class="link-card-icon">📋</div><div><h4>Example sketches</h4><p>Arduino code samples for common setups</p></div><span class="arrow">↗</span></a>
<a class="link-card" href="../docs.html"><div class="link-card-icon">🌿</div><div><h4>LoRa long-range setup</h4><p>Multi-node mesh with LoRa radio</p></div><span class="arrow">→</span></a>
<a class="link-card" href="../products.html"><div class="link-card-icon">⚡</div><div><h4>Pair with the Relay Board</h4><p>Add 4-channel mains-rated switching</p></div><span class="arrow">→</span></a>'''

sb_docs = {'overview': sb_overview, 'links': sb_links}
sb_svg_large = sensor_svg.replace('width="72%"', 'width="78%"')

with open('./products/sensor-board.html', 'w', encoding='utf-8') as f:
    f.write(product_detail(
        'Sensor Board', 'Original Automato node', 'Sensor Board', '$30',
        'The original Automato node. ESP32 + LoRa radio, built-in display, 14-channel screw-terminal I/O, LiPo battery charging, and microSD data logging. Designed for wired sensor installations and long-range LoRa mesh networks.',
        sb_svg_large, sb_specs_tags, sb_specs_rows, sb_pins_rows, sb_docs,
        'https://github.com/InterstitialTech/automato-sensor',
        STRIPE_SENSOR_BOARD
    ))
print("sensor-board.html done")

# ── RELAY BOARD ───────────────────────────────────────────────────────────────
rb_specs_tags = '''<span class="spec-tag">4× relay</span><span class="spec-tag">AC/DC PSU</span><span class="spec-tag">Mains-rated</span>
<span class="spec-tag">Optoisolated</span><span class="spec-tag">74HC595</span><span class="spec-tag">USB-C control</span><span class="spec-tag">GPIO control</span><span class="spec-tag">Open source</span>'''

rb_specs_rows = '''
<tr><td>Relay channels</td><td>4× Omron G5LE-14 DC3 — SPDT, rated 10 A / 250 VAC</td></tr>
<tr><td>Relay driver</td><td>Toshiba 74HC595D shift register — SPI-controlled, daisy-chainable</td></tr>
<tr><td>MOSFET drivers</td><td>Diodes Inc. DMG3418L (N-ch) — one per relay coil</td></tr>
<tr><td>Freewheeling diodes</td><td>SMC 1N4007 (per relay), BAS16LT1G (signal path)</td></tr>
<tr><td>AC/DC power supply</td><td>Hi-Link HLK-PM03 — 100–240 VAC input, 3.3 V / 3 W output</td></tr>
<tr><td>Mains protection</td><td>Littelfuse TMOV14RP140E metal-oxide varistor (MOV)</td></tr>
<tr><td>Mains connectors</td><td>TE Connectivity 3-213598-4 (live, neutral, earth) and 5-pin screw terminal</td></tr>
<tr><td>Low-voltage connector</td><td>Phoenix Contact 1935789 (3-pin, for GPIO control signal + 5V + GND)</td></tr>
<tr><td>Host control — Option 1</td><td>USB-C connector from Sensor Board (not in current schematic — planned addition)</td></tr>
<tr><td>Host control — Option 2</td><td>Direct GPIO pin from any Automato sensor node via 3-pin screw terminal</td></tr>
<tr><td>Status LEDs</td><td>4× Würth green LED — one per relay channel</td></tr>
<tr><td>Decoupling</td><td>Kemet 47 nF (×4 relay), 220 µF bulk, 100 nF and 10 µF supply caps</td></tr>
<tr><td>License</td><td>MIT (hardware)</td></tr>'''

rb_pins_rows = '''
<tr><td>Relay OUT 1–4</td><td>—</td><td>SPDT switched contacts — NO, COM, NC per channel</td></tr>
<tr><td>AC LINE IN</td><td>—</td><td>Live, neutral, earth mains input</td></tr>
<tr><td>USB-C (host)</td><td>—</td><td>Control connection from Sensor Board via USB-C cable (planned — not in current schematic)</td></tr>
<tr><td>GPIO CTRL</td><td>SPI (74HC595)</td><td>Direct GPIO control from sensor node — SER, SRCLK, RCLK via 3-pin screw terminal</td></tr>
<tr><td>VCC</td><td>—</td><td>5 V logic supply from host or USB hub</td></tr>
<tr><td>GND</td><td>—</td><td>Common ground (low-voltage side, isolated from mains)</td></tr>'''

rb_overview = '''<div style="display:grid;grid-template-columns:1fr 1fr;gap:2rem;margin-bottom:2rem;">
  <div>
    <h3 style="font-size:17px;font-weight:700;margin-bottom:.8rem;">Mains switching for your grow</h3>
    <p style="font-size:14px;color:var(--text-body);line-height:1.8;">The Relay Board gives any Automato sensor node the ability to switch mains-voltage loads — pumps, lights, heaters, fans, solenoids. Four independent SPDT channels, each rated 10 A / 250 VAC.</p>
    <p style="font-size:14px;color:var(--text-body);line-height:1.8;margin-top:.8rem;">The onboard Hi-Link PSU powers the board directly from mains — no separate supply needed. Optoisolated control keeps your microcontroller safely isolated from line voltage.</p>
  </div>
  <div>
    <h3 style="font-size:17px;font-weight:700;margin-bottom:.8rem;">Two ways to control it</h3>
    <ul style="font-size:14px;color:var(--text-body);line-height:2.1;padding-left:1.2rem;">
      <li><strong>USB-C</strong> — connect directly to the Sensor Board via USB-C cable for plug-and-play control <em>(planned addition — not in current schematic)</em></li>
      <li><strong>GPIO pin</strong> — wire any Automato node directly via the 3-pin screw terminal (SPI to 74HC595)</li>
    </ul>
    <p style="font-size:12px;color:var(--text-muted);margin-top:.8rem;"><strong>Safety note:</strong> This board connects to mains voltage. Follow all local electrical codes. If in doubt, consult a licensed electrician.</p>
  </div>
</div>
<div style="background:var(--green-pale);border:1.5px solid var(--green-tag);border-radius:12px;padding:1.2rem 1.4rem;margin-bottom:1rem;">
  <p style="font-size:13px;color:var(--text-body);line-height:1.7;"><strong>Safety defaults:</strong> All relays default to OFF at boot, on power loss, and on connectivity loss. This is by design and cannot be changed.</p>
</div>
<div style="background:var(--amber-pale);border:1.5px solid var(--amber-tag);border-radius:12px;padding:1.2rem 1.4rem;">
  <p style="font-size:13px;color:var(--text-body);line-height:1.7;"><strong>Pairing with the Brain Board?</strong> Connect via Qwiic to the SparkFun Qwiic GPIO (TCA9534, I2C 0x20) for relay control without consuming GPIO pins on the microcontroller.</p>
</div>'''

rb_links = '''
<a class="link-card" href="../docs.html"><div class="link-card-icon">🔧</div><div><h4>Relay wiring &amp; safety guide</h4><p>Mains wiring, best practices, safety checklist</p></div><span class="arrow">→</span></a>
<a class="link-card" href="../docs.html"><div class="link-card-icon">🚀</div><div><h4>First relay automation</h4><p>Quick start — control a pump from sensor data</p></div><span class="arrow">→</span></a>
<a class="link-card" href="https://github.com/InterstitialTech/automato-relay" target="_blank"><div class="link-card-icon">💻</div><div><h4>Hardware files on GitHub</h4><p>KiCad schematics, BOM, PCB layout</p></div><span class="arrow">↗</span></a>
<a class="link-card" href="../docs.html"><div class="link-card-icon">⚡</div><div><h4>Relay control API</h4><p>HTTP endpoints and automation rules</p></div><span class="arrow">→</span></a>
<a class="link-card" href="brain-board.html"><div class="link-card-icon">🧠</div><div><h4>Pair with the Brain Board</h4><p>Qwiic GPIO expansion for relay control</p></div><span class="arrow">→</span></a>
<a class="link-card" href="sensor-board.html"><div class="link-card-icon">📡</div><div><h4>Pair with the Sensor Board</h4><p>LoRa + relay for distributed setups</p></div><span class="arrow">→</span></a>'''

rb_docs = {'overview': rb_overview, 'links': rb_links}
rb_svg_large = relay_svg.replace('width="72%"', 'width="78%"')

with open('./products/relay-board.html', 'w', encoding='utf-8') as f:
    f.write(product_detail(
        'Relay Board', 'Mains-rated relay controller', 'Relay Board', '$32',
        '4-channel relay board with mains-rated contacts (10 A / 250 VAC) and onboard AC/DC power supply. Connect to the Sensor Board via USB-C cable, or control any channel via a direct GPIO pin. Switch pumps, lights, heaters, and fans from any Automato sensor node.',
        rb_svg_large, rb_specs_tags, rb_specs_rows, rb_pins_rows, rb_docs,
        'https://github.com/InterstitialTech/automato-relay',
        STRIPE_RELAY_BOARD
    ))
print("relay-board.html done")

print("\nAll pages generated successfully!")

# ── NETLIFY CONFIG ────────────────────────────────────────────────────────────
# netlify.toml — caching, security headers, publish directory
with open('./netlify.toml', 'w', encoding='utf-8') as f:
    f.write('''[build]
  publish = "."

[[headers]]
  for = "/*"
  [headers.values]
    X-Frame-Options = "DENY"
    X-Content-Type-Options = "nosniff"
    Referrer-Policy = "strict-origin-when-cross-origin"

[[headers]]
  for = "/*.html"
  [headers.values]
    Cache-Control = "public, max-age=0, must-revalidate"

[[headers]]
  for = "/assets/*"
  [headers.values]
    Cache-Control = "public, max-age=31536000, immutable"
''')
print("netlify.toml done")

# _redirects — clean URLs (no .html extension) and www → root redirect
with open('./_redirects', 'w', encoding='utf-8') as f:
    f.write('''# Clean URLs — strip .html extension
/products     /products.html    200
/docs         /docs.html        200
/github       /github.html      200
/about        /about.html       200
/contact      /contact.html     200
/products/brain-board    /products/brain-board.html    200
/products/sensor-board   /products/sensor-board.html   200
/products/relay-board    /products/relay-board.html    200

# www → root
https://www.automato.ag/*  https://automato.ag/:splat  301!
''')
print("_redirects done")
