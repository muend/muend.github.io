"""Shared page shell: head, topbar, footer and the reusable snippets.

Every page is emitted through these helpers so the chrome cannot drift between
files or between languages.

English lives at the site root, Turkish under /tr/ with the same tree. A page is
identified by its site-relative path ("projects/benchfck.html"), which is all we
need to compute both the asset prefix and the link to its counterpart.
"""

SITE = "https://muend.github.io"
EMAIL = "nsduraan@gmail.com"
LANGS = ("en", "tr")

ARROW = ('<svg viewBox="0 0 16 16" aria-hidden="true">'
         '<path d="M3 13 13 3M6 3h7v7" fill="none" stroke="currentColor" stroke-width="1.7"/></svg>')
EXPAND_ICON = ('<svg viewBox="0 0 16 16" aria-hidden="true">'
               '<path d="M2 6V2h4M14 10v4h-4M2 2l5 5M14 14l-5-5" fill="none" '
               'stroke="currentColor" stroke-width="1.7"/></svg>')

# Active language, set by the builder before each page is emitted.
LANG = "en"


def T(en, tr):
    """Pick the string for the language currently being emitted."""
    return tr if LANG == "tr" else en


UI = {
    "nav": {
        "projects": ("Projects", "Projeler"),
        "research": ("Research", "Araştırma"),
        "practice": ("Practice", "Yöntem"),
        "contact":  ("Contact",  "İletişim"),
    },
    "skip":      ("Skip to content", "İçeriğe geç"),
    "status":    ("Open source · active", "Açık kaynak · aktif"),
    "expand":    ("Expand", "Büyüt"),
    "close":     ("Close", "Kapat"),
    "dlg_title": ("Technical diagram", "Teknik diyagram"),
    "home_aria": ("Muhammed Enes Duran — home", "Muhammed Enes Duran — ana sayfa"),
    "nav_aria":  ("Primary", "Ana"),
    "crumb_aria":("Breadcrumb", "Sayfa yolu"),
    "lang_aria": ("Change language", "Dili değiştir"),
    "more_aria": ("More projects", "Diğer projeler"),
    "home":      ("Home", "Ana sayfa"),
    "prev":      ("previous", "önceki"),
    "next":      ("next", "sonraki"),
}


def u(key):
    en, tr = UI[key]
    return T(en, tr)


NAV_ORDER = [
    ("projects", "index.html#projects"),
    ("research", "research.html"),
    ("practice", "practice.html"),
    ("contact",  "index.html#contact"),
]


def _depth(page_path, lang):
    """How many directory levels below the site root this file sits."""
    return page_path.count("/") + (1 if lang == "tr" else 0)


def rel(page_path, lang):
    return "../" * _depth(page_path, lang)


def _lang_root(lang):
    return "tr/" if lang == "tr" else ""


def head(title, description, page, page_path):
    lang = LANG
    r = rel(page_path, lang)
    here = f"{SITE}/{_lang_root(lang)}{page_path}".replace("/index.html", "/")
    alt_en = f"{SITE}/{page_path}".replace("/index.html", "/")
    alt_tr = f"{SITE}/tr/{page_path}".replace("/index.html", "/")
    return f"""<!DOCTYPE html>
<html lang="{lang}" data-page="{page}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<script>document.documentElement.classList.add('js');</script>
<link rel="icon" type="image/svg+xml" href="{r}assets/brand/favicon.svg">
<link rel="icon" sizes="any" href="{r}assets/brand/favicon.ico">
<link rel="icon" type="image/png" sizes="32x32" href="{r}assets/brand/favicon-32.png">
<link rel="apple-touch-icon" href="{r}assets/brand/favicon-180.png">
<link rel="manifest" href="{r}assets/brand/site.webmanifest">
<link rel="canonical" href="{here}">
<link rel="alternate" hreflang="en" href="{alt_en}">
<link rel="alternate" hreflang="tr" href="{alt_tr}">
<link rel="alternate" hreflang="x-default" href="{alt_en}">
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
<meta property="og:url" content="{here}">
<meta property="og:site_name" content="Muhammed Enes Duran">
<meta property="og:locale" content="{'tr_TR' if lang == 'tr' else 'en_US'}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{description}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wdth,wght@12..96,75..100,400..800&family=IBM+Plex+Mono:wght@400;500;600&family=Instrument+Sans:ital,wght@0,400..700;1,400..600&display=swap">
<link rel="stylesheet" href="{r}assets/site.css">
</head>
<body>
<a class="skip-link" href="#main">{u('skip')}</a>
<div class="progress" id="progress" aria-hidden="true"></div>
<div class="cur cur-ring" id="cur-ring" aria-hidden="true"></div>
<div class="cur cur-dot" id="cur-dot" aria-hidden="true"></div>
<div class="cur cur-cap" id="cur-cap" aria-hidden="true"></div>
{topbar(page_path)}
"""


def lang_switch(page_path):
    """Link to the same page in the other language."""
    lang = LANG
    r = rel(page_path, lang)
    other = "tr" if lang == "en" else "en"
    href = r + ("tr/" if lang == "en" else "") + page_path
    labels = {"en": "EN", "tr": "TR"}
    items = []
    for code in LANGS:
        if code == lang:
            items.append(f'<span class="lang-opt is-on" aria-current="true">{labels[code]}</span>')
        else:
            items.append(f'<a class="lang-opt" href="{href}" hreflang="{other}" '
                         f'lang="{other}">{labels[code]}</a>')
    return (f'<div class="langsw mono" role="group" aria-label="{u("lang_aria")}">'
            + '<span aria-hidden="true">/</span>'.join(items) + '</div>')


def topbar(page_path):
    r = rel(page_path, LANG)
    links = "\n        ".join(
        f'<a href="{r}{_lang_root(LANG)}{href}" data-nav="{key}">{T(*UI["nav"][key])}</a>'
        for key, href in NAV_ORDER
    )
    return f"""<div class="topbar" id="topbar">
  <div class="wrap">
    <a class="brand" href="{r}{_lang_root(LANG)}index.html" aria-label="{u('home_aria')}">muend<b>.</b></a>
    <div class="nav-area">
      <nav class="navlinks mono" aria-label="{u('nav_aria')}">
        {links}
      </nav>
      {lang_switch(page_path)}
      <span class="status-pill mono"><i aria-hidden="true"></i><span>{u('status')}</span></span>
    </div>
  </div>
</div>
"""


CONTACT_COPY = {
    "kicker":  ("Open to collaboration", "İş birliğine açık"),
    "title":   ("Build spatial systems that hold up.", "Sağlam duran mekânsal sistemler kuralım."),
    "body":    ("Available for collaboration around GeoAI agent systems, production-grade spatial "
                "data science, remote-sensing ML pipelines, GIS automation, decision-support "
                "products and applied simulations.",
                "GeoAI ajan sistemleri, üretim düzeyinde mekânsal veri bilimi, uzaktan algılama ML "
                "hatları, CBS otomasyonu, karar destek ürünleri ve uygulamalı simülasyonlar "
                "konularında iş birliğine açığım."),
    "note":    ("Based in Türkiye · Open-source, research and production collaboration welcome.",
                "Türkiye merkezli · Açık kaynak, araştırma ve üretim iş birliklerine açık."),
    "eng":     ("Engagement", "Çalışma alanları"),
    "open":    ("2026 / open", "2026 / açık"),
    "e1":      ("Agent skill systems and evaluation harnesses",
                "Ajan skill sistemleri ve değerlendirme koşumları"),
    "e2":      ("Guarded GIS automation and MCP infrastructure",
                "Korumalı CBS otomasyonu ve MCP altyapısı"),
    "e3":      ("Reproducible remote-sensing pipelines",
                "Yeniden üretilebilir uzaktan algılama hatları"),
    "e4":      ("Spatial decision-support products",
                "Mekânsal karar destek ürünleri"),
    "e5":      ("Research software and citable releases",
                "Araştırma yazılımı ve atıf verilebilir sürümler"),
    "efoot":   ("Written briefs preferred. Every engagement starts with explicit invariants, data "
                "contracts and success criteria.",
                "Yazılı brief tercih edilir. Her iş, açıkça tanımlanmış değişmezler, veri "
                "sözleşmeleri ve başarı ölçütleriyle başlar."),
    "allproj": ("All projects", "Tüm projeler"),
    "set_in":  ("Set in Bricolage Grotesque, Instrument Sans &amp; IBM Plex Mono",
                "Bricolage Grotesque, Instrument Sans ve IBM Plex Mono ile dizildi"),
    "static":  ("Static site · no trackers", "Statik site · izleyici yok"),
}


def c(key):
    return T(*CONTACT_COPY[key])


def footer(page_path, contact=False):
    r = rel(page_path, LANG)
    home = f"{r}{_lang_root(LANG)}index.html"
    if contact:
        block = f"""
<section class="contact" id="contact" aria-labelledby="contact-title">
  <div class="wrap">
    <div class="contact-grid">
      <div>
        <span class="kicker mono rv">{c('kicker')}</span>
        <h2 id="contact-title" class="rv" style="--d:60ms">{c('title')}</h2>
        <p class="rv" style="--d:120ms">{c('body')}</p>
        <div class="cta rv" style="--d:180ms">
          <a class="btn btn--solid" href="mailto:{EMAIL}"><span>{EMAIL}</span></a>
          <a class="btn btn--ghost" href="https://github.com/muend" target="_blank" rel="noopener"><span class="dot" aria-hidden="true"></span><span>github.com/muend</span></a>
          <a class="btn btn--accent" href="https://pypi.org/user/muend/" target="_blank" rel="noopener"><span>PyPI</span></a>
        </div>
        <p class="contact-note rv" style="--d:240ms">{c('note')}</p>
      </div>
      <aside class="avail rv" style="--d:200ms">
        <div class="avail-head mono"><strong>{c('eng')}</strong><span>{c('open')}</span></div>
        <ul>
          <li><i aria-hidden="true"></i>{c('e1')}</li>
          <li><i aria-hidden="true"></i>{c('e2')}</li>
          <li><i aria-hidden="true"></i>{c('e3')}</li>
          <li><i aria-hidden="true"></i>{c('e4')}</li>
          <li><i aria-hidden="true"></i>{c('e5')}</li>
        </ul>
        <div class="avail-foot">{c('efoot')}</div>
      </aside>
    </div>
    <div class="colophon mono">
      <span>© 2026 Muhammed Enes Duran</span>
      <span>{c('set_in')}</span>
      <span>{c('static')}</span>
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
        <span class="kicker mono rv">{c('kicker')}</span>
        <h2 class="rv" style="--d:60ms">{c('title')}</h2>
        <div class="cta rv" style="--d:140ms">
          <a class="btn btn--solid" href="mailto:{EMAIL}"><span>{EMAIL}</span></a>
          <a class="btn btn--ghost" href="{home}#projects"><span class="dot" aria-hidden="true"></span><span>{c('allproj')}</span></a>
        </div>
      </div>
    </div>
    <div class="colophon mono">
      <span>© 2026 Muhammed Enes Duran</span>
      <span>{c('static')}</span>
    </div>
  </div>
</section>
"""
    return f"""{block}
</main>

<dialog class="dlg" id="dlg" aria-labelledby="dlg-title">
  <div class="dlg-head">
    <strong id="dlg-title">{u('dlg_title')}</strong>
    <button class="dlg-close" type="button" data-close>{u('close')}</button>
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
    return f'<a href="{href}"{ext}><span class="u">{label}</span>{ARROW}</a>'


def btn(href, label, kind="ghost", external=True, icon=True):
    ext = ' target="_blank" rel="noopener"' if external else ""
    return f'<a class="btn btn--{kind}" href="{href}"{ext}><span>{label}</span>{ARROW if icon else ""}</a>'


def plate(fig_no, title, svg, note=""):
    note_html = f'\n  <p class="fig-note">{note}</p>' if note else ""
    return f"""<div class="plate rv" data-plate data-title="{fig_no} — {title}">
  <div class="plate-bar"><strong>{fig_no} / {title}</strong>
    <button class="expand" type="button" data-expand>{u('expand')}{EXPAND_ICON}</button>
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
