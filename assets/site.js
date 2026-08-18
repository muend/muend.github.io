(function () {
  'use strict';
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var $  = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };

  /* ---------- 1. Reveal choreography ---------------------------------- */
  var revealIO = 'IntersectionObserver' in window
    ? new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          if (!e.isIntersecting) return;
          e.target.classList.add('is-in');
          revealIO.unobserve(e.target);
        });
      }, { rootMargin: '0px 0px -12% 0px', threshold: 0.06 })
    : null;

  if (revealIO) { $$('.rv, .principle, .method-track').forEach(function (n) { revealIO.observe(n); }); }
  else { $$('.rv, .principle, .method-track').forEach(function (n) { n.classList.add('is-in'); }); }

  /* Hero headline underline fires immediately */
  requestAnimationFrame(function () {
    var h1 = $('#hero-name'); if (h1) h1.classList.add('is-in');
  });

  /* ---------- 2. Diagram plates: measure, then draw ------------------- */
  function measurePlate(plate) {
    $$('.d-flow, .d-flow--a, .d-flow--m', plate).forEach(function (p) {
      if (typeof p.getTotalLength !== 'function') return;
      var len = 0;
      try { len = p.getTotalLength(); } catch (err) { len = 0; }
      if (len > 0) p.style.setProperty('--len', Math.ceil(len + 2));
    });
  }

  var plates = $$('[data-plate]');
  plates.forEach(measurePlate);

  var drawIO = 'IntersectionObserver' in window
    ? new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          if (!e.isIntersecting) return;
          e.target.classList.add('is-drawn');
          drawIO.unobserve(e.target);
        });
      }, { rootMargin: '0px 0px -10% 0px', threshold: 0.12 })
    : null;

  var drawable = plates.concat($$('[data-measure]'));
  if (drawIO) { drawable.forEach(function (n) { drawIO.observe(n); }); }
  else { drawable.forEach(function (n) { n.classList.add('is-drawn'); }); }

  /* Plate spotlight follows the pointer (fine pointers only) */
  if (window.matchMedia('(hover: hover) and (pointer: fine)').matches && !reduce) {
    plates.forEach(function (plate) {
      var raf = 0, x = 50, y = 45;
      plate.addEventListener('pointermove', function (ev) {
        var r = plate.getBoundingClientRect();
        x = ((ev.clientX - r.left) / r.width) * 100;
        y = ((ev.clientY - r.top) / r.height) * 100;
        if (raf) return;
        raf = requestAnimationFrame(function () {
          raf = 0;
          plate.style.setProperty('--px', x.toFixed(2) + '%');
          plate.style.setProperty('--py', y.toFixed(2) + '%');
        });
      });
    });
  }

  /* ---------- 3. Counters --------------------------------------------- */
  function runCount(el) {
    var target = parseFloat(el.getAttribute('data-count'));
    if (isNaN(target)) return;
    if (reduce) { el.textContent = String(target); return; }
    var dur = 1250, t0 = null;
    function step(ts) {
      if (t0 === null) t0 = ts;
      var p = Math.min((ts - t0) / dur, 1);
      var eased = 1 - Math.pow(1 - p, 4);
      el.textContent = String(Math.round(target * eased));
      if (p < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }

  var countIO = 'IntersectionObserver' in window
    ? new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          if (!e.isIntersecting) return;
          runCount(e.target);
          countIO.unobserve(e.target);
        });
      }, { threshold: 0.6 })
    : null;
  if (countIO) { $$('[data-count]').forEach(function (n) { countIO.observe(n); }); }

  /* ---------- 4. Scroll progress, sticky bar, nav state ---------------- */
  var progress = $('#progress');
  var topbar   = $('#topbar');
  var ticking  = false;

  function onScroll() {
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(function () {
      ticking = false;
      var h = document.documentElement.scrollHeight - window.innerHeight;
      var p = h > 0 ? window.scrollY / h : 0;
      if (progress) progress.style.transform = 'scaleX(' + p.toFixed(4) + ')';
      if (topbar) topbar.setAttribute('data-stuck', window.scrollY > 12 ? 'true' : 'false');
    });
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* Cross-page nav: the document declares which section it belongs to. */
  var navLinks = $$('.navlinks a');
  var here = document.documentElement.getAttribute('data-page') || '';
  navLinks.forEach(function (a) {
    a.setAttribute('aria-current', a.getAttribute('data-nav') === here ? 'true' : 'false');
  });

  /* On pages that anchor-scroll, let the visible section take over. */
  var sections = navLinks
    .map(function (a) {
      var h = a.getAttribute('href') || '';
      return h.charAt(0) === '#' ? document.getElementById(h.slice(1)) : null;
    })
    .filter(Boolean);

  if ('IntersectionObserver' in window && sections.length) {
    var navIO = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        navLinks.forEach(function (a) {
          a.setAttribute('aria-current', a.getAttribute('href') === '#' + e.target.id ? 'true' : 'false');
        });
      });
    }, { rootMargin: '-45% 0px -50% 0px' });
    sections.forEach(function (s) { navIO.observe(s); });
  }

  /* ---------- 5. Capability tabs (full keyboard support) --------------- */
  var tabs = $$('.cap-tab');
  function selectTab(tab, focus) {
    tabs.forEach(function (t) {
      var on = t === tab;
      t.setAttribute('aria-selected', on ? 'true' : 'false');
      t.tabIndex = on ? 0 : -1;
      var panel = document.getElementById(t.getAttribute('aria-controls'));
      if (panel) { if (on) panel.removeAttribute('hidden'); else panel.setAttribute('hidden', ''); }
    });
    if (focus) tab.focus();
  }
  tabs.forEach(function (tab, i) {
    tab.addEventListener('click', function () { selectTab(tab, false); });
    tab.addEventListener('keydown', function (ev) {
      var k = ev.key, next = null;
      if (k === 'ArrowDown' || k === 'ArrowRight') next = tabs[(i + 1) % tabs.length];
      else if (k === 'ArrowUp' || k === 'ArrowLeft') next = tabs[(i - 1 + tabs.length) % tabs.length];
      else if (k === 'Home') next = tabs[0];
      else if (k === 'End') next = tabs[tabs.length - 1];
      if (!next) return;
      ev.preventDefault();
      selectTab(next, true);
    });
  });

  /* ---------- 6. Diagram inspection dialog ----------------------------- */
  var dlg = $('#dlg'), dlgBody = $('#dlg-body'), dlgTitle = $('#dlg-title');
  var lastTrigger = null;

  $$('[data-expand]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var plate = btn.closest('[data-plate]');
      var svg = plate && plate.querySelector(':scope > svg');
      if (!svg || !dlg) return;
      lastTrigger = btn;
      dlgTitle.textContent = plate.getAttribute('data-title') || 'Technical diagram';
      dlgBody.innerHTML = '';
      var clone = svg.cloneNode(true);
      clone.removeAttribute('style');
      dlgBody.appendChild(clone);
      $$('.d-flow, .d-flow--a, .d-flow--m', clone).forEach(function (p) {
        p.style.strokeDasharray = 'none';
        p.style.strokeDashoffset = '0';
        p.style.opacity = '1';
      });
      $$('.d-pop', clone).forEach(function (g) { g.style.opacity = '1'; g.style.transform = 'none'; });
      if (typeof dlg.showModal === 'function') dlg.showModal();
      else dlg.setAttribute('open', '');
    });
  });

  if (dlg) {
    $$('[data-close]', dlg).forEach(function (b) {
      b.addEventListener('click', function () { dlg.close(); });
    });
    dlg.addEventListener('click', function (ev) {
      if (ev.target === dlg) dlg.close();
    });
    dlg.addEventListener('close', function () {
      dlgBody.innerHTML = '';
      if (lastTrigger) { lastTrigger.focus(); lastTrigger = null; }
    });
  }

  /* ---------- 7. Curatorial cursor ------------------------------------- */
  (function mountCursor() {
    if (reduce) return;
    if (!window.matchMedia('(hover: hover) and (pointer: fine)').matches) return;

    var dot = $('#cur-dot'), ring = $('#cur-ring'), cap = $('#cur-cap');
    if (!dot || !ring || !cap) return;

    var body = document.body;
    body.classList.add('cur-on');

    var mx = window.innerWidth / 2, my = window.innerHeight / 2;
    var rx = mx, ry = my;
    var running = false, idleTimer = 0;

    /* What the reticle says when it locks onto something. */
    var LABELS = [
      ['[data-expand]',            'inspect'],
      ['.cap-tab',                 'switch'],
      ['a[href^="mailto:"]',       'write'],
      ['.rrow',                    'open study'],
      ['.sheet-body h3 a',         'open repo'],
      ['.sheet-links a',           'open'],
      ['.btn',                     'go'],
      ['.navlinks a',              'jump'],
      ['.brand',                   'top'],
      ['.dlg-close',               'close'],
      ['[data-plate]',             'diagram'],
      ['a',                        'open']
    ];

    function labelFor(target) {
      for (var i = 0; i < LABELS.length; i++) {
        var el = target.closest(LABELS[i][0]);
        if (el) return { el: el, text: el.getAttribute('data-cursor') || LABELS[i][1] };
      }
      return null;
    }

    function frame() {
      rx += (mx - rx) * 0.18;
      ry += (my - ry) * 0.18;
      dot.style.transform  = 'translate3d(' + mx.toFixed(1) + 'px,' + my.toFixed(1) + 'px,0)';
      cap.style.transform  = 'translate3d(' + mx.toFixed(1) + 'px,' + my.toFixed(1) + 'px,0)';
      ring.style.transform = 'translate3d(' + rx.toFixed(1) + 'px,' + ry.toFixed(1) + 'px,0)';
      if (Math.abs(mx - rx) > 0.3 || Math.abs(my - ry) > 0.3) requestAnimationFrame(frame);
      else running = false;
    }
    function kick() { if (!running) { running = true; requestAnimationFrame(frame); } }

    window.addEventListener('pointermove', function (ev) {
      if (ev.pointerType !== 'mouse') return;
      mx = ev.clientX; my = ev.clientY;
      body.classList.remove('cur-idle');
      clearTimeout(idleTimer);
      idleTimer = setTimeout(function () { body.classList.add('cur-idle'); }, 4000);
      kick();

      var hit = ev.target && ev.target.closest ? labelFor(ev.target) : null;
      if (hit) {
        body.classList.add('cur-hot');
        if (cap.textContent !== hit.text) cap.textContent = hit.text;
      } else {
        body.classList.remove('cur-hot');
      }
    }, { passive: true });

    window.addEventListener('pointerdown', function () { body.classList.add('cur-down'); kick(); }, { passive: true });
    window.addEventListener('pointerup',   function () { body.classList.remove('cur-down'); }, { passive: true });
    document.addEventListener('mouseleave', function () { body.classList.add('cur-idle'); });
    document.addEventListener('mouseenter', function () { body.classList.remove('cur-idle'); });

    /* A real pointing device is required; a touch anywhere retires the reticle. */
    window.addEventListener('touchstart', function () {
      body.classList.remove('cur-on', 'cur-hot', 'cur-down');
    }, { passive: true, once: true });
  })();

  /* ---------- 8. Re-measure diagrams after fonts settle ---------------- */
  if (document.fonts && document.fonts.ready) {
    document.fonts.ready.then(function () {
      plates.forEach(function (p) { if (!p.classList.contains('is-drawn')) measurePlate(p); });
    });
  }
})();
