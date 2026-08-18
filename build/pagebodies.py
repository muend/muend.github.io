"""Per-page content. Every fact here is transcribed from the project's own
repository, package page or store listing."""
import pathlib
import shell
from build import project_page, svg, catalog, ROOT
from projects import PROJECTS

SVGDIR = pathlib.Path(__file__).resolve().parent / "svg"


def narrow(s):
    """Mark a plate whose diagram reads vertically, so it stays at drawing scale."""
    return s.replace('<div class="plate rv"', '<div class="plate plate--narrow rv"', 1)


# ============================================================ 00 benchfck
project_page(
    "benchfck",
    spec_rows=[
        ("Version", "0.4.0-alpha · engineering candidate"),
        ("License", "Apache-2.0 (code) · CC BY 4.0 (future datasets)"),
        ("Language", "Rust, 2024 edition"),
        ("Machine", "30,000 cells · 8-bit wrapping · 8,000,000 step cap"),
        ("Tokenizer", "<code>cl100k_base</code> for BPE measurement"),
        ("Model runs", "0 published · 0 leaderboards"),
    ],
    sections=f"""
{shell.prose("Why", "A benchmark that cannot be gamed by its own judge",
  "<p>Most reasoning benchmarks ship a fixed dataset and score answers with another model. Both "
  "choices leak: the dataset ages into the training corpus, and the judge brings its own errors. "
  "benchfck removes both. It generates every item from a seed, and every step from execution to "
  "scoring is exact arithmetic on a pinned virtual machine.</p>"
  "<p>The cost of that choice is scope. It measures controlled machine-state reasoning, and nothing "
  "else. It does not claim to measure general capability.</p>")}

{shell.figure("Fig. 01", "From seed to score",
  "A candidate program is only accepted if the typed intermediate representation and three of the "
  "four encodings agree on every one of the 256 possible input bindings. Anything that disagrees is "
  "discarded before a model ever sees it.",
  shell.plate("Fig. 01", "Generation and verification chain", svg("benchfck.svg")))}

{shell.prose("Encodings", "Four rungs of the same program",
  "<p>Each accepted program is rendered into four instruction encodings. They describe identical "
  "behaviour with very different surface forms, which separates a model that reasons about machine "
  "state from one that pattern-matches familiar Brainfuck idioms.</p>"
  "<ul>"
  "<li><strong>E0</strong> — canonical Brainfuck with implicit pointer-relative addressing.</li>"
  "<li><strong>E1</strong> — per-item symbol permutation plus an operational legend, so memorised "
  "glyphs stop helping.</li>"
  "<li><strong>E2</strong> — compact explicit operations with a run-length carrier, 3.356× the token "
  "count of E0.</li>"
  "<li><strong>E3</strong> — verbose explicit operations, 7.072× E0.</li>"
  "</ul>")}

<section class="fig">
  <div class="fig-head">
    <span class="n">Gates</span>
    <h3>What a generated item has to clear</h3>
    <span class="rule" aria-hidden="true"></span>
  </div>
  <p>Population-level gates are published before any model is run, so the acceptance criteria cannot
  be tuned after seeing results.</p>
{catalog([
    ("Trace semantic density", "≥ 0.30", "Execution has to actually do work, not idle through steps."),
    ("Avalanche score", "≥ 0.60", "Small input changes must propagate into the machine state."),
    ("Canonical-idiom rate", "&lt; 0.08", "Programs that collapse into memorised idioms are rejected."),
    ("Constructor breadth", "1,730", "Unique semantic functions identified across 51 coarse profile buckets."),
])}
</section>

{shell.prose("Testing", "Property tests over a 10,000-program population",
  "<p>Four balanced, non-overlapping CI jobs partition a 10,000-program population, so a regression "
  "in one structural family cannot hide behind the others. GitHub Actions runs CI and CodeQL; local "
  "control scripts reproduce the same checks offline.</p>")}

{shell.note("Scope", "This is a <strong>v0.4.0-alpha engineering candidate</strong>. No model results "
  "have been produced and no leaderboard exists. The release scope is arity 1, with arity 2 deferred "
  "to v0.5. The public generator reveals its constructor family by design, so the eight public "
  "constructors are a narrow subset of the identified space, and the private scoring epoch has not "
  "been activated.", warn=True)}
""")


# ============================================================ 01 geoai-skills
EVIDENCE = SVGDIR.joinpath("evidence.html").read_text(encoding="utf-8")

project_page(
    "geoai-skills",
    spec_rows=[
        ("Version", "0.2.0"),
        ("License", "MIT"),
        ("Skills", "18, grouped into five lifecycle stages"),
        ("Claude Code", "<code>claude plugin marketplace add muend/geoai-skills</code>"),
        ("Codex", "<code>npx skills add muend/geoai-skills --skill '*' -a codex</code>"),
        ("Evaluation", "167 native cases + 5 external"),
    ],
    sections=f"""
{shell.prose("Why", "Geospatial work fails quietly",
  "<p>A wrong projection does not raise an exception. Neither does a train/test split that lets the "
  "same field appear on both sides, an area computed in degrees, or a confident number with no "
  "uncertainty attached. The analysis completes, the map renders, and the error ships.</p>"
  "<p>These eighteen skills give a general-purpose agent the reflexes a geospatial specialist has: "
  "check the CRS before trusting a distance, treat spatial autocorrelation as the default, and refuse "
  "to state a result the evidence does not support.</p>")}

{shell.figure("Fig. 01", "Eighteen skills across one lifecycle",
  "The orchestrator decomposes a request and routes it across the five stages. Skills are written to "
  "trigger narrowly: negative and collision cases in the suite test specifically against "
  "over-triggering.",
  shell.plate("Fig. 01", "Lifecycle routing atlas", svg("atlas.svg")))}

<section class="fig">
  <div class="fig-head">
    <span class="n">Fig. 02</span>
    <h3>Measured routing behaviour</h3>
    <span class="rule" aria-hidden="true"></span>
  </div>
  <p>Deterministic scoring from recorded activations against a frozen suite, with an enabled/disabled
  control. The control is the part that matters: with the skills switched off, the same model on the
  same cases activates nothing at all.</p>
{EVIDENCE}
</section>

{shell.prose("Invariants", "What every skill enforces, regardless of task",
  "<ul>"
  "<li>CRS and units are explicit before any measurement is trusted.</li>"
  "<li>Spatial leakage is the default risk, not an edge case.</li>"
  "<li>Every stage ends with a verification step.</li>"
  "<li>Uncertainty and sensitivity are outputs, not footnotes.</li>"
  "<li>Missing evidence narrows the claim, or blocks it.</li>"
  "</ul>")}

{shell.note("Scope", "The published metrics describe <strong>routing behaviour</strong>: whether the "
  "right skill activates for the right request on Claude Code 2.1.214 with claude-sonnet-5, measured "
  "2026-08-05. They say nothing about the quality of the answers those skills then produce. The "
  "held-out split was already consumed by a prior run, which limits its power to confirm improvement.")}
""")


# ============================================================ 02 arcgis-mcp-bridge
project_page(
    "arcgis-mcp-bridge",
    spec_rows=[
        ("License", "Apache-2.0"),
        ("Package", "<code>pip install arcgis-mcp-bridge</code>"),
        ("Tools", "100 across 10 verticals"),
        ("Requires", "Python 3.11+ · ArcGIS Pro 3.1–3.3 tested"),
        ("Platform", "Windows, with a licensed ArcGIS Pro install"),
        ("Tests", "86 offline, ArcPy mocked"),
    ],
    sections=f"""
{shell.prose("Why", "Untrusted arguments, licensed runtime",
  "<p>An MCP tool call arrives as JSON from a language model. Handing that straight to ArcPy means "
  "letting generated text address the filesystem of a machine with a licensed ArcGIS Pro install on "
  "it. The interesting problem is not exposing geoprocessing; it is exposing it without turning the "
  "model into an unsandboxed local shell.</p>"
  "<p>The answer here is two processes that do not trust each other, with the same path validation "
  "implemented independently on both sides of the boundary.</p>")}

{shell.figure("Fig. 01", "Two processes, one security floor",
  "Layer A never imports ArcPy, so a crash or a hostile path never reaches the licensed runtime "
  "through the server process. PathGuard runs before dispatch and again inside the worker: a bypass "
  "requires defeating both.",
  narrow(shell.plate("Fig. 01", "Two-process architecture", svg("mcp.svg"))))}

<section class="fig">
  <div class="fig-head">
    <span class="n">Catalog</span>
    <h3>100 tools across ten verticals</h3>
    <span class="rule" aria-hidden="true"></span>
  </div>
  <p>Every tool is declarative: a typed Pydantic v2 contract in, a structured NDJSON result frame out.
  Failures are values, not stack traces.</p>
{catalog([
    ("Geometry analysis", "23", "Overlay, buffer, dissolve, proximity, topology-aware operations."),
    ("Data management", "22", "Feature classes, fields, geodatabases, conversion, append."),
    ("Raster operations", "15", "Clip, mosaic, resample, project, extract by mask, zonal statistics."),
    ("Map layer management", "10", "Add, order, symbolise, toggle and zoom layers in a project."),
    ("Export &amp; layout", "9", "Layout PDF and PNG export, legend and text element updates."),
    ("Editing &amp; topology", "7", "Repair geometry, eliminate parts, detect and check topology."),
    ("Spatial statistics", "5", "Hot spots, autocorrelation, mean centre, directional distribution."),
    ("Network analysis", "4", "Route, service area, closest facility, OD cost matrix."),
    ("Coordinate &amp; projection", "4", "Define, project, describe and validate spatial references."),
    ("Vision analytics", "1", "Sketch-to-GIS: ORB + RANSAC registration with HSV segmentation."),
])}
  <p class="fig-note">The vision tool turns a photographed hand-drawn parcel boundary into
  geodatabase features by registering the sketch against a reference frame, then segmenting the drawn
  lines in HSV space.</p>
</section>

{shell.prose("Safety", "What PathGuard actually does",
  "<p>Every path-bearing argument is normalised and checked against an allowed root before dispatch, "
  "then re-validated inside the worker that holds the licence. Destructive operations sit behind an "
  "explicit confirmation gate rather than a flag a model can set on its own.</p>"
  "<p>The 86-test suite runs with ArcPy mocked, so contributors without a Windows licence can still "
  "verify validation, security, licence handling and geoprocessing contracts offline.</p>")}
""")


# ============================================================ 03 sentinel-crop-pipeline
project_page(
    "sentinel-crop-pipeline",
    spec_rows=[
        ("License", "Apache-2.0"),
        ("Package", "<code>pip install sentinel-crop-pipeline</code>"),
        ("DOI", "10.5281/zenodo.21284444"),
        ("Status", "Beta research software"),
        ("Source", "Copernicus Data Space Ecosystem · Sentinel-2 L2A"),
        ("Bands", "B02, B03, B04, B08 + derived MASK"),
        ("Config", "YAML, one file per run"),
    ],
    sections=f"""
{shell.prose("Why", "The dataset is the experiment",
  "<p>Most of the reproducibility problem in remote-sensing machine learning sits upstream of the "
  "model. Which scenes were selected and why, how many pixels the cloud mask removed, whether two "
  "patches from the same field ended up on opposite sides of the split — these decisions determine "
  "the result, and they are usually undocumented.</p>"
  "<p>This pipeline treats them as first-class outputs. Every stage writes a timestamped JSON summary, "
  "and the patch manifest records the split assignment and invalid-pixel percentage of every patch.</p>")}

{shell.figure("Fig. 01", "Five stages, each one auditable",
  "Stages run individually or as <code>sentinel-crop run-all</code>. The illustrations show what each "
  "stage does to the data, not what it is called.",
  shell.plate("Fig. 01", "Sentinel-2 data lineage", svg("sentinel.svg")))}

<section class="fig">
  <div class="fig-head">
    <span class="n">Stages</span>
    <h3>What each command produces</h3>
    <span class="rule" aria-hidden="true"></span>
  </div>
{catalog([
    ("discover", "01", "STAC search with deterministic scene selection; writes per-scene accept and reject decisions."),
    ("download", "02", "AOI-cropped retrieval through the CDSE Process API rather than whole tiles."),
    ("preprocess", "03", "SCL masking, reflectance normalisation, NDVI / NDRE / NDWI where bands allow."),
    ("patch", "04", "Fixed-size patches with spatially blocked train, validation and test assignment."),
    ("label", "05", "Rasterises externally prepared ground-truth polygons into uint8 masks."),
])}
  <p class="fig-note">Whole grid blocks are assigned to a single split, which reduces the spatial
  autocorrelation that makes random splits flatter the model.</p>
</section>

{shell.prose("Outputs", "The audit trail is part of the deliverable",
  "<ul>"
  "<li><code>logs/run_&lt;stage&gt;_&lt;timestamp&gt;.json</code> — per-stage summaries.</li>"
  "<li><code>logs/selection_results.json</code> — why each scene was kept or dropped.</li>"
  "<li><code>data/patches/index.csv</code> — the patch manifest: split, paths, invalid percentage.</li>"
  "<li><code>data/patches/cog/</code> — georeferenced GeoTIFFs you can open and look at.</li>"
  "<li>Training exports as COG/TIFF, NPY, and optional TFRecord.</li>"
  "</ul>"
  "<p>A validated live run over an Urla area of interest produced 990 training patches from 9 "
  "Sentinel-2 L2A scenes in June 2025.</p>")}

{shell.note("Limitations", "The interim Urla AOI is a rectangle, not an official boundary. Spatial "
  "blocks reduce leakage but do not eliminate it where fields cross block edges. The label stage "
  "requires externally prepared ground-truth polygons; nothing is downloaded automatically. And the "
  "pipeline prepares data — <strong>it makes no claim about downstream model accuracy</strong>.")}
""")


# ============================================================ 04 agri-dss
project_page(
    "agri-dss",
    spec_rows=[
        ("License", "Apache-2.0"),
        ("Live", "tarimsalkoridor.online"),
        ("Coverage", "5 districts · 147 neighbourhoods"),
        ("Districts", "Demre, Finike, Kaş, Kemer, Kumluca"),
        ("Stack", "Vanilla JavaScript, HTML, CSS"),
        ("Backend", "None — static deployment, local persistence"),
    ],
    sections=f"""
{shell.prose("Why", "A recommendation someone can act on",
  "<p>Regional agricultural analysis usually ends as a PDF nobody in the field reads. This system ends "
  "as a single A4 sheet a cooperative can pin to a village board: pick a district, pick a "
  "neighbourhood, get ranked crop recommendations with the reasoning attached.</p>"
  "<p>It weights soil and climate suitability together with expected market prices, because a crop "
  "that grows well and sells badly is still the wrong answer.</p>")}

{shell.figure("Fig. 01", "From regional data to a printable plan",
  "The scoring is schema-driven and every input is traceable, so a recommendation can be argued with "
  "rather than merely accepted. There is no server-side black box: the whole chain runs in the browser.",
  narrow(shell.plate("Fig. 01", "Auditable decision chain", svg("agri.svg"))))}

<section class="fig">
  <div class="fig-head">
    <span class="n">Coverage</span>
    <h3>The Western Antalya corridor</h3>
    <span class="rule" aria-hidden="true"></span>
  </div>
{catalog([
    ("Neighbourhoods", "147", "Each one resolves to its own ranked recommendation set."),
    ("Districts", "5", "Demre, Finike, Kaş, Kemer and Kumluca."),
    ("Recommendation types", "3", "Seasonal crops, long-term orchard investment, emerging market openings."),
    ("Output", "A4", "One printable typographic sheet per neighbourhood."),
])}
  <p class="fig-note">Crops covered include tomato, pepper, lettuce, avocado, olive, pomegranate,
  almond and the Finike orange.</p>
</section>

{shell.note("Data status", "The current dataset is <strong>conceptual</strong>, derived from regional "
  "economy, environment, land-use and climate reports. It demonstrates the system's logic and "
  "interface. A production deployment would need to be backed by real soil, climate and market data "
  "feeds before any of its recommendations should drive a planting decision.", warn=True)}
""")


# ============================================================ 05 FOUNDER.EXE
project_page(
    "founder-exe",
    spec_rows=[
        ("Platform", "Windows x64"),
        ("Price", "$4.99 USD or more"),
        ("Status", "In development · updated 2026-07-30"),
        ("Languages", "English and Turkish"),
        ("Genre", "Simulation · Educational · Strategy"),
        ("Regimes", "Türkiye and USA, modelled separately"),
    ],
    sections=f"""
{shell.prose("Why", "Rules are more interesting than resources",
  "<p>Most business simulations model money and ignore institutions. The part that actually kills "
  "early companies — a tax deadline you did not diary, a company structure that blocks the financing "
  "you need, a hire that looks affordable until payroll lands — never appears.</p>"
  "<p>FOUNDER.EXE encodes two real regulatory regimes as separate rule sets, so the same strategy "
  "produces different outcomes in Türkiye and the USA. The lesson is the divergence, not the score.</p>")}

{shell.figure("Fig. 01", "One monthly tick, four coupled dimensions",
  "Cash, compliance, product and people are not independent bars to fill. Hiring shortens runway, "
  "shipping fast accrues technical debt, and a financing round dilutes the cap table you will care "
  "about later.",
  shell.plate("Fig. 01", "Rule-driven operating model", svg("founder.svg")))}

<section class="fig">
  <div class="fig-head">
    <span class="n">Systems</span>
    <h3>What is in the build</h3>
    <span class="rule" aria-hidden="true"></span>
  </div>
{catalog([
    ("Academy modules", "26", "Structured lessons with career certification, playable outside a run."),
    ("Decision scenarios", "5", "Standalone situations you can attempt without a full campaign."),
    ("Jurisdictions", "2", "Türkiye and USA, with separate institutions and company structures."),
    ("Interface", "OS", "Founder OS: a desktop metaphor rather than a menu stack."),
])}
  <p class="fig-note">Also included: live market data, an optional AI assistant, leaderboards, local
  saves with export and import, and accessibility modes covering high contrast and colour-blind
  palettes.</p>
</section>

{shell.prose("Design note", "Delayed consequence as the core mechanic",
  "<p>The simulation is built around actions whose cost arrives late. Growth can hide a weak product "
  "for several months before churn makes it visible; shipping past a quality threshold builds "
  "technical debt that only bites when the team scales. A run that looks healthy on the dashboard can "
  "already be lost.</p>")}
""")


# ============================================================ research
AGRI_UNET_NOTE = shell.note(
    "Status",
    "Segmentation work sits downstream of "
    "<a href='projects/sentinel-crop-pipeline.html' style='text-decoration:underline'>"
    "sentinel-crop-pipeline</a>, which supplies the spatially blocked patches and aligned label "
    "masks. The repository is not yet populated, so there are no published metrics or trained "
    "weights to report here.")

RESEARCH_BODY = f"""<main id="main">

<div class="wrap">
  <nav class="crumb mono" aria-label="Breadcrumb">
    <a href="index.html">Home</a><span>/</span><span>Research</span>
  </nav>
</div>

<header class="phead">
  <div class="wrap phead-grid">
    <div>
      <span class="kind mono rv">Academic &amp; research</span>
      <h1 class="rv" style="--d:60ms">Research</h1>
      <p class="deck rv" style="--d:120ms">Studies spanning spatial econometrics, composite
        territorial indicators and remote-sensing segmentation — with the methods and the limits
        stated in the same breath.</p>
    </div>
    <div class="phead-side rv" style="--d:160ms">
      <div class="spec">
        <div><span class="k">Studies</span><span class="v">3</span></div>
        <div><span class="k">Reproducibility</span><span class="v">Notebooks, figures and data provenance published</span></div>
        <div><span class="k">Stance</span><span class="v">Descriptive unless a design supports more</span></div>
      </div>
    </div>
  </div>
</header>

<div class="wrap">

<section class="fig">
  <div class="fig-head">
    <span class="n">R / 01</span>
    <h3>turkiye-housing-prices-pandemic</h3>
    <span class="rule" aria-hidden="true"></span>
  </div>
  <p>A reproducible, region-level analysis separating real inflation-adjusted house price growth from
  inflation itself, across 150 months of Türkiye's housing market.</p>
{catalog([
    ("Period", "150", "Months, November 2013 to April 2026."),
    ("Pre-pandemic", "−2%", "Real growth 2014–2019, against +84% nominal."),
    ("Post-pandemic", "+106%", "Real growth 2020–2025, against +1521% nominal."),
    ("Regional spread", "141%", "Ankara's real growth, against İstanbul's 91%."),
])}
  <p class="fig-note">Method: real index construction from the TCMB residential property price index
  deflated by headline CPI, with CAGR, Fisher identity validation and alternative deflator
  comparison. Spatial structure tested with global Moran's I and LISA. Data from TCMB EVDS and TÜİK;
  province boundaries derived from OpenStreetMap.</p>
{shell.note("Limitations", "Maps are simplified rather than cartometric. LISA has limited power at 19 "
  "spatial units. The analysis is <strong>descriptive, not causal</strong>, and no multiple-comparison "
  "correction is applied.")}
  <div class="plinks">{shell.btn("https://github.com/muend/turkiye-housing-prices-pandemic", "Repository", "solid")}</div>
</section>

<section class="fig">
  <div class="fig-head">
    <span class="n">R / 02</span>
    <h3>kutri-resilience-index</h3>
    <span class="rule" aria-hidden="true"></span>
  </div>
  <p>The Kaş Urban-Territorial Resilience Index: a reproducible five-pillar composite indicator
  prototype for the Kaş/Bayındır planning area in Antalya.</p>
{catalog([
    ("Indicators", "40", "Distributed 7 / 7 / 8 / 10 / 8 across the five pillars."),
    ("Pillars", "5", "Hazard, socio-demographic, economic, infrastructure, environmental-cultural."),
    ("Normalisation", "0–1", "Directional logic per indicator, positive or negative."),
    ("Aggregation", "AHP", "Arithmetic mean within pillars, weighted geometric mean across them."),
])}
  <p class="fig-note">Pillars: Natural Hazard &amp; Physical Vulnerability; Socio-Demographic Adaptive
  Capacity; Economic Resilience; Infrastructure &amp; Service Continuity; Environmental &amp; Cultural
  Capital. Weights come from an Analytic Hierarchy Process eigenvector, with nominal policy weights
  tested as an alternative. MIT licence covers the source; raw data is not redistributed.</p>
{shell.note("Limitations", "Explicitly <strong>not a universal or fully validated resilience model</strong>. "
  "It is a case-specific evidence base for planning decisions in one district.")}
  <div class="plinks">{shell.btn("https://github.com/muend/kutri-resilience-index", "Repository", "solid")}</div>
</section>

<section class="fig">
  <div class="fig-head">
    <span class="n">R / 03</span>
    <h3>agri-unet</h3>
    <span class="rule" aria-hidden="true"></span>
  </div>
  <p>Downstream agricultural pattern identification from satellite imagery, kept separate from the
  reusable data-preparation layer so that experiments stay auditable and the dataset work can be
  cited on its own.</p>
{AGRI_UNET_NOTE}
</section>

</div>
"""

(ROOT / "research.html").write_text(
    shell.head("Research — spatial econometrics, resilience indicators, remote sensing",
               "Reproducible studies on Türkiye housing prices, urban-territorial resilience "
               "indicators and agricultural segmentation, with methods and limitations stated.",
               "research", depth=0, canonical="research.html")
    + RESEARCH_BODY + shell.footer(depth=0, contact=False),
    encoding="utf-8")


# ============================================================ practice
PRACTICE_BODY = f"""<main id="main">

<div class="wrap">
  <nav class="crumb mono" aria-label="Breadcrumb">
    <a href="index.html">Home</a><span>/</span><span>Practice</span>
  </nav>
</div>

<header class="phead">
  <div class="wrap phead-grid">
    <div>
      <span class="kind mono rv">How I build</span>
      <h1 class="rv" style="--d:60ms">Practice</h1>
      <p class="deck rv" style="--d:120ms">The same sequence governs infrastructure, research
        software, decision systems and simulations. It is ordered so that the expensive mistakes are
        made cheap.</p>
    </div>
    <div class="phead-side rv" style="--d:160ms">
      <div class="spec">
        <div><span class="k">Stages</span><span class="v">Four, always in order</span></div>
        <div><span class="k">Primary domain</span><span class="v">GeoAI and spatial data science</span></div>
        <div><span class="k">Failure mode</span><span class="v">Silent spatial error</span></div>
      </div>
    </div>
  </div>
</header>

<div class="wrap">

<section class="page-sec">
  <div class="method-track" data-track>
    <article class="mstep" style="--d:0ms"><span class="phase mono">Phase 01</span><h3>Define invariants</h3><p>Make CRS, units, data contracts, safety boundaries and success criteria explicit before implementation.</p></article>
    <article class="mstep" style="--d:180ms"><span class="phase mono">Phase 02</span><h3>Build the pipeline</h3><p>Separate components, isolate risky runtimes, preserve provenance, and make intermediate states inspectable.</p></article>
    <article class="mstep" style="--d:360ms"><span class="phase mono">Phase 03</span><h3>Stress the failure modes</h3><p>Test negative cases, leakage, invalid paths, ambiguous routing, missing data and operational boundaries.</p></article>
    <article class="mstep" style="--d:540ms"><span class="phase mono">Phase 04</span><h3>Ship a usable artifact</h3><p>Deliver a package, live interface, citable release, benchmark, print output or deployment-ready system.</p></article>
  </div>
</section>

<section class="fig">
  <div class="fig-head">
    <span class="n">Principles</span>
    <h3>What that sequence is protecting against</h3>
    <span class="rule" aria-hidden="true"></span>
  </div>
  <div class="principles">
    <article class="principle rv"><span class="n mono">01 / Spatial rigor</span><h3>CRS and units are explicit</h3><p>Area, distance, raster alignment, scale and geometry assumptions are checked before methods are trusted.</p></article>
    <article class="principle rv" style="--d:80ms"><span class="n mono">02 / Honest validation</span><h3>Leakage is treated as a risk</h3><p>Spatially dependent data requires blocked splits, appropriate baselines and validation designs that reflect deployment.</p></article>
    <article class="principle rv" style="--d:160ms"><span class="n mono">03 / Reproducibility</span><h3>Evidence is versioned</h3><p>Typed contracts, CI, immutable benchmark packages, test harnesses and DOI-backed releases keep work reviewable.</p></article>
    <article class="principle rv" style="--d:240ms"><span class="n mono">04 / Product utility</span><h3>Methods become usable systems</h3><p>Analysis is translated into interfaces, reports, local automation or playable simulations rather than left as notebooks.</p></article>
  </div>
</section>

<section class="fig">
  <div class="fig-head">
    <span class="n">Stack</span>
    <h3>Technical core</h3>
    <span class="rule" aria-hidden="true"></span>
  </div>
  <p>A spatial-first stack spanning research methods, agent infrastructure, production engineering and
  browser-native product work.</p>
  <div class="cap rv">
    <div class="cap-nav" role="tablist" aria-label="Technical capability categories">
      <button class="cap-tab mono" role="tab" id="tab-spatial" aria-controls="panel-spatial" aria-selected="true" data-panel="spatial"><span>Spatial / EO</span><span class="c">10</span></button>
      <button class="cap-tab mono" role="tab" id="tab-agents"  aria-controls="panel-agents"  aria-selected="false" tabindex="-1" data-panel="agents"><span>Agents / Eval</span><span class="c">08</span></button>
      <button class="cap-tab mono" role="tab" id="tab-ml"      aria-controls="panel-ml"      aria-selected="false" tabindex="-1" data-panel="ml"><span>AI / ML</span><span class="c">07</span></button>
      <button class="cap-tab mono" role="tab" id="tab-systems" aria-controls="panel-systems" aria-selected="false" tabindex="-1" data-panel="systems"><span>Systems / Product</span><span class="c">10</span></button>
      <div class="cap-fill" aria-hidden="true"></div>
    </div>
    <div class="cap-panels">
      <article class="cap-panel" role="tabpanel" id="panel-spatial" aria-labelledby="tab-spatial" tabindex="0">
        <div>
          <span class="mono field">Spatial / remote sensing</span>
          <h3>Geospatial methods with operational discipline.</h3>
          <p>Vector, raster, EO, spatial statistics, cartography and proprietary GIS workflows handled with explicit projections, scale, validation and output checks.</p>
          <div class="cap-proof">
            <div><span>Primary domain</span><strong>GeoAI</strong></div>
            <div><span>Core failure mode</span><strong>Silent spatial error</strong></div>
            <div><span>Delivery</span><strong>Package · map · DSS</strong></div>
          </div>
        </div>
        <div class="chip-box">
          <span class="mono">Working set<span>10</span></span>
          <div class="chips"><span>GeoPandas</span><span>Shapely</span><span>ArcPy</span><span>Rasterio</span><span>PySAL</span><span>QGIS</span><span>Sentinel-2</span><span>CDSE</span><span>STAC</span><span>PostGIS</span></div>
        </div>
      </article>
      <article class="cap-panel" role="tabpanel" id="panel-agents" aria-labelledby="tab-agents" tabindex="0" hidden>
        <div>
          <span class="mono field">Agents / evaluation</span>
          <h3>Tool-using agents that route, execute and fail safely.</h3>
          <p>Agent Skills, MCP, runtime isolation, typed evaluation contracts, blind request preparation, deterministic scoring and evidence-aware benchmark publication.</p>
          <div class="cap-proof">
            <div><span>Primary domain</span><strong>Agentic GIS</strong></div>
            <div><span>Core failure mode</span><strong>Unsafe or wrong routing</strong></div>
            <div><span>Delivery</span><strong>Plugin · MCP · benchmark</strong></div>
          </div>
        </div>
        <div class="chip-box">
          <span class="mono">Working set<span>08</span></span>
          <div class="chips"><span>Agent Skills</span><span>MCP</span><span>JSON-RPC</span><span>JSON Schema</span><span>Routing evals</span><span>Behavior evals</span><span>Guarded execution</span><span>Benchmark harnesses</span></div>
        </div>
      </article>
      <article class="cap-panel" role="tabpanel" id="panel-ml" aria-labelledby="tab-ml" tabindex="0" hidden>
        <div>
          <span class="mono field">AI / ML / data</span>
          <h3>Models built on defensible data and evaluation.</h3>
          <p>Deep-learning and classical ML workflows with spatial splitting, class-imbalance handling, reproducible preprocessing and georeferencing-preserving inference.</p>
          <div class="cap-proof">
            <div><span>Primary domain</span><strong>Spatial ML</strong></div>
            <div><span>Core failure mode</span><strong>Leakage / false confidence</strong></div>
            <div><span>Delivery</span><strong>Dataset · model · report</strong></div>
          </div>
        </div>
        <div class="chip-box">
          <span class="mono">Working set<span>07</span></span>
          <div class="chips"><span>Python</span><span>PyTorch</span><span>TensorFlow</span><span>scikit-learn</span><span>NumPy</span><span>pandas</span><span>SciPy</span></div>
        </div>
      </article>
      <article class="cap-panel" role="tabpanel" id="panel-systems" aria-labelledby="tab-systems" tabindex="0" hidden>
        <div>
          <span class="mono field">Systems / product</span>
          <h3>Research logic translated into software people can operate.</h3>
          <p>Typed Python services, static web products, CI, testing, distribution, browser-native interfaces, local persistence and low-maintenance deployment architectures.</p>
          <div class="cap-proof">
            <div><span>Primary domain</span><strong>Product engineering</strong></div>
            <div><span>Core failure mode</span><strong>Unmaintainable delivery</strong></div>
            <div><span>Delivery</span><strong>PyPI · web · game</strong></div>
          </div>
        </div>
        <div class="chip-box">
          <span class="mono">Working set<span>10</span></span>
          <div class="chips"><span>FastAPI</span><span>Pydantic v2</span><span>Docker</span><span>Pytest</span><span>Ruff</span><span>Mypy</span><span>GitHub Actions</span><span>Vanilla JS</span><span>HTML/CSS</span><span>Web storage</span></div>
        </div>
      </article>
    </div>
  </div>
</section>

{shell.figure("Fig. 01", "How the projects feed each other",
  "The work compounds: methods inform infrastructure, infrastructure enables execution, and both feed "
  "products that can be used outside a research notebook.",
  shell.plate("Fig. 01", "System atlas", svg("map.svg")))}

</div>
"""

(ROOT / "practice.html").write_text(
    shell.head("Practice — how I build spatial systems",
               "A four-stage method for building GeoAI infrastructure, research software and "
               "decision systems, plus the full capability matrix and system map.",
               "practice", depth=0, canonical="practice.html")
    + PRACTICE_BODY + shell.footer(depth=0, contact=False),
    encoding="utf-8")
