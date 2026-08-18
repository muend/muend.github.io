# muend.github.io

Personal website of **Muhammed Enes Duran** — GeoAI agent systems, spatial ML, secure GIS
automation, and applied simulation.

🔗 Live: https://muend.github.io

## About this repo

A single, self-contained static page (`index.html`) served via GitHub Pages. No build step and
no dependencies: HTML, CSS, and a small amount of vanilla JavaScript, with fonts loaded from
Google Fonts and brand assets under `assets/brand/`.

Every technical diagram is hand-authored inline SVG that shares one drawing language, so the
page ships as one file with no image requests.

### Design system

- **Surfaces** — a single tinted-paper family in OKLCH (`97.6% → 93.2%`, hue 148). No pure
  black or white anywhere.
- **Color** — green carries the system, amber is the only accent and stays under 10% of the
  surface. Red and blue appear solely as diagram semantics.
- **Type** — Bricolage Grotesque (display), Instrument Sans (body), IBM Plex Mono (technical
  labels). Skill and package identifiers are set lowercase to distinguish them from generic
  uppercase labels.
- **Rhythm** — all vertical spacing derives from the body line height (28px).
- **Motion** — staggered scroll reveals, one-shot diagram draw-in, and a reticle cursor on fine
  pointers. Everything is disabled under `prefers-reduced-motion`.

Verified at 1440 / 820 / 390px: no console errors, no overflow, and zero WCAG AA contrast
failures.

## Featured systems

| # | Project | Role |
|---|---|---|
| 00 | [benchfck](https://github.com/muend/benchfck) | Deterministic evaluation, exact Rust harness |
| 01 | [geoai-skills](https://github.com/muend/geoai-skills) | 18-skill GeoAI knowledge layer for agents |
| 02 | [arcgis-mcp-bridge](https://github.com/muend/arcgis-mcp-bridge) | Local-first MCP server for ArcGIS Pro |
| 03 | [sentinel-crop-pipeline](https://github.com/muend/sentinel-crop-pipeline) | Reproducible Sentinel-2 data pipeline |
| 04 | [agri-dss](https://tarimsalkoridor.online) | Spatial decision-support product |
| 05 | [FOUNDER.EXE](https://muend.itch.io/founderexe) | Applied simulation, browser game |

Published routing metrics on the page come from the frozen 18-skill, 167-case suite in
[`geoai-skills/BENCHMARK.md`](https://github.com/muend/geoai-skills/blob/main/BENCHMARK.md)
(v0.2.0, 2026-08-05). They describe routing behavior only, not answer quality.

## Contact

- Email: nsduraan@gmail.com
- GitHub: https://github.com/muend
- PyPI: https://pypi.org/user/muend/
