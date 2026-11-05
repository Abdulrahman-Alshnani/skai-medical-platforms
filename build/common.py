"""Shared partials for the SKAI medical platform pages (static site generator)."""

CAL = "https://calendly.com/founders-skaigroup/20min"
MAIL = "founders@skaigroup.tech"

_P = {
    "check": '<path d="M20 6 9 17l-5-5"/>',
    "arrow": '<path d="M7 17 17 7"/><path d="M8 7h9v9"/>',
    "right": '<path d="M5 12h14"/><path d="m13 6 6 6-6 6"/>',
    "x": '<path d="M18 6 6 18"/><path d="m6 6 12 12"/>',
    "grid": '<rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/>',
    "box": '<path d="M21 8 12 3 3 8v8l9 5 9-5z"/><path d="m3 8 9 5 9-5"/><path d="M12 13v8"/>',
    "inbox": '<path d="M22 12h-6l-2 3h-4l-2-3H2"/><path d="M5.5 5h13L22 12v6a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2v-6z"/>',
    "truck": '<path d="M14 18V6H2v12h2"/><path d="M14 9h4l4 4v5h-2"/><circle cx="7" cy="18" r="2"/><circle cx="17" cy="18" r="2"/><path d="M9 18h6"/>',
    "list": '<path d="M9 6h12M9 12h12M9 18h12"/><path d="M4 6h.01M4 12h.01M4 18h.01"/>',
    "chart": '<path d="M3 3v18h18"/><path d="M7 15l4-4 3 3 5-6"/>',
    "scan": '<path d="M3 7V5a2 2 0 0 1 2-2h2M17 3h2a2 2 0 0 1 2 2v2M21 17v2a2 2 0 0 1-2 2h-2M7 21H5a2 2 0 0 1-2-2v-2"/><path d="M7 8v8M11 8v8M15 8v8M18 8v8"/>',
    "route": '<circle cx="6" cy="19" r="3"/><path d="M9 19h8.5a3.5 3.5 0 0 0 0-7h-11a3.5 3.5 0 0 1 0-7H15"/><circle cx="18" cy="5" r="3"/>',
    "thermo": '<path d="M14 4v10.54a4 4 0 1 1-4 0V4a2 2 0 0 1 4 0Z"/>',
    "trend": '<path d="m22 7-8.5 8.5-5-5L2 17"/><path d="M16 7h6v6"/>',
    "layers": '<path d="m12 2 10 5-10 5L2 7z"/><path d="m2 17 10 5 10-5"/><path d="m2 12 10 5 10-5"/>',
    "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/>',
    "plug": '<path d="M12 22v-5"/><path d="M9 8V2M15 8V2"/><path d="M18 8v5a6 6 0 0 1-12 0V8z"/>',
    "users": '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/>',
    "cart": '<circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.7 13.4a2 2 0 0 0 2 1.6h9.7a2 2 0 0 0 2-1.6L23 6H6"/>',
    "wallet": '<path d="M20 12V8H6a2 2 0 0 1 0-4h12v4"/><path d="M4 6v12a2 2 0 0 0 2 2h14v-4"/><path d="M18 12a2 2 0 0 0 0 4h4v-4z"/>',
    "file": '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M9 15l2 2 4-4"/>',
    "bot": '<rect x="3" y="8" width="18" height="12" rx="3"/><path d="M12 8V4M8 4h8"/><path d="M9 14h.01M15 14h.01"/>',
    "spark": '<path d="M12 3l1.9 5.6L19.5 10l-5.6 1.9L12 17.5l-1.9-5.6L4.5 10l5.6-1.4z"/><path d="M19 3v4M17 5h4"/>',
    "check2": '<path d="M9 11l3 3L22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/>',
    "settings": '<circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 1 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 1 1-4 0v-.09a1.65 1.65 0 0 0-1-1.51 1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 1 1-2.83-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 1 1 0-4h.09a1.65 1.65 0 0 0 1.51-1 1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 1 1 2.83-2.83l.06.06a1.65 1.65 0 0 0 1.82.33h0a1.65 1.65 0 0 0 1-1.51V3a2 2 0 1 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 1 1 2.83 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82v0a1.65 1.65 0 0 0 1.51 1H21a2 2 0 1 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z"/>',
    "bell": '<path d="M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9"/><path d="M10.3 21a1.94 1.94 0 0 0 3.4 0"/>',
    "lock": '<rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>',
    "globe": '<circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>',
    "snow": '<path d="M12 2v20M17 5l-5 5-5-5M17 19l-5-5-5 5M2 12h20M5 7l5 5-5 5M19 7l-5 5 5 5"/>',
}


def ic(name, cls=""):
    return (f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{_P[name]}</svg>')


LOGO = ('<svg viewBox="0 0 60 20" aria-hidden="true"><text x="0" y="17.5" font-family="Hanken Grotesk, Helvetica Neue, Arial, sans-serif" '
        'font-weight="700" font-size="21" letter-spacing="1" fill="currentColor">SK</text>'
        '<polygon points="29.6,19.5 38.6,1 47.6,19.5 43.2,19.5 38.6,9 34,19.5" fill="currentColor"/>'
        '<text x="50" y="17.5" font-family="Hanken Grotesk, Helvetica Neue, Arial, sans-serif" font-weight="700" font-size="21" fill="currentColor">I</text></svg>')

APEX_BG = ('<svg class="apex-bg" viewBox="0 0 100 100" aria-hidden="true"><polygon fill="currentColor" '
           'points="0,100 49.4,0 100,100 74.5,100 49.4,43 25,100"/></svg>')


def logo(home="/"):
    return f'<a class="logo" href="{home}" aria-label="SKAI Group">{LOGO}<span class="grp">GROUP</span></a>'


def head(title, desc, path):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta name="theme-color" content="#ffffff">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600&family=IBM+Plex+Mono:wght@400&family=Instrument+Serif:ital@1&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/site.css">
<script>if(matchMedia("(prefers-reduced-motion: no-preference)").matches&&"IntersectionObserver"in window)document.documentElement.classList.add("js")</script>
</head>
<body>
<a class="sr-only" href="#main">Skip to content</a>
"""


PLATFORMS = [("IT Transformation", [("/inventory/", "box", "Warehouse &amp; Inventory Control"), ("/business/", "layers", "Business Management")]),
             ("AI Transformation", [("/supply-chain/", "trend", "Intelligent Warehouse &amp; Supply Chain"), ("/cold-chain/", "thermo", "Temperature-Protected Supply Chain"),
                                    ("/business-ai/", "bot", "Intelligent Business Management")])]


def switcher(cur):
    body = ""
    for g, items in PLATFORMS:
        body += f"<small>{g}</small>" + "".join(f'<a href="{h}" class="{"cur" if h == cur else ""}">{ic(i)}{t}</a>' for h, i, t in items)
    body += '<small>All</small><a href="/">' + ic("grid") + 'All platforms</a>'
    chev = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="m6 9 6 6 6-6"/></svg>'
    return f'<div class="switch"><button type="button" aria-expanded="false" aria-haspopup="true">Platforms {chev}</button><div class="pop">{body}</div></div>'


def menu_platforms(cur):
    return '<div class="shell plat">' + "".join(f'<a href="{h}" class="{"cur" if h == cur else ""}">{t}</a>' for _, items in PLATFORMS for h, _i, t in items) + "</div>"


def band(items, light=False, rev=False, dur=40):
    one = "".join(f"<span>{t}<i></i></span>" for t in items)
    cls = "band" + (" light" if light else "") + (" rev" if rev else "")
    return f'<div class="{cls}" aria-hidden="true" style="--dur:{dur}s"><div class="track">{one}{one}</div></div>'


def header(nav, cur=""):
    links = "".join(f'<a href="{h}">{l}</a>' for h, l in nav)
    items = "".join(
        f'<li style="--i:{i}"><a href="{h}"><span class="n">0{i+1}</span><span>{l}</span></a></li>' for i, (h, l) in enumerate(nav))
    return f"""<div class="header-spacer" aria-hidden="true"></div>
<header class="site-header">
  <div class="shell bar">
    {logo()}
    <nav class="nav" aria-label="Sections">{links}</nav>
    <div style="display:flex;align-items:center;gap:8px">
      {switcher(cur)}
      <a class="btn sm header-cta" href="{CAL}" target="_blank" rel="noopener">Book a discovery call {ic('arrow')}</a>
      <button class="menu-btn" type="button" aria-label="Open menu" aria-controls="menu" aria-expanded="false"><span></span></button>
    </div>
  </div>
  <div class="progress" aria-hidden="true"></div>
</header>
<div class="menu" id="menu" role="dialog" aria-modal="true" aria-label="Menu" aria-hidden="true" inert>
  <div class="shell top">{logo()}<button class="close" type="button" aria-label="Close menu">{ic('x')}</button></div>
  <ol class="shell">{items}</ol>
  {menu_platforms(cur)}
  <div class="shell foot">
    <a class="btn" href="{CAL}" target="_blank" rel="noopener">Book a free 20-minute discovery call {ic('arrow')}</a>
    <a class="mail" href="mailto:{MAIL}">{MAIL}</a>
  </div>
</div>
<main id="main">
"""


def eyebrow(idx, text):
    i = f'<span class="idx">{idx}</span><span class="rule"></span>' if idx else ""
    return f'<p class="eyebrow">{i}{text}</p>'


def sec_head(idx, eb, title, lead=None, center=False):
    l = f'<p class="lead">{lead}</p>' if lead else ""
    return f'<div class="sec-head{" center" if center else ""}" data-reveal>{eyebrow(idx, eb)}<h2 class="h2">{title}</h2>{l}</div>'


def cta(label="Book a free 20-minute discovery call"):
    return f'<a class="btn" href="{CAL}" target="_blank" rel="noopener">{label} {ic("arrow")}</a>'


def features(items):
    out = []
    for i, (icon, t, d) in enumerate(items):
        out.append(f'<div data-reveal style="--d:{i*90}ms"><article class="card"><div class="ico">{ic(icon)}</div>'
                   f'<h3 class="h3">{t}</h3><p>{d}</p></article></div>')
    return f'<div class="features">{"".join(out)}</div>'


def checks(items):
    return '<ul class="checks">' + "".join(f'<li>{ic("check")}<span>{t}</span></li>' for t in items) + "</ul>"


def dark(idx, title, lead, stats):
    st = "".join(f'<div class="stat" data-reveal style="--d:{i*100}ms"><div class="v">{v}</div><p class="l">{l}</p></div>'
                 for i, (v, l) in enumerate(stats))
    return f"""<section class="section dark" id="results">
  {APEX_BG}
  <div class="shell" style="position:relative">
    <div class="sec-head" data-reveal>{eyebrow(idx, 'Results')}<h2 class="h2">{title}</h2><p class="lead">{lead}</p></div>
    <div class="stats">{st}</div>
    <div class="cta-row" data-reveal>{cta()}<a class="mail" href="mailto:{MAIL}">{MAIL}</a></div>
    <p class="small" style="color:#6b7177;margin-top:28px;position:relative">Illustrative estimates for a mid-size pharmaceutical warehouse.</p>
  </div>
</section>
"""


def footer():
    return f"""</main>
<footer class="footer">
  <div class="shell row">
    {logo()}
    <div class="links">
      <a href="/">All platforms</a>
      <a href="https://skaigroup.tech" target="_blank" rel="noopener">skaigroup.tech</a>
      <a href="mailto:{MAIL}">{MAIL}</a>
      <span style="display:inline-flex;align-items:center;min-height:44px">Amman, Jordan</span>
    </div>
  </div>
</footer>
<div class="cta-bar"><a class="btn" href="{CAL}" target="_blank" rel="noopener">Book a free 20-minute discovery call {ic('arrow')}</a></div>
<button class="to-top" type="button" aria-label="Back to top"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="m18 15-6-6-6 6"/></svg></button>
<script src="/assets/site.js" defer></script>
<script src="/assets/interact.js" defer></script>
</body>
</html>
"""


def frame(url, inner, cls=""):
    return (f'<div class="frame {cls}"><div class="chrome"><i></i><i></i><i></i><span class="url">{url}</span></div>'
            f'{inner}</div>')


def side(ws_label, ws, items, on):
    a = "".join(f'<a class="{"on" if l == on else ""}">{ic(i)}{l}</a>' for i, l in items)
    return f'<aside class="app-side"><div class="ws"><small>{ws_label}</small><b>{ws}</b></div>{a}</aside>'


def kpis(items):
    out = []
    for k, v, d, *opt in items:
        c = " c" if "c" in opt else ""
        up = " up" if "up" in opt else ""
        out.append(f'<div class="kpi"><div class="k">{k}</div><div class="v{c} tabular">{v}</div><div class="d{up}">{d}</div></div>')
    return f'<div class="kpis">{"".join(out)}</div>'


def app_head(title, sub, tools=("Search", "All sites", "Export")):
    t = "".join(f"<span>{x}</span>" for x in tools)
    return f'<div class="app-head"><div><h4>{title}</h4><div class="sub">{sub}</div></div><div class="tools">{t}</div></div>'


def chip(kind, text, live=False):
    return f'<span class="chip {kind}{" live" if live else ""}">{text}</span>'
