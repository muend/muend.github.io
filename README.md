# muend.github.io

Personal site of **Muhammed Enes Duran** — GeoAI agent systems, spatial ML, secure GIS
automation and applied simulation.

🔗 Live: https://muend.github.io

## Structure

A landing page that lets a visitor understand each system in one line, with a dedicated page
behind every project holding the technical diagrams and specifications.

```
index.html              landing — hero, project index, contact
research.html           academic work
practice.html           method, capability matrix, system map
projects/*.html         one page per flagship system (6)
assets/site.css         the whole design system, one file
assets/site.js          reveal choreography, tabs, diagram dialog, cursor
assets/brand/           favicon set and web manifest
build/                  the generator that emits every page
```

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

Verified at 1440 / 820 / 390px across all nine pages: no console errors, no horizontal
overflow, no broken internal links, and zero WCAG AA contrast failures.

## Systems

| # | Project | Role |
|---|---|---|
| 00 | [benchfck](https://github.com/muend/benchfck) | Deterministic evaluation, exact Rust harness |
| 01 | [geoai-skills](https://github.com/muend/geoai-skills) | 18-skill GeoAI discipline layer for agents |
| 02 | [arcgis-mcp-bridge](https://github.com/muend/arcgis-mcp-bridge) | Local-first MCP server for ArcGIS Pro |
| 03 | [sentinel-crop-pipeline](https://github.com/muend/sentinel-crop-pipeline) | Reproducible Sentinel-2 data preparation |
| 04 | [agri-dss](https://tarimsalkoridor.online) | Spatial decision-support product |
| 05 | [FOUNDER.EXE](https://muend.itch.io/founderexe) | Applied simulation, Windows |

Every figure on the site is transcribed from the project's own repository, package page or
store listing. Routing metrics come from the frozen 18-skill, 167-case suite in
[`geoai-skills/BENCHMARK.md`](https://github.com/muend/geoai-skills/blob/main/BENCHMARK.md)
(v0.2.0, 2026-08-05) and describe routing behaviour only, not answer quality.

## Contact

- Email: nsduraan@gmail.com
- GitHub: https://github.com/muend
- PyPI: https://pypi.org/user/muend/
