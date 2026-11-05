(function () {
  var root = document.documentElement;
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var hasIO = "IntersectionObserver" in window;

  /* Header: condensed state + reading progress */
  var header = document.querySelector(".site-header");
  var progress = document.querySelector(".progress");
  var ticking = false;
  function onScroll() {
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(function () {
      var y = window.scrollY || 0;
      if (header) header.classList.toggle("scrolled", y > 12);
      if (progress) {
        var max = document.documentElement.scrollHeight - window.innerHeight;
        progress.style.transform = "scaleX(" + (max > 0 ? Math.min(1, y / max) : 0) + ")";
      }
      ticking = false;
    });
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  window.addEventListener("resize", onScroll);
  onScroll();

  /* Active nav link */
  var links = Array.prototype.slice.call(document.querySelectorAll(".nav a[href^='#']"));
  if (hasIO && links.length) {
    var map = {};
    links.forEach(function (a) { map[a.getAttribute("href").slice(1)] = a; });
    var navIO = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        links.forEach(function (a) { a.classList.remove("active"); });
        var a = map[e.target.id];
        if (a) a.classList.add("active");
      });
    }, { rootMargin: "-45% 0px -50% 0px" });
    Object.keys(map).forEach(function (id) { var el = document.getElementById(id); if (el) navIO.observe(el); });
  }

  /* Mobile menu */
  var menu = document.getElementById("menu");
  var openBtn = document.querySelector(".menu-btn");
  var closeBtn = menu && menu.querySelector(".close");
  function setMenu(open) {
    if (!menu) return;
    menu.classList.toggle("open", open);
    menu.setAttribute("aria-hidden", open ? "false" : "true");
    if (open) { menu.removeAttribute("inert"); } else { menu.setAttribute("inert", ""); }
    openBtn && openBtn.setAttribute("aria-expanded", open ? "true" : "false");
    document.body.style.overflow = open ? "hidden" : "";
    if (open && closeBtn) closeBtn.focus();
  }
  openBtn && openBtn.addEventListener("click", function () { setMenu(true); });
  closeBtn && closeBtn.addEventListener("click", function () { setMenu(false); openBtn && openBtn.focus(); });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape" && menu && menu.classList.contains("open")) setMenu(false); });
  menu && menu.querySelectorAll("a[href^='#']").forEach(function (a) {
    a.addEventListener("click", function (e) {
      e.preventDefault();
      var id = a.getAttribute("href");
      setMenu(false);
      requestAnimationFrame(function () {
        var t = document.querySelector(id);
        if (t) t.scrollIntoView({ behavior: reduce ? "auto" : "smooth", block: "start" });
        history.replaceState(null, "", id);
      });
    });
  });

  /* Sticky phone CTA: visible after the hero, hidden over the closing section */
  var bar = document.querySelector(".cta-bar");
  var hero = document.querySelector(".hero");
  var closing = document.querySelector(".dark");
  if (bar && hero && hasIO) {
    var pastHero = false, atClose = false;
    var upd = function () { bar.classList.toggle("show", pastHero && !atClose); };
    new IntersectionObserver(function (es) {
      var e = es[0]; pastHero = !e.isIntersecting && e.boundingClientRect.top < 0; upd();
    }).observe(hero);
    if (closing) new IntersectionObserver(function (es) { atClose = es[0].isIntersecting; upd(); }, { rootMargin: "0px 0px -30% 0px" }).observe(closing);
  }

  if (reduce || !hasIO) {
    document.querySelectorAll("[data-type]").forEach(function (el) { el.querySelector(".typing") && el.querySelector(".typing").remove(); });
    return;
  }
  root.classList.add("js");

  /* Reveal on scroll (also triggers chart draw-ins inside) */
  var revealIO = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) { e.target.classList.add("in"); revealIO.unobserve(e.target); }
    });
  }, { rootMargin: "0px 0px -8% 0px", threshold: 0.01 });
  document.querySelectorAll("[data-reveal], [data-draw]").forEach(function (el) { revealIO.observe(el); });

  /* Count-up numbers */
  var NUM = /\d[\d,]*(?:\.\d+)?/g;
  function fmt(v, p) {
    return v.replace(NUM, function (m) {
      var target = parseFloat(m.replace(/,/g, ""));
      var dec = (m.split(".")[1] || "").length;
      var n = target * p;
      return m.indexOf(",") > -1 ? n.toLocaleString("en-US", { minimumFractionDigits: dec, maximumFractionDigits: dec }) : n.toFixed(dec);
    });
  }
  var countIO = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (!e.isIntersecting) return;
      countIO.unobserve(e.target);
      var el = e.target, final = el.getAttribute("data-count"), live = el.querySelector(".live"), t0 = performance.now();
      (function tick(t) {
        var p = Math.min(1, (t - t0) / 1400), eased = 1 - Math.pow(1 - p, 3);
        live.textContent = p === 1 ? final : fmt(final, eased);
        if (p < 1) requestAnimationFrame(tick);
      })(t0);
    });
  }, { threshold: 0.6 });
  document.querySelectorAll("[data-count]").forEach(function (el) {
    var final = el.getAttribute("data-count");
    el.innerHTML = '<span class="sr-only">' + final + '</span><span aria-hidden="true" style="display:inline-grid"><span style="grid-area:1/1;visibility:hidden">' + final + '</span><span class="live" style="grid-area:1/1">' + fmt(final, 0) + '</span></span>';
    countIO.observe(el);
  });

  /* AI assistant: short typing indicator before the answer, first time it is seen */
  document.querySelectorAll("[data-type]").forEach(function (box) {
    var typing = box.querySelector(".typing"), answer = box.querySelector(".answer");
    if (!typing || !answer) return;
    answer.style.display = "none";
    var io = new IntersectionObserver(function (es) {
      if (!es[0].isIntersecting) return;
      io.disconnect();
      setTimeout(function () { typing.remove(); answer.style.display = ""; answer.setAttribute("data-reveal", ""); requestAnimationFrame(function () { answer.classList.add("in"); }); }, 1300);
    }, { threshold: 0.5 });
    io.observe(box);
  });
})();
