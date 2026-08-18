#!/usr/bin/env python3
"""Emit the whole static site from one shared shell.

Run:  python3 build/site.py
"""
import os
import pathlib
import shell
import glyphs
from projects import PROJECTS, BY_SLUG

ROOT = pathlib.Path(__file__).resolve().parent.parent
SVG = pathlib.Path(__file__).resolve().parent / "svg"


def svg(name):
    return SVG.joinpath(name).read_text(encoding="utf-8").rstrip()


def catalog(items):
    """items: (name, number, description)"""
    body = "\n".join(
        f'  <div><div class="c"><strong>{n}</strong><span class="n">{v}</span></div>'
        f'<p>{d}</p></div>' for n, v, d in items
    )
    return f'<div class="catalog rv">\n{body}\n</div>'


def tags(items):
    kinds = {"live": "tag-chip--live", "new": "tag-chip--new", "pkg": "tag-chip--pkg"}
    out = []
    for it in items:
        if isinstance(it, tuple):
            out.append(f'<span class="tag-chip {kinds.get(it[0], "")}">{it[1]}</span>')
        else:
            out.append(f'<span class="tag-chip">{it}</span>')
    return f'<div class="ptags">{"".join(out)}</div>'


# ---------------------------------------------------------------- landing

def build_index():
    rows = []
    for p in PROJECTS:
        kind_cls = {"live": "tag-chip--live", "new": "tag-chip--new", "pkg": "tag-chip--pkg"}
        rows.append(f"""      <a class="prow rv" href="projects/{p['slug']}.html">
        <span class="pno">{p['no']}</span>
        {glyphs.BY_SLUG[p['slug']]}
        <div class="prow-main">
          <span class="kind">{p['kind']}</span>
          <h2>{p['name']}</h2>
          <p>{p['blurb']}</p>
        </div>
        <div class="prow-fig">
          <strong>{p['fig'][0]}</strong><span>{p['fig'][1]}</span>
        </div>
        <span class="go" aria-hidden="true"><svg viewBox="0 0 16 16" width="13" height="13"><path d="M3 13 13 3M6 3h7v7" fill="none" stroke="currentColor" stroke-width="1.7"/></svg></span>
      </a>""")
    rows_html = "\n".join(rows)

    body = f"""<main id="main">

<header class="lead">
  <div class="wrap">
    <div class="eyebrow rv">
      <span class="kicker mono">GeoAI · Spatial ML · Agent systems</span>
      <span class="line" aria-hidden="true"></span>
      <span class="edition mono">Portfolio / 2026</span>
    </div>
    <div class="lead-grid">
      <div>
        <h1 class="rv" id="hero-name" style="--d:60ms">Muhammed <em>Enes</em> Duran</h1>
        <p class="deck rv" style="--d:130ms">I turn geospatial methods into reliable software systems.</p>
        <p class="lede rv" style="--d:200ms">
          Six systems, each occupying one layer of the same stack: <strong>deterministic evaluation</strong>,
          geospatial knowledge for agents, guarded execution, reproducible data preparation, decision
          delivery, and simulation. Every claim below links to something you can inspect.
        </p>
        <div class="cta rv" style="--d:260ms">
          <a class="btn btn--solid" href="#projects"><span>See the systems</span></a>
          <a class="btn btn--ghost" href="https://github.com/muend" target="_blank" rel="noopener"><span class="dot" aria-hidden="true"></span><span>GitHub</span></a>
        </div>
      </div>
      <div class="lead-side rv" style="--d:200ms">
        <dl>
          <dt>Focus</dt><dd>GeoAI agent systems, spatial ML, secure GIS automation</dd>
          <dt>Shipped</dt><dd>2 PyPI packages, 1 DOI release, 2 live products</dd>
          <dt>Method</dt><dd>Invariants first, failure modes second, artifact last</dd>
          <dt>Based</dt><dd>Türkiye · open to collaboration</dd>
        </dl>
      </div>
    </div>
  </div>
</header>

<section class="sec" id="projects" aria-labelledby="projects-title">
  <div class="wrap">
    <div class="sec-head rv">
      <span class="idx mono">01</span>
      <h2 id="projects-title">Systems</h2>
      <span class="rule" aria-hidden="true"></span>
      <span class="tag mono">06 · open each for diagrams</span>
    </div>

    <div class="figs rv" style="margin-bottom:var(--s-8)">
      <div><strong data-count="18">18</strong><span>GeoAI agent skills</span></div>
      <div><strong data-count="100">100</strong><span>ArcGIS tools exposed</span></div>
      <div><strong>96.41%</strong><span>Full-route accuracy*</span></div>
      <div><strong data-count="147">147</strong><span>Neighbourhoods modelled</span></div>
    </div>

    <div class="pindex">
{rows_html}
    </div>

    <p class="mono rv" style="color:var(--ink-mute);margin-top:var(--s-6);max-width:88ch;line-height:1.7;text-transform:none;letter-spacing:.02em">
      * Routing metrics come from the frozen 18-skill, 167-case suite measured on Claude Code 2.1.214
      with claude-sonnet-5 (2026-08-05). They describe routing behaviour, not answer quality.
    </p>
  </div>
</section>

<section class="sec sec--sunk" aria-labelledby="more-title">
  <div class="wrap">
    <div class="sec-head rv">
      <span class="idx mono">02</span>
      <h2 id="more-title">Behind the systems</h2>
      <span class="rule" aria-hidden="true"></span>
      <span class="tag mono">method &amp; research</span>
    </div>

    <div class="teasers">
      <a class="teaser rv" href="practice.html">
        <span class="kind mono">How I build</span>
        <h2>Practice</h2>
        <p>The same four-stage sequence governs infrastructure, research software, decision systems
          and simulations. Plus the full capability matrix and how the projects feed each other.</p>
        <ul>
          <li><i aria-hidden="true"></i>Define invariants before implementation</li>
          <li><i aria-hidden="true"></i>Stress the failure modes, not the happy path</li>
          <li><i aria-hidden="true"></i>Ship an artifact someone can operate</li>
        </ul>
        <span class="more">Read the method {shell.ARROW}</span>
      </a>

      <a class="teaser rv" style="--d:80ms" href="research.html">
        <span class="kind mono">Academic work</span>
        <h2>Research</h2>
        <p>Studies spanning remote-sensing segmentation, spatial econometrics and composite
          territorial indicators, with methods and limitations stated in full.</p>
        <ul>
          <li><i aria-hidden="true"></i>Türkiye housing prices, 150 months, real vs nominal</li>
          <li><i aria-hidden="true"></i>KUTRI: 40 indicators across five resilience pillars</li>
          <li><i aria-hidden="true"></i>agri-unet: downstream segmentation work</li>
        </ul>
        <span class="more">Read the studies {shell.ARROW}</span>
      </a>
    </div>
  </div>
</section>
"""
    html = (shell.head(
        "Muhammed Enes Duran — GeoAI Agent Systems · Spatial ML · Applied Simulation",
        "GeoAI agent systems, secure ArcGIS automation, reproducible Sentinel-2 pipelines, spatial "
        "decision-support products and applied simulations — each with inspectable evidence.",
        "projects", depth=0)
        + body + shell.footer(depth=0, contact=True))
    (ROOT / "index.html").write_text(html, encoding="utf-8")


# ---------------------------------------------------------------- project pages

def pager(slug):
    i = [p["slug"] for p in PROJECTS].index(slug)
    prev_p = PROJECTS[i - 1] if i > 0 else PROJECTS[-1]
    next_p = PROJECTS[(i + 1) % len(PROJECTS)]
    return f"""<div class="wrap">
  <nav class="pager" aria-label="More projects">
    <a href="{prev_p['slug']}.html"><span class="mono">← {prev_p['no']} · previous</span><strong>{prev_p['name']}</strong></a>
    <a href="{next_p['slug']}.html"><span class="mono">{next_p['no']} · next →</span><strong>{next_p['name']}</strong></a>
  </nav>
</div>
"""


def project_page(slug, spec_rows, sections, extra_tags=None):
    p = BY_SLUG[slug]
    links = "\n          ".join(
        shell.btn(u, t, kind=("solid" if i == 0 else "ghost"), icon=True)
        for i, (u, t) in enumerate(p["links"]))
    tag_list = list(p["tags"])
    body = f"""<main id="main">

<div class="wrap">
  <nav class="crumb mono" aria-label="Breadcrumb">
    <a href="../index.html#projects">Projects</a><span>/</span><span>{p['no']} · {p['name']}</span>
  </nav>
</div>

<header class="phead">
  <div class="wrap phead-grid">
    <div>
      <span class="kind mono rv">{p['kind']}</span>
      <h1 class="rv" style="--d:60ms">{p['name']}</h1>
      <p class="deck rv" style="--d:120ms">{p['deck']}</p>
    </div>
    <div class="phead-side rv" style="--d:160ms">
      {tags(tag_list)}
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
    html = (shell.head(p["title"], p["desc"], "projects", depth=1,
                       canonical=f"projects/{slug}.html")
            + body + shell.footer(depth=1, contact=False))
    (ROOT / "projects" / f"{slug}.html").write_text(html, encoding="utf-8")


if __name__ == "__main__":
    os.chdir(pathlib.Path(__file__).resolve().parent)
    build_index()
    import pagebodies  # noqa: F401  (writes the project, research and practice pages)
    print("built:", sorted(str(q.relative_to(ROOT)) for q in ROOT.rglob("*.html")))
