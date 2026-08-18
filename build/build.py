#!/usr/bin/env python3
"""Emit the whole static site, in both languages, from one shared shell.

Run:  python3 build/build.py

English is written to the repo root, Turkish to /tr/ with an identical tree.
"""
import os
import pathlib
import shell
import glyphs
from shell import T
from projects import PROJECTS, BY_SLUG

ROOT = pathlib.Path(__file__).resolve().parent.parent
SVG = pathlib.Path(__file__).resolve().parent / "svg"


def svg(name):
    return SVG.joinpath(name).read_text(encoding="utf-8").rstrip()


def out_path(page_path):
    """Where this site-relative path lands for the language being emitted."""
    prefix = "tr/" if shell.LANG == "tr" else ""
    p = ROOT / (prefix + page_path)
    p.parent.mkdir(parents=True, exist_ok=True)
    return p


def catalog(items):
    """items: (name, number, description); name and description may be (en, tr)."""
    def s(v):
        return T(*v) if isinstance(v, tuple) else v
    body = "\n".join(
        f'  <div><div class="c"><strong>{s(n)}</strong><span class="n">{v}</span></div>'
        f'<p>{s(d)}</p></div>' for n, v, d in items
    )
    return f'<div class="catalog rv">\n{body}\n</div>'


def tags(items):
    kinds = {"live": "tag-chip--live", "new": "tag-chip--new", "pkg": "tag-chip--pkg"}
    out = []
    for it in items:
        if isinstance(it, tuple):
            kind, label = it
            out.append(f'<span class="tag-chip {kinds.get(kind, "")}">{T(*label)}</span>')
        else:
            out.append(f'<span class="tag-chip">{it}</span>')
    return f'<div class="ptags">{"".join(out)}</div>'


# ---------------------------------------------------------------- landing copy

LEAD = {
    "kicker": ("GeoAI · Spatial ML · Agent systems", "GeoAI · Mekânsal ML · Ajan sistemleri"),
    "edition": ("Portfolio / 2026", "Portfolyo / 2026"),
    "deck": ("I turn geospatial methods into reliable software systems.",
             "Mekânsal yöntemleri güvenilir yazılım sistemlerine dönüştürüyorum."),
    "lede": ("Six systems, each occupying one layer of the same stack: "
             "<strong>deterministic evaluation</strong>, geospatial knowledge for agents, guarded "
             "execution, reproducible data preparation, decision delivery, and simulation. Every "
             "claim below links to something you can inspect.",
             "Altı sistem, her biri aynı yığının bir katmanında: "
             "<strong>deterministik değerlendirme</strong>, ajanlar için mekânsal bilgi, korumalı "
             "yürütme, yeniden üretilebilir veri hazırlığı, karar teslimi ve simülasyon. "
             "Aşağıdaki her iddia, inceleyebileceğiniz bir şeye bağlanıyor."),
    "cta1": ("See the systems", "Sistemlere bak"),
    "focus": ("Focus", "Odak"),
    "focus_v": ("GeoAI agent systems, spatial ML, secure GIS automation",
                "GeoAI ajan sistemleri, mekânsal ML, güvenli CBS otomasyonu"),
    "shipped": ("Shipped", "Yayınlanan"),
    "shipped_v": ("2 PyPI packages, 1 DOI release, 2 live products",
                  "2 PyPI paketi, 1 DOI sürümü, 2 canlı ürün"),
    "method": ("Method", "Yöntem"),
    "method_v": ("Invariants first, failure modes second, artifact last",
                 "Önce değişmezler, sonra hata kipleri, en son çıktı"),
    "based": ("Based", "Konum"),
    "based_v": ("Türkiye · open to collaboration", "Türkiye · iş birliğine açık"),
    "systems": ("Systems", "Sistemler"),
    "systems_tag": ("06 · open each for diagrams", "06 · diyagramlar için tıklayın"),
    "f1": ("GeoAI agent skills", "GeoAI ajan skill'i"),
    "f2": ("ArcGIS tools exposed", "Açılan ArcGIS aracı"),
    "f3": ("Full-route accuracy*", "Tam rota doğruluğu*"),
    "f4": ("Neighbourhoods modelled", "Modellenen mahalle"),
    "foot": ("* Routing metrics come from the frozen 18-skill, 167-case suite measured on Claude "
             "Code 2.1.214 with claude-sonnet-5 (2026-08-05). They describe routing behaviour, not "
             "answer quality.",
             "* Yönlendirme metrikleri, Claude Code 2.1.214 ve claude-sonnet-5 üzerinde ölçülen "
             "dondurulmuş 18 skill / 167 vakalık takımdan gelir (2026-08-05). Cevap kalitesini "
             "değil, yönlendirme davranışını tanımlar."),
    "behind": ("Behind the systems", "Sistemlerin ardında"),
    "behind_tag": ("method &amp; research", "yöntem ve araştırma"),
    "p_kind": ("How I build", "Nasıl inşa ediyorum"),
    "p_title": ("Practice", "Yöntem"),
    "p_body": ("The same four-stage sequence governs infrastructure, research software, decision "
               "systems and simulations. Plus the full capability matrix and how the projects feed "
               "each other.",
               "Aynı dört aşamalı sıra altyapıyı, araştırma yazılımını, karar sistemlerini ve "
               "simülasyonları yönetir. Ayrıca tam yetkinlik matrisi ve projelerin birbirini nasıl "
               "beslediği."),
    "p1": ("Define invariants before implementation", "Uygulamadan önce değişmezleri tanımla"),
    "p2": ("Stress the failure modes, not the happy path",
           "Mutlu yolu değil, hata kiplerini zorla"),
    "p3": ("Ship an artifact someone can operate",
           "Birinin çalıştırabileceği bir çıktı teslim et"),
    "p_more": ("Read the method", "Yöntemi oku"),
    "r_kind": ("Academic work", "Akademik çalışma"),
    "r_title": ("Research", "Araştırma"),
    "r_body": ("Studies spanning remote-sensing segmentation, spatial econometrics and composite "
               "territorial indicators, with methods and limitations stated in full.",
               "Uzaktan algılama segmentasyonu, mekânsal ekonometri ve bileşik bölgesel "
               "göstergeleri kapsayan çalışmalar; yöntem ve sınırlar eksiksiz belirtilmiş."),
    "r1": ("Türkiye housing prices, 150 months, real vs nominal",
           "Türkiye konut fiyatları, 150 ay, reel ve nominal"),
    "r2": ("KUTRI: 40 indicators across five resilience pillars",
           "KUTRİ: beş dayanıklılık sütununda 40 gösterge"),
    "r3": ("agri-unet: downstream segmentation work",
           "agri-unet: aşağı akış segmentasyon çalışması"),
    "r_more": ("Read the studies", "Çalışmaları oku"),
}


def L(key):
    return T(*LEAD[key])


def build_index():
    rows = []
    for p in PROJECTS:
        rows.append(f"""      <a class="prow rv" href="projects/{p['slug']}.html">
        <span class="pno">{p['no']}</span>
        {glyphs.BY_SLUG[p['slug']]}
        <div class="prow-main">
          <span class="kind">{T(*p['kind'])}</span>
          <h2>{p['name']}</h2>
          <p>{T(*p['blurb'])}</p>
        </div>
        <div class="prow-fig">
          <strong>{p['fig'][0]}</strong><span>{T(*p['fig'][1])}</span>
        </div>
        <span class="go" aria-hidden="true"><svg viewBox="0 0 16 16" width="13" height="13"><path d="M3 13 13 3M6 3h7v7" fill="none" stroke="currentColor" stroke-width="1.7"/></svg></span>
      </a>""")
    rows_html = "\n".join(rows)

    body = f"""<main id="main">

<header class="lead">
  <div class="wrap">
    <div class="eyebrow rv">
      <span class="kicker mono">{L('kicker')}</span>
      <span class="line" aria-hidden="true"></span>
      <span class="edition mono">{L('edition')}</span>
    </div>
    <div class="lead-grid">
      <div>
        <h1 class="rv" id="hero-name" style="--d:60ms">Muhammed <em>Enes</em> Duran</h1>
        <p class="deck rv" style="--d:130ms">{L('deck')}</p>
        <p class="lede rv" style="--d:200ms">{L('lede')}</p>
        <div class="cta rv" style="--d:260ms">
          <a class="btn btn--solid" href="#projects"><span>{L('cta1')}</span></a>
          <a class="btn btn--ghost" href="https://github.com/muend" target="_blank" rel="noopener"><span class="dot" aria-hidden="true"></span><span>GitHub</span></a>
        </div>
      </div>
      <div class="lead-side rv" style="--d:200ms">
        <dl>
          <dt>{L('focus')}</dt><dd>{L('focus_v')}</dd>
          <dt>{L('shipped')}</dt><dd>{L('shipped_v')}</dd>
          <dt>{L('method')}</dt><dd>{L('method_v')}</dd>
          <dt>{L('based')}</dt><dd>{L('based_v')}</dd>
        </dl>
      </div>
    </div>
  </div>
</header>

<section class="sec" id="projects" aria-labelledby="projects-title">
  <div class="wrap">
    <div class="sec-head rv">
      <span class="idx mono">01</span>
      <h2 id="projects-title">{L('systems')}</h2>
      <span class="rule" aria-hidden="true"></span>
      <span class="tag mono">{L('systems_tag')}</span>
    </div>

    <div class="figs rv" style="margin-bottom:var(--s-8)">
      <div><strong data-count="18">18</strong><span>{L('f1')}</span></div>
      <div><strong data-count="100">100</strong><span>{L('f2')}</span></div>
      <div><strong>96.41%</strong><span>{L('f3')}</span></div>
      <div><strong data-count="147">147</strong><span>{L('f4')}</span></div>
    </div>

    <div class="pindex">
{rows_html}
    </div>

    <p class="mono rv" style="color:var(--ink-mute);margin-top:var(--s-6);max-width:88ch;line-height:1.7;text-transform:none;letter-spacing:.02em">
      {L('foot')}
    </p>
  </div>
</section>

<section class="sec sec--sunk" aria-labelledby="more-title">
  <div class="wrap">
    <div class="sec-head rv">
      <span class="idx mono">02</span>
      <h2 id="more-title">{L('behind')}</h2>
      <span class="rule" aria-hidden="true"></span>
      <span class="tag mono">{L('behind_tag')}</span>
    </div>

    <div class="teasers">
      <a class="teaser rv" href="practice.html">
        <span class="kind mono">{L('p_kind')}</span>
        <h2>{L('p_title')}</h2>
        <p>{L('p_body')}</p>
        <ul>
          <li><i aria-hidden="true"></i>{L('p1')}</li>
          <li><i aria-hidden="true"></i>{L('p2')}</li>
          <li><i aria-hidden="true"></i>{L('p3')}</li>
        </ul>
        <span class="more">{L('p_more')} {shell.ARROW}</span>
      </a>

      <a class="teaser rv" style="--d:80ms" href="research.html">
        <span class="kind mono">{L('r_kind')}</span>
        <h2>{L('r_title')}</h2>
        <p>{L('r_body')}</p>
        <ul>
          <li><i aria-hidden="true"></i>{L('r1')}</li>
          <li><i aria-hidden="true"></i>{L('r2')}</li>
          <li><i aria-hidden="true"></i>{L('r3')}</li>
        </ul>
        <span class="more">{L('r_more')} {shell.ARROW}</span>
      </a>
    </div>
  </div>
</section>
"""
    title = T("Muhammed Enes Duran — GeoAI Agent Systems · Spatial ML · Applied Simulation",
              "Muhammed Enes Duran — GeoAI Ajan Sistemleri · Mekânsal ML · Uygulamalı Simülasyon")
    desc = T("GeoAI agent systems, secure ArcGIS automation, reproducible Sentinel-2 pipelines, "
             "spatial decision-support products and applied simulations — each with inspectable "
             "evidence.",
             "GeoAI ajan sistemleri, güvenli ArcGIS otomasyonu, yeniden üretilebilir Sentinel-2 "
             "hatları, mekânsal karar destek ürünleri ve uygulamalı simülasyonlar — her biri "
             "incelenebilir kanıtla.")
    html = (shell.head(title, desc, "projects", "index.html")
            + body + shell.footer("index.html", contact=True))
    out_path("index.html").write_text(html, encoding="utf-8")


# ---------------------------------------------------------------- project pages

def pager(slug):
    i = [p["slug"] for p in PROJECTS].index(slug)
    prev_p = PROJECTS[i - 1] if i > 0 else PROJECTS[-1]
    next_p = PROJECTS[(i + 1) % len(PROJECTS)]
    return f"""<div class="wrap">
  <nav class="pager" aria-label="{shell.u('more_aria')}">
    <a href="{prev_p['slug']}.html"><span class="mono">← {prev_p['no']} · {shell.u('prev')}</span><strong>{prev_p['name']}</strong></a>
    <a href="{next_p['slug']}.html"><span class="mono">{next_p['no']} · {shell.u('next')} →</span><strong>{next_p['name']}</strong></a>
  </nav>
</div>
"""


def project_page(slug, spec_rows, sections):
    p = BY_SLUG[slug]
    page_path = f"projects/{slug}.html"
    r = shell.rel(page_path, shell.LANG)
    links = "\n          ".join(
        shell.btn(url, T(*label), kind=("solid" if i == 0 else "ghost"))
        for i, (url, label) in enumerate(p["links"]))
    home = f"{r}{'tr/' if shell.LANG == 'tr' else ''}index.html"
    body = f"""<main id="main">

<div class="wrap">
  <nav class="crumb mono" aria-label="{shell.u('crumb_aria')}">
    <a href="{home}#projects">{T(*shell.UI['nav']['projects'])}</a><span>/</span><span>{p['no']} · {p['name']}</span>
  </nav>
</div>

<header class="phead">
  <div class="wrap phead-grid">
    <div>
      <span class="kind mono rv">{T(*p['kind'])}</span>
      <h1 class="rv" style="--d:60ms">{p['name']}</h1>
      <p class="deck rv" style="--d:120ms">{T(*p['deck'])}</p>
    </div>
    <div class="phead-side rv" style="--d:160ms">
      {tags(p['tags'])}
      {shell.spec(spec_rows)}
      <div class="plinks">
          {links}
      </div>
    </div>
  </div>
</header>

<div class="wrap">
{sections}
</div>

{pager(slug)}
"""
    html = (shell.head(T(*p["title"]), T(*p["desc"]), "projects", page_path)
            + body + shell.footer(page_path, contact=False))
    out_path(page_path).write_text(html, encoding="utf-8")


def build_all():
    import pagebodies
    for lang in shell.LANGS:
        shell.LANG = lang
        build_index()
        pagebodies.build()
    print("built:", sorted(
        str(q.relative_to(ROOT)) for q in ROOT.rglob("*.html") if "build" not in q.parts))


if __name__ == "__main__":
    os.chdir(pathlib.Path(__file__).resolve().parent)
    build_all()
