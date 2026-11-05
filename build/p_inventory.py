from common import *

NAV = [("#capabilities", "Capabilities"), ("#scanning", "Scanning"), ("#operations", "Operations"), ("#how", "How it works"), ("#results", "Results")]

ROWS = [
    ("Amoxicillin 500mg", "Capsules · 20s", "AMX-2604-118", "Amman", "A-02-14", "12,480", "18 Aug 2027", ("ok", "OK")),
    ("Insulin Glargine 100IU/mL", "Pen · 3mL · Cold chain", "IGL-2611-04", "Amman", "C-01-03", "1,260", "02 Dec 2026", ("warn", "Expiring soon")),
    ("Paracetamol 500mg", "Tablets · 24s", "PCM-2609-221", "Irbid", "A-05-02", "48,000", "30 Sep 2027", ("ok", "OK")),
    ("Omeprazole 20mg", "Capsules · 14s", "OMP-2603-077", "Riyadh", "B-03-11", "6,720", "21 Nov 2026", ("warn", "Expiring soon")),
    ("Ceftriaxone 1g", "Vial · IV/IM", "CFX-2510-019", "Dubai", "B-07-04", "340", "28 Oct 2026", ("crit", "Expired")),
    ("Metformin 850mg", "Tablets · 30s", "MTF-2607-145", "Amman", "A-08-09", "22,350", "14 Jun 2027", ("ok", "OK")),
    ("Atorvastatin 20mg", "Tablets · 30s", "ATV-2605-063", "Riyadh", "B-01-06", "9,600", "05 Mar 2027", ("ok", "OK")),
    ("Salbutamol 100mcg", "Inhaler · 200 doses", "SLB-2608-031", "Dubai", "B-04-01", "1,880", "11 Jan 2027", ("ok", "OK")),
]


def inv_table():
    body = ""
    for i, (p, f, b, s, z, q, e, (k, t)) in enumerate(ROWS[:6]):
        body += (f'<tr><td class="main">{p}<small>{f}</small></td><td class="meta mono" data-l="Batch">{b}</td>'
                 f'<td class="meta hide-c2" data-l="Site">{s}</td><td class="meta mono hide-m hide-c" data-l="Bin">{z}</td>'
                 f'<td class="meta num" data-l="Qty">{q}</td><td class="meta nw" data-l="Expiry">{e}</td>'
                 f'<td class="end">{chip(k, t, live=(k == "crit"))}</td></tr>')
    return (f'<div class="panel"><div class="ph">All batches <span>Sort: FEFO</span></div>'
            f'<table class="rtable lim"><thead><tr><th>Product</th><th>Batch</th><th class="hide-c2">Site</th><th class="hide-c">Zone / Bin</th>'
            f'<th class="num">Qty</th><th>Expiry</th><th>Status</th></tr></thead><tbody>{body}</tbody></table></div>')


def hero_mock():
    inner = ('<div class="app">' + side("Workspace", "Levant Pharma", [("grid", "Overview"), ("box", "Inventory"), ("inbox", "Receiving"),
                                                                     ("truck", "Dispatch"), ("list", "Counts"), ("chart", "Reports")], "Inventory")
             + '<div class="app-main">' + app_head("Inventory", "Stock by batch · Updated 14:32 AST", ("Search product or batch", "All sites", "Export"))
             + kpis([("Total SKUs", "4,812", "+38 this month"), ("Batches tracked", "18,346", "4 sites"),
                     ("Expiring in 30 days", "127", "Value JOD 41,920"), ("Stock accuracy", "99.8%", "Last cycle count", "c")])
             + inv_table() + "</div></div>")
    return frame("app.skaigroup.tech/inventory", inner)


def phone():
    return f"""<div class="phone" data-reveal><div class="notch"><i></i></div>
<div style="padding:6px 16px 18px;font-size:13px">
  <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px"><b style="font-size:15px">Receive · PO-4471</b>{chip('info','Scanning')}</div>
  <div style="aspect-ratio:4/3;border-radius:14px;background:#0b0b0b;position:relative;overflow:hidden;display:grid;place-items:center">
    <div style="width:70%;height:46%;border:2px solid #fff;border-radius:10px;position:relative">
      <div style="position:absolute;left:8%;right:8%;top:50%;height:2px;background:#0047ff"></div>
    </div>
    <svg viewBox="0 0 120 30" style="position:absolute;bottom:14px;width:46%;opacity:.9"><g fill="#fff">{''.join(f'<rect x="{x}" y="0" width="{w}" height="30"/>' for x, w in [(0,3),(5,1),(8,2),(12,1),(15,4),(21,1),(24,2),(28,3),(33,1),(36,2),(40,1),(43,4),(49,1),(52,2),(56,3),(61,1),(64,2),(68,1),(71,4),(77,1),(80,2),(84,3),(89,1),(92,2),(96,1),(99,4),(105,1),(108,2),(112,3),(117,2)])}</g></svg>
  </div>
  <div style="border:1px solid #e3e5e8;border-radius:12px;padding:12px;margin-top:12px">
    <div style="display:flex;justify-content:space-between;gap:8px"><b>Amoxicillin 500mg</b>{chip('ok','Matched')}</div>
    <div class="mono" style="margin-top:6px">Batch AMX-2604-118</div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-top:10px">
      <div><div class="muted" style="font-size:11.5px">Expiry</div><b>18 Aug 2027</b></div>
      <div><div class="muted" style="font-size:11.5px">Put-away</div><b>A-02-14</b></div>
    </div>
  </div>
  <div class="btn" style="width:100%;min-height:44px;margin-top:12px;font-size:14px">Confirm 480 units</div>
</div></div>"""


def queue():
    bars = [18, 26, 34, 42, 38, 52, 61, 47, 30, 22]
    mx = 64
    svg = "".join(f'<rect class="grow" style="--i:{i}" x="{8 + i*31}" y="{100 - v/mx*90:.1f}" width="20" height="{v/mx*90:.1f}" rx="3" fill="{"#0047ff" if i == 6 else "#000"}" opacity="{1 if i <= 6 else .18}"/>'
                  for i, v in enumerate(bars))
    rows = [("IN-2291", "Hikma Pharmaceuticals", "Inbound", "24 lines", "09:40", ("ok", "Received")),
            ("OUT-8843", "Irbid Specialty Hospital", "Outbound", "12 lines", "10:15", ("info", "Picking")),
            ("IN-2294", "Gulf BioPharma Trading", "Inbound", "8 lines · cold", "11:00", ("warn", "At dock")),
            ("OUT-8851", "Hayat Pharmacy Group", "Outbound", "31 lines", "11:30", ("info", "Packed"))]
    tr = "".join(f'<tr><td class="main mono" style="color:#000">{a}<small style="font-family:var(--body)">{b}</small></td>'
                 f'<td class="meta" data-l="Type">{c}</td><td class="meta" data-l="Lines">{d}</td><td class="meta" data-l="Slot">{e}</td>'
                 f'<td class="end">{chip(k, t)}</td></tr>' for a, b, c, d, e, (k, t) in rows)
    inner = (f'<div class="app"><div class="app-main">{app_head("Receiving and dispatch", "Today · Amman WH-1", ("Inbound", "Outbound"))}'
             f'<div class="panel" style="margin-bottom:12px" data-draw><div class="ph">Lines handled per hour <span>07:00 to now</span></div>'
             f'<svg class="chart" viewBox="0 0 320 112" role="img" aria-label="Hourly throughput">{svg}'
             f'<g font-size="9"><text x="8" y="111">07</text><text x="101" y="111">10</text><text x="194" y="111">13</text><text x="287" y="111">16</text></g></svg></div>'
             f'<div class="panel"><table class="rtable"><thead><tr><th>Reference</th><th>Type</th><th>Lines</th><th>Slot</th><th>Status</th></tr></thead><tbody>{tr}</tbody></table></div>'
             f'</div></div>')
    return frame("app.skaigroup.tech/receiving", inner)


def build():
    steps = [("Connect", "We map your warehouses, bins and current stock in days, not months."),
             ("Label", "Every batch gets a barcode linked to its expiry and supplier."),
             ("Track", "Each receipt, move and dispatch is scanned and recorded live."),
             ("Report", "Stock, expiry and accuracy reports are ready whenever you need them.")]
    st = "".join(f'<div class="step" data-reveal style="--d:{i*90}ms"><div class="n">0{i+1}</div><h3 class="h3">{t}</h3><p>{d}</p></div>'
                 for i, (t, d) in enumerate(steps))
    return (head("Warehouse & Inventory Control Platform · SKAI Group",
                 "Real-time control of pharmaceutical stock by batch, expiry and bin, across every warehouse you run.", "/inventory/")
            + header(NAV, "/inventory/")
            + f"""<section class="hero" id="top"><div class="shell hero-grid two">
  <div class="hero-copy">{eyebrow(None, 'Warehouse &amp; Inventory Control Platform')}
    <h1 class="display split">Every item, every location, <span class="accent">every batch.</span></h1>
    <p class="lead fade-in" style="--fd:550ms">Real-time control of pharmaceutical stock by batch, expiry and bin, across every warehouse you run.</p>
    <div class="fade-in" style="--fd:700ms">{cta()}</div><p class="hero-note fade-in" style="--fd:850ms">Built for pharma warehouses and distributors in Jordan and the Gulf.</p></div>
  <div class="perspective fade-in" style="--fd:400ms"><div class="tilt">{hero_mock()}</div></div></div></section>
{band(['Batch and expiry tracking', 'FEFO picking', 'Barcode on any phone', 'Supplier-to-pharmacy traceability', 'Multi-site stock', 'Arabic and English', 'Audit-ready records', 'Cycle counts in hours'])}
<section class="section" id="capabilities"><div class="shell">
  {sec_head('01', 'Capabilities', 'Control that starts at the shelf.', 'Three things every pharmaceutical warehouse needs, in one system.')}
  {features([("box", "Stock by batch and expiry", "See every batch, where it sits and when it expires. Picking follows FEFO automatically."),
             ("scan", "Barcode receiving, picking and dispatch", "Scan on any phone. No paper lists, no double entry, no guesswork at the dock."),
             ("route", "Traceability from supplier to customer", "Follow any batch back to its supplier and forward to every pharmacy that received it.")])}
</div></section>
<section class="section slate" id="scanning"><div class="shell duo">
  <div data-reveal>{eyebrow('02', 'Mobile scanning')}<h2 class="h2" style="margin:16px 0">The phone in your pocket is the scanner.</h2>
    <p class="lead">Receive a pallet, confirm the batch and expiry, and put it away in seconds.</p>
    {checks(["Batch and expiry captured on every scan", "Put-away location suggested instantly", "Works in Arabic and English"])}</div>
  <div>{phone()}</div></div></section>
<section class="section" id="operations"><div class="shell duo flip">
  <div data-reveal>{eyebrow('03', 'Receiving and dispatch')}<h2 class="h2" style="margin:16px 0">Every truck in, every order out, on one screen.</h2>
    <p class="lead">Your team sees what arrives, what ships and what is late, hour by hour.</p>
    {checks(["Inbound and outbound in one queue", "Cold-chain lines flagged at the dock", "Live throughput for every shift"])}</div>
  <div data-reveal>{queue()}</div></div></section>
<section class="section slate" id="how"><div class="shell">
  {sec_head('04', 'How it works', 'Live in four steps.')}
  <div class="steps-wrap"><svg class="steps-line" viewBox="0 0 1000 2" preserveAspectRatio="none" aria-hidden="true"><line class="flow" x1="0" y1="1" x2="1000" y2="1" stroke="#000" stroke-width="2"/></svg><div class="steps">{st}</div></div></div></section>
"""
            + dark('05', 'What changes in your warehouse.', 'Designed for the numbers that matter to pharmaceutical operators.',
                   [('<span data-count="3">3</span> days <em>→</em> <span data-count="2">2</span> h', 'Full stock count'),
                    ('<span data-count="99.8">99.8</span>%', 'Inventory accuracy'),
                    ('−<span data-count="80">80</span>%', 'Expired write-offs')])
            + footer())
