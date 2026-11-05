from common import *
from charts import bars

NAV = [("#capabilities", "Capabilities"), ("#orders", "Orders"), ("#access", "Access"), ("#results", "Results")]


def hero_mock():
    sales = [262, 281, 300, 276, 305, 318, 312, 327, 341, 330, 356, 413]
    months = ["Dec", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov"]
    cust = [("Hayat Pharmacy Group", "Amman", "48,210", 100), ("Irbid Specialty Hospital", "Irbid", "41,880", 87),
            ("Al Shifa Pharmacies", "Riyadh", "36,540", 76), ("Gulf Care Hospital", "Dubai", "29,970", 62), ("Rawda Pharmacy", "Amman", "21,315", 44)]
    cl = "".join(f'<li><div class="top"><span><span class="muted" style="margin-right:8px">{i+1}</span><b style="font-weight:500">{n}</b> <span class="muted hide-sm">{c}</span></span>'
                 f'<span class="tabular" style="font-weight:600">{v}</span></div><div style="height:4px;background:#eef0f2;border-radius:4px;overflow:hidden">'
                 f'<div class="grow-x" style="width:{p}%;height:100%;background:{"#0047ff" if i == 0 else "#000"};opacity:{1 if i == 0 else .75}"></div></div></li>'
                 for i, (n, c, v, p) in enumerate(cust))
    inv = [("INV-2026-1184", "Irbid Specialty Hospital", "Insulin Glargine 100IU", "18 Nov 2026", "12,480.00", ("warn", "Pending")),
           ("INV-2026-1183", "Hayat Pharmacy Group", "Amoxicillin 500mg", "15 Nov 2026", "7,420.50", ("ok", "Paid")),
           ("INV-2026-1179", "Al Shifa Pharmacies", "Omeprazole 20mg", "31 Oct 2026", "9,860.00", ("crit", "Overdue"))]
    tr = "".join(f'<tr><td class="main mono" style="color:#000">{a}<small style="font-family:var(--body)">{b}</small></td><td class="meta hide-c" data-l="Item">{c}</td>'
                 f'<td class="meta nw" data-l="Due">{d}</td><td class="meta num" data-l="JOD">{e}</td><td class="end">{chip(k, t)}</td></tr>' for a, b, c, d, e, (k, t) in inv)
    inner = ('<div class="app">' + side("Company", "Al Noor Medical", [("grid", "Overview"), ("cart", "Sales"), ("truck", "Purchasing"), ("box", "Inventory"),
                                                                        ("wallet", "Finance"), ("users", "People"), ("chart", "Reports"), ("shield", "Roles & access")], "Overview")
             + '<div class="app-main">' + app_head("Business overview", "All sites · Updated 2 min ago", ("Search orders, batches, people", "November 2026"))
             + '<div class="kpis"><div class="kpi"><div class="k">Revenue this month</div><div class="v c tabular">JOD 412,860</div><div class="d up">+12.4% vs October</div></div>'
             '<div class="kpi"><div class="k">Open purchase orders</div><div class="v tabular">38</div><div class="d">JOD 186,420 committed</div></div>'
             f'<div class="kpi"><div class="k">Receivables</div><div class="v tabular">JOD 254,300</div><div style="margin-top:4px">{chip("warn", "14 overdue", True)}</div></div>'
             '<div class="kpi"><div class="k">Team members</div><div class="v tabular">126</div><div class="d">Across 4 sites</div></div></div>'
             + f'<div class="grid-2" style="margin-bottom:12px"><div class="panel" data-draw><div class="ph">Monthly sales <span>JOD thousands</span></div>'
             f'<div style="padding:8px 6px 2px">{bars(sales, [m[:1] if i % 2 else m for i, m in enumerate(months)], hl=11)}</div></div>'
             f'<div class="panel" data-draw><div class="ph">Top customers <span>JOD, Nov</span></div><ul class="alerts">{cl}</ul></div></div>'
             f'<div class="panel"><div class="ph">Recent invoices <span style="color:var(--cobalt)">View all</span></div><table class="rtable"><thead><tr><th>Invoice</th>'
             f'<th class="hide-c">Main item</th><th>Due</th><th class="num">Amount (JOD)</th><th>Status</th></tr></thead><tbody>{tr}</tbody></table></div>'
             + "</div></div>")
    return frame("app.skaigroup.tech/overview", inner)


def orders_mock():
    rows = [("SO-31842", "Hayat Pharmacy Group", "Sales", "18 lines", "7,420.50", ("ok", "Delivered")),
            ("PO-12207", "Hikma Pharmaceuticals", "Purchase", "42 lines", "64,900.00", ("info", "Approved")),
            ("SO-31845", "Irbid Specialty Hospital", "Sales", "9 lines · cold", "12,480.00", ("warn", "Picking")),
            ("PO-12211", "Gulf BioPharma Trading", "Purchase", "6 lines", "18,350.00", ("warn", "Awaiting")),
            ("SO-31851", "Al Shifa Pharmacies", "Sales", "27 lines", "9,860.00", ("ok", "Invoiced"))]
    tr = "".join(f'<tr><td class="main mono" style="color:#000">{a}<small style="font-family:var(--body)">{b}</small></td><td class="meta" data-l="Type">{c}</td>'
                 f'<td class="meta" data-l="Lines">{d}</td><td class="meta num" data-l="JOD">{e}</td><td class="end">{chip(k, t)}</td></tr>' for a, b, c, d, e, (k, t) in rows)
    inner = (f'<div class="app"><div class="app-main">{app_head("Sales and purchasing", "This week · All branches", ("Sales", "Purchasing", "New order"))}'
             + kpis([("Orders this week", "214", "+9% vs last week", "up"), ("Average order", "JOD 3,180", "Sales"), ("Awaiting supplier", "6", "Purchase orders"), ("On-time delivery", "97.2%", "Last 30 days", "c")])
             + f'<div class="panel"><table class="rtable lim"><thead><tr><th>Order</th><th>Type</th><th>Lines</th><th class="num">Amount (JOD)</th><th>Status</th></tr></thead><tbody>{tr}</tbody></table></div></div></div>')
    return frame("app.skaigroup.tech/orders", inner)


def roles_mock():
    roles = [("Warehouse Manager", "6 members"), ("Accountant", "4 members"), ("Sales Rep", "22 members"), ("Pharmacist", "9 members")]
    rl = "".join(f'<li style="{"background:var(--cobalt-soft);" if i == 0 else ""}"><div class="top"><b style="font-weight:{600 if i == 0 else 500};color:{"var(--cobalt)" if i == 0 else "#000"}">{r}</b>'
                 f'<span class="muted" style="font-size:12px">{m}</span></div></li>' for i, (r, m) in enumerate(roles))
    mods = [("Inventory", [1, 1, 1, 0]), ("Receiving", [1, 1, 1, 0]), ("Sales orders", [1, 0, 0, 0]), ("Purchasing", [1, 1, 0, 0]), ("Finance", [0, 0, 0, 0]), ("Reports", [1, 0, 0, 1])]
    acts = ["View", "Create", "Edit", "Export"]

    def tog(on):
        bg = "#0047ff" if on else "#d7dbe0"
        return (f'<span style="display:inline-block;width:30px;height:18px;border-radius:9px;background:{bg};position:relative;vertical-align:middle">'
                f'<span style="position:absolute;top:2px;{"right" if on else "left"}:2px;width:14px;height:14px;border-radius:50%;background:#fff"></span></span>')
    th = "".join(f'<th style="text-align:center">{a}</th>' for a in acts)
    rows = "".join(f'<tr><td style="font-weight:500">{m}</td>' + "".join(f'<td style="text-align:center">{tog(v)}</td>' for v in vals) + "</tr>" for m, vals in mods)
    inner = (f'<div class="app"><div class="app-main">{app_head("Roles and permissions", "Warehouse Manager · 6 members", ("Audit log",))}'
             f'<div class="grid-2" style="grid-template-columns:minmax(0,1fr)"><div class="panel"><div class="ph">Roles <span>4 of 9</span></div><ul class="alerts" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr))">{rl}</ul></div>'
             f'<div class="panel" style="overflow-x:auto"><table class="perm" style="width:100%;border-collapse:collapse;font-size:13px"><thead><tr><th style="text-align:left">Module</th>{th}</tr></thead><tbody>{rows}</tbody></table></div></div>'
             f'<p class="muted" style="font-size:12px;margin-top:10px">Last change by Rana H. · 2 Nov 2026 · logged</p></div></div>')
    return frame("app.skaigroup.tech/roles", inner)


def build():
    return (head("Business Management Platform · SKAI Group",
                 "One system for sales, purchasing, finance and people, built for pharmaceutical distributors in Jordan and the Gulf.", "/business/")
            + header(NAV, "/business/")
            + f"""<section class="hero" id="top"><div class="shell">
  <div class="hero-top"><div class="hero-copy" style="max-width:none">{eyebrow(None, 'Business Management Platform')}
    <h1 class="display split">One system for sales, purchasing, finance <span class="accent">and people.</span></h1></div>
    <div class="hero-copy"><p class="lead fade-in" style="--fd:550ms">Built for pharmaceutical warehouses and medical distributors across Jordan and the Gulf.</p>{cta()}</div></div>
  <div class="perspective fade-in" style="--fd:500ms"><div class="tilt">{hero_mock()}</div></div></div></section>
{band(['Sales and invoicing', 'Purchasing and approvals', 'Finance and receivables', 'People and roles', 'Batch-linked orders', 'Role-based access', 'Audit trail', 'Connects to your tools'])}
<section class="section" id="capabilities"><div class="shell">
  {sec_head('01', 'Capabilities', 'Every department, one version of the truth.')}
  {features([("layers", "Sales, purchasing, finance and people", "One platform from the first quote to the last invoice, and everyone who works on it."),
             ("shield", "Role-based access for every team", "Each person sees exactly what their role needs, down to the field."),
             ("plug", "Connects to your existing tools", "Accounting, e-invoicing, banks and suppliers stay in sync, no re-typing.")])}
</div></section>
<section class="section slate" id="orders"><div class="shell duo">
  <div data-reveal>{eyebrow('02', 'Sales and purchasing')}<h2 class="h2" style="margin:16px 0">From quote to cash, without the spreadsheets.</h2>
    <p class="lead">Every order, its stock, its invoice and its payment, connected.</p>
    {checks(["Orders linked to batch and expiry", "Purchase approvals in one click", "Invoices generated from delivered orders"])}</div>
  <div data-reveal>{orders_mock()}</div></div></section>
<section class="section" id="access"><div class="shell duo flip">
  <div data-reveal>{eyebrow('03', 'Roles and access')}<h2 class="h2" style="margin:16px 0">The right access for every role.</h2>
    <p class="lead">Permissions are clear, auditable and easy to change as your team grows.</p>
    {checks(["Ready-made roles for pharma teams", "Every change logged with who and when", "Access per branch, module and action"])}</div>
  <div data-reveal>{roles_mock()}</div></div></section>
"""
            + dark('04', 'Run the business, not the paperwork.', 'Designed to give managers time back and auditors a clean trail.',
                   [('−<span data-count="65">65</span>%', 'Admin hours'), ('1', 'Version of the truth'), ('<span data-count="100">100</span>%', 'Audit trail')])
            + footer())
