# muend.github.io

Personal site of **Muhammed Enes Duran** — AI engineering, LLM evaluation, agent systems,
applied ML and simulation.

🔗 Live: https://muend.github.io

## Structure

A landing page that lets a visitor understand each system in one line, with a dedicated page
behind every project holding the technical diagrams and specifications.

```
index.html              landing — hero, project index, experience, contact
research.html           academic work
practice.html           method, capability matrix, system map
projects/*.html         one page per system (12)
tr/                     the same fifteen pages in Turkish
assets/site.css         the whole design system, one file
assets/site.js          reveal choreography, tabs, diagram dialog, cursor
assets/brand/           favicon set and web manifest
assets/video/           launch films, 720p/1080p H.264, loaded only on play
build/                  the generator that emits every page
```

## Languages

English lives at the root, Turkish under `/tr/` with an identical tree, so every page has a
shareable URL in both languages and `hreflang` can point search engines at the right one. The
switcher in the header links to the current page's counterpart, not to the homepage.

Diagram labels stay in English on purpose: most are proper nouns (PathGuard, ArcPy, NDVI) or
terms used in English inside Turkish technical writing, and keeping one set of SVGs means the
two languages cannot drift apart. Everything around them — headings, captions, notes, prose —
is translated.

Structure lives once in `build/`; only the strings are paired as `(en, tr)`.

## Publishing

`deploy.ps1` takes a delivered bundle, extracts it over the working copy, shows what changed,
asks once, then commits and pushes:

```powershell
.\deploy.ps1                 # newest muend-site-*.zip in Downloads
.\deploy.ps1 -Zip path.zip -Message "Update diagrams"
```

It also pins the commit identity to the GitHub noreply address, since pushes that expose a
private address are rejected with GH007.

## Build

Pages share one shell, so the chrome can never drift between files. Regenerate after editing
anything under `build/`:

```bash
python3 build/build.py    # rewrites index.html, research.html, practice.html, projects/*.html
```

No dependencies, no toolchain, no node_modules. Editing the generated HTML directly works too;
just re-run the generator afterwards or your change will be overwritten.

## Design system

- **Surfaces** — one tinted-paper family in OKLCH (`97.6% → 93.2%`, hue 148). No pure black or
  white anywhere.
- **Color** — green carries the system, amber is the only accent and stays under 10% of the
  surface. Red and blue appear solely as diagram semantics.
- **Type** — Bricolage Grotesque (display), Instrument Sans (body), IBM Plex Mono (technical
  labels). Skill and package identifiers are set lowercase to distinguish them from generic
  uppercase labels.
- **Rhythm** — all vertical spacing derives from the body line height (28px).
- **Diagrams** — hand-authored inline SVG sharing one drawing language, with viewBox widths
  matched to render width so labels stay legible. Each has a full-screen inspection dialog.
- **Motion** — staggered scroll reveals, one-shot diagram draw-in, and a reticle cursor on fine
  pointers. All of it is disabled under `prefers-reduced-motion`.

`python build/check_site.py` checks all thirty pages for local links/assets, language
alternates, headings, duplicate IDs and the current project facts. Browser spot checks
cover the desktop home and mobile home, Plan Forge, Girişim Haritası, neuron-to-gpt
and GeoAI Skills. These checks are not a new full accessibility audit.

## Systems

| # | Project | Role |
|---|---|---|
| 00 | EatBetter | Client work: production LLM evaluation and data quality |
| 01 | [benchfck](https://github.com/muend/benchfck) | Deterministic evaluation, exact Rust harness |
| 02 | [neuron-to-gpt](https://github.com/muend/neuron-to-gpt) | From scalar autograd to GPT-2 124M, BPE and checked GPU experiments |
| 03 | [geoai-skills](https://github.com/muend/geoai-skills) | 18-skill GeoAI discipline layer for agents |
| 04 | [arcgis-mcp-bridge](https://github.com/muend/arcgis-mcp-bridge) | Local-first MCP server for ArcGIS Pro |
| 05 | Pixel LLM | LLM development game, in development (private) |
| 06 | Mendirek / PlaceTwin | Urban digital twin and studio platform (private) |
| 07 | FOUNDER.EXE | v1.7 Windows package ready; web demo live |
| 08 | [sentinel-crop-pipeline](https://github.com/muend/sentinel-crop-pipeline) | Reproducible Sentinel-2 data preparation |
| 09 | [agri-dss](https://tarimsalkoridor.online) | Spatial decision-support product |
| 10 | [Girişim Haritası](https://izmir-girisim-haritasi.founderexe.workers.dev) | Source-linked company data, PostgreSQL and APIs |
| 11 | Plan Forge | Local-first Windows document/report software |

Every figure on the site is transcribed from the project's own repository, package page,
store listing or, for client work, the engagement's own records. Routing metrics come from the frozen 18-skill, 167-case suite in
[`geoai-skills/BENCHMARK.md`](https://github.com/muend/geoai-skills/blob/main/BENCHMARK.md)
(2026-08-05) and describe routing behaviour only, not answer quality. The v0.4.1 paired behavior package is reported separately and retains its unmet quality gate.

Updated 2 November 2026: GPT-2 124M, the 1,712-structure Mendirek inventory, Girişim Haritası and Plan Forge; corrected engagement and graduation dates. ArcGIS MCP has Glama TDQS A (3.5/5, score dated 25 Sep 2026); GeoAI Skills appears in Awesome Claude Code and Awesome Geospatial. Smithery links were removed after the service change.

Current case studies live in `build/currentpages.py`; generated HTML remains bilingual. No private repository contents or client reports are published.

## Contact

- Email: nsduraan@gmail.com
- GitHub: https://github.com/muend
- PyPI: https://pypi.org/user/muend/
