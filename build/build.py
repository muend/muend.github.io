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
    """items: (name, number, description); each may be (en, tr)."""
    def s(v):
        return T(*v) if isinstance(v, tuple) else v
    body = "\n".join(
        f'  <div><div class="c"><strong>{s(n)}</strong><span class="n">{s(v)}</span></div>'
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
    "kicker": ("AI engineering · LLM evaluation · agent systems",
               "Yapay zekâ mühendisliği · LLM değerlendirme · ajan sistemleri"),
    "edition": ("Portfolio / 2026", "Portfolyo / 2026"),
    "deck": ("I build AI systems that are measured before they are trusted.",
             "Güvenilmeden önce ölçülen yapay zekâ sistemleri kuruyorum."),
    "lede": ("Ten systems along one line of work: <strong>LLM evaluation in production</strong>, "
             "deterministic benchmarks, a GPT built from scratch, agent skills, guarded tool "
             "execution, an urban digital twin with a grounded assistant, simulation, reproducible "
             "data preparation and decision delivery. Open work links to something you can inspect; "
             "client work is described from its own records.",
             "Tek bir çalışma çizgisinde on sistem: <strong>üretimde LLM değerlendirme</strong>, "
             "deterministik kıyaslamalar, sıfırdan kurulan bir GPT, ajan skill'leri, korumalı araç "
             "yürütme, veriye dayanan asistanıyla bir kentsel dijital ikiz, simülasyon, yeniden "
             "üretilebilir veri hazırlığı ve karar teslimi. Açık işler inceleyebileceğiniz bir şeye "
             "bağlanıyor; müşteri işi kendi kayıtlarından anlatılıyor."),
    "cta1": ("See the systems", "Sistemlere bak"),
    "focus": ("Focus", "Odak"),
    "focus_v": ("LLM evaluation, agent systems, MCP tooling, applied ML",
                "LLM değerlendirme, ajan sistemleri, MCP araçları, uygulamalı ML"),
    "shipped": ("Shipped", "Yayınlanan"),
    "shipped_v": ("2 PyPI packages, 1 DOI release, 2 live products",
                  "2 PyPI paketi, 1 DOI sürümü, 2 canlı ürün"),
    "method": ("Method", "Yöntem"),
    "method_v": ("Invariants first, failure modes second, artifact last",
                 "Önce değişmezler, sonra hata kipleri, en son çıktı"),
    "based": ("Based", "Konum"),
    "based_v": ("Türkiye · open to collaboration", "Türkiye · iş birliğine açık"),
    "systems": ("Systems", "Sistemler"),
    "systems_tag": ("10 · open each for diagrams", "10 · diyagramlar için tıklayın"),
    "f0": ("LLM eval cases built", "Kurulan LLM değerlendirme vakası"),
    "f1": ("Agent skills", "Ajan skill'i"),
    "f2": ("MCP tools exposed", "Açılan MCP aracı"),
    "f3": ("Full-route accuracy*", "Tam rota doğruluğu*"),
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
    "recent": ("Experience", "Deneyim"),
    "recent_tag": ("work · research · education", "iş · araştırma · eğitim"),
    "x_more": ("Read the full case study", "Vaka çalışmasının tamamını oku"),
    "x_label": ("Sep 2026", "Eyl 2026"),
    "x_title": ("AI Engineer (Contract) · EatBetter",
                "Yapay Zekâ Mühendisi (Sözleşmeli) · EatBetter"),
    "x_body": (
        "<p>Contract work on an AI-powered nutrition app, run on one rule: measure the model "
        "before changing it.</p>"
        "<ul>"
        "<li><strong>Evaluation platform.</strong> Built a 923-case benchmark from scratch: 569 "
        "human-adjudicated gold labels, a 277-case sealed holdout, 16 deterministic metrics and "
        "742 automated tests in CI. Comparisons use user-clustered bootstrap confidence intervals, "
        "and the release gate counts missing evidence as a failure.</li>"
        "<li><strong>Model decisions by measurement.</strong> Retired a model that cost 7× more "
        "after showing no gain (ΔF1 −0.006, 95% CI [−0.023, +0.012]), and shut down a candidate "
        "pipeline that lost to the bare model in 4 of 4 comparisons.</li>"
        "<li><strong>Assistant safety.</strong> On a frozen 400-case scorecard, a fix for users "
        "with long memory profiles cut the missed-allergy-context veto rate from 96.4% to 2.1%, "
        "the only one of ten candidates to pass the gate. The LLM judge was calibrated on 80 "
        "hand-labelled meals (agreement 0.82 against a 0.66 rule baseline).</li>"
        "<li><strong>Production data quality.</strong> In a live PostgreSQL catalogue of about "
        "387k rows, soft-deleted 88,970 and unpublished 90,735. Every write ran as a ROLLBACK "
        "rehearsal against a predicted row count before a human-approved COMMIT, and a rule plus "
        "LLM write gate closed the source.</li>"
        "</ul>"
        "<p>Python · TypeScript / Node.js · PostgreSQL · Azure OpenAI</p>",
        "<p>Yapay zekâ destekli bir beslenme uygulamasında sözleşmeli çalışma; tek kuralla "
        "yürüdü: modeli değiştirmeden önce ölç.</p>"
        "<ul>"
        "<li><strong>Değerlendirme platformu.</strong> 923 vakalık bir kıyaslamayı sıfırdan "
        "kurdum: insan hakemli 569 altın etiket, 277 vakalık mühürlü ayrık küme, 16 deterministik "
        "metrik ve CI'da 742 otomatik test. Karşılaştırmalar kullanıcı kümeli bootstrap güven "
        "aralıklarıyla yapılır; yayın kapısı eksik kanıtı geçme değil, kalma sayar.</li>"
        "<li><strong>Ölçüme dayalı model kararları.</strong> 7 kat pahalı bir modeli, kazanç "
        "sağlamadığını göstererek devreden çıkardım (ΔF1 −0,006; %95 GA [−0,023, +0,012]); yalın "
        "modele 4 karşılaştırmanın 4'ünde yenilen bir aday hattı kapattım.</li>"
        "<li><strong>Asistan güvenliği.</strong> Dondurulmuş 400 vakalık bir puan kartında, uzun "
        "bellek profilli kullanıcılar için yaptığım düzeltme, gözden kaçan alerji bağlamı veto "
        "oranını %96,4'ten %2,1'e indirdi; on aday arasında kapıyı geçen tek düzeltme oldu. LLM "
        "hakemini elle etiketlenmiş 80 öğünle kalibre ettim (uyum 0,82; kural tabanlı temel "
        "çizgi 0,66).</li>"
        "<li><strong>Üretim veri kalitesi.</strong> Yaklaşık 387 bin satırlık canlı bir PostgreSQL "
        "kataloğunda 88.970 satırı yumuşak sildim, 90.735 satırı yayından kaldırdım. Her yazmayı, "
        "insan onaylı COMMIT'ten önce öngörülen satır sayısına karşı bir ROLLBACK provası olarak "
        "çalıştırdım; kaynağı kural ve LLM tabanlı bir yazma kapısıyla kapattım.</li>"
        "</ul>"
        "<p>Python · TypeScript / Node.js · PostgreSQL · Azure OpenAI</p>"),
    "t_label": ("2026 – 2027", "2026 – 2027"),
    "t_title": ("Undergraduate Researcher · TÜBİTAK 2209-A",
                "Lisans Araştırmacısı · TÜBİTAK 2209-A"),
    "t_body": (
        "<p>A Sentinel-2 crop-classification study using U-Net semantic segmentation with "
        "spatially blocked validation. "
        "<a href='projects/sentinel-crop-pipeline.html' style='text-decoration:underline'>"
        "sentinel-crop-pipeline</a> is the study's reproducible data backbone; its Urla run "
        "produced 990 training patches from 9 scenes.</p>",
        "<p>U-Net anlamsal segmentasyonu ve mekânsal bloklu doğrulamayla yürütülen bir Sentinel-2 "
        "ürün sınıflandırma çalışması. Çalışmanın yeniden üretilebilir veri omurgası "
        "<a href='projects/sentinel-crop-pipeline.html' style='text-decoration:underline'>"
        "sentinel-crop-pipeline</a>; Urla koşusu 9 sahneden 990 eğitim yaması üretti.</p>"),
    "e_label": ("Education", "Eğitim"),
    "e_title": ("City &amp; Regional Planning, with a second degree in MIS",
                "Şehir ve Bölge Planlama; ikinci lisans YBS"),
    "e_body": (
        "<p>B.Sc. City and Regional Planning, İzmir Institute of Technology (İYTE), 2021 – June "
        "2027 (expected). B.Sc. Management Information Systems, Istanbul University (AUZEF), "
        "concurrent second degree, 2022 – 2027 (expected).</p>",
        "<p>Şehir ve Bölge Planlama lisansı, İzmir Yüksek Teknoloji Enstitüsü (İYTE), 2021 – "
        "Haziran 2027 (beklenen). Yönetim Bilişim Sistemleri lisansı, İstanbul Üniversitesi "
        "(AUZEF), eşzamanlı ikinci lisans, 2022 – 2027 (beklenen).</p>"),
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
    x_more = ('<div class="plinks" style="margin-top:var(--s-5)">'
              + shell.btn("projects/eatbetter.html", L('x_more'), "solid", external=False)
              + '</div>')

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
      <div><strong data-count="923">923</strong><span>{L('f0')}</span></div>
      <div><strong data-count="18">18</strong><span>{L('f1')}</span></div>
      <div><strong data-count="100">100</strong><span>{L('f2')}</span></div>
      <div><strong>96.41%</strong><span>{L('f3')}</span></div>
    </div>

    <div class="pindex">
{rows_html}
    </div>

    <p class="mono rv" style="color:var(--ink-mute);margin-top:var(--s-6);max-width:88ch;line-height:1.7;text-transform:none;letter-spacing:.02em">
      {L('foot')}
    </p>
  </div>
</section>

<section class="sec" id="recent" aria-labelledby="recent-title">
  <div class="wrap">
    <div class="sec-head rv">
      <span class="idx mono">02</span>
      <h2 id="recent-title">{L('recent')}</h2>
      <span class="rule" aria-hidden="true"></span>
      <span class="tag mono">{L('recent_tag')}</span>
    </div>

{shell.prose(L('x_label'), L('x_title'), L('x_body') + x_more)}

{shell.prose(L('t_label'), L('t_title'), L('t_body'))}

{shell.prose(L('e_label'), L('e_title'), L('e_body'))}

  </div>
</section>

<section class="sec sec--sunk" aria-labelledby="more-title">
  <div class="wrap">
    <div class="sec-head rv">
      <span class="idx mono">03</span>
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
    title = T("Muhammed Enes Duran — AI Engineer · LLM Evaluation · Agent Systems",
              "Muhammed Enes Duran — Yapay Zekâ Mühendisi · LLM Değerlendirme · Ajan Sistemleri")
    desc = T("LLM evaluation in production, deterministic benchmarks, agent skills and MCP "
             "tooling, a GPT built from scratch, an urban digital twin and applied simulations — "
             "each with inspectable evidence.",
             "Üretimde LLM değerlendirme, deterministik kıyaslamalar, ajan skill'leri ve MCP "
             "araçları, sıfırdan kurulan bir GPT, bir kentsel dijital ikiz ve uygulamalı "
             "simülasyonlar — her biri incelenebilir kanıtla.")
    html = (shell.head(title, desc, "projects", "index.html", person=True)
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
    plinks = f"""
      <div class="plinks">
          {links}
      </div>""" if p["links"] else ""
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
      {shell.spec(spec_rows)}{plinks}
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
    import pagebodies_more
    for lang in shell.LANGS:
        shell.LANG = lang
        build_index()
        pagebodies.build()
        pagebodies_more.build()
    print("built:", sorted(
        str(q.relative_to(ROOT)) for q in ROOT.rglob("*.html") if "build" not in q.parts))


if __name__ == "__main__":
    os.chdir(pathlib.Path(__file__).resolve().parent)
    build_all()
