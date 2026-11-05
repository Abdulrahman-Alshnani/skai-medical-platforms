(function () {
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var fine = window.matchMedia("(hover: hover) and (pointer: fine)").matches;

  /* Headline: split into words for the load-in reveal */
  document.querySelectorAll(".split").forEach(function (el) {
    var i = 0;
    (function walk(node) {
      Array.prototype.slice.call(node.childNodes).forEach(function (n) {
        if (n.nodeType === 3) {
          var frag = document.createDocumentFragment();
          n.textContent.split(/(\s+)/).forEach(function (part) {
            if (!part) return;
            if (/^\s+$/.test(part)) { frag.appendChild(document.createTextNode(part)); return; }
            var w = document.createElement("span"); w.className = "w";
            var s = document.createElement("span"); s.textContent = part; s.style.setProperty("--wi", i++);
            w.appendChild(s); frag.appendChild(w);
          });
          n.parentNode.replaceChild(frag, n);
        } else if (n.nodeType === 1) {
          if (n.classList.contains("accent")) {
            var w = document.createElement("span"); w.className = "w";
            n.parentNode.insertBefore(w, n); w.appendChild(n); n.style.setProperty("--wi", i++);
          } else walk(n);
        }
      });
    })(el);
  });

  /* Platform switcher */
  document.querySelectorAll(".switch").forEach(function (sw) {
    var b = sw.querySelector("button");
    b.addEventListener("click", function (e) { e.stopPropagation(); var o = !sw.classList.contains("open"); sw.classList.toggle("open", o); b.setAttribute("aria-expanded", o); });
    document.addEventListener("click", function () { sw.classList.remove("open"); b.setAttribute("aria-expanded", "false"); });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape") sw.classList.remove("open"); });
  });

  /* Back to top */
  var top = document.querySelector(".to-top");
  if (top) {
    window.addEventListener("scroll", function () { top.classList.toggle("show", window.scrollY > window.innerHeight * 1.5); }, { passive: true });
    top.addEventListener("click", function () { window.scrollTo({ top: 0, behavior: reduce ? "auto" : "smooth" }); });
  }

  /* Live values in mockups (gentle jitter, as if streaming) */
  if (!reduce) {
    var ticks = Array.prototype.slice.call(document.querySelectorAll("[data-tick]"));
    if (ticks.length) setInterval(function () {
      var el = ticks[Math.floor(Math.random() * ticks.length)];
      var base = parseFloat(el.getAttribute("data-tick")), d = parseFloat(el.getAttribute("data-dev") || "0.2");
      var v = base + (Math.random() * 2 - 1) * d; var dec = (el.getAttribute("data-tick").split(".")[1] || "").length;
      el.textContent = v.toFixed(dec); el.classList.add("flash"); setTimeout(function () { el.classList.remove("flash"); }, 600);
    }, 1800);
  }

  if (reduce || !fine) return;

  /* Hero: cursor-revealed dot grid + soft glow */
  document.querySelectorAll(".hero").forEach(function (h) {
    var glow = document.createElement("div"); glow.className = "glow"; h.prepend(glow);
    h.addEventListener("mousemove", function (e) {
      var r = h.getBoundingClientRect(), x = e.clientX - r.left, y = e.clientY - r.top;
      h.style.setProperty("--mx", x + "px"); h.style.setProperty("--my", y + "px");
      h.style.setProperty("--gx", x + "px"); h.style.setProperty("--gy", y + "px");
    });
  });

  /* 3D tilt of the hero product */
  document.querySelectorAll(".tilt").forEach(function (t) {
    var host = t.closest(".hero") || t;
    host.addEventListener("mousemove", function (e) {
      var r = t.getBoundingClientRect();
      var px = (e.clientX - (r.left + r.width / 2)) / (window.innerWidth / 2), py = (e.clientY - (r.top + r.height / 2)) / (window.innerHeight / 2);
      t.style.transform = "rotateY(" + (px * 4).toFixed(2) + "deg) rotateX(" + (-py * 3).toFixed(2) + "deg)";
    });
    host.addEventListener("mouseleave", function () { t.style.transform = ""; });
  });

  /* Card spotlight */
  document.querySelectorAll(".card").forEach(function (c) {
    c.addEventListener("mousemove", function (e) {
      var r = c.getBoundingClientRect();
      c.style.setProperty("--cx", (e.clientX - r.left) + "px"); c.style.setProperty("--cy", (e.clientY - r.top) + "px");
    });
  });

  /* Magnetic primary buttons */
  document.querySelectorAll(".btn:not(.sm)").forEach(function (b) {
    if (b.closest(".menu") || b.closest(".cta-bar")) return;
    b.classList.add("magnet");
    b.addEventListener("mousemove", function (e) {
      var r = b.getBoundingClientRect(), x = e.clientX - (r.left + r.width / 2), y = e.clientY - (r.top + r.height / 2);
      b.style.transform = "translate(" + (x * 0.12).toFixed(1) + "px," + (y * 0.25).toFixed(1) + "px)";
    });
    b.addEventListener("mouseleave", function () { b.style.transform = ""; });
  });

  /* Custom cursor: precise dot + trailing ring that grows over interactive things */
  var dot = document.createElement("div"), ring = document.createElement("div");
  dot.className = "cursor-dot"; ring.className = "cursor-ring";
  document.body.append(dot, ring);
  var mx = -100, my = -100, rx = -100, ry = -100;
  window.addEventListener("mousemove", function (e) {
    mx = e.clientX; my = e.clientY; document.body.classList.add("cursor-on");
    dot.style.transform = "translate(" + mx + "px," + my + "px)";
    var hot = e.target.closest && e.target.closest("a, button, .card, [data-hot]");
    ring.classList.toggle("hot", !!hot);
    document.body.classList.toggle("dark-hover", !!(e.target.closest && e.target.closest(".dark, .band:not(.light)")));
  }, { passive: true });
  document.addEventListener("mouseleave", function () { document.body.classList.remove("cursor-on"); });
  (function loop() {
    rx += (mx - rx) * 0.18; ry += (my - ry) * 0.18;
    ring.style.transform = "translate(" + rx.toFixed(1) + "px," + ry.toFixed(1) + "px)";
    requestAnimationFrame(loop);
  })();
})();
