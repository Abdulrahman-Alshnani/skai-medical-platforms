from common import *

NAV = [("#platforms", "Platforms"), ("#results", "Contact")]

PLATFORMS = [
    ("IT Transformation", [("/inventory/", "box", "Warehouse &amp; Inventory Control Platform", "Every item, every location, every batch."),
                           ("/business/", "layers", "Business Management Platform", "One system for sales, purchasing, finance and people.")]),
    ("AI Transformation", [("/supply-chain/", "trend", "Intelligent Warehouse &amp; Supply Chain Platform", "Predict expiry and stock-outs before they happen."),
                           ("/supply-chain/#cold-chain", "thermo", "Temperature-Protected Supply Chain", "Every degree recorded, every breach caught in minutes."),
                           ("/business-ai/", "bot", "Intelligent Business Management Platform", "Forecasts and answers, in Arabic and English.")]),
]


def diagram():
    nodes = [("Warehouse &amp; Inventory", "IT", 100), ("Business Management", "IT", 290), ("Intelligent Warehouse", "AI", 500), ("Temperature-Protected", "AI", 710), ("Intelligent Business", "AI", 900)]
    lines = "".join(f'<path class="flow" d="M500,96 C500,170 {x},150 {x},232" fill="none" stroke="{"#000" if g == "IT" else "#0047ff"}" stroke-width="1.6"/>' for _, g, x in nodes)
    boxes = "".join(f'<g transform="translate({x},262)"><rect x="-88" y="-28" width="176" height="56" rx="12" fill="#fff" stroke="#e3e5e8"/>'
                    f'<text y="-4" text-anchor="middle" font-size="11" style="fill:{"#5f6368" if g == "IT" else "#0047ff"};letter-spacing:.12em;font-weight:500">{g}</text>'
                    f'<text y="14" text-anchor="middle" font-size="14" style="fill:#000;font-weight:600;font-family:Hanken Grotesk,Arial">{n}</text></g>' for n, g, x in nodes)
    core = ('<g transform="translate(500,58)"><circle r="54" fill="rgba(0,71,255,.06)"/><circle r="40" fill="#000"/>'
            '<polygon points="-16,14 0,-18 16,14 8,14 0,-2 -8,14" fill="#fff"/></g>')
    return f'<div class="hub hide-sm" data-reveal><svg viewBox="0 0 1000 300" style="width:100%;height:auto" role="img" aria-label="SKAI platforms connected to one core">{lines}{core}{boxes}</svg></div>'


def build():
    groups = ""
    for gi, (g, items) in enumerate(PLATFORMS):
        cards = "".join(
            f'<div data-reveal style="--d:{i*90}ms"><a class="card" href="{h}" style="display:flex;flex-direction:column;height:100%">'
            f'<div class="ico">{ic(icn)}</div><h3 class="h3">{t}</h3><p style="flex:1">{d}</p>'
            f'<span style="margin-top:24px;display:inline-flex;gap:8px;align-items:center;color:var(--cobalt);font-weight:500;font-size:var(--t-small)">See the platform <svg style="width:16px;height:16px" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14"/><path d="m13 6 6 6-6 6"/></svg></span></a></div>'
            for i, (h, icn, t, d) in enumerate(items))
        groups += (f'<div class="mt-40">{eyebrow(f"0{gi+1}", g)}<div class="features" style="margin-top:20px">{cards}</div></div>')
    return (head("SKAI Group · Platforms for healthcare supply chains",
                 "Software and AI for pharmaceutical warehouses, medical distributors and healthcare logistics in Jordan and the Gulf.", "/")
            + header(NAV, "/")
            + f"""<section class="hero" id="top"><div class="shell">
  <div class="hero-copy" style="max-width:860px">{eyebrow(None, 'SKAI Group · Healthcare')}
    <h1 class="display split">Every shelf, every shipment, every patient: <span class="accent">protected, traceable, ready to grow.</span></h1>
    <p class="lead fade-in" style="--fd:700ms">Software and AI for pharmaceutical warehouses, medical distributors and healthcare logistics in Jordan and the Gulf.</p>
    <div class="fade-in" style="--fd:850ms">{cta()}</div></div></div></section>
{band(["Pharmaceutical warehouses","Medical supply companies","Pharmacy distribution","Healthcare logistics","Temperature-controlled storage","Jordan and the Gulf"])}
<section class="section" id="platforms"><div class="shell">
  {sec_head(None, 'Our platforms', 'Two transformations, one partner.', 'Start with the system you need today and add intelligence when you are ready.')}
  {diagram()}
  {groups}
</div></section>
"""
            + dark('03', 'Let us show you on a call.', 'Twenty minutes, your questions, our platforms on screen.',
                   [('<span data-count="30">30</span>+', 'Projects delivered'), ('<span data-count="20">20</span>+', 'Awards in AI'), ('2', 'Languages, Arabic and English')], ink=True).replace(
                '<p class="small" style="color:var(--soft);margin-top:28px;position:relative">Illustrative estimates for a mid-size pharmaceutical warehouse.</p>', '')
            + footer())
