"""Project registry.

Everything the landing index, the page headers and the prev/next pager need.
Facts here are transcribed from each project's own repository or store page.
"""

PROJECTS = [
    dict(
        slug="benchfck",
        no="00",
        name="benchfck",
        kind="Deterministic evaluation · Exact Rust harness",
        blurb="Generates its own machine-state tasks and scores them exactly, so no learned "
              "judge sits between a model and its result.",
        fig=("4", "instruction encodings"),
        status=("new", "Alpha"),
        title="benchfck — exact machine-state benchmark harness",
        desc="A Brainfuck-based generator and exact Rust harness that produces, validates and "
             "scores machine-state tasks across four controlled instruction encodings.",
        deck="A generator and exact harness for machine-state tasks, built so that nothing in the "
             "scoring path depends on a learned judge.",
        links=[
            ("https://github.com/muend/benchfck", "Repository"),
            ("https://github.com/muend/benchfck/blob/main/VALIDITY.md", "Validity contract"),
        ],
        tags=["v0.4.0-alpha", "Apache-2.0", "Rust"],
    ),
    dict(
        slug="geoai-skills",
        no="01",
        name="geoai-skills",
        kind="Agent skills · GeoAI knowledge infrastructure",
        blurb="Eighteen agent skills that make an AI assistant fail loudly on CRS, leakage, "
              "units and uncertainty instead of quietly guessing.",
        fig=("18", "specialist skills"),
        status=("live", "Active"),
        title="geoai-skills — a GeoAI discipline layer for AI agents",
        desc="Eighteen vendor-neutral Agent Skills covering the full geospatial lifecycle, with a "
             "frozen 167-case routing benchmark and an enabled/disabled control.",
        deck="Stop silent CRS, spatial-leakage, validity, unit and uncertainty failures before "
             "they ship.",
        links=[
            ("https://github.com/muend/geoai-skills", "Repository"),
            ("https://github.com/muend/geoai-skills/blob/main/BENCHMARK.md", "Benchmark"),
        ],
        tags=["v0.2.0", "MIT", "18 skills"],
    ),
    dict(
        slug="arcgis-mcp-bridge",
        no="02",
        name="arcgis-mcp-bridge",
        kind="MCP · Secure GIS execution",
        blurb="Exposes ArcGIS Pro geoprocessing to AI agents while keeping the licensed ArcPy "
              "runtime behind a validated process boundary.",
        fig=("100", "geoprocessing tools"),
        status=("pkg", "PyPI"),
        title="arcgis-mcp-bridge — a local-first MCP server for ArcGIS Pro",
        desc="100 declarative ArcGIS Pro geoprocessing tools exposed over MCP, with PathGuard "
             "enforced independently in two isolated processes.",
        deck="100 declarative geoprocessing tools. Two isolated processes. One security floor.",
        links=[
            ("https://github.com/muend/arcgis-mcp-bridge", "Repository"),
            ("https://pypi.org/project/arcgis-mcp-bridge/", "PyPI"),
            ("https://smithery.ai/server/muend/arcgis-mcp-bridge", "Smithery"),
            ("https://glama.ai/mcp/servers/muend/arcgis-mcp-bridge", "Glama"),
            ("https://www.pulsemcp.com/servers/muend-arcgis-bridge", "PulseMCP"),
            ("https://dev.to/muend/building-a-secure-mcp-bridge-for-arcgis-pro-and-arcpy-511g", "Write-up"),
        ],
        tags=["Apache-2.0", "100 tools", "Windows"],
    ),
    dict(
        slug="sentinel-crop-pipeline",
        no="03",
        name="sentinel-crop-pipeline",
        kind="Remote sensing · Reproducible data pipeline",
        blurb="Takes Sentinel-2 scenes from search to training patches, counting every pixel it "
              "throws away along the way.",
        fig=("5", "auditable stages"),
        status=("pkg", "Zenodo DOI"),
        title="sentinel-crop-pipeline — reproducible Sentinel-2 data preparation",
        desc="A five-stage Sentinel-2 L2A preparation pipeline for crop classification, with SCL "
             "masking, spatially blocked splits and a full accounting trail.",
        deck="A reproducible Sentinel-2 data preparation pipeline for crop-classification "
             "research, where every discarded pixel is accounted for.",
        links=[
            ("https://github.com/muend/sentinel-crop-pipeline", "Repository"),
            ("https://pypi.org/project/sentinel-crop-pipeline/", "PyPI"),
            ("https://doi.org/10.5281/zenodo.21284444", "Zenodo DOI"),
        ],
        tags=["Apache-2.0", "Beta", "CDSE"],
    ),
    dict(
        slug="agri-dss",
        no="04",
        name="agri-dss",
        kind="Spatial DSS · Public-facing product",
        blurb="Turns regional agricultural data for 147 neighbourhoods into a crop plan a "
              "cooperative can pin to a village board.",
        fig=("147", "neighbourhoods"),
        status=("live", "Live"),
        title="agri-dss — decision support for the Western Antalya corridor",
        desc="A zero-backend decision-support system covering five districts and 147 "
             "neighbourhoods, producing printable single-sheet crop plans.",
        deck="Decision support for the Western Antalya agricultural corridor, ending in something "
             "you can print on one A4 sheet.",
        links=[
            ("https://tarimsalkoridor.online", "Live app"),
            ("https://github.com/muend/agri-dss", "Repository"),
        ],
        tags=["Apache-2.0", "5 districts", "No backend"],
    ),
    dict(
        slug="founder-exe",
        no="05",
        name="FOUNDER.EXE",
        kind="Applied simulation · Desktop game",
        blurb="A startup simulation where cash, compliance, product and people interact under two "
              "real regulatory regimes.",
        fig=("26", "academy modules"),
        status=("new", "In development"),
        title="FOUNDER.EXE — a startup simulation across two regulatory regimes",
        desc="A Windows startup simulation modelling cash, compliance, cap tables and SAFE "
             "negotiations across the Türkiye and USA ecosystems.",
        deck="A startup simulation where cash, compliance, product and people interact across the "
             "Türkiye and USA ecosystems.",
        links=[
            ("https://muend.itch.io/founderexe", "itch.io"),
        ],
        tags=["Windows x64", "EN / TR", "Simulation"],
    ),
]

BY_SLUG = {p["slug"]: p for p in PROJECTS}
