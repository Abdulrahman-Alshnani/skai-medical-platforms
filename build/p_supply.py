from common import *
from charts import forecast_chart

NAV = [("#capabilities", "Capabilities"), ("#cold-chain", "Cold chain"), ("#routes", "Routes"), ("#results", "Results")]

ACT = [4300, 4450, 4380, 4700, 4900, 4820, 5100, 5250, 5180, 5400, 5600]
FC = [5600, 5850, 6050, 6300, 6420, 6600]
BAND = [0, 180, 300, 420, 520, 620]
WEEKS = [f"W{n}" for n in range(27, 43)]

ALERTS = [("crit", "Stock-out", "2 min", "Insulin Glargine 100IU", "Stock-out predicted in 9 days at Riyadh DC. Reorder 1,200 units.", "Create PO", True),
          ("warn", "Expiry", "18 min", "Amoxicillin 500mg · AMX-24117", "3,400 units expire 16 Dec at Amman WH-2. Transfer to Irbid.", "Transfer", False),
          ("info", "Demand", "1 h", "Omeprazole 20mg", "Demand up 22% in Dubai. Raise safety stock to 2,800 units.", "Apply", False),
          ("ok", "Resolved", "3 h", "Paracetamol 500mg", "Replenishment of 8,000 units confirmed for Irbid WH-1.", None, False)]


def alerts(n=4):
    li = ""
    for k, tag, t, title, body, act, live in ALERTS[:n]:
        a = f'<span class="act">{act}</span>' if act else ""
        li += f'<li><div class="top">{chip(k, tag, live)}<span class="muted" style="font-size:12px">{t}</span></div><div class="t">{title}</div><div class="m">{body}</div>{a}</li>'
    return f'<ul class="alerts">{li}</ul>'


def hero_mock():
    chart = forecast_chart(ACT, FC, BAND, WEEKS, 3800, 7000, [4000, 5000, 6000, 7000], stock=5900, stock_label="Available stock 5,900")
    inner = ('<div class="app">' + side("Workspace", "Supply Chain", [("grid", "Control Tower"), ("box", "Inventory"), ("list", "Expiry"), ("trend", "Forecasts"),
                                                                       ("thermo", "Cold Chain"), ("route", "Routes")], "Control Tower")
             + '<div class="app-main">' + app_head("Control Tower", "All sites · Last 30 days · Updated 2 min ago", ("Search SKU, batch, site", "All sites"))
             + kpis([("Stock-out risk", "3 SKUs", "High risk, next 14 days"), ("Batches expiring in 60 days", "47", "JOD 182,400 at risk"),
                     ("Temperature compliance", "99.9%", "18 assets, 2–8 °C", "c"), ("On-time deliveries", "96.4%", "1,284 of 1,332 orders", "up")])
             + f'<div class="grid-2"><div class="panel" data-draw><div class="ph">Demand forecast · Insulin Glargine <span>Next 6 weeks</span></div>'
             f'<div style="padding:8px 6px 4px">{chart}</div>'
             f'<div style="display:flex;gap:16px;padding:8px 12px;border-top:1px solid var(--line);font-size:12px" class="muted">'
             f'<span>Forecast accuracy <b style="color:#000">94.2%</b></span><span>Gap vs stock <b style="color:var(--crit)">−1,200 units</b></span></div></div>'
             f'<div class="panel"><div class="ph">AI alerts <span style="color:var(--cobalt)">4 new</span></div>{alerts(3)}</div></div>'
             + "</div></div>")
    return frame("app.skaigroup.tech/control-tower", inner)


def cold_mock():
    assets = [("Cold Room A · Amman", "4.6", "ok", "In range"), ("Cold Room B · Amman", "5.1", "ok", "In range"), ("Cold Room C2 · Riyadh", "3.8", "ok", "In range"),
              ("Truck JO-4471 · Irbid", "8.9", "crit", "Breach · 3 min"), ("Truck JO-2208 · Zarqa", "6.2", "ok", "In range"), ("Fridge F-12 · Dubai", "4.1", "ok", "In range"),
              ("Truck SA-1130 · Riyadh", "7.6", "warn", "Near limit"), ("Cold Room D · Irbid", "4.9", "ok", "In range")]
    g = ""
    for n, t, k, l in assets:
        bc = ' style="border-color:#f3b3b3"' if k == "crit" else ""
        col = ' style="color:var(--crit)"' if k == "crit" else ""
        tv = t if k == "crit" else f'<span class="tick" data-tick="{t}" data-dev="0.15">{t}</span>'
        g += f'<div class="kpi"{bc}><div class="k">{n}</div><div class="v tabular"{col}>{tv} °C</div><div style="margin-top:6px">{chip(k, l, k == "crit")}</div></div>'
    pts = [96, 92, 98, 90, 94, 88, 92, 86, 90, 84, 80, 70, 56, 38, 22, 30, 34]
    d = "M" + " L".join(f"{34 + i*(520/(len(pts)-1)):.1f},{p}" for i, p in enumerate(pts))
    chart = (f'<svg class="chart" viewBox="0 0 560 190" role="img" aria-label="Temperature over 24 hours">'
             f'<rect x="34" y="40" width="520" height="100" fill="#eef3ff"/>'
             f'<line x1="34" x2="554" y1="40" y2="40" stroke="#0047ff" stroke-dasharray="4 4"/><line x1="34" x2="554" y1="140" y2="140" stroke="#0047ff" stroke-dasharray="4 4"/>'
             f'<g font-size="10"><text x="4" y="44">8 °C</text><text x="4" y="144">2 °C</text><text x="34" y="182">00:00</text><text x="160" y="182">06:00</text>'
             f'<text x="290" y="182">12:00</text><text x="420" y="182">18:00</text><text x="526" y="182">Now</text></g>'
             f'<path class="draw" pathLength="1" d="{d}" fill="none" stroke="#000" stroke-width="2" stroke-linejoin="round"/>'
             f'<circle class="fade-late" cx="{34 + 14*(520/16):.1f}" cy="22" r="5" fill="#b42318"/></svg>')
    al = ('<ul class="alerts">'
          f'<li><div class="top">{chip("crit","Breach",True)}<span class="muted" style="font-size:12px">Now</span></div><div class="t">Truck JO-4471</div><div class="m">8.9 °C on the Irbid route. Caught in 3 min, driver and QA notified.</div></li>'
          f'<li><div class="top">{chip("warn","Warning")}<span class="muted" style="font-size:12px">12 min</span></div><div class="t">Truck SA-1130</div><div class="m">Trending up, 7.6 °C. Reroute to Riyadh DC suggested.</div></li>'
          f'<li><div class="top">{chip("ok","Resolved")}<span class="muted" style="font-size:12px">1 h</span></div><div class="t">Cold Room B</div><div class="m">Door open 4 min. Back in range at 5.1 °C.</div></li></ul>')
    inner = (f'<div class="app"><div class="app-main">{app_head("Cold chain monitoring", "18 assets · Safe range 2–8 °C · Live", ("Rooms", "Trucks"))}'
             f'<div class="kpis">{g}</div><div class="grid-2"><div class="panel" data-draw><div class="ph">Truck JO-4471 · last 24 hours <span>°C</span></div>'
             f'<div style="padding:8px 6px 4px">{chart}</div></div><div class="panel"><div class="ph">Alerts <span>Today</span></div>{al}</div></div></div></div>')
    return frame("app.skaigroup.tech/cold-chain", inner)


def routes_mock():
    city = {"Irbid": (120, 40), "Amman": (150, 170), "Zarqa": (230, 150), "Mafraq": (260, 60), "Madaba": (110, 230)}
    paths = [("M150,170 C140,120 130,80 120,40", "#0047ff"), ("M150,170 C190,170 210,160 230,150 C250,120 255,90 260,60", "#000"),
             ("M150,170 C135,195 120,215 110,230", "#8a9096")]
    p = "".join(f'<path class="draw" pathLength="1" d="{d}" fill="none" stroke="{c}" stroke-width="3" stroke-linecap="round"/>' for d, c in paths)
    c = "".join(f'<circle cx="{x}" cy="{y}" r="6" fill="#fff" stroke="#000" stroke-width="2"/><text x="{x+11}" y="{y+4}" font-size="12" style="fill:#000;font-weight:500">{n}</text>'
                for n, (x, y) in city.items())
    svg = f'<svg class="chart" viewBox="0 0 340 260" role="img" aria-label="Route map"><rect width="340" height="260" fill="#f8f9fa"/>{p}{c}</svg>'
    veh = [("JO-4471", "Amman → Irbid", 86, "#0047ff"), ("JO-2208", "Amman → Zarqa → Mafraq", 72, "#000"), ("JO-1902", "Amman → Madaba", 54, "#8a9096")]
    v = "".join(f'<li><div class="top"><span class="t mono" style="color:#000">{a}</span><span class="muted" style="font-size:12px">{l}% load</span></div>'
                f'<div class="m">{r}</div><div style="height:6px;background:#eef0f2;border-radius:6px;margin-top:8px;overflow:hidden">'
                f'<div class="grow-x" style="width:{l}%;height:100%;background:{col};border-radius:6px"></div></div></li>' for a, r, l, col in veh)
    inner = (f'<div class="app"><div class="app-main">{app_head("Delivery routes", "Tomorrow · 3 vehicles · 41 drops", ("Optimise",))}'
             f'<div class="grid-2" data-draw><div class="panel">{svg}</div><div class="panel"><div class="ph">Vehicles <span>Planned by AI</span></div><ul class="alerts">{v}</ul></div></div></div></div>')
    return frame("app.skaigroup.tech/routes", inner)


def build():
    return (head("Intelligent Warehouse & Supply Chain Platform · SKAI Group",
                 "One AI control tower that predicts expiry and stock-outs for pharmaceutical warehouses and distributors.", "/supply-chain/")
            + header(NAV, "/supply-chain/")
            + f"""<section class="hero" id="top"><div class="shell">
  <div class="hero-top"><div class="hero-copy" style="max-width:none">{eyebrow(None, 'Intelligent Warehouse &amp; Supply Chain Platform')}
    <h1 class="display split">Predict expiry and stock-outs <span class="accent">before they happen.</span></h1></div>
    <div class="hero-copy"><p class="lead fade-in" style="--fd:550ms">One AI control tower for pharmaceutical warehouses and medical distributors across Jordan and the Gulf.</p>{cta()}</div></div>
  <div class="perspective fade-in" style="--fd:500ms"><div class="tilt">{hero_mock()}</div></div></div></section>
{band(['Demand forecasting', 'Expiry prediction', 'Stock-out alerts', 'Cold chain 2–8 °C', 'Breach alerts in minutes', 'Route and load planning', 'Multi-site control tower', 'GDP-ready records'])}
<section class="section" id="capabilities"><div class="shell">
  {sec_head('01', 'Capabilities', 'From reacting to predicting.', 'The platform watches stock, expiry, temperature and routes, and tells you what to do next.')}
  {features([("trend", "Predicts demand, expiry and stock-outs", "Forecasts every SKU at every site and flags risk weeks before it becomes a loss."),
             ("thermo", "Monitors every shelf and shipment", "Cold rooms, fridges and trucks report their temperature around the clock."),
             ("route", "Plans routes and loads", "Deliveries are grouped and sequenced to cut distance and keep cold lines cold.")])}
</div></section>
<section class="section slate" id="cold-chain"><div class="shell">
  <div class="duo" style="margin-bottom:40px"><div data-reveal>{eyebrow('02', 'Temperature-protected supply chain')}
    <h2 class="h2" style="margin:16px 0">Every degree recorded, every breach caught in minutes.</h2></div>
    <div data-reveal>{checks(["24/7 monitoring of rooms, fridges and trucks", "Instant alerts to the driver and quality team", "Audit-ready temperature history for every batch"])}</div></div>
  <div data-reveal>{cold_mock()}</div></div></section>
<section class="section" id="routes"><div class="shell duo flip">
  <div data-reveal>{eyebrow('03', 'Routes and loads')}<h2 class="h2" style="margin:16px 0">Fewer kilometres, fuller trucks, colder cargo.</h2>
    <p class="lead">The platform plans tomorrow's deliveries tonight, with cold-chain lines first.</p>
    {checks(["Routes optimised across all drops", "Load balanced per vehicle", "Cold-chain stops sequenced first"])}</div>
  <div data-reveal>{routes_mock()}</div></div></section>
"""
            + dark('04', 'Less waste, fewer surprises.', 'Designed to protect stock, margins and patients.',
                   [('−<span data-count="80">80</span>%', 'Expired write-offs'), ('24/7', 'Temperature monitoring'), ('&lt;<span data-count="5">5</span> min', 'To catch a temperature breach')])
            + footer())
