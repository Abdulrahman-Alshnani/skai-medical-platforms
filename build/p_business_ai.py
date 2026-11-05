from common import *
from charts import forecast_chart

NAV = [("#capabilities", "Capabilities"), ("#assistant", "Assistant"), ("#approvals", "Approvals"), ("#results", "Results")]


def assistant(v2=False):
    if v2:
        return assistant2()
    ar_rows = [("أموكسيسيلين 500 ملغ", "12,480", "+18%"), ("باراسيتامول 500 ملغ", "10,920", "+6%"), ("إنسولين غلارجين 100 وحدة", "3,240", "+11%")]
    tr = "".join(f'<tr><td style="padding:6px 0">{a}</td><td class="tabular" style="padding:6px 8px"><bdi dir="ltr">{b}</bdi></td><td class="tabular" style="padding:6px 0;color:var(--cobalt)"><bdi dir="ltr">{c}</bdi></td></tr>' for a, b, c in ar_rows)
    sup = [("Gulf BioPharma Trading", "avg 3.2 days", ("crit", "4 late")), ("Levant Medical Supply", "avg 1.5 days", ("warn", "2 late")), ("Nour Distribution", "avg 0.8 days", ("warn", "1 late"))]
    sl = "".join(f'<div style="display:flex;justify-content:space-between;gap:8px;align-items:center;padding:5px 0"><span>{a}</span><span style="display:flex;gap:8px;align-items:center"><span class="muted hide-sm" style="font-size:12px">{b}</span>{chip(k, t)}</span></div>' for a, b, (k, t) in sup)
    q = 'style="align-self:flex-end;max-width:88%;background:#000;color:#fff;border-radius:12px 12px 2px 12px;padding:9px 12px"'
    a = 'style="max-width:94%;border:1px solid var(--line);border-radius:12px 12px 12px 2px;padding:10px 12px"'
    return f"""<div class="panel" style="display:flex;flex-direction:column"><div class="ph"><span style="display:flex;align-items:center;gap:8px;color:#000;font-weight:600;font-size:13px">
<span style="width:24px;height:24px;border-radius:6px;background:var(--cobalt);display:grid;place-items:center;color:#fff">{ic('spark')}</span>AI Assistant</span><span>AR · EN</span></div>
<div style="display:flex;flex-direction:column;gap:10px;padding:12px;font-size:13px" data-type>
  <div dir="rtl" lang="ar" {q}>ما هي أكثر الأدوية مبيعاً هذا الشهر في عمّان؟</div>
  <div class="typing" aria-hidden="true"><i></i><i></i><i></i></div>
  <div class="answer" dir="rtl" lang="ar" {a}><div style="margin-bottom:6px">أكثر ثلاثة أدوية مبيعاً في عمّان خلال نوفمبر:</div>
    <table style="width:100%;border-collapse:collapse;font-size:12.5px"><tbody>{tr}</tbody></table></div>
  <div {q}>Which suppliers delayed deliveries this quarter?</div>
  <div {a}><div style="margin-bottom:4px">3 suppliers missed delivery dates in Q4:</div>{sl}</div>
</div>
<div style="margin:0 12px 12px;border:1px solid var(--line);border-radius:8px;padding:9px 12px;color:var(--grey-2);font-size:12.5px">Ask in Arabic or English</div></div>"""


def assistant2():
    q = 'style="align-self:flex-end;max-width:88%;background:#000;color:#fff;border-radius:12px 12px 2px 12px;padding:9px 12px"'
    a = 'style="max-width:94%;border:1px solid var(--line);border-radius:12px 12px 12px 2px;padding:10px 12px"'
    rows = [("سيفترياكسون 1 غ", "CFX-2510-019", "12 يوماً"), ("أوميبرازول 20 ملغ", "OMP-2603-077", "38 يوماً"), ("إنسولين غلارجين", "IGL-2611-04", "54 يوماً")]
    tr = "".join(f'<tr><td style="padding:6px 0">{x}</td><td class="mono" style="padding:6px 8px"><bdi dir="ltr">{y}</bdi></td><td style="padding:6px 0;color:var(--warn)">{z}</td></tr>' for x, y, z in rows)
    return f"""<div class="panel" style="display:flex;flex-direction:column;background:#fff"><div class="ph"><span style="display:flex;align-items:center;gap:8px;color:#000;font-weight:600;font-size:13px">
<span style="width:24px;height:24px;border-radius:6px;background:var(--cobalt);display:grid;place-items:center;color:#fff">{ic('spark')}</span>AI Assistant</span><span>AR · EN</span></div>
<div style="display:flex;flex-direction:column;gap:10px;padding:12px;font-size:13px" data-type>
  <div dir="rtl" lang="ar" {q}>ما هي الدفعات التي تنتهي صلاحيتها خلال 60 يوماً في إربد؟</div>
  <div class="typing" aria-hidden="true"><i></i><i></i><i></i></div>
  <div class="answer" dir="rtl" lang="ar" {a}><div style="margin-bottom:6px">3 دفعات بقيمة 41,920 دينار. أقترح نقل أول دفعتين إلى عمّان:</div>
    <table style="width:100%;border-collapse:collapse;font-size:12.5px"><tbody>{tr}</tbody></table></div>
  <div {q}>What will cash flow look like in December?</div>
  <div {a}>Net cash flow is forecast at <b>JOD 768K</b> (+8%), with 92% confidence. Two large receivables from Irbid hospitals drive most of the change.</div>
</div>
<div style="margin:0 12px 12px;border:1px solid var(--line);border-radius:8px;padding:9px 12px;color:var(--grey-2);font-size:12.5px">Ask in Arabic or English</div></div>"""


def hero_mock():
    act = [1.82, 1.9, 2.05, 2.0, 2.22, 2.35, 2.31, 2.48, 2.56, 2.74]
    fc = [2.74, 2.88, 3.03]
    chart = forecast_chart([v * 1000 for v in act], [v * 1000 for v in fc], [0, 90, 160], ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
                           1500, 3200, [2000, 2500, 3000], unit="M", h=200)
    chart = chart.replace(">2M<", ">2.0M<").replace(">3M<", ">3.0M<")
    inner = ('<div class="app">' + side("Company", "Al-Noor Pharma", [("grid", "Overview"), ("trend", "Forecasts"), ("cart", "Purchasing"), ("box", "Inventory"),
                                                                       ("thermo", "Cold chain"), ("check2", "Approvals"), ("file", "Reports")], "Overview")
             + '<div class="app-main">' + app_head("Executive overview", "All branches · Amman, Irbid, Riyadh, Dubai · Updated 08:40", ("Search",))
             + kpis([("Revenue, Oct", "JOD 2.74M", "+5.0% MoM", "up"), ("Q4 sales forecast", "JOD 8.65M", "92% confidence", "c"),
                     ("Net cash flow, Oct", "JOD 712K", "+7.6% MoM", "up"), ("Batches expiring < 90 days", "14", "JOD 96K at risk")])
             + f'<div class="grid-2"><div class="panel" data-draw><div class="ph">Sales forecast, 2026 <span>JOD · AI forecast</span></div><div style="padding:8px 6px 4px">{chart}</div></div>'
             f'{assistant()}</div>' + "</div></div>")
    return frame("app.skaigroup.tech/executive", inner)


def approvals_mock():
    reqs = [("PR-7712", "Insulin Glargine 100IU · 1,200 pens", "JOD 18,600", ("ok", "Approve"), "Forecast shows stock-out in 9 days"),
            ("PR-7715", "Amoxicillin 500mg · 20,000 caps", "JOD 6,400", ("warn", "Review"), "Current stock covers 11 weeks"),
            ("PR-7718", "Cold boxes · 40 units", "JOD 2,150", ("ok", "Approve"), "Within budget, preferred supplier"),
            ("PR-7720", "Omeprazole 20mg · 9,000 caps", "JOD 3,980", ("ok", "Approve"), "Demand up 22% in Dubai")]
    li = "".join(f'<li><div class="top"><span><span class="mono" style="color:#000;margin-right:8px">{a}</span><b style="font-weight:500">{c}</b></span>{chip(k, t)}</div>'
                 f'<div class="t" style="font-weight:500">{b}</div><div class="m">{ic("spark", "")} {r}</div></li>' for a, b, c, (k, t), r in reqs)
    li = li.replace('<svg class=""', '<svg style="display:inline;width:13px;height:13px;vertical-align:-2px;color:var(--cobalt)"')
    inner = (f'<div class="app"><div class="app-main">{app_head("Approvals", "6 waiting · auto-routed by amount and risk", ("Approve all suggested",))}'
             f'<div class="panel"><ul class="alerts">{li}</ul></div></div></div>')
    return frame("app.skaigroup.tech/approvals", inner)


def report_mock():
    items = [("Sales", "JOD 642K", "+6.1%"), ("Gross margin", "31.4%", "+0.8 pts"), ("Stock value", "JOD 2.1M", "−2.3%"), ("Expiry risk", "JOD 96K", "−18%")]
    g = "".join(f'<div class="kpi"><div class="k">{a}</div><div class="v tabular">{b}</div><div class="d up">{c}</div></div>' for a, b, c in items)
    inner = (f'<div class="app"><div class="app-main">{app_head("Weekly report · Week 45", "Generated automatically · Sunday 07:00", ("Send to board",))}'
             f'<div class="kpis">{g}</div><div class="panel" style="padding:14px;font-size:13px"><b style="display:block;margin-bottom:6px">Summary</b>'
             f'<p class="muted">Sales grew 6.1%, led by Amman pharmacies. Expiry risk fell to JOD 96K after transfers to Irbid. Two suppliers remain late; purchasing has been notified.</p></div></div></div>')
    return frame("app.skaigroup.tech/reports", inner)


def build():
    return (head("Intelligent Business Management Platform · SKAI Group",
                 "AI that forecasts sales, purchasing and cash flow for pharma distributors, and answers your team in Arabic and English.", "/business-ai/")
            + header(NAV, "/business-ai/")
            + f"""<section class="hero" id="top"><div class="shell">
  <div class="hero-top"><div class="hero-copy" style="max-width:none">{eyebrow(None, 'Intelligent Business Management Platform')}
    <h1 class="display split">Forecasts and answers, <span class="accent">in Arabic and English.</span></h1></div>
    <div class="hero-copy"><p class="lead fade-in" style="--fd:550ms">AI that forecasts sales, purchasing and cash flow for pharma distributors, and answers your team in their language.</p>{cta()}</div></div>
  <div class="perspective fade-in" style="--fd:500ms"><div class="tilt">{hero_mock()}</div></div></div></section>
{band(['Sales forecasting', 'Cash-flow forecasting', 'Arabic and English assistant', 'Automated approvals', 'Weekly board reports', 'Answers from your own data', 'Permission-aware AI', 'Purchasing recommendations'])}
<section class="section" id="capabilities"><div class="shell">
  {sec_head('01', 'Capabilities', 'Decisions with the numbers already done.')}
  {features([("trend", "Forecasts sales, purchasing and cash flow", "See next quarter before it happens, with the confidence behind every number."),
             ("bot", "An assistant in Arabic and English", "Ask about stock, sales or suppliers in plain language and get the answer with the data."),
             ("check2", "Automated reports and approvals", "Reports write themselves and routine approvals route to the right person.")])}
</div></section>
<section class="section slate" id="assistant"><div class="shell duo">
  <div data-reveal>{eyebrow('02', 'AI assistant')}<h2 class="h2" style="margin:16px 0">Ask your business a question. In Arabic.</h2>
    <p class="lead">Your team gets answers from your own data, in the language they think in.</p>
    {checks(["Answers grounded in your ERP data", "Arabic and English in the same chat", "Respects every user's permissions"])}</div>
  <div data-reveal>{assistant(True)}</div></div></section>
<section class="section" id="approvals"><div class="shell duo flip">
  <div data-reveal>{eyebrow('03', 'Approvals and reports')}<h2 class="h2" style="margin:16px 0">Routine decisions, handled. Exceptions, flagged.</h2>
    <p class="lead">Every purchase request comes with a recommendation and the reason behind it.</p>
    {checks(["AI recommendation on every request", "Weekly board report written automatically", "Full audit trail of every decision"])}</div>
  <div data-reveal style="display:grid;gap:16px">{approvals_mock()}{report_mock()}</div></div></section>
"""
            + dark('04', 'More decisions, less admin.', 'Designed to give leaders the answer before the meeting starts.',
                   [('−<span data-count="65">65</span>%', 'Admin hours'), ('2', 'Languages, one assistant'), ('24/7', 'Answers, every day')])
            + footer())
