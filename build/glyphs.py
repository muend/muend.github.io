"""One distinct mark per project.

Each glyph is a 64x64 line drawing in the same stroke language as the technical
plates, so the index reads as a contact sheet of the diagrams behind it.
"""

BENCHFCK = """<svg class="glyph" viewBox="0 0 64 64" aria-hidden="true">
  <rect class="gaf" x="22" y="27" width="11" height="14"/>
  <path class="ga" d="M27.5 8v8"/>
  <path class="gaf" d="M23.5 15h8l-4 6z"/>
  <rect class="gk" x="5"  y="26" width="16" height="16"/>
  <rect class="gk" x="21" y="26" width="13" height="16"/>
  <rect class="gk" x="34" y="26" width="13" height="16"/>
  <path class="gk" d="M47 26h12v16H47"/>
  <path class="gk" d="M5 51h54"/>
  <path class="gk" d="M9 51v5M22 51v5M35 51v5M48 51v5"/>
</svg>"""

GEOAI_SKILLS = """<svg class="glyph" viewBox="0 0 64 64" aria-hidden="true">
  <rect class="gk" x="17" y="5" width="30" height="11"/>
  <path class="ga" d="M32 16v7"/>
  <path class="gk" d="M6 23h52"/>
  <path class="gk" d="M6 23v8M19 23v8M32 23v8M45 23v8M58 23v8"/>
  <rect class="gk" x="2"  y="31" width="8" height="11"/>
  <rect class="gk" x="15" y="31" width="8" height="11"/>
  <rect class="gk" x="28" y="31" width="8" height="11"/>
  <rect class="gk" x="41" y="31" width="8" height="11"/>
  <rect class="gk" x="54" y="31" width="8" height="11"/>
  <path class="gg" d="M2 51h60"/>
  <path class="gg" d="M2 57h60" opacity=".45"/>
</svg>"""

ARCGIS_MCP = """<svg class="glyph" viewBox="0 0 64 64" aria-hidden="true">
  <rect class="gk" x="4" y="5" width="56" height="15"/>
  <path class="ga" d="M32 20v6"/>
  <rect class="gaf" x="23" y="26" width="18" height="9"/>
  <path class="ga" d="M32 35v6"/>
  <rect class="gk" x="4" y="41" width="56" height="17" stroke-dasharray="4 3"/>
  <path class="gk" d="M12 47h14M12 52h20"/>
</svg>"""

SENTINEL = """<svg class="glyph" viewBox="0 0 64 64" aria-hidden="true">
  <rect class="gf" x="6"  y="6"  width="13" height="13" opacity=".22"/>
  <rect class="gf" x="32" y="19" width="13" height="13" opacity=".38"/>
  <rect class="gf" x="19" y="32" width="13" height="13" opacity=".16"/>
  <rect class="gf" x="45" y="45" width="13" height="13" opacity=".3"/>
  <path class="gk" d="M6 6h52v52H6z"/>
  <path class="gk" d="M19 6v52M32 6v52M45 6v52M6 19h52M6 32h52M6 45h52" opacity=".55"/>
  <path class="ga" d="M15 24 41 15 49 39 23 47Z"/>
</svg>"""

AGRI_DSS = """<svg class="glyph" viewBox="0 0 64 64" aria-hidden="true">
  <path class="gk" d="M5 6v9M18.5 6v9M32 6v9M45.5 6v9M59 6v9"/>
  <path class="gk" d="M5 15h54"/>
  <path class="gk" d="M5 15 32 34M59 15 32 34M18.5 15 32 34M45.5 15 32 34M32 15v19" opacity=".6"/>
  <path class="ga" d="M32 34v6"/>
  <rect class="gk" x="14" y="40" width="36" height="18"/>
  <path class="gaf" d="M20 46h18v3H20z"/>
  <path class="gf" d="M20 51h11v2H20z" opacity=".45"/>
</svg>"""

FOUNDER = """<svg class="glyph" viewBox="0 0 64 64" aria-hidden="true">
  <rect class="gk" x="4" y="7" width="56" height="50"/>
  <path class="gk" d="M4 18h56"/>
  <circle class="gf" cx="11" cy="12.5" r="2"/>
  <circle class="gf" cx="18" cy="12.5" r="2" opacity=".5"/>
  <circle class="gf" cx="25" cy="12.5" r="2" opacity=".3"/>
  <path class="ga" d="M11 26 22 32 33 35 44 43 53 49"/>
  <path class="gk" d="M11 49h42" opacity=".5"/>
</svg>"""

BY_SLUG = {
    "benchfck": BENCHFCK,
    "geoai-skills": GEOAI_SKILLS,
    "arcgis-mcp-bridge": ARCGIS_MCP,
    "sentinel-crop-pipeline": SENTINEL,
    "agri-dss": AGRI_DSS,
    "founder-exe": FOUNDER,
}
