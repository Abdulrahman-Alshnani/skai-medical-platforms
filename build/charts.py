"""SVG chart helpers (draw-in animations are CSS-driven)."""


def line_path(vals, x0, x1, y0, y1, lo, hi, start=0, total=None):
    total = total or len(vals)
    pts = []
    for i, v in enumerate(vals):
        x = x0 + (start + i) / (total - 1) * (x1 - x0)
        y = y1 - (v - lo) / (hi - lo) * (y1 - y0)
        pts.append((x, y))
    return pts, "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts)


def forecast_chart(actual, forecast, band, labels, lo, hi, ticks, unit="k", w=520, h=210, stock=None, stock_label=""):
    x0, x1, y0, y1 = 36, w - 10, 12, h - 24
    total = len(actual) + len(forecast) - 1
    _, a_d = line_path(actual, x0, x1, y0, y1, lo, hi, 0, total)
    fs = len(actual) - 1
    fpts, f_d = line_path(forecast, x0, x1, y0, y1, lo, hi, fs, total)
    up, _ = line_path([f + b for f, b in zip(forecast, band)], x0, x1, y0, y1, lo, hi, fs, total)
    dn, _ = line_path([f - b for f, b in zip(forecast, band)], x0, x1, y0, y1, lo, hi, fs, total)
    band_d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in up + dn[::-1]) + " Z"
    tx = x0 + fs / (total - 1) * (x1 - x0)
    g = ""
    for t in ticks:
        y = y1 - (t - lo) / (hi - lo) * (y1 - y0)
        g += f'<line x1="{x0}" x2="{x1}" y1="{y:.1f}" y2="{y:.1f}" stroke="#eef0f2"/><text x="{x0-6}" y="{y+3:.1f}" text-anchor="end" font-size="10">{t/1000:g}{unit}</text>'
    step = max(1, len(labels) // 6)
    for i, l in enumerate(labels):
        if i % step: continue
        x = x0 + i / (len(labels) - 1) * (x1 - x0)
        g += f'<text x="{x:.1f}" y="{h-6}" text-anchor="middle" font-size="10">{l}</text>'
    s = ""
    if stock is not None:
        sy = y1 - (stock - lo) / (hi - lo) * (y1 - y0)
        s = (f'<g class="fade-late"><line x1="{tx:.1f}" x2="{x1}" y1="{sy:.1f}" y2="{sy:.1f}" stroke="#b42318" stroke-dasharray="3 3"/>'
             f'<text x="{x1-2}" y="{sy-5:.1f}" text-anchor="end" font-size="10" style="fill:#b42318">{stock_label}</text></g>')
    return (f'<svg class="chart" viewBox="0 0 {w} {h}" role="img" aria-label="Forecast chart">{g}'
            f'<line x1="{tx:.1f}" x2="{tx:.1f}" y1="{y0}" y2="{y1}" stroke="#cfd3d8" stroke-dasharray="2 3"/>'
            f'<text x="{tx+5:.1f}" y="{y0+9}" font-size="10">Today</text>'
            f'<path class="fade-late" d="{band_d}" fill="#eef3ff"/>'
            f'<path class="draw" pathLength="1" d="{a_d}" fill="none" stroke="#000" stroke-width="2" stroke-linejoin="round"/>'
            f'<path class="fade-late" d="{f_d}" fill="none" stroke="#0047ff" stroke-width="2" stroke-dasharray="6 4"/>'
            f'{s}<circle class="fade-late" cx="{fpts[-1][0]:.1f}" cy="{fpts[-1][1]:.1f}" r="3.5" fill="#0047ff"/></svg>')


def bars(vals, labels, w=520, h=190, hl=None, lo_op=0.12):
    x0, x1, y0, y1 = 30, w - 6, 10, h - 22
    import math
    mx = math.ceil(max(vals) * 1.05 / 50) * 50
    n = len(vals)
    bw = (x1 - x0) / n * 0.62
    out = ""
    for t in [0, 0.5, 1]:
        y = y1 - t * (y1 - y0)
        out += f'<line x1="{x0}" x2="{x1}" y1="{y:.1f}" y2="{y:.1f}" stroke="#eef0f2"/><text x="{x0-6}" y="{y+3:.1f}" text-anchor="end" font-size="10">{round(mx*t):g}</text>'
    for i, v in enumerate(vals):
        cx = x0 + (i + 0.5) * (x1 - x0) / n
        bh = v / mx * (y1 - y0)
        col = "#0047ff" if i == hl else "#d7dbe0"
        out += f'<rect class="grow" style="--i:{i}" x="{cx-bw/2:.1f}" y="{y1-bh:.1f}" width="{bw:.1f}" height="{bh:.1f}" rx="3" fill="{col}"/>'
        out += f'<text x="{cx:.1f}" y="{h-6}" text-anchor="middle" font-size="10">{labels[i]}</text>'
    return f'<svg class="chart" viewBox="0 0 {w} {h}" role="img" aria-label="Bar chart">{out}</svg>'
