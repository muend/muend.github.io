"""Project registry.

Everything the landing index, the page headers and the prev/next pager need.
Facts are transcribed from each project's own repository or store page; every
visitor-facing string carries both languages as (en, tr).
"""

PROJECTS = [
    dict(
        slug="benchfck",
        no="00",
        name="benchfck",
        kind=("Deterministic evaluation · Exact Rust harness",
              "Deterministik değerlendirme · Kesin Rust koşumu"),
        blurb=("Generates its own machine-state tasks and scores them exactly, so no learned judge "
               "sits between a model and its result.",
               "Kendi makine-durumu görevlerini üretir ve kesin olarak puanlar; modelle sonuç "
               "arasında öğrenilmiş bir hakem durmaz."),
        fig=("4", ("instruction encodings", "komut kodlaması")),
        title=("benchfck — exact machine-state benchmark harness",
               "benchfck — kesin makine-durumu değerlendirme koşumu"),
        desc=("A Brainfuck-based generator and exact Rust harness that produces, validates and "
              "scores machine-state tasks across four controlled instruction encodings.",
              "Dört kontrollü komut kodlaması üzerinde makine-durumu görevleri üreten, doğrulayan "
              "ve puanlayan Brainfuck tabanlı üreteç ve kesin Rust koşumu."),
        deck=("A generator and exact harness for machine-state tasks, built so that nothing in the "
              "scoring path depends on a learned judge.",
              "Makine-durumu görevleri için bir üreteç ve kesin koşum: puanlama yolundaki hiçbir "
              "adım öğrenilmiş bir hakeme bağlı değil."),
        links=[
            ("https://github.com/muend/benchfck", ("Repository", "Depo")),
            ("https://github.com/muend/benchfck/blob/main/VALIDITY.md",
             ("Validity contract", "Geçerlilik sözleşmesi")),
        ],
        tags=[("new", ("v0.4.0-alpha", "v0.4.0-alfa")), "Apache-2.0", "Rust"],
    ),
    dict(
        slug="geoai-skills",
        no="01",
        name="geoai-skills",
        kind=("Agent skills · GeoAI knowledge infrastructure",
              "Ajan skill'leri · GeoAI bilgi altyapısı"),
        blurb=("Eighteen agent skills that make an AI assistant fail loudly on CRS, leakage, units "
               "and uncertainty instead of quietly guessing.",
               "On sekiz ajan skill'i: yapay zekâ asistanının CRS, sızıntı, birim ve belirsizlik "
               "konularında sessizce tahmin yürütmek yerine yüksek sesle hata vermesini sağlar."),
        fig=("18", ("specialist skills", "uzman skill")),
        title=("geoai-skills — a GeoAI discipline layer for AI agents",
               "geoai-skills — yapay zekâ ajanları için GeoAI disiplin katmanı"),
        desc=("Eighteen vendor-neutral Agent Skills covering the full geospatial lifecycle, with a "
              "frozen 167-case routing benchmark and an enabled/disabled control.",
              "Tüm mekânsal yaşam döngüsünü kapsayan, sağlayıcıdan bağımsız on sekiz Agent Skill; "
              "dondurulmuş 167 vakalık yönlendirme kıyaslaması ve açık/kapalı kontrol koşuluyla."),
        deck=("Stop silent CRS, spatial-leakage, validity, unit and uncertainty failures before "
              "they ship.",
              "Sessiz CRS, mekânsal sızıntı, geçerlilik, birim ve belirsizlik hatalarını "
              "yayına çıkmadan durdurur."),
        links=[
            ("https://github.com/muend/geoai-skills", ("Repository", "Depo")),
            ("https://github.com/muend/geoai-skills/blob/main/BENCHMARK.md",
             ("Benchmark", "Kıyaslama")),
        ],
        tags=[("live", ("Active", "Aktif")), "v0.4.0", "MIT",
              ("", ("18 skills", "18 skill"))],
    ),
    dict(
        slug="arcgis-mcp-bridge",
        no="02",
        name="arcgis-mcp-bridge",
        kind=("MCP · Secure GIS execution", "MCP · Güvenli CBS yürütme"),
        blurb=("Exposes ArcGIS Pro geoprocessing to AI agents while keeping the licensed ArcPy "
               "runtime behind a validated process boundary.",
               "ArcGIS Pro coğrafi işlemlerini yapay zekâ ajanlarına açarken lisanslı ArcPy "
               "çalışma zamanını doğrulanmış bir süreç sınırının arkasında tutar."),
        fig=("100", ("geoprocessing tools", "coğrafi işlem aracı")),
        title=("arcgis-mcp-bridge — a local-first MCP server for ArcGIS Pro",
               "arcgis-mcp-bridge — ArcGIS Pro için yerel öncelikli MCP sunucusu"),
        desc=("100 declarative ArcGIS Pro geoprocessing tools exposed over MCP, with PathGuard "
              "enforced independently in two isolated processes.",
              "MCP üzerinden açılan 100 bildirimsel ArcGIS Pro coğrafi işlem aracı; PathGuard iki "
              "yalıtılmış süreçte bağımsız olarak uygulanır."),
        deck=("100 declarative geoprocessing tools. Two isolated processes. One security floor.",
              "100 bildirimsel coğrafi işlem aracı. İki yalıtılmış süreç. Tek güvenlik tabanı."),
        links=[
            ("https://github.com/muend/arcgis-mcp-bridge", ("Repository", "Depo")),
            ("https://pypi.org/project/arcgis-mcp-bridge/", ("PyPI", "PyPI")),
            ("https://smithery.ai/server/muend/arcgis-mcp-bridge", ("Smithery", "Smithery")),
            ("https://glama.ai/mcp/servers/muend/arcgis-mcp-bridge", ("Glama", "Glama")),
            ("https://www.pulsemcp.com/servers/muend-arcgis-bridge", ("PulseMCP", "PulseMCP")),
            ("https://dev.to/muend/building-a-secure-mcp-bridge-for-arcgis-pro-and-arcpy-511g",
             ("Write-up", "Yazı")),
        ],
        tags=[("pkg", ("PyPI", "PyPI")), "Apache-2.0",
              ("", ("100 tools", "100 araç")), ("", ("Windows", "Windows"))],
    ),
    dict(
        slug="sentinel-crop-pipeline",
        no="03",
        name="sentinel-crop-pipeline",
        kind=("Remote sensing · Reproducible data pipeline",
              "Uzaktan algılama · Yeniden üretilebilir veri hattı"),
        blurb=("Takes Sentinel-2 scenes from search to training patches, counting every pixel it "
               "throws away along the way.",
               "Sentinel-2 sahnelerini aramadan eğitim yamalarına taşır ve yol boyunca attığı her "
               "pikseli hesaba katar."),
        fig=("5", ("auditable stages", "denetlenebilir aşama")),
        title=("sentinel-crop-pipeline — reproducible Sentinel-2 data preparation",
               "sentinel-crop-pipeline — yeniden üretilebilir Sentinel-2 veri hazırlığı"),
        desc=("A five-stage Sentinel-2 L2A preparation pipeline for crop classification, with SCL "
              "masking, spatially blocked splits and a full accounting trail.",
              "Ürün sınıflandırması için beş aşamalı Sentinel-2 L2A hazırlık hattı: SCL maskeleme, "
              "mekânsal bloklu ayrım ve eksiksiz hesap izi."),
        deck=("A reproducible Sentinel-2 data preparation pipeline for crop-classification "
              "research, where every discarded pixel is accounted for.",
              "Ürün sınıflandırma araştırması için yeniden üretilebilir bir Sentinel-2 veri "
              "hazırlık hattı; atılan her piksel kayda geçer."),
        links=[
            ("https://github.com/muend/sentinel-crop-pipeline", ("Repository", "Depo")),
            ("https://pypi.org/project/sentinel-crop-pipeline/", ("PyPI", "PyPI")),
            ("https://doi.org/10.5281/zenodo.21284444", ("Zenodo DOI", "Zenodo DOI")),
        ],
        tags=[("pkg", ("Zenodo DOI", "Zenodo DOI")), "Apache-2.0",
              ("", ("Beta", "Beta")), ("", ("CDSE", "CDSE"))],
    ),
    dict(
        slug="agri-dss",
        no="04",
        name="agri-dss",
        kind=("Spatial DSS · Public-facing product", "Mekânsal KDS · Kamuya açık ürün"),
        blurb=("Turns regional agricultural data for 147 neighbourhoods into a crop plan a "
               "cooperative can pin to a village board.",
               "147 mahalleye ait bölgesel tarım verisini, bir kooperatifin köy panosuna asabileceği "
               "bir ürün planına dönüştürür."),
        fig=("147", ("neighbourhoods", "mahalle")),
        title=("agri-dss — decision support for the Western Antalya corridor",
               "agri-dss — Batı Antalya koridoru için karar desteği"),
        desc=("A zero-backend decision-support system covering five districts and 147 "
              "neighbourhoods, producing printable single-sheet crop plans.",
              "Beş ilçe ve 147 mahalleyi kapsayan, tek sayfalık yazdırılabilir ürün planları "
              "üreten, sunucusuz bir karar destek sistemi."),
        deck=("Decision support for the Western Antalya agricultural corridor, ending in something "
              "you can print on one A4 sheet.",
              "Batı Antalya tarımsal koridoru için karar desteği; sonucu tek bir A4 sayfaya "
              "yazdırabildiğiniz bir çıktı."),
        links=[
            ("https://tarimsalkoridor.online", ("Live app", "Canlı uygulama")),
            ("https://github.com/muend/agri-dss", ("Repository", "Depo")),
        ],
        tags=[("live", ("Live", "Canlı")), "Apache-2.0",
              ("", ("5 districts", "5 ilçe")), ("", ("No backend", "Sunucusuz"))],
    ),
    dict(
        slug="founder-exe",
        no="05",
        name="FOUNDER.EXE",
        kind=("Applied simulation · Desktop game", "Uygulamalı simülasyon · Masaüstü oyunu"),
        blurb=("A startup simulation where cash, compliance, product and people interact under two "
               "real regulatory regimes.",
               "Nakit, uyum, ürün ve insanın iki gerçek düzenleyici rejim altında etkileştiği bir "
               "girişim simülasyonu."),
        fig=("26", ("academy modules", "akademi modülü")),
        title=("FOUNDER.EXE — a startup simulation across two regulatory regimes",
               "FOUNDER.EXE — iki düzenleyici rejim arasında bir girişim simülasyonu"),
        desc=("A Windows startup simulation modelling cash, compliance, cap tables and SAFE "
              "negotiations across the Türkiye and USA ecosystems.",
              "Türkiye ve ABD ekosistemlerinde nakit, uyum, pay tablosu ve SAFE müzakerelerini "
              "modelleyen bir Windows girişim simülasyonu."),
        deck=("A startup simulation where cash, compliance, product and people interact across the "
              "Türkiye and USA ecosystems.",
              "Nakit, uyum, ürün ve insanın Türkiye ve ABD ekosistemleri boyunca etkileştiği bir "
              "girişim simülasyonu."),
        links=[
            ("https://muend.itch.io/founderexe", ("itch.io", "itch.io")),
        ],
        tags=[("new", ("In development", "Geliştiriliyor")),
              ("", ("Windows x64", "Windows x64")), ("", ("EN / TR", "EN / TR"))],
    ),
]

BY_SLUG = {p["slug"]: p for p in PROJECTS}
