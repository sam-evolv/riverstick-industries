/* Riverstick Industries · site behaviour. Vanilla, no dependencies. */
(function () {
  var doc = document.documentElement;
  doc.classList.add('js');
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* Header: solid on scroll, floating call button on mobile */
  var header = document.querySelector('.header');
  var fab = document.querySelector('.fab');
  function onScroll() {
    var y = window.scrollY || 0;
    if (header) header.classList.toggle('is-solid', y > 8);
    if (fab) fab.classList.toggle('is-visible', y > window.innerHeight * 0.6);
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* Mobile menu */
  var menuBtn = document.querySelector('.menu-btn');
  function setMenu(open) {
    doc.classList.toggle('menu-open', open);
    if (menuBtn) {
      menuBtn.setAttribute('aria-expanded', String(open));
      menuBtn.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    }
    document.body.style.overflow = open ? 'hidden' : '';
  }
  if (menuBtn) {
    menuBtn.addEventListener('click', function () { setMenu(!doc.classList.contains('menu-open')); });
    document.querySelectorAll('.mobile-menu a').forEach(function (a) { a.addEventListener('click', function () { setMenu(false); }); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') setMenu(false); });
    window.addEventListener('resize', function () { if (window.innerWidth > 900) setMenu(false); });
  }

  /* Hero carousel: slow crossfade, dots to pick a slide */
  var hero = document.querySelector('.hero[data-carousel]');
  if (hero) {
    var slides = hero.querySelectorAll('.hero-slide');
    var dots = hero.querySelectorAll('.dots button');
    var DUR = 6000, idx = 0, timer = null;
    function go(n) {
      idx = (n + slides.length) % slides.length;
      slides.forEach(function (s, i) { s.classList.toggle('is-active', i === idx); s.setAttribute('aria-hidden', i === idx ? 'false' : 'true'); });
      dots.forEach(function (d, i) { d.classList.toggle('is-active', i === idx); d.setAttribute('aria-current', i === idx ? 'true' : 'false'); });
      clearTimeout(timer);
      if (!reduce) timer = setTimeout(function () { go(idx + 1); }, DUR);
    }
    dots.forEach(function (d, i) { d.addEventListener('click', function () { go(i); }); });
    document.addEventListener('visibilitychange', function () { if (document.hidden) clearTimeout(timer); else go(idx); });
    go(0);
  }

  /* Scroll reveal */
  var els = document.querySelectorAll('[data-reveal]');
  if (!reduce && 'IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); } });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    els.forEach(function (el) { io.observe(el); });
  } else {
    els.forEach(function (el) { el.classList.add('is-in'); });
  }

  /* Live opening status (Mon to Fri, 09:00 to 17:30, Irish time) */
  var status = document.querySelectorAll('[data-open-status]');
  if (status.length) {
    try {
      var parts = new Intl.DateTimeFormat('en-GB', { timeZone: 'Europe/Dublin', weekday: 'short', hour: '2-digit', minute: '2-digit', hour12: false }).formatToParts(new Date());
      var get = function (t) { return (parts.find(function (p) { return p.type === t; }) || {}).value; };
      var day = get('weekday'), mins = parseInt(get('hour'), 10) * 60 + parseInt(get('minute'), 10);
      var open = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'].indexOf(day) > -1 && mins >= 540 && mins < 1050;
      status.forEach(function (s) { s.textContent = open ? 'Open now' : 'Closed now'; s.classList.toggle('open', open); s.hidden = false; });
    } catch (e) { /* leave hidden */ }
  }

  /* Footer year */
  document.querySelectorAll('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();
