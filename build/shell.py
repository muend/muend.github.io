"""Shared page shell: head, topbar, footer, and the small reusable snippets.

Every page in the site is emitted through these helpers so the chrome can never
drift between files. `depth` is 0 for pages at the repo root and 1 for anything
under projects/.
"""

SITE = "https://muend.github.io"
EMAIL = "nsduraan@gmail.com"

ARROW = ('<svg viewBox="0 0 16 16" aria-hidden="true">'
         '<path d="M3 13 13 3M6 3h7v7" fill="none" stroke="currentColor" stroke-width="1.7"/></svg>')
EXPAND_ICON = ('<svg viewBox="0 0 16 16" aria-hidden="true">'
               '<path d="M2 6V2h4M14 10v4h-4M2 2l5 5M14 14l-5-5" fill="none" '
               'stroke="currentColor" stroke-width="1.7"/></svg>')

NAV = [
    ("projects", "Projects", "index.html#projects"),
    ("research", "Research", "research.html"),
    ("practice", "Practice", "practice.html"),
    ("contact",  "Contact",  "index.html#contact"),
]


def rel(depth):
    return "../" * depth


def head(title, description, page, depth=0, canonical=""):
    r = rel(depth)
    canon = f"{SITE}/{canonical}" if canonical else f"{SITE}/"
    return f"""<!DOCTYPE html>
<html lang="en" data-page="{page}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<script>document.documentElement.classList.add('js');</script>
<link rel="icon" type="image/svg+xml" href="{r}assets/brand/favicon.svg">
<link rel="icon" sizes="any" href="{r}assets/brand/favicon.ico">
<link rel="icon" type="image/png" sizes="32x32" href="{r}assets/brand/favicon-32.png">
<link rel="apple-touch-icon" href="{r}assets/brand/favicon-180.png">
<link rel="manifest" href="{r}assets/brand/site.webmanifest">
<link rel="canonical" href="{canon}">
<title>{title}</title>
<meta name="description" content="{description}">
<meta name="theme-color" content="#F7F7F1">
<meta name="color-scheme" content="light">
<meta name="referrer" content="strict-origin-when-cross-origin">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta name="author" content="Muhammed Enes Duran">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="website">
<meta property="og:url" content="{canon}">
<meta property="og:site_name" content="Muhammed Enes Duran">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{description}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wdth,wght@12..96,75..100,400..800&family=IBM+Plex+Mono:wght@400;500;600&family=Instrument+Sans:ital,wght@0,400..700;1,400..600&display=swap">
<link rel="stylesheet" href="{r}assets/site.css">
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
<div class="progress" id="progress" aria-hidden="true"></div>
<div class="cur cur-ring" id="cur-ring" aria-hidden="true"></div>
<div class="cur cur-dot" id="cur-dot" aria-hidden="true"></div>
<div class="cur cur-cap" id="cur-cap" aria-hidden="true"></div>
{topbar(depth)}
"""


def topbar(depth):
    r = rel(depth)
    links = "\n        ".join(
        f'<a href="{r}{href}" data-nav="{key}">{label}</a>' for key, label, href in NAV
    )
    return f"""<div class="topbar" id="topbar">
  <div class="wrap">
    <a class="brand" href="{r}index.html" aria-label="Muhammed Enes Duran — home">muend<b>.</b></a>
    <div class="nav-area">
      <nav class="navlinks mono" aria-label="Primary">
        {links}
      </nav>
      <span class="status-pill mono"><i aria-hidden="true"></i><span>Open source · active</span></span>
    </div>
  </div>
</div>
"""


def footer(depth=0, contact=False):
    r = rel(depth)
    block = ""
    if contact:
        block = f"""
<section class="contact" id="contact" aria-labelledby="contact-title">
  <div class="wrap">
    <div class="contact-grid">
      <div>
        <span class="kicker mono rv">Open to collaboration</span>
        <h2 id="contact-title" class="rv" style="--d:60ms">Build spatial systems that hold up.</h2>
        <p class="rv" style="--d:120ms">
          Available for collaboration around GeoAI agent systems, production-grade spatial data science,
          remote-sensing ML pipelines, GIS automation, decision-support products, and applied simulations.
        </p>
        <div class="cta rv" style="--d:180ms">
          <a class="btn btn--solid" href="mailto:{EMAIL}"><span>{EMAIL}</span></a>
          <a class="btn btn--ghost" href="https://github.com/muend" target="_blank" rel="noopener"><span class="dot" aria-hidden="true"></span><span>github.com/muend</span></a>
          <a class="btn btn--accent" href="https://pypi.org/user/muend/" target="_blank" rel="noopener"><span>PyPI profile</span></a>
        </div>
        <p class="contact-note rv" style="--d:240ms">Based in Türkiye · Open-source, research, and production collaboration welcome.</p>
      </div>
      <aside class="avail rv" style="--d:200ms" aria-label="Engagement types">
        <div class="avail-head mono"><strong>Engagement</strong><span>2026 / open</span></div>
        <ul>
          <li><i aria-hidden="true"></i>Agent skill systems and evaluation harnesses</li>
          <li><i aria-hidden="true"></i>Guarded GIS automation and MCP infrastructure</li>
          <li><i aria-hidden="true"></i>Reproducible remote-sensing pipelines</li>
          <li><i aria-hidden="true"></i>Spatial decision-support products</li>
          <li><i aria-hidden="true"></i>Research software and citable releases</li>
        </ul>
        <div class="avail-foot">Written briefs preferred. Every engagement starts with explicit invariants, data contracts, and success criteria.</div>
      </aside>
    </div>
    <div class="colophon mono">
      <span>© 2026 Muhammed Enes Duran</span>
      <span>Set in Bricolage Grotesque, Instrument Sans &amp; IBM Plex Mono</span>
      <span>Static site · no trackers</span>
    </div>
  </div>
</section>
"""
    else:
        block = f"""
<section class="contact">
  <div class="wrap">
    <div class="contact-grid">
      <div>
        <span class="kicker mono rv">Open to collaboration</span>
        <h2 class="rv" style="--d:60ms">Build spatial systems that hold up.</h2>
        <div class="cta rv" style="--d:140ms">
          <a class="btn btn--solid" href="mailto:{EMAIL}"><span>{EMAIL}</span></a>
          <a class="btn btn--ghost" href="{r}index.html#projects"><span class="dot" aria-hidden="true"></span><span>All projects</span></a>
        </div>
      </div>
    </div>
    <div class="colophon mono">
      <span>© 2026 Muhammed Enes Duran</span>
      <span>Static site · no trackers</span>
    </div>
  </div>
</section>
"""
    return f"""{block}
</main>

<dialog class="dlg" id="dlg" aria-labelledby="dlg-title">
  <div class="dlg-head">
    <strong id="dlg-title">Technical diagram</strong>
    <button class="dlg-close" type="button" data-close>Close</button>
  </div>
  <div class="dlg-body" id="dlg-body"></div>
</dialog>

<script src="{r}assets/site.js" defer></script>
</body>
</html>
"""


# ---------------------------------------------------------------- snippets

def link(href, label, external=True):
    ext = ' target="_blank" rel="noopener"' if external else ""
    return (f'<a href="{href}"{ext}><span class="u">{label}</span>{ARROW}</a>')


def btn(href, label, kind="ghost", external=True, icon=True):
    ext = ' target="_blank" rel="noopener"' if external else ""
    ic = ARROW if icon else ""
    return f'<a class="btn btn--{kind}" href="{href}"{ext}><span>{label}</span>{ic}</a>'


def plate(fig_no, title, svg, note=""):
    """A diagram plate with its own expand control."""
    note_html = f'\n  <p class="fig-note">{note}</p>' if note else ""
    return f"""<div class="plate rv" data-plate data-title="{fig_no} — {title}">
  <div class="plate-bar"><strong>{fig_no} / {title}</strong>
    <button class="expand" type="button" data-expand>Expand{EXPAND_ICON}</button>
  </div>
{svg}
</div>{note_html}"""


def figure(n, heading, intro, svg_plate):
    intro_html = f"  <p>{intro}</p>\n" if intro else ""
    return f"""<section class="fig">
  <div class="fig-head">
    <span class="n">{n}</span>
    <h3>{heading}</h3>
    <span class="rule" aria-hidden="true"></span>
  </div>
{intro_html}{svg_plate}
</section>"""


def spec(rows):
    body = "\n".join(
        f'  <div><span class="k">{k}</span><span class="v">{v}</span></div>' for k, v in rows
    )
    return f'<div class="spec">\n{body}\n</div>'


def note(label, text, warn=False):
    cls = "note note--warn" if warn else "note"
    return f'<div class="{cls}"><span class="mono">{label}</span><p>{text}</p></div>'


def prose(label, heading, body):
    h = f"<h3>{heading}</h3>\n    " if heading else ""
    return f"""<section class="prose rv">
  <span class="mono">{label}</span>
  <div>
    {h}{body}
  </div>
</section>"""
