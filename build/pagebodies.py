"""Per-page content, in both languages.

Every fact is transcribed from the project's own repository, package page or
store listing. Structure lives once; only the strings are paired as (en, tr).

Diagram labels stay in English: most are proper nouns (PathGuard, ArcPy, NDVI)
or terms used in English inside Turkish technical writing. Everything around
them — headings, captions, notes, prose — is translated.
"""
import pathlib
import shell
from shell import T as _
from build import project_page, svg, catalog, out_path

SVGDIR = pathlib.Path(__file__).resolve().parent / "svg"


def narrow(s):
    """Mark a plate whose diagram reads vertically, so it stays at drawing scale."""
    return s.replace('<div class="plate rv"', '<div class="plate plate--narrow rv"', 1)


def fighead(n, heading):
    return f"""  <div class="fig-head">
    <span class="n">{n}</span>
    <h3>{heading}</h3>
    <span class="rule" aria-hidden="true"></span>
  </div>"""


def build():
    # ======================================================== 00 benchfck
    project_page(
        "benchfck",
        spec_rows=[
            (_("Version", "Sürüm"), _("0.4.0-alpha · engineering candidate",
                                      "0.4.0-alfa · mühendislik adayı")),
            (_("License", "Lisans"), _("Apache-2.0 (code) · CC BY 4.0 (future datasets)",
                                       "Apache-2.0 (kod) · CC BY 4.0 (gelecek veri setleri)")),
            (_("Language", "Dil"), _("Rust, 2024 edition", "Rust, 2024 sürümü")),
            (_("Machine", "Makine"), _("30,000 cells · 8-bit wrapping · 8,000,000 step cap",
                                       "30.000 hücre · 8-bit döngü · 8.000.000 adım sınırı")),
            (_("Tokenizer", "Tokenleştirici"), _("<code>cl100k_base</code> for BPE measurement",
                                                 "BPE ölçümü için <code>cl100k_base</code>")),
            (_("Model runs", "Model koşusu"), _("0 published · 0 leaderboards",
                                                "0 yayımlanmış · 0 liderlik tablosu")),
        ],
        sections=f"""
{shell.prose(_("Why", "Neden"),
  _("A benchmark that cannot be gamed by its own judge",
    "Kendi hakemiyle oynanamayan bir kıyaslama"),
  _("<p>Most reasoning benchmarks ship a fixed dataset and score answers with another model. Both "
    "choices leak: the dataset ages into the training corpus, and the judge brings its own errors. "
    "benchfck removes both. It generates every item from a seed, and every step from execution to "
    "scoring is exact arithmetic on a pinned virtual machine.</p>"
    "<p>The cost of that choice is scope. It measures controlled machine-state reasoning, and "
    "nothing else. It does not claim to measure general capability.</p>",
    "<p>Akıl yürütme kıyaslamalarının çoğu sabit bir veri seti yayımlar ve cevapları başka bir "
    "modelle puanlar. İki tercih de sızdırır: veri seti zamanla eğitim külliyatına karışır, hakem "
    "ise kendi hatalarını getirir. benchfck ikisini de kaldırır. Her öğeyi bir tohumdan üretir; "
    "yürütmeden puanlamaya kadar her adım, sabitlenmiş bir sanal makine üzerinde kesin "
    "aritmetiktir.</p>"
    "<p>Bu tercihin bedeli kapsamdır. Kontrollü makine-durumu akıl yürütmesini ölçer, başka bir "
    "şeyi değil. Genel yetenek ölçtüğü iddiasında değildir.</p>"))}

{shell.figure(_("Fig. 01", "Şekil 01"),
  _("From seed to score", "Tohumdan puana"),
  _("A candidate program is only accepted if the typed intermediate representation and the "
    "encodings agree on every one of the 256 possible input bindings. Anything that disagrees is "
    "discarded before a model ever sees it.",
    "Bir aday program, ancak tipli ara temsil ile kodlamalar 256 olası girdi bağlamasının her "
    "birinde aynı sonucu verirse kabul edilir. Uyuşmayan her şey, bir model görmeden önce elenir."),
  shell.plate(_("Fig. 01", "Şekil 01"),
              _("Generation and verification chain", "Üretim ve doğrulama zinciri"),
              svg("benchfck.svg")))}

{shell.prose(_("Encodings", "Kodlamalar"),
  _("Four rungs of the same program", "Aynı programın dört basamağı"),
  _("<p>Each accepted program is rendered into four instruction encodings. They describe identical "
    "behaviour with very different surface forms, which separates a model that reasons about "
    "machine state from one that pattern-matches familiar Brainfuck idioms.</p>"
    "<ul>"
    "<li><strong>E0</strong> — canonical Brainfuck with implicit pointer-relative addressing.</li>"
    "<li><strong>E1</strong> — per-item symbol permutation plus an operational legend, so memorised "
    "glyphs stop helping.</li>"
    "<li><strong>E2</strong> — compact explicit operations with a run-length carrier, 3.356× the "
    "token count of E0.</li>"
    "<li><strong>E3</strong> — verbose explicit operations, 7.072× E0.</li>"
    "</ul>",
    "<p>Kabul edilen her program dört komut kodlamasına dönüştürülür. Hepsi aynı davranışı çok "
    "farklı yüzey biçimleriyle anlatır; bu da makine durumu üzerine akıl yürüten bir modeli, tanıdık "
    "Brainfuck kalıplarını eşleştiren bir modelden ayırır.</p>"
    "<ul>"
    "<li><strong>E0</strong> — örtük işaretçi-göreli adreslemeli kanonik Brainfuck.</li>"
    "<li><strong>E1</strong> — öğe başına sembol permütasyonu ve işlem açıklaması; ezberlenmiş "
    "simgeler işe yaramaz hale gelir.</li>"
    "<li><strong>E2</strong> — koşu uzunluğu taşıyıcılı, sıkışık açık işlemler; E0'ın 3,356 katı "
    "token.</li>"
    "<li><strong>E3</strong> — ayrıntılı açık işlemler; E0'ın 7,072 katı.</li>"
    "</ul>"))}

<section class="fig">
{fighead(_("Gates", "Eşikler"), _("What a generated item has to clear",
                                  "Üretilen bir öğenin geçmesi gerekenler"))}
  <p>{_("Population-level gates are published before any model is run, so the acceptance criteria "
        "cannot be tuned after seeing results.",
        "Popülasyon düzeyindeki eşikler herhangi bir model çalıştırılmadan önce yayımlanır; böylece "
        "kabul ölçütleri sonuçlar görüldükten sonra ayarlanamaz.")}</p>
{catalog([
    (_("Trace semantic density", "İz anlamsal yoğunluğu"), "≥ 0.30",
     _("Execution has to actually do work, not idle through steps.",
       "Yürütme gerçekten iş yapmalı, adımları boşa geçmemeli.")),
    (_("Avalanche score", "Çığ skoru"), "≥ 0.60",
     _("Small input changes must propagate into the machine state.",
       "Küçük girdi değişimleri makine durumuna yayılmalı.")),
    (_("Canonical-idiom rate", "Kanonik kalıp oranı"), "&lt; 0.08",
     _("Programs that collapse into memorised idioms are rejected.",
       "Ezberlenmiş kalıplara indirgenen programlar reddedilir.")),
    (_("Constructor breadth", "Kurucu genişliği"), "1,730",
     _("Unique semantic functions identified across 51 coarse profile buckets.",
       "51 kaba profil kovasında saptanan benzersiz anlamsal fonksiyon.")),
])}
</section>

{shell.prose(_("Testing", "Test"),
  _("Property tests over a 10,000-program population",
    "10.000 programlık popülasyon üzerinde özellik testleri"),
  _("<p>Four balanced, non-overlapping CI jobs partition a 10,000-program population, so a "
    "regression in one structural family cannot hide behind the others. GitHub Actions runs CI and "
    "CodeQL; local control scripts reproduce the same checks offline.</p>",
    "<p>Dört dengeli ve örtüşmeyen CI işi, 10.000 programlık popülasyonu böler; böylece bir yapısal "
    "ailedeki gerileme diğerlerinin arkasına saklanamaz. GitHub Actions CI ve CodeQL çalıştırır; "
    "yerel kontrol betikleri aynı denetimleri çevrimdışı tekrarlar.</p>"))}

{shell.note(_("Scope", "Kapsam"),
  _("This is a <strong>v0.4.0-alpha engineering candidate</strong>. No model results have been "
    "produced and no leaderboard exists. The release scope is arity 1, with arity 2 deferred to "
    "v0.5. The public generator reveals its constructor family by design, so the eight public "
    "constructors are a narrow subset of the identified space, and the private scoring epoch has "
    "not been activated.",
    "Bu bir <strong>v0.4.0-alfa mühendislik adayı</strong>. Hiçbir model sonucu üretilmedi ve bir "
    "liderlik tablosu yok. Sürüm kapsamı arity 1; arity 2 v0.5'e ertelendi. Genel üreteç, tasarım "
    "gereği kurucu ailesini açığa vurur; bu yüzden sekiz genel kurucu, saptanan uzayın dar bir alt "
    "kümesidir ve özel puanlama dönemi henüz başlatılmadı."), warn=True)}
""")

    # ======================================================== 01 geoai-skills
    evidence = SVGDIR.joinpath("evidence.html").read_text(encoding="utf-8")
    if shell.LANG == "tr":
        for en, tr in [
            ("Routing benchmark", "Yönlendirme kıyaslaması"),
            ("Strict full-route accuracy on the frozen 18-skill suite: 124 positive and 43 negative cases.",
             "Dondurulmuş 18 skill takımında katı tam rota doğruluğu: 124 pozitif, 43 negatif vaka."),
            ("full route", "tam rota"),
            ("Frozen cases", "Dondurulmuş vaka"),
            ("Held-out cases", "Ayrılmış vaka"),
            ("Published result card", "Yayımlanan sonuç kartı"),
            ("Measured routing behavior", "Ölçülen yönlendirme davranışı"),
            ("Deterministic scoring from recorded activations on Claude Code 2.1.214 with claude-sonnet-5,\n              run against an enabled/disabled control with explicit scope limitations.",
             "Claude Code 2.1.214 ve claude-sonnet-5 üzerinde kaydedilmiş aktivasyonlardan deterministik\n              puanlama; açık/kapalı kontrol koşuluyla ve kapsam sınırları açıkça belirtilerek."),
            ("Open evidence", "Kanıtı aç"),
            ("Precision", "Kesinlik"),
            ("Recall", "Duyarlılık"),
            ("Accuracy", "Doğruluk"),
            ("Route accuracy", "Rota doğruluğu"),
            ("Control · skills disabled", "Kontrol · skill'ler kapalı"),
            ("0 activations", "0 aktivasyon"),
            ("across all 167 cases. Recall 0%, route accuracy 0%, overall accuracy\n            25.75%. The lift is attributable to the skills, not to the base model.",
             "167 vakanın tamamında. Duyarlılık %0, rota doğruluğu %0, genel doğruluk\n            %25,75. Kazanç temel modele değil, skill'lere ait."),
            ("Installable research and infrastructure packages",
             "Kurulabilir araştırma ve altyapı paketleri"),
            ("Citable Sentinel-2 pipeline artifact", "Atıf verilebilir Sentinel-2 hattı çıktısı"),
            ("Held-out split", "Ayrılmış küme"),
            ("62 unseen cases · 100% precision · 95.16% route accuracy",
             "62 görülmemiş vaka · %100 kesinlik · %95,16 rota doğruluğu"),
        ]:
            evidence = evidence.replace(en, tr)

    project_page(
        "geoai-skills",
        spec_rows=[
            (_("Version", "Sürüm"), "0.4.0"),
            (_("License", "Lisans"), "MIT"),
            (_("Skills", "Skill sayısı"), _("18, grouped into five lifecycle stages",
                                            "18, beş yaşam döngüsü aşamasına ayrılmış")),
            ("Claude Code", "<code>claude plugin marketplace add muend/geoai-skills</code>"),
            ("Codex", "<code>npx skills add muend/geoai-skills --skill '*' -a codex</code>"),
            (_("Evaluation", "Değerlendirme"), _("167 native cases + 5 external",
                                                 "167 yerel vaka + 5 dış vaka")),
        ],
        sections=f"""
{shell.prose(_("Why", "Neden"),
  _("Geospatial work fails quietly", "Mekânsal iş sessizce bozulur"),
  _("<p>A wrong projection does not raise an exception. Neither does a train/test split that lets "
    "the same field appear on both sides, an area computed in degrees, or a confident number with "
    "no uncertainty attached. The analysis completes, the map renders, and the error ships.</p>"
    "<p>These eighteen skills give a general-purpose agent the reflexes a geospatial specialist "
    "has: check the CRS before trusting a distance, treat spatial autocorrelation as the default, "
    "and refuse to state a result the evidence does not support.</p>",
    "<p>Yanlış bir projeksiyon istisna fırlatmaz. Aynı tarlanın iki tarafta birden yer almasına izin "
    "veren bir eğitim/test ayrımı da, derece cinsinden hesaplanmış bir alan da, belirsizliği "
    "belirtilmemiş kendinden emin bir sayı da fırlatmaz. Analiz tamamlanır, harita çizilir ve hata "
    "yayına çıkar.</p>"
    "<p>Bu on sekiz skill, genel amaçlı bir ajana mekânsal uzmanın reflekslerini kazandırır: bir "
    "mesafeye güvenmeden önce CRS'i kontrol et, mekânsal otokorelasyonu varsayılan kabul et ve "
    "kanıtın desteklemediği bir sonucu söylemeyi reddet.</p>"))}

{shell.figure(_("Fig. 01", "Şekil 01"),
  _("Eighteen skills across one lifecycle", "Tek bir yaşam döngüsünde on sekiz skill"),
  _("The orchestrator decomposes a request and routes it across the five stages. Skills are written "
    "to trigger narrowly: negative and collision cases in the suite test specifically against "
    "over-triggering.",
    "Orkestratör isteği parçalara ayırır ve beş aşama boyunca yönlendirir. Skill'ler dar tetiklenecek "
    "biçimde yazılmıştır: takımdaki negatif ve çakışma vakaları özellikle aşırı tetiklenmeyi sınar."),
  shell.plate(_("Fig. 01", "Şekil 01"),
              _("Lifecycle routing atlas", "Yaşam döngüsü yönlendirme atlası"),
              svg("atlas.svg")))}

<section class="fig">
{fighead(_("Fig. 02", "Şekil 02"), _("Measured routing behaviour", "Ölçülen yönlendirme davranışı"))}
  <p>{_("Deterministic scoring from recorded activations against a frozen suite, with an "
        "enabled/disabled control. The control is the part that matters: with the skills switched "
        "off, the same model on the same cases activates nothing at all.",
        "Dondurulmuş bir takıma karşı kaydedilmiş aktivasyonlardan deterministik puanlama ve "
        "açık/kapalı kontrol koşulu. Asıl önemli olan kontrol: skill'ler kapalıyken aynı model aynı "
        "vakalarda hiçbir şey tetiklemiyor.")}</p>
{evidence}
</section>

{shell.prose(_("Invariants", "Değişmezler"),
  _("What every skill enforces, regardless of task",
    "Her skill'in, görevden bağımsız olarak dayattığı kurallar"),
  _("<ul>"
    "<li>CRS and units are explicit before any measurement is trusted.</li>"
    "<li>Spatial leakage is the default risk, not an edge case.</li>"
    "<li>Every stage ends with a verification step.</li>"
    "<li>Uncertainty and sensitivity are outputs, not footnotes.</li>"
    "<li>Missing evidence narrows the claim, or blocks it.</li>"
    "</ul>",
    "<ul>"
    "<li>Herhangi bir ölçüme güvenilmeden önce CRS ve birimler açıkça belirtilir.</li>"
    "<li>Mekânsal sızıntı uç durum değil, varsayılan risktir.</li>"
    "<li>Her aşama bir doğrulama adımıyla biter.</li>"
    "<li>Belirsizlik ve duyarlılık dipnot değil, çıktıdır.</li>"
    "<li>Eksik kanıt iddiayı daraltır ya da engeller.</li>"
    "</ul>"))}

{shell.note(_("Scope", "Kapsam"),
  _("The published metrics describe <strong>routing behaviour</strong>: whether the right skill "
    "activates for the right request on Claude Code 2.1.214 with claude-sonnet-5, measured "
    "2026-08-05. They say nothing about the quality of the answers those skills then produce. The "
    "held-out split was already consumed by a prior run, which limits its power to confirm "
    "improvement.",
    "Yayımlanan metrikler <strong>yönlendirme davranışını</strong> tanımlar: doğru istek için doğru "
    "skill'in tetiklenip tetiklenmediğini, Claude Code 2.1.214 ve claude-sonnet-5 üzerinde, "
    "2026-08-05 tarihinde ölçülmüş. Bu skill'lerin ürettiği cevapların kalitesi hakkında hiçbir şey "
    "söylemezler. Ayrılmış küme önceki bir koşuda kullanılmıştı; bu da iyileşmeyi doğrulama gücünü "
    "sınırlar."))}
""")

    # ======================================================== 02 arcgis-mcp-bridge
    project_page(
        "arcgis-mcp-bridge",
        spec_rows=[
            (_("License", "Lisans"), "Apache-2.0"),
            (_("Package", "Paket"), "<code>pip install arcgis-mcp-bridge</code>"),
            (_("Tools", "Araçlar"), _("100 across 10 verticals", "10 dikeyde 100 araç")),
            (_("Requires", "Gereksinim"), _("Python 3.11+ · ArcGIS Pro 3.1–3.3 tested",
                                            "Python 3.11+ · ArcGIS Pro 3.1–3.3 test edildi")),
            (_("Platform", "Platform"), _("Windows, with a licensed ArcGIS Pro install",
                                          "Windows, lisanslı ArcGIS Pro kurulumuyla")),
            (_("Tests", "Testler"), _("86 offline, ArcPy mocked",
                                      "86 çevrimdışı test, ArcPy taklit edilmiş")),
        ],
        sections=f"""
{shell.prose(_("Why", "Neden"),
  _("Untrusted arguments, licensed runtime", "Güvenilmeyen argümanlar, lisanslı çalışma zamanı"),
  _("<p>An MCP tool call arrives as JSON from a language model. Handing that straight to ArcPy means "
    "letting generated text address the filesystem of a machine with a licensed ArcGIS Pro install "
    "on it. The interesting problem is not exposing geoprocessing; it is exposing it without "
    "turning the model into an unsandboxed local shell.</p>"
    "<p>The answer here is two processes that do not trust each other, with the same path "
    "validation implemented independently on both sides of the boundary.</p>",
    "<p>Bir MCP araç çağrısı, dil modelinden JSON olarak gelir. Bunu doğrudan ArcPy'ye vermek, "
    "üretilmiş metnin lisanslı ArcGIS Pro kurulu bir makinenin dosya sistemine erişmesine izin "
    "vermek demektir. İlginç olan sorun coğrafi işlemi açmak değil; modeli yalıtılmamış bir yerel "
    "kabuğa dönüştürmeden açmaktır.</p>"
    "<p>Buradaki cevap, birbirine güvenmeyen iki süreç ve sınırın her iki tarafında bağımsız olarak "
    "uygulanan aynı yol doğrulamasıdır.</p>"))}

{shell.figure(_("Fig. 01", "Şekil 01"),
  _("Two processes, one security floor", "İki süreç, tek güvenlik tabanı"),
  _("Layer A never imports ArcPy, so a crash or a hostile path never reaches the licensed runtime "
    "through the server process. PathGuard runs before dispatch and again inside the worker: a "
    "bypass requires defeating both.",
    "A Katmanı ArcPy'yi hiç içe aktarmaz; bu yüzden bir çökme ya da kötü niyetli bir yol, sunucu "
    "süreci üzerinden lisanslı çalışma zamanına asla ulaşmaz. PathGuard hem gönderimden önce hem de "
    "işçi sürecinin içinde çalışır: atlatmak için ikisini birden aşmak gerekir."),
  narrow(shell.plate(_("Fig. 01", "Şekil 01"),
                     _("Two-process architecture", "İki süreçli mimari"), svg("mcp.svg"))))}

<section class="fig">
{fighead(_("Catalog", "Katalog"), _("100 tools across ten verticals", "On dikeyde 100 araç"))}
  <p>{_("Every tool is declarative: a typed Pydantic v2 contract in, a structured NDJSON result "
        "frame out. Failures are values, not stack traces.",
        "Her araç bildirimseldir: girişte tipli bir Pydantic v2 sözleşmesi, çıkışta yapılandırılmış "
        "bir NDJSON sonuç çerçevesi. Hatalar yığın izi değil, değerdir.")}</p>
{catalog([
    (_("Geometry analysis", "Geometri analizi"), "23",
     _("Overlay, buffer, dissolve, proximity, topology-aware operations.",
       "Bindirme, tampon, birleştirme, yakınlık ve topoloji duyarlı işlemler.")),
    (_("Data management", "Veri yönetimi"), "22",
     _("Feature classes, fields, geodatabases, conversion, append.",
       "Öznitelik sınıfları, alanlar, coğrafi veritabanları, dönüşüm, ekleme.")),
    (_("Raster operations", "Raster işlemleri"), "15",
     _("Clip, mosaic, resample, project, extract by mask, zonal statistics.",
       "Kırpma, mozaik, yeniden örnekleme, projeksiyon, maskeyle çıkarma, bölgesel istatistik.")),
    (_("Map layer management", "Harita katmanı yönetimi"), "10",
     _("Add, order, symbolise, toggle and zoom layers in a project.",
       "Projede katman ekleme, sıralama, sembolleştirme, açma-kapama ve yakınlaştırma.")),
    (_("Export &amp; layout", "Dışa aktarma ve düzen"), "9",
     _("Layout PDF and PNG export, legend and text element updates.",
       "Düzenin PDF ve PNG dışa aktarımı, lejant ve metin ögesi güncellemeleri.")),
    (_("Editing &amp; topology", "Düzenleme ve topoloji"), "7",
     _("Repair geometry, eliminate parts, detect and check topology.",
       "Geometri onarma, parça eleme, topoloji saptama ve denetleme.")),
    (_("Spatial statistics", "Mekânsal istatistik"), "5",
     _("Hot spots, autocorrelation, mean centre, directional distribution.",
       "Sıcak noktalar, otokorelasyon, ortalama merkez, yönsel dağılım.")),
    (_("Network analysis", "Ağ analizi"), "4",
     _("Route, service area, closest facility, OD cost matrix.",
       "Rota, servis alanı, en yakın tesis, OD maliyet matrisi.")),
    (_("Coordinate &amp; projection", "Koordinat ve projeksiyon"), "4",
     _("Define, project, describe and validate spatial references.",
       "Mekânsal referansları tanımlama, dönüştürme, betimleme ve doğrulama.")),
    (_("Vision analytics", "Görüntü analitiği"), "1",
     _("Sketch-to-GIS: ORB + RANSAC registration with HSV segmentation.",
       "Krokiden CBS'ye: HSV segmentasyonuyla ORB + RANSAC çakıştırma.")),
])}
  <p class="fig-note">{_(
    "The vision tool turns a photographed hand-drawn parcel boundary into geodatabase features by "
    "registering the sketch against a reference frame, then segmenting the drawn lines in HSV space.",
    "Görüntü aracı, fotoğraflanmış el çizimi bir parsel sınırını, krokiyi bir referans çerçeveye "
    "çakıştırıp çizilen çizgileri HSV uzayında ayırarak coğrafi veritabanı nesnelerine dönüştürür.")}</p>
</section>

{shell.prose(_("Safety", "Güvenlik"),
  _("What PathGuard actually does", "PathGuard tam olarak ne yapar"),
  _("<p>Every path-bearing argument is normalised and checked against an allowed root before "
    "dispatch, then re-validated inside the worker that holds the licence. Destructive operations "
    "sit behind an explicit confirmation gate rather than a flag a model can set on its own.</p>"
    "<p>The 86-test suite runs with ArcPy mocked, so contributors without a Windows licence can "
    "still verify validation, security, licence handling and geoprocessing contracts offline.</p>",
    "<p>Yol içeren her argüman gönderimden önce normalleştirilir ve izin verilen kök dizine karşı "
    "denetlenir; ardından lisansı tutan işçi sürecinin içinde yeniden doğrulanır. Yıkıcı işlemler, "
    "modelin kendi başına ayarlayabileceği bir bayrağın değil, açık bir onay kapısının arkasındadır.</p>"
    "<p>86 testlik takım ArcPy taklit edilerek çalışır; böylece Windows lisansı olmayan katkıcılar "
    "da doğrulama, güvenlik, lisans işleme ve coğrafi işlem sözleşmelerini çevrimdışı "
    "sınayabilir.</p>"))}
""")

    # ======================================================== 03 sentinel-crop-pipeline
    project_page(
        "sentinel-crop-pipeline",
        spec_rows=[
            (_("License", "Lisans"), "Apache-2.0"),
            (_("Package", "Paket"), "<code>pip install sentinel-crop-pipeline</code>"),
            ("DOI", "10.5281/zenodo.21284444"),
            (_("Status", "Durum"), _("Beta research software", "Beta araştırma yazılımı")),
            (_("Source", "Kaynak"), _("Copernicus Data Space Ecosystem · Sentinel-2 L2A",
                                      "Copernicus Data Space Ecosystem · Sentinel-2 L2A")),
            (_("Bands", "Bantlar"), _("B02, B03, B04, B08 + derived MASK",
                                      "B02, B03, B04, B08 + türetilmiş MASK")),
            (_("Config", "Yapılandırma"), _("YAML, one file per run",
                                            "YAML, koşu başına tek dosya")),
        ],
        sections=f"""
{shell.prose(_("Why", "Neden"),
  _("The dataset is the experiment", "Veri setinin kendisi deneydir"),
  _("<p>Most of the reproducibility problem in remote-sensing machine learning sits upstream of the "
    "model. Which scenes were selected and why, how many pixels the cloud mask removed, whether two "
    "patches from the same field ended up on opposite sides of the split — these decisions "
    "determine the result, and they are usually undocumented.</p>"
    "<p>This pipeline treats them as first-class outputs. Every stage writes a timestamped JSON "
    "summary, and the patch manifest records the split assignment and invalid-pixel percentage of "
    "every patch.</p>",
    "<p>Uzaktan algılama makine öğrenmesindeki yeniden üretilebilirlik sorununun büyük kısmı modelin "
    "yukarısındadır. Hangi sahnelerin neden seçildiği, bulut maskesinin kaç pikseli çıkardığı, aynı "
    "tarladan iki yamanın ayrımın karşı taraflarına düşüp düşmediği — sonucu bu kararlar belirler "
    "ve genellikle belgelenmez.</p>"
    "<p>Bu hat onları birinci sınıf çıktı sayar. Her aşama zaman damgalı bir JSON özeti yazar; yama "
    "manifestosu her yamanın küme atamasını ve geçersiz piksel yüzdesini kaydeder.</p>"))}

{shell.figure(_("Fig. 01", "Şekil 01"),
  _("Five stages, each one auditable", "Beş aşama, her biri denetlenebilir"),
  _("Stages run individually or as <code>sentinel-crop run-all</code>. The illustrations show what "
    "each stage does to the data, not what it is called.",
    "Aşamalar tek tek ya da <code>sentinel-crop run-all</code> ile çalışır. Görseller her aşamanın "
    "adını değil, veriye ne yaptığını gösterir."),
  shell.plate(_("Fig. 01", "Şekil 01"),
              _("Sentinel-2 data lineage", "Sentinel-2 veri soy ağacı"), svg("sentinel.svg")))}

<section class="fig">
{fighead(_("Stages", "Aşamalar"), _("What each command produces", "Her komutun ürettiği"))}
{catalog([
    ("discover", "01", _("STAC search with deterministic scene selection; writes per-scene accept "
                         "and reject decisions.",
                         "Deterministik sahne seçimiyle STAC araması; sahne başına kabul ve ret "
                         "kararlarını yazar.")),
    ("download", "02", _("AOI-cropped retrieval through the CDSE Process API rather than whole tiles.",
                         "Tüm karolar yerine CDSE Process API üzerinden AOI'ye kırpılmış indirme.")),
    ("preprocess", "03", _("SCL masking, reflectance normalisation, NDVI / NDRE / NDWI where bands "
                           "allow.",
                           "SCL maskeleme, yansıma normalizasyonu, bantlar elverdiğinde NDVI / NDRE "
                           "/ NDWI.")),
    ("patch", "04", _("Fixed-size patches with spatially blocked train, validation and test "
                      "assignment.",
                      "Sabit boyutlu yamalar; mekânsal bloklu eğitim, doğrulama ve test ataması.")),
    ("label", "05", _("Rasterises externally prepared ground-truth polygons into uint8 masks.",
                      "Dışarıda hazırlanmış yer gerçeği poligonlarını uint8 maskelere rasterleştirir.")),
])}
  <p class="fig-note">{_(
    "Whole grid blocks are assigned to a single split, which reduces the spatial autocorrelation "
    "that makes random splits flatter the model.",
    "Izgara blokları bütün olarak tek bir kümeye atanır; bu da rastgele ayrımların modeli olduğundan "
    "iyi göstermesine yol açan mekânsal otokorelasyonu azaltır.")}</p>
</section>

{shell.prose(_("Outputs", "Çıktılar"),
  _("The audit trail is part of the deliverable", "Denetim izi teslimatın parçasıdır"),
  _("<ul>"
    "<li><code>logs/run_&lt;stage&gt;_&lt;timestamp&gt;.json</code> — per-stage summaries.</li>"
    "<li><code>logs/selection_results.json</code> — why each scene was kept or dropped.</li>"
    "<li><code>data/patches/index.csv</code> — the patch manifest: split, paths, invalid percentage.</li>"
    "<li><code>data/patches/cog/</code> — georeferenced GeoTIFFs you can open and look at.</li>"
    "<li>Training exports as COG/TIFF, NPY, and optional TFRecord.</li>"
    "</ul>"
    "<p>A validated live run over an Urla area of interest produced 990 training patches from 9 "
    "Sentinel-2 L2A scenes in June 2025.</p>",
    "<ul>"
    "<li><code>logs/run_&lt;asama&gt;_&lt;zaman&gt;.json</code> — aşama başına özetler.</li>"
    "<li><code>logs/selection_results.json</code> — her sahnenin neden tutulduğu ya da elendiği.</li>"
    "<li><code>data/patches/index.csv</code> — yama manifestosu: küme, yollar, geçersiz yüzdesi.</li>"
    "<li><code>data/patches/cog/</code> — açıp bakabileceğiniz coğrafi referanslı GeoTIFF'ler.</li>"
    "<li>Eğitim çıktıları COG/TIFF, NPY ve isteğe bağlı TFRecord olarak.</li>"
    "</ul>"
    "<p>Urla çalışma alanı üzerinde doğrulanmış bir canlı koşu, Haziran 2025'te 9 Sentinel-2 L2A "
    "sahnesinden 990 eğitim yaması üretti.</p>"))}

{shell.note(_("Limitations", "Sınırlar"),
  _("The interim Urla AOI is a rectangle, not an official boundary. Spatial blocks reduce leakage "
    "but do not eliminate it where fields cross block edges. The label stage requires externally "
    "prepared ground-truth polygons; nothing is downloaded automatically. And the pipeline prepares "
    "data — <strong>it makes no claim about downstream model accuracy</strong>.",
    "Geçici Urla çalışma alanı resmî bir sınır değil, bir dikdörtgendir. Mekânsal bloklar sızıntıyı "
    "azaltır ama tarlaların blok kenarlarını aştığı yerlerde tamamen ortadan kaldırmaz. Etiketleme "
    "aşaması dışarıda hazırlanmış yer gerçeği poligonları gerektirir; hiçbir şey otomatik indirilmez. "
    "Ve bu hat veriyi hazırlar — <strong>aşağı akıştaki model doğruluğu hakkında bir iddiada "
    "bulunmaz</strong>."))}
""")

    # ======================================================== 04 agri-dss
    project_page(
        "agri-dss",
        spec_rows=[
            (_("License", "Lisans"), "Apache-2.0"),
            (_("Live", "Canlı"), "tarimsalkoridor.online"),
            (_("Coverage", "Kapsam"), _("5 districts · 147 neighbourhoods",
                                        "5 ilçe · 147 mahalle")),
            (_("Districts", "İlçeler"), "Demre, Finike, Kaş, Kemer, Kumluca"),
            (_("Stack", "Yığın"), _("Vanilla JavaScript, HTML, CSS",
                                    "Saf JavaScript, HTML, CSS")),
            (_("Backend", "Sunucu"), _("None — static deployment, local persistence",
                                       "Yok — statik dağıtım, yerel saklama")),
        ],
        sections=f"""
{shell.prose(_("Why", "Neden"),
  _("A recommendation someone can act on", "Üzerine iş yapılabilecek bir öneri"),
  _("<p>Regional agricultural analysis usually ends as a PDF nobody in the field reads. This system "
    "ends as a single A4 sheet a cooperative can pin to a village board: pick a district, pick a "
    "neighbourhood, get ranked crop recommendations with the reasoning attached.</p>"
    "<p>It weights soil and climate suitability together with expected market prices, because a "
    "crop that grows well and sells badly is still the wrong answer.</p>",
    "<p>Bölgesel tarım analizi genellikle sahada kimsenin okumadığı bir PDF olarak biter. Bu sistem, "
    "bir kooperatifin köy panosuna asabileceği tek bir A4 sayfayla biter: ilçeyi seç, mahalleyi seç, "
    "gerekçesiyle birlikte sıralanmış ürün önerilerini al.</p>"
    "<p>Toprak ve iklim uygunluğunu beklenen piyasa fiyatlarıyla birlikte ağırlıklandırır; çünkü iyi "
    "yetişip kötü satan bir ürün yine de yanlış cevaptır.</p>"))}

{shell.figure(_("Fig. 01", "Şekil 01"),
  _("From regional data to a printable plan", "Bölgesel veriden yazdırılabilir plana"),
  _("The scoring is schema-driven and every input is traceable, so a recommendation can be argued "
    "with rather than merely accepted. There is no server-side black box: the whole chain runs in "
    "the browser.",
    "Puanlama şema güdümlüdür ve her girdi izlenebilirdir; böylece bir öneri sadece kabul edilmek "
    "yerine tartışılabilir. Sunucu tarafında kara kutu yok: tüm zincir tarayıcıda çalışır."),
  narrow(shell.plate(_("Fig. 01", "Şekil 01"),
                     _("Auditable decision chain", "Denetlenebilir karar zinciri"), svg("agri.svg"))))}

<section class="fig">
{fighead(_("Coverage", "Kapsam"), _("The Western Antalya corridor", "Batı Antalya koridoru"))}
{catalog([
    (_("Neighbourhoods", "Mahalle"), "147",
     _("Each one resolves to its own ranked recommendation set.",
       "Her biri kendi sıralı öneri kümesine çözümlenir.")),
    (_("Districts", "İlçe"), "5", _("Demre, Finike, Kaş, Kemer and Kumluca.",
                                    "Demre, Finike, Kaş, Kemer ve Kumluca.")),
    (_("Recommendation types", "Öneri türü"), "3",
     _("Seasonal crops, long-term orchard investment, emerging market openings.",
       "Mevsimlik ürünler, uzun vadeli bahçe yatırımı, gelişen pazar fırsatları.")),
    (_("Output", "Çıktı"), "A4", _("One printable typographic sheet per neighbourhood.",
                                   "Mahalle başına yazdırılabilir tek tipografik sayfa.")),
])}
  <p class="fig-note">{_(
    "Crops covered include tomato, pepper, lettuce, avocado, olive, pomegranate, almond and the "
    "Finike orange.",
    "Kapsanan ürünler arasında domates, biber, marul, avokado, zeytin, nar, badem ve Finike "
    "portakalı bulunuyor.")}</p>
</section>

{shell.note(_("Data status", "Veri durumu"),
  _("The current dataset is <strong>conceptual</strong>, derived from regional economy, "
    "environment, land-use and climate reports. It demonstrates the system's logic and interface. A "
    "production deployment would need to be backed by real soil, climate and market data feeds "
    "before any of its recommendations should drive a planting decision.",
    "Mevcut veri seti <strong>kavramsaldır</strong>; bölgesel ekonomi, çevre, arazi kullanımı ve "
    "iklim raporlarından türetilmiştir. Sistemin mantığını ve arayüzünü gösterir. Önerilerinden "
    "herhangi biri bir ekim kararını yönlendirmeden önce, üretim dağıtımının gerçek toprak, iklim ve "
    "piyasa veri akışlarıyla desteklenmesi gerekir."), warn=True)}
""")

    # ======================================================== 05 FOUNDER.EXE
    project_page(
        "founder-exe",
        spec_rows=[
            (_("Platform", "Platform"), "Windows x64"),
            (_("Price", "Fiyat"), _("$4.99 USD or more", "4,99 USD ve üzeri")),
            (_("Status", "Durum"), _("In development · updated 2026-07-30",
                                     "Geliştiriliyor · güncelleme 2026-07-30")),
            (_("Languages", "Diller"), _("English and Turkish", "İngilizce ve Türkçe")),
            (_("Genre", "Tür"), _("Simulation · Educational · Strategy",
                                  "Simülasyon · Eğitici · Strateji")),
            (_("Regimes", "Rejimler"), _("Türkiye and USA, modelled separately",
                                         "Türkiye ve ABD, ayrı ayrı modellenmiş")),
        ],
        sections=f"""
{shell.prose(_("Why", "Neden"),
  _("Rules are more interesting than resources", "Kurallar kaynaklardan daha ilginçtir"),
  _("<p>Most business simulations model money and ignore institutions. The part that actually kills "
    "early companies — a tax deadline you did not diary, a company structure that blocks the "
    "financing you need, a hire that looks affordable until payroll lands — never appears.</p>"
    "<p>FOUNDER.EXE encodes two real regulatory regimes as separate rule sets, so the same strategy "
    "produces different outcomes in Türkiye and the USA. The lesson is the divergence, not the "
    "score.</p>",
    "<p>İş simülasyonlarının çoğu parayı modelleyip kurumları görmezden gelir. Erken aşama "
    "şirketleri asıl öldüren kısım — ajandaya yazmadığınız bir vergi son tarihi, ihtiyacınız olan "
    "finansmanı engelleyen bir şirket yapısı, bordro gelene kadar uygun fiyatlı görünen bir işe alım "
    "— hiç görünmez.</p>"
    "<p>FOUNDER.EXE iki gerçek düzenleyici rejimi ayrı kural kümeleri olarak kodlar; böylece aynı "
    "strateji Türkiye'de ve ABD'de farklı sonuçlar verir. Ders, skor değil, bu ayrışmadır.</p>"))}

{shell.figure(_("Fig. 01", "Şekil 01"),
  _("One monthly tick, four coupled dimensions", "Tek aylık tur, dört bağlı boyut"),
  _("Cash, compliance, product and people are not independent bars to fill. Hiring shortens runway, "
    "shipping fast accrues technical debt, and a financing round dilutes the cap table you will care "
    "about later.",
    "Nakit, uyum, ürün ve insan doldurulacak bağımsız çubuklar değildir. İşe alım pisti kısaltır, "
    "hızlı yayınlamak teknik borç biriktirir ve bir finansman turu, sonra önemseyeceğiniz pay "
    "tablosunu seyreltir."),
  shell.plate(_("Fig. 01", "Şekil 01"),
              _("Rule-driven operating model", "Kural güdümlü işletme modeli"), svg("founder.svg")))}

<section class="fig">
{fighead(_("Systems", "Sistemler"), _("What is in the build", "Yapıda neler var"))}
{catalog([
    (_("Academy modules", "Akademi modülü"), "26",
     _("Structured lessons with career certification, playable outside a run.",
       "Kariyer sertifikasyonlu yapılandırılmış dersler; bir koşunun dışında da oynanabilir.")),
    (_("Decision scenarios", "Karar senaryosu"), "5",
     _("Standalone situations you can attempt without a full campaign.",
       "Tam bir kampanya olmadan deneyebileceğiniz bağımsız durumlar.")),
    (_("Jurisdictions", "Yargı bölgesi"), "2",
     _("Türkiye and USA, with separate institutions and company structures.",
       "Türkiye ve ABD; ayrı kurumlar ve şirket yapılarıyla.")),
    (_("Interface", "Arayüz"), "OS",
     _("Founder OS: a desktop metaphor rather than a menu stack.",
       "Founder OS: menü yığını yerine bir masaüstü metaforu.")),
])}
  <p class="fig-note">{_(
    "Also included: live market data, an optional AI assistant, leaderboards, local saves with "
    "export and import, and accessibility modes covering high contrast and colour-blind palettes.",
    "Ayrıca: canlı piyasa verisi, isteğe bağlı yapay zekâ asistanı, liderlik tabloları, dışa/içe "
    "aktarmalı yerel kayıtlar ve yüksek kontrast ile renk körü paletlerini kapsayan erişilebilirlik "
    "kipleri.")}</p>
</section>

{shell.prose(_("Design note", "Tasarım notu"),
  _("Delayed consequence as the core mechanic", "Çekirdek mekanik: gecikmeli sonuç"),
  _("<p>The simulation is built around actions whose cost arrives late. Growth can hide a weak "
    "product for several months before churn makes it visible; shipping past a quality threshold "
    "builds technical debt that only bites when the team scales. A run that looks healthy on the "
    "dashboard can already be lost.</p>",
    "<p>Simülasyon, bedeli geç gelen eylemler üzerine kurulu. Büyüme, kayıp oranı görünür hale "
    "gelene kadar zayıf bir ürünü aylarca gizleyebilir; kalite eşiğini aşarak yayınlamak, ancak ekip "
    "büyüdüğünde ısıran bir teknik borç biriktirir. Gösterge panelinde sağlıklı görünen bir koşu "
    "çoktan kaybedilmiş olabilir.</p>"))}
""")

    # ======================================================== research
    agri_note = shell.note(
        _("Status", "Durum"),
        _("Segmentation work sits downstream of "
          "<a href='projects/sentinel-crop-pipeline.html' style='text-decoration:underline'>"
          "sentinel-crop-pipeline</a>, which supplies the spatially blocked patches and aligned "
          "label masks. The repository is not yet populated, so there are no published metrics or "
          "trained weights to report here.",
          "Segmentasyon çalışması, mekânsal bloklu yamaları ve hizalanmış etiket maskelerini sağlayan "
          "<a href='projects/sentinel-crop-pipeline.html' style='text-decoration:underline'>"
          "sentinel-crop-pipeline</a>'ın aşağı akışında yer alır. Depo henüz doldurulmadığı için "
          "burada raporlanacak yayımlanmış metrik veya eğitilmiş ağırlık yok."))

    research_body = f"""<main id="main">

<div class="wrap">
  <nav class="crumb mono" aria-label="{shell.u('crumb_aria')}">
    <a href="index.html">{shell.u('home')}</a><span>/</span><span>{_("Research", "Araştırma")}</span>
  </nav>
</div>

<header class="phead">
  <div class="wrap phead-grid">
    <div>
      <span class="kind mono rv">{_("Academic &amp; research", "Akademik çalışma ve araştırma")}</span>
      <h1 class="rv" style="--d:60ms">{_("Research", "Araştırma")}</h1>
      <p class="deck rv" style="--d:120ms">{_(
        "Studies spanning spatial econometrics, composite territorial indicators and remote-sensing "
        "segmentation — with the methods and the limits stated in the same breath.",
        "Mekânsal ekonometri, bileşik bölgesel göstergeler ve uzaktan algılama segmentasyonunu "
        "kapsayan çalışmalar — yöntem ve sınırlar aynı nefeste belirtilmiş.")}</p>
    </div>
    <div class="phead-side rv" style="--d:160ms">
      <div class="spec">
        <div><span class="k">{_("Studies", "Çalışma")}</span><span class="v">3</span></div>
        <div><span class="k">{_("Reproducibility", "Yeniden üretilebilirlik")}</span><span class="v">{_(
          "Notebooks, figures and data provenance published",
          "Not defterleri, şekiller ve veri kaynağı yayımlanmış")}</span></div>
        <div><span class="k">{_("Stance", "Duruş")}</span><span class="v">{_(
          "Descriptive unless a design supports more",
          "Tasarım fazlasını desteklemedikçe betimleyici")}</span></div>
      </div>
    </div>
  </div>
</header>

<div class="wrap">

<section class="fig">
{fighead("R / 01", "turkiye-housing-prices-pandemic")}
  <p>{_("A reproducible, region-level analysis separating real inflation-adjusted house price growth "
        "from inflation itself, across 150 months of Türkiye's housing market.",
        "Türkiye konut piyasasının 150 ayı boyunca, enflasyondan arındırılmış reel konut fiyatı "
        "büyümesini enflasyonun kendisinden ayıran, bölge düzeyinde yeniden üretilebilir bir "
        "analiz.")}</p>
{catalog([
    (_("Period", "Dönem"), "150", _("Months, November 2013 to April 2026.",
                                    "Ay, Kasım 2013'ten Nisan 2026'ya.")),
    (_("Pre-pandemic", "Pandemi öncesi"), "−2%",
     _("Real growth 2014–2019, against +84% nominal.",
       "2014–2019 reel büyüme; nominal +%84'e karşılık.")),
    (_("Post-pandemic", "Pandemi sonrası"), "+106%",
     _("Real growth 2020–2025, against +1521% nominal.",
       "2020–2025 reel büyüme; nominal +%1521'e karşılık.")),
    (_("Regional spread", "Bölgesel açıklık"), "141%",
     _("Ankara's real growth, against İstanbul's 91%.",
       "Ankara'nın reel büyümesi; İstanbul'un %91'ine karşılık.")),
])}
  <p class="fig-note">{_(
    "Method: real index construction from the TCMB residential property price index deflated by "
    "headline CPI, with CAGR, Fisher identity validation and alternative deflator comparison. "
    "Spatial structure tested with global Moran's I and LISA. Data from TCMB EVDS and TÜİK; province "
    "boundaries derived from OpenStreetMap.",
    "Yöntem: TCMB konut fiyat endeksinin manşet TÜFE ile deflate edilerek reel endekse çevrilmesi; "
    "YBBO, Fisher özdeşliği doğrulaması ve alternatif deflatör karşılaştırması. Mekânsal yapı global "
    "Moran's I ve LISA ile sınandı. Veriler TCMB EVDS ve TÜİK'ten; il sınırları OpenStreetMap'ten "
    "türetildi.")}</p>
{shell.note(_("Limitations", "Sınırlar"),
  _("Maps are simplified rather than cartometric. LISA has limited power at 19 spatial units. The "
    "analysis is <strong>descriptive, not causal</strong>, and no multiple-comparison correction is "
    "applied.",
    "Haritalar kartometrik değil, basitleştirilmiştir. 19 mekânsal birimde LISA'nın gücü sınırlıdır. "
    "Analiz <strong>betimleyicidir, nedensel değildir</strong> ve çoklu karşılaştırma düzeltmesi "
    "uygulanmamıştır."))}
  <div class="plinks">{shell.btn("https://github.com/muend/turkiye-housing-prices-pandemic", _("Repository", "Depo"), "solid")}</div>
</section>

<section class="fig">
{fighead("R / 02", "kutri-resilience-index")}
  <p>{_("The Kaş Urban-Territorial Resilience Index: a reproducible five-pillar composite indicator "
        "prototype for the Kaş/Bayındır planning area in Antalya.",
        "Kaş Kentsel-Bölgesel Dayanıklılık Endeksi: Antalya Kaş/Bayındır planlama alanı için beş "
        "sütunlu, yeniden üretilebilir bir bileşik gösterge prototipi.")}</p>
{catalog([
    (_("Indicators", "Gösterge"), "40", _("Distributed 7 / 7 / 8 / 10 / 8 across the five pillars.",
                                          "Beş sütuna 7 / 7 / 8 / 10 / 8 olarak dağıtılmış.")),
    (_("Pillars", "Sütun"), "5",
     _("Hazard, socio-demographic, economic, infrastructure, environmental-cultural.",
       "Afet, sosyo-demografik, ekonomik, altyapı, çevresel-kültürel.")),
    (_("Normalisation", "Normalizasyon"), "0–1",
     _("Directional logic per indicator, positive or negative.",
       "Gösterge başına yönlü mantık: pozitif ya da negatif.")),
    (_("Aggregation", "Toplulaştırma"), "AHP",
     _("Arithmetic mean within pillars, weighted geometric mean across them.",
       "Sütun içinde aritmetik ortalama, sütunlar arasında ağırlıklı geometrik ortalama.")),
])}
  <p class="fig-note">{_(
    "Pillars: Natural Hazard &amp; Physical Vulnerability; Socio-Demographic Adaptive Capacity; "
    "Economic Resilience; Infrastructure &amp; Service Continuity; Environmental &amp; Cultural "
    "Capital. Weights come from an Analytic Hierarchy Process eigenvector, with nominal policy "
    "weights tested as an alternative. MIT licence covers the source; raw data is not redistributed.",
    "Sütunlar: Doğal Afet ve Fiziksel Kırılganlık; Sosyo-Demografik Uyum Kapasitesi; Ekonomik "
    "Dayanıklılık; Altyapı ve Hizmet Sürekliliği; Çevresel ve Kültürel Sermaye. Ağırlıklar Analitik "
    "Hiyerarşi Süreci özvektöründen gelir; alternatif olarak nominal politika ağırlıkları sınanmıştır. "
    "MIT lisansı kaynağı kapsar; ham veri yeniden dağıtılmaz.")}</p>
{shell.note(_("Limitations", "Sınırlar"),
  _("Explicitly <strong>not a universal or fully validated resilience model</strong>. It is a "
    "case-specific evidence base for planning decisions in one district.",
    "Açıkça <strong>evrensel ya da tam doğrulanmış bir dayanıklılık modeli değildir</strong>. Tek bir "
    "ilçedeki planlama kararları için vakaya özgü bir kanıt tabanıdır."))}
  <div class="plinks">{shell.btn("https://github.com/muend/kutri-resilience-index", _("Repository", "Depo"), "solid")}</div>
</section>

<section class="fig">
{fighead("R / 03", "agri-unet")}
  <p>{_("Downstream agricultural pattern identification from satellite imagery, kept separate from "
        "the reusable data-preparation layer so that experiments stay auditable and the dataset work "
        "can be cited on its own.",
        "Uydu görüntülerinden aşağı akış tarımsal örüntü tanıma; deneylerin denetlenebilir kalması ve "
        "veri seti çalışmasının kendi başına atıf alabilmesi için yeniden kullanılabilir veri hazırlık "
        "katmanından ayrı tutulmuştur.")}</p>
{agri_note}
</section>

</div>
"""
    out_path("research.html").write_text(
        shell.head(
            _("Research — spatial econometrics, resilience indicators, remote sensing",
              "Araştırma — mekânsal ekonometri, dayanıklılık göstergeleri, uzaktan algılama"),
            _("Reproducible studies on Türkiye housing prices, urban-territorial resilience "
              "indicators and agricultural segmentation, with methods and limitations stated.",
              "Türkiye konut fiyatları, kentsel-bölgesel dayanıklılık göstergeleri ve tarımsal "
              "segmentasyon üzerine, yöntem ve sınırları belirtilmiş yeniden üretilebilir çalışmalar."),
            "research", "research.html")
        + research_body + shell.footer("research.html", contact=False),
        encoding="utf-8")

    # ======================================================== practice
    steps = [
        (_("Phase 01", "Aşama 01"), _("Define invariants", "Değişmezleri tanımla"),
         _("Make CRS, units, data contracts, safety boundaries and success criteria explicit before "
           "implementation.",
           "CRS'i, birimleri, veri sözleşmelerini, güvenlik sınırlarını ve başarı ölçütlerini "
           "uygulamadan önce açıkça belirle.")),
        (_("Phase 02", "Aşama 02"), _("Build the pipeline", "Hattı kur"),
         _("Separate components, isolate risky runtimes, preserve provenance, and make intermediate "
           "states inspectable.",
           "Bileşenleri ayır, riskli çalışma zamanlarını yalıt, kaynağı koru ve ara durumları "
           "incelenebilir yap.")),
        (_("Phase 03", "Aşama 03"), _("Stress the failure modes", "Hata kiplerini zorla"),
         _("Test negative cases, leakage, invalid paths, ambiguous routing, missing data and "
           "operational boundaries.",
           "Negatif vakaları, sızıntıyı, geçersiz yolları, belirsiz yönlendirmeyi, eksik veriyi ve "
           "operasyonel sınırları sına.")),
        (_("Phase 04", "Aşama 04"), _("Ship a usable artifact", "Kullanılabilir bir çıktı teslim et"),
         _("Deliver a package, live interface, citable release, benchmark, print output or "
           "deployment-ready system.",
           "Bir paket, canlı arayüz, atıf verilebilir sürüm, kıyaslama, baskı çıktısı ya da dağıtıma "
           "hazır sistem teslim et.")),
    ]
    steps_html = "\n    ".join(
        f'<article class="mstep" style="--d:{i*180}ms"><span class="phase mono">{ph}</span>'
        f'<h3>{h}</h3><p>{b}</p></article>' for i, (ph, h, b) in enumerate(steps))

    principles = [
        (_("01 / Spatial rigor", "01 / Mekânsal titizlik"),
         _("CRS and units are explicit", "CRS ve birimler açıktır"),
         _("Area, distance, raster alignment, scale and geometry assumptions are checked before "
           "methods are trusted.",
           "Alan, mesafe, raster hizalaması, ölçek ve geometri varsayımları, yöntemlere güvenilmeden "
           "önce denetlenir.")),
        (_("02 / Honest validation", "02 / Dürüst doğrulama"),
         _("Leakage is treated as a risk", "Sızıntı bir risk olarak ele alınır"),
         _("Spatially dependent data requires blocked splits, appropriate baselines and validation "
           "designs that reflect deployment.",
           "Mekânsal bağımlı veri; bloklu ayrımlar, uygun temel çizgiler ve dağıtımı yansıtan "
           "doğrulama tasarımları gerektirir.")),
        (_("03 / Reproducibility", "03 / Yeniden üretilebilirlik"),
         _("Evidence is versioned", "Kanıt sürümlenir"),
         _("Typed contracts, CI, immutable benchmark packages, test harnesses and DOI-backed "
           "releases keep work reviewable.",
           "Tipli sözleşmeler, CI, değişmez kıyaslama paketleri, test koşumları ve DOI destekli "
           "sürümler işi incelenebilir tutar.")),
        (_("04 / Product utility", "04 / Ürün faydası"),
         _("Methods become usable systems", "Yöntemler kullanılabilir sistemlere dönüşür"),
         _("Analysis is translated into interfaces, reports, local automation or playable "
           "simulations rather than left as notebooks.",
           "Analiz, not defteri olarak bırakılmak yerine arayüzlere, raporlara, yerel otomasyona ya "
           "da oynanabilir simülasyonlara çevrilir.")),
    ]
    principles_html = "\n    ".join(
        f'<article class="principle rv" style="--d:{i*80}ms"><span class="n mono">{n}</span>'
        f'<h3>{h}</h3><p>{b}</p></article>' for i, (n, h, b) in enumerate(principles))

    panels = [
        ("spatial", _("Spatial / EO", "Mekânsal / EO"), "10",
         _("Spatial / remote sensing", "Mekânsal / uzaktan algılama"),
         _("Geospatial methods with operational discipline.",
           "Operasyonel disiplinle mekânsal yöntemler."),
         _("Vector, raster, EO, spatial statistics, cartography and proprietary GIS workflows "
           "handled with explicit projections, scale, validation and output checks.",
           "Vektör, raster, EO, mekânsal istatistik, kartografya ve tescilli CBS iş akışları; açık "
           "projeksiyon, ölçek, doğrulama ve çıktı denetimleriyle ele alınır."),
         [(_("Primary domain", "Ana alan"), "GeoAI"),
          (_("Core failure mode", "Temel hata kipi"), _("Silent spatial error", "Sessiz mekânsal hata")),
          (_("Delivery", "Teslimat"), _("Package · map · DSS", "Paket · harita · KDS"))],
         ["GeoPandas", "Shapely", "ArcPy", "Rasterio", "PySAL", "QGIS", "Sentinel-2", "CDSE",
          "STAC", "PostGIS"]),
        ("agents", _("Agents / Eval", "Ajanlar / Değerlendirme"), "08",
         _("Agents / evaluation", "Ajanlar / değerlendirme"),
         _("Tool-using agents that route, execute and fail safely.",
           "Yönlendiren, yürüten ve güvenle hata veren araç kullanan ajanlar."),
         _("Agent Skills, MCP, runtime isolation, typed evaluation contracts, blind request "
           "preparation, deterministic scoring and evidence-aware benchmark publication.",
           "Agent Skills, MCP, çalışma zamanı yalıtımı, tipli değerlendirme sözleşmeleri, kör istek "
           "hazırlığı, deterministik puanlama ve kanıt bilinçli kıyaslama yayını."),
         [(_("Primary domain", "Ana alan"), _("Agentic GIS", "Ajan tabanlı CBS")),
          (_("Core failure mode", "Temel hata kipi"),
           _("Unsafe or wrong routing", "Güvensiz ya da yanlış yönlendirme")),
          (_("Delivery", "Teslimat"), _("Plugin · MCP · benchmark", "Eklenti · MCP · kıyaslama"))],
         ["Agent Skills", "MCP", "JSON-RPC", "JSON Schema", "Routing evals", "Behavior evals",
          "Guarded execution", "Benchmark harnesses"]),
        ("ml", _("AI / ML", "YZ / ML"), "07",
         _("AI / ML / data", "YZ / ML / veri"),
         _("Models built on defensible data and evaluation.",
           "Savunulabilir veri ve değerlendirme üzerine kurulu modeller."),
         _("Deep-learning and classical ML workflows with spatial splitting, class-imbalance "
           "handling, reproducible preprocessing and georeferencing-preserving inference.",
           "Mekânsal ayrım, sınıf dengesizliği yönetimi, yeniden üretilebilir ön işleme ve coğrafi "
           "referansı koruyan çıkarımla derin öğrenme ve klasik ML iş akışları."),
         [(_("Primary domain", "Ana alan"), _("Spatial ML", "Mekânsal ML")),
          (_("Core failure mode", "Temel hata kipi"),
           _("Leakage / false confidence", "Sızıntı / yanlış güven")),
          (_("Delivery", "Teslimat"), _("Dataset · model · report", "Veri seti · model · rapor"))],
         ["Python", "PyTorch", "TensorFlow", "scikit-learn", "NumPy", "pandas", "SciPy"]),
        ("systems", _("Systems / Product", "Sistemler / Ürün"), "10",
         _("Systems / product", "Sistemler / ürün"),
         _("Research logic translated into software people can operate.",
           "Araştırma mantığının, insanların çalıştırabileceği yazılıma çevrilmesi."),
         _("Typed Python services, static web products, CI, testing, distribution, browser-native "
           "interfaces, local persistence and low-maintenance deployment architectures.",
           "Tipli Python servisleri, statik web ürünleri, CI, test, dağıtım, tarayıcı yerlisi "
           "arayüzler, yerel saklama ve düşük bakımlı dağıtım mimarileri."),
         [(_("Primary domain", "Ana alan"), _("Product engineering", "Ürün mühendisliği")),
          (_("Core failure mode", "Temel hata kipi"),
           _("Unmaintainable delivery", "Sürdürülemez teslimat")),
          (_("Delivery", "Teslimat"), _("PyPI · web · game", "PyPI · web · oyun"))],
         ["FastAPI", "Pydantic v2", "Docker", "Pytest", "Ruff", "Mypy", "GitHub Actions",
          "Vanilla JS", "HTML/CSS", "Web storage"]),
    ]
    tabs_html = "\n      ".join(
        f'<button class="cap-tab mono" role="tab" id="tab-{k}" aria-controls="panel-{k}" '
        f'aria-selected="{"true" if i == 0 else "false"}"'
        f'{"" if i == 0 else " tabindex=-1"} data-panel="{k}">'
        f'<span>{label}</span><span class="c">{cnt}</span></button>'
        for i, (k, label, cnt, *_rest) in enumerate(panels))
    panels_html = "\n      ".join(
        f'<article class="cap-panel" role="tabpanel" id="panel-{k}" aria-labelledby="tab-{k}" '
        f'tabindex="0"{"" if i == 0 else " hidden"}>\n'
        f'        <div>\n'
        f'          <span class="mono field">{field}</span>\n'
        f'          <h3>{h}</h3>\n'
        f'          <p>{body}</p>\n'
        f'          <div class="cap-proof">'
        + "".join(f'<div><span>{a}</span><strong>{b}</strong></div>' for a, b in proof)
        + f'</div>\n        </div>\n'
        f'        <div class="chip-box">\n'
        f'          <span class="mono">{_("Working set", "Çalışma kümesi")}<span>{cnt}</span></span>\n'
        f'          <div class="chips">' + "".join(f'<span>{c}</span>' for c in chips)
        + '</div>\n        </div>\n      </article>'
        for i, (k, _label, cnt, field, h, body, proof, chips) in enumerate(panels))

    practice_body = f"""<main id="main">

<div class="wrap">
  <nav class="crumb mono" aria-label="{shell.u('crumb_aria')}">
    <a href="index.html">{shell.u('home')}</a><span>/</span><span>{_("Practice", "Yöntem")}</span>
  </nav>
</div>

<header class="phead">
  <div class="wrap phead-grid">
    <div>
      <span class="kind mono rv">{_("How I build", "Nasıl inşa ediyorum")}</span>
      <h1 class="rv" style="--d:60ms">{_("Practice", "Yöntem")}</h1>
      <p class="deck rv" style="--d:120ms">{_(
        "The same sequence governs infrastructure, research software, decision systems and "
        "simulations. It is ordered so that the expensive mistakes are made cheap.",
        "Aynı sıra altyapıyı, araştırma yazılımını, karar sistemlerini ve simülasyonları yönetir. "
        "Sıralama, pahalı hataların ucuza yapılabilmesi için böyle kurulmuştur.")}</p>
    </div>
    <div class="phead-side rv" style="--d:160ms">
      <div class="spec">
        <div><span class="k">{_("Stages", "Aşama")}</span><span class="v">{_("Four, always in order", "Dört, her zaman sırayla")}</span></div>
        <div><span class="k">{_("Primary domain", "Ana alan")}</span><span class="v">{_("GeoAI and spatial data science", "GeoAI ve mekânsal veri bilimi")}</span></div>
        <div><span class="k">{_("Failure mode", "Hata kipi")}</span><span class="v">{_("Silent spatial error", "Sessiz mekânsal hata")}</span></div>
      </div>
    </div>
  </div>
</header>

<div class="wrap">

<section class="page-sec">
  <div class="method-track" data-track>
    {steps_html}
  </div>
</section>

<section class="fig">
{fighead(_("Principles", "İlkeler"), _("What that sequence is protecting against",
                                       "Bu sıra neye karşı koruyor"))}
  <div class="principles">
    {principles_html}
  </div>
</section>

<section class="fig">
{fighead(_("Stack", "Yığın"), _("Technical core", "Teknik çekirdek"))}
  <p>{_("A spatial-first stack spanning research methods, agent infrastructure, production "
        "engineering and browser-native product work.",
        "Araştırma yöntemleri, ajan altyapısı, üretim mühendisliği ve tarayıcı yerlisi ürün işini "
        "kapsayan, mekân öncelikli bir yığın.")}</p>
  <div class="cap rv">
    <div class="cap-nav" role="tablist" aria-label="{_("Technical capability categories", "Teknik yetkinlik kategorileri")}">
      {tabs_html}
      <div class="cap-fill" aria-hidden="true"></div>
    </div>
    <div class="cap-panels">
      {panels_html}
    </div>
  </div>
</section>

{shell.figure(_("Fig. 01", "Şekil 01"),
  _("How the projects feed each other", "Projeler birbirini nasıl besliyor"),
  _("The work compounds: methods inform infrastructure, infrastructure enables execution, and both "
    "feed products that can be used outside a research notebook.",
    "İş birikimlidir: yöntemler altyapıyı biçimlendirir, altyapı yürütmeyi mümkün kılar ve ikisi de "
    "bir araştırma not defterinin dışında kullanılabilen ürünleri besler."),
  shell.plate(_("Fig. 01", "Şekil 01"), _("System atlas", "Sistem atlası"), svg("map.svg")))}

</div>
"""
    out_path("practice.html").write_text(
        shell.head(_("Practice — how I build spatial systems",
                     "Yöntem — mekânsal sistemleri nasıl inşa ediyorum"),
                   _("A four-stage method for building GeoAI infrastructure, research software and "
                     "decision systems, plus the full capability matrix and system map.",
                     "GeoAI altyapısı, araştırma yazılımı ve karar sistemleri kurmak için dört "
                     "aşamalı bir yöntem; ayrıca tam yetkinlik matrisi ve sistem haritası."),
                   "practice", "practice.html")
        + practice_body + shell.footer("practice.html", contact=False),
        encoding="utf-8")
