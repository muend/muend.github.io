# muend.github.io

Personal site of **Muhammed Enes Duran** — AI engineering, LLM evaluation, GeoAI agent
systems, spatial ML and applied simulation.

🔗 Live: https://muend.github.io

## Structure

A landing page that lets a visitor understand each system in one line, with a dedicated page
behind every project holding the technical diagrams and specifications.

```
index.html              landing — hero, project index, experience, contact
research.html           academic work
practice.html           method, capability matrix, system map
projects/*.html         one page per system (10)
tr/                     the same thirteen pages in Turkish
assets/site.css         the whole design system, one file
assets/site.js          reveal choreography, tabs, diagram dialog, cursor
assets/brand/           favicon set and web manifest
assets/video/           launch films, 720p H.264, loaded only on play
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

Verified at 1440 / 820 / 390px across all eighteen pages: no console errors, no horizontal
overflow, no broken internal links, and zero WCAG AA contrast failures.

## Systems

| # | Project | Role |
|---|---|---|
| 00 | EatBetter | Client work: production LLM evaluation and data quality |
| 01 | [benchfck](https://github.com/muend/benchfck) | Deterministic evaluation, exact Rust harness |
| 02 | [geoai-skills](https://github.com/muend/geoai-skills) | 18-skill GeoAI discipline layer for agents |
| 03 | [arcgis-mcp-bridge](https://github.com/muend/arcgis-mcp-bridge) | Local-first MCP server for ArcGIS Pro |
| 04 | [sentinel-crop-pipeline](https://github.com/muend/sentinel-crop-pipeline) | Reproducible Sentinel-2 data preparation |
| 05 | [agri-dss](https://tarimsalkoridor.online) | Spatial decision-support product |
| 06 | PlaceTwin | Urban digital twin and studio platform (private) |
| 07 | [neuron-to-gpt](https://github.com/muend/neuron-to-gpt) | Character-level GPT built from one neuron up |
| 08 | Pixel LLM | LLM development game, in development (private) |
| 09 | [FOUNDER.EXE](https://muend.itch.io/founderexe) | Applied simulation, Windows |

Every figure on the site is transcribed from the project's own repository, package page,
store listing or, for client work, the engagement's own records. Routing metrics come from the frozen 18-skill, 167-case suite in
[`geoai-skills/BENCHMARK.md`](https://github.com/muend/geoai-skills/blob/main/BENCHMARK.md)
(v0.2.0, 2026-08-05) and describe routing behaviour only, not answer quality.

## Contact

- Email: nsduraan@gmail.com
- GitHub: https://github.com/muend
- PyPI: https://pypi.org/user/muend/
