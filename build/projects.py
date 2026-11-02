"""Bilingual project registry. Facts verified on 2026-11-02."""

PROJECTS = [{'slug': 'eatbetter',
  'no': '00',
  'name': 'EatBetter',
  'kind': ('Client work · LLM evaluation and data quality',
           'Müşteri işi · LLM değerlendirme ve veri kalitesi'),
  'blurb': ('Contract AI engineering on a nutrition app: a measurement platform, a cleaned food '
            'catalogue and a safer assistant, each change earned by evidence.',
            'Bir beslenme uygulamasında sözleşmeli yapay zekâ mühendisliği: bir ölçüm platformu, '
            'temizlenmiş bir yemek kataloğu ve daha güvenli bir asistan; her değişiklik kanıtla '
            'hak edildi.'),
  'fig': ('923', ('benchmark cases', 'kıyaslama vakası')),
  'title': ('EatBetter — production LLM evaluation and data quality',
            'EatBetter — üretimde LLM değerlendirme ve veri kalitesi'),
  'desc': ('Contract AI engineering on a nutrition app: a 923-case evaluation platform with '
           'human-adjudicated labels, a guarded cleanup of a live PostgreSQL catalogue and a '
           'measured safety fix for the in-app assistant.',
           'Bir beslenme uygulamasında sözleşmeli yapay zekâ mühendisliği: insan hakemli '
           'etiketlere sahip 923 vakalık değerlendirme platformu, canlı bir PostgreSQL kataloğunun '
           'korumalı temizliği ve uygulama içi asistan için ölçülmüş bir güvenlik düzeltmesi.'),
  'deck': ('Contract AI engineering on a nutrition app, where every change to the model, the '
           'catalogue or the assistant had to be earned by a measurement.',
           'Bir beslenme uygulamasında sözleşmeli yapay zekâ mühendisliği; modele, kataloğa ya da '
           'asistana yapılan her değişiklik bir ölçümle hak edildi.'),
  'links': [],
  'tags': [('live', ('Production data work', 'Canlı veri çalışması')),
           ('', ('September 2026', 'Eylül 2026')),
           ('', ('Private client repositories', 'Özel müşteri depoları'))]},
 {'slug': 'benchfck',
  'no': '01',
  'name': 'benchfck',
  'kind': ('Deterministic evaluation · Exact Rust harness',
           'Deterministik değerlendirme · Kesin Rust koşumu'),
  'blurb': ('Generates its own machine-state tasks and scores them exactly, so no learned judge '
            'sits between a model and its result.',
            'Kendi makine-durumu görevlerini üretir ve kesin olarak puanlar; modelle sonuç '
            'arasında öğrenilmiş bir hakem durmaz.'),
  'fig': ('4', ('instruction encodings', 'komut kodlaması')),
  'title': ('benchfck — exact machine-state benchmark harness',
            'benchfck — kesin makine-durumu değerlendirme koşumu'),
  'desc': ('A Brainfuck-based generator and exact Rust harness that produces, validates and scores '
           'machine-state tasks across four controlled instruction encodings.',
           'Dört kontrollü komut kodlaması üzerinde makine-durumu görevleri üreten, doğrulayan ve '
           'puanlayan Brainfuck tabanlı üreteç ve kesin Rust koşumu.'),
  'deck': ('A generator and exact harness for machine-state tasks, built so that nothing in the '
           'scoring path depends on a learned judge.',
           'Makine-durumu görevleri için bir üreteç ve kesin koşum: puanlama yolundaki hiçbir adım '
           'öğrenilmiş bir hakeme bağlı değil.'),
  'links': [('https://github.com/muend/benchfck', ('Repository', 'Depo')),
            ('https://github.com/muend/benchfck/blob/main/VALIDITY.md',
             ('Validity contract', 'Geçerlilik sözleşmesi'))],
  'tags': [('new', ('v0.4.0-alpha', 'v0.4.0-alfa')), 'Apache-2.0', 'Rust']},
 {'slug': 'neuron-to-gpt',
  'no': '02',
  'name': 'neuron-to-gpt',
  'kind': ('LLM foundations · GPT-2 implementation', 'LLM temelleri · GPT-2 uygulaması'),
  'blurb': ('From scalar autograd to a 124M-parameter GPT-2: byte-level BPE, checked pretrained '
            'imports and GPU training diagnostics.',
            'Skaler otomatik türevden 124M parametreli GPT-2’ye: byte-level BPE, doğrulanmış '
            'ağırlık aktarımı ve GPU eğitim kontrolleri.'),
  'fig': ('124M', ('GPT-2 parameters', 'GPT-2 parametresi')),
  'title': ('neuron-to-gpt — from one neuron to GPT-2 124M',
            'neuron-to-gpt — tek nörondan GPT-2 124M’e'),
  'desc': ('Ten runnable stages from autograd to GPT-2 with 124,439,808 parameters, BPE, logits '
           'parity and matched single-batch experiments on A100 and T4.',
           'Otomatik türevden 124.439.808 parametreli GPT-2’ye on aşama; BPE, logits paritesi ve '
           'A100/T4 üzerinde eşlenmiş tek-batch deneyleri.'),
  'deck': ('Ten stages from a single neuron to GPT-2 124M, with the implementation, weight import '
           'and training mechanics checked separately.',
           'Tek bir nörondan GPT-2 124M’e on aşama; uygulama, ağırlık aktarımı ve eğitim '
           'mekanikleri ayrı ayrı doğrulanır.'),
  'links': [('https://github.com/muend/neuron-to-gpt', ('Repository', 'Depo')),
            ('https://github.com/muend/neuron-to-gpt/blob/main/week10/results/submission_report.md',
             ('124M results', '124M sonuçları')),
            ('https://github.com/muend/neuron-to-gpt/tree/main/week09',
             ('BPE implementation', 'BPE uygulaması'))],
  'tags': [('live', ('Public', 'Açık')),
           'PyTorch',
           'GPT-2 124M',
           ('', ('A100 + T4 verified', 'A100 + T4 doğrulandı'))]},
 {'slug': 'geoai-skills',
  'no': '03',
  'name': 'geoai-skills',
  'kind': ('Agent skills · GeoAI knowledge infrastructure',
           "Ajan skill'leri · GeoAI bilgi altyapısı"),
  'blurb': ('Eighteen agent skills that make an AI assistant fail loudly on CRS, leakage, units '
            'and uncertainty instead of quietly guessing.',
            "On sekiz ajan skill'i: yapay zekâ asistanının CRS, sızıntı, birim ve belirsizlik "
            'konularında sessizce tahmin yürütmek yerine yüksek sesle hata vermesini sağlar.'),
  'fig': ('18', ('specialist skills', 'uzman skill')),
  'title': ('geoai-skills — a GeoAI discipline layer for AI agents',
            'geoai-skills — yapay zekâ ajanları için GeoAI disiplin katmanı'),
  'desc': ('18 vendor-neutral Agent Skills, routing and paired behavior evaluations, and listings '
           'in Awesome Claude Code and Awesome Geospatial.',
           'Sağlayıcıdan bağımsız 18 Agent Skill; yönlendirme ve eşlenmiş davranış ölçümleri, '
           'Awesome Claude Code ve Awesome Geospatial listelerinde yer alıyor.'),
  'deck': ('Stop silent CRS, spatial-leakage, validity, unit and uncertainty failures before they '
           'ship.',
           'Sessiz CRS, mekânsal sızıntı, geçerlilik, birim ve belirsizlik hatalarını yayına '
           'çıkmadan durdurur.'),
  'links': [('https://github.com/muend/geoai-skills', ('Repository', 'Depo')),
            ('https://github.com/muend/geoai-skills/blob/main/BENCHMARK.md',
             ('Routing evidence', 'Yönlendirme kanıtı')),
            ('https://github.com/muend/geoai-skills/blob/main/BEHAVIOR.md',
             ('Behavior evidence', 'Davranış kanıtı')),
            ('https://skills.sh/muend/geoai-skills', ('skills.sh', 'skills.sh')),
            ('https://github.com/hesreallyhim/awesome-claude-code#research--scientific-inquiry',
             ('Awesome Claude Code', 'Awesome Claude Code')),
            ('https://github.com/sacridini/Awesome-Geospatial#agent-skills',
             ('Awesome Geospatial', 'Awesome Geospatial')),
            ('https://doi.org/10.5281/zenodo.22288662', ('Zenodo DOI', 'Zenodo DOI'))],
  'tags': [('live', ('Active', 'Aktif')),
           'v0.4.1',
           'MIT',
           ('', ('2 Awesome lists', '2 Awesome listesi'))]},
 {'slug': 'arcgis-mcp-bridge',
  'no': '04',
  'name': 'arcgis-mcp-bridge',
  'kind': ('MCP · Secure GIS execution', 'MCP · Güvenli CBS yürütme'),
  'blurb': ('Exposes ArcGIS Pro geoprocessing to AI agents while keeping the licensed ArcPy '
            'runtime behind a validated process boundary.',
            'ArcGIS Pro coğrafi işlemlerini yapay zekâ ajanlarına açarken lisanslı ArcPy çalışma '
            'zamanını doğrulanmış bir süreç sınırının arkasında tutar.'),
  'fig': ('100', ('geoprocessing tools', 'coğrafi işlem aracı')),
  'title': ('arcgis-mcp-bridge — a local-first MCP server for ArcGIS Pro',
            'arcgis-mcp-bridge — ArcGIS Pro için yerel öncelikli MCP sunucusu'),
  'desc': ('100 declarative ArcGIS Pro geoprocessing tools exposed over MCP, with PathGuard '
           'enforced independently in two isolated processes.',
           'MCP üzerinden açılan 100 bildirimsel ArcGIS Pro coğrafi işlem aracı; PathGuard iki '
           'yalıtılmış süreçte bağımsız olarak uygulanır.'),
  'deck': ('100 declarative geoprocessing tools. Two isolated processes. One security floor.',
           '100 bildirimsel coğrafi işlem aracı. İki yalıtılmış süreç. Tek güvenlik tabanı.'),
  'links': [('https://github.com/muend/arcgis-mcp-bridge', ('Repository', 'Depo')),
            ('https://pypi.org/project/arcgis-mcp-bridge/', ('PyPI', 'PyPI')),
            ('https://glama.ai/mcp/servers/muend/arcgis-mcp-bridge', ('Glama', 'Glama')),
            ('https://dev.to/muend/building-a-secure-mcp-bridge-for-arcgis-pro-and-arcpy-511g',
             ('Write-up', 'Yazı')),
            ('https://github.com/muend/arcgis-mcp-bridge/tree/main/benchmarks',
             ('Real runtime evidence', 'Gerçek runtime kanıtı'))],
  'tags': [('pkg', ('PyPI', 'PyPI')),
           'Apache-2.0',
           ('', ('100 tools', '100 araç')),
           ('', ('Windows', 'Windows')),
           ('', ('Glama TDQS A · 3.5/5', 'Glama TDQS A · 3,5/5'))]},
 {'slug': 'pixel-llm',
  'no': '05',
  'name': 'Pixel LLM',
  'kind': ('Applied simulation · LLM development game',
           'Uygulamalı simülasyon · LLM geliştirme oyunu'),
  'blurb': ('A run-based game where each run trains one language model through ten stages, and '
            'every shortcut taken upstream shows up in the final model card.',
            'Her koşunun on aşamada bir dil modeli eğittiği, koşu tabanlı bir oyun; yukarı akışta '
            'alınan her kestirme final model kartında ortaya çıkar.'),
  'fig': ('10', ('stages, data to launch', 'aşama, veriden lansmana')),
  'title': ('Pixel LLM — a game about building a language model',
            'Pixel LLM — dil modeli inşa etmek üzerine bir oyun'),
  'desc': ('A Godot game that turns the LLM pipeline into ten playable stages, from data '
           'collection to launch, across three difficulty tiers and ending in a model card.',
           'LLM hattını veri toplamadan lansmana on oynanabilir aşamaya çeviren bir Godot oyunu; '
           'üç zorluk kademesi var ve koşu bir model kartıyla biter.'),
  'deck': ('A game about building a language model: ten stages from data collection to launch, '
           'where upstream decisions carry through to a final model card.',
           'Dil modeli inşa etmek üzerine bir oyun: veri toplamadan lansmana on aşama; yukarı '
           'akıştaki kararlar final model kartına kadar taşınır.'),
  'links': [],
  'tags': [('new', ('In development', 'Geliştiriliyor')),
           'Godot 4.7.1',
           ('', ('EN / TR', 'EN / TR')),
           ('', ('Working title', 'Geçici ad'))]},
 {'slug': 'placetwin',
  'no': '06',
  'name': 'Mendirek / PlaceTwin',
  'kind': ('Urban digital twin · Studio platform', 'Kentsel dijital ikiz · Stüdyo platformu'),
  'blurb': ('1,712 structures, 669 parcels and a team workspace: analysis remains linked to its '
            'source and confidence class.',
            '1.712 yapı, 669 parsel ve ekip çalışma alanı; analiz, kaynağına ve güven sınıfına '
            'bağlı kalır.'),
  'fig': ('1,712', ('structures modelled', 'modellenen yapı')),
  'title': ('Mendirek / PlaceTwin — a source-aware urban digital twin',
            'Mendirek / PlaceTwin — kaynaklarını bilen kentsel dijital ikiz'),
  'desc': ('A 43.6-hectare Ayvalık twin with 1,712 structures and 669 parcels; cadastral, survey '
           'and field data, spatial analysis, team workflows and a grounded assistant.',
           'Ayvalık’ta 43,6 hektarlık ikiz: 1.712 yapı ve 669 parsel; kadastro, halihazır ve saha '
           'verisi, mekânsal analiz, ekip akışları ve veriye dayalı asistan.'),
  'deck': ('A digital twin and studio workspace that joins cadastral, survey and field records '
           'into inspectable analysis for two Ayvalık study areas.',
           'Ayvalık’taki iki çalışma alanı için kadastro, halihazır ve saha kayıtlarını '
           'incelenebilir analizde birleştiren dijital ikiz ve stüdyo platformu.'),
  'links': [],
  'tags': [('live', ('In studio use', 'Stüdyoda kullanımda')),
           ('', ('Private repository', 'Özel depo')),
           ('', ('TR / EN outputs', 'TR / EN çıktı'))]},
 {'slug': 'founder-exe',
  'no': '07',
  'name': 'FOUNDER.EXE',
  'kind': ('Applied simulation · Desktop game', 'Uygulamalı simülasyon · Masaüstü oyunu'),
  'blurb': ('A startup simulation where cash, compliance, product and people interact under two '
            'real regulatory regimes.',
            'Nakit, uyum, ürün ve insanın iki gerçek düzenleyici rejim altında etkileştiği bir '
            'girişim simülasyonu.'),
  'fig': ('26', ('academy modules', 'akademi modülü')),
  'title': ('FOUNDER.EXE — a startup simulation across two regulatory regimes',
            'FOUNDER.EXE — iki düzenleyici rejim arasında bir girişim simülasyonu'),
  'desc': ('A Windows startup simulation modelling cash, compliance, cap tables and SAFE '
           'negotiations across the Türkiye and USA ecosystems.',
           'Türkiye ve ABD ekosistemlerinde nakit, uyum, pay tablosu ve SAFE müzakerelerini '
           'modelleyen bir Windows girişim simülasyonu.'),
  'deck': ('A startup simulation where cash, compliance, product and people interact across the '
           'Türkiye and USA ecosystems.',
           'Nakit, uyum, ürün ve insanın Türkiye ve ABD ekosistemleri boyunca etkileştiği bir '
           'girişim simülasyonu.'),
  'links': [('https://izmir-girisim-haritasi.founderexe.workers.dev/simulasyon',
             ('Play the web demo', 'Web demosunu oyna'))],
  'tags': [('live', ('Web demo live', 'Web demosu canlı')),
           'v1.7.0',
           ('', ('Windows package ready', 'Windows paketi hazır')),
           ('', ('EN / TR', 'EN / TR'))]},
 {'slug': 'sentinel-crop-pipeline',
  'no': '08',
  'name': 'sentinel-crop-pipeline',
  'kind': ('Remote sensing · Reproducible data pipeline',
           'Uzaktan algılama · Yeniden üretilebilir veri hattı'),
  'blurb': ('Takes Sentinel-2 scenes from search to training patches, counting every pixel it '
            'throws away along the way.',
            'Sentinel-2 sahnelerini aramadan eğitim yamalarına taşır ve yol boyunca attığı her '
            'pikseli hesaba katar.'),
  'fig': ('5', ('auditable stages', 'denetlenebilir aşama')),
  'title': ('sentinel-crop-pipeline — reproducible Sentinel-2 data preparation',
            'sentinel-crop-pipeline — yeniden üretilebilir Sentinel-2 veri hazırlığı'),
  'desc': ('A five-stage Sentinel-2 L2A preparation pipeline for crop classification, with SCL '
           'masking, spatially blocked splits and a full accounting trail.',
           'Ürün sınıflandırması için beş aşamalı Sentinel-2 L2A hazırlık hattı: SCL maskeleme, '
           'mekânsal bloklu ayrım ve eksiksiz hesap izi.'),
  'deck': ('A reproducible Sentinel-2 data preparation pipeline for crop-classification research, '
           'where every discarded pixel is accounted for.',
           'Ürün sınıflandırma araştırması için yeniden üretilebilir bir Sentinel-2 veri hazırlık '
           'hattı; atılan her piksel kayda geçer.'),
  'links': [('https://github.com/muend/sentinel-crop-pipeline', ('Repository', 'Depo')),
            ('https://pypi.org/project/sentinel-crop-pipeline/', ('PyPI', 'PyPI')),
            ('https://doi.org/10.5281/zenodo.21284444', ('Zenodo DOI', 'Zenodo DOI'))],
  'tags': [('pkg', ('Zenodo DOI', 'Zenodo DOI')),
           'Apache-2.0',
           ('', ('Beta', 'Beta')),
           ('', ('CDSE', 'CDSE'))]},
 {'slug': 'agri-dss',
  'no': '09',
  'name': 'agri-dss',
  'kind': ('Spatial DSS · Public-facing product', 'Mekânsal KDS · Kamuya açık ürün'),
  'blurb': ('Turns regional agricultural data for 147 neighbourhoods into a crop plan a '
            'cooperative can pin to a village board.',
            '147 mahalleye ait bölgesel tarım verisini, bir kooperatifin köy panosuna asabileceği '
            'bir ürün planına dönüştürür.'),
  'fig': ('147', ('neighbourhoods', 'mahalle')),
  'title': ('agri-dss — decision support for the Western Antalya corridor',
            'agri-dss — Batı Antalya koridoru için karar desteği'),
  'desc': ('A zero-backend decision-support system covering five districts and 147 neighbourhoods, '
           'producing printable single-sheet crop plans.',
           'Beş ilçe ve 147 mahalleyi kapsayan, tek sayfalık yazdırılabilir ürün planları üreten, '
           'sunucusuz bir karar destek sistemi.'),
  'deck': ('Decision support for the Western Antalya agricultural corridor, ending in something '
           'you can print on one A4 sheet.',
           'Batı Antalya tarımsal koridoru için karar desteği; sonucu tek bir A4 sayfaya '
           'yazdırabildiğiniz bir çıktı.'),
  'links': [('https://tarimsalkoridor.online', ('Live app', 'Canlı uygulama')),
            ('https://github.com/muend/agri-dss', ('Repository', 'Depo'))],
  'tags': [('live', ('Live', 'Canlı')),
           'Apache-2.0',
           ('', ('5 districts', '5 ilçe')),
           ('', ('No backend', 'Sunucusuz'))]},
 {'slug': 'girisim-haritasi',
  'no': '10',
  'name': 'Girişim Haritası',
  'kind': ('Data engineering · Web platform', 'Veri mühendisliği · Web platformu'),
  'blurb': ('A source-linked company catalogue with repeatable collection, entity resolution, '
            'PostgreSQL and a quota-controlled API.',
            'Tekrarlanabilir toplama, varlık eşleştirme, PostgreSQL ve kota kontrollü API ile '
            'kaynaklı firma kataloğu.'),
  'fig': ('3,257', ('company profiles', 'firma profili')),
  'title': ('Girişim Haritası — source-linked company data and APIs',
            'Girişim Haritası — kaynaklı firma verisi ve API’ler'),
  'desc': ('3,257 profiles from 23 collection methods, with source provenance, scheduled feeds, '
           'PostgreSQL and Cloudflare Workers APIs.',
           '23 toplama yöntemiyle 3.257 profil; kaynak izlenebilirliği, düzenli besleme, '
           'PostgreSQL ve Cloudflare Workers API’leri.'),
  'deck': ('A working data product that turns heterogeneous public company records into traceable '
           'profiles, search and APIs.',
           'Farklı açık firma kayıtlarını izlenebilir profillere, aramaya ve API’lere dönüştüren '
           'çalışan veri ürünü.'),
  'links': [('https://izmir-girisim-haritasi.founderexe.workers.dev',
             ('Live platform', 'Canlı platform')),
            ('https://izmir-girisim-haritasi.founderexe.workers.dev/api/v1/openapi.json',
             ('OpenAPI', 'OpenAPI'))],
  'tags': [('live', ('Live prototype', 'Canlı prototip')),
           'PostgreSQL',
           'Workers / D1',
           ('', ('Private repository', 'Özel depo'))]},
 {'slug': 'plan-forge',
  'no': '11',
  'name': 'Plan Forge',
  'kind': ('Desktop software · Document engineering', 'Masaüstü yazılım · Belge mühendisliği'),
  'blurb': ('A Windows report builder with local document parsing, versioned templates, expert '
            'approval and traceable DOCX/PDF output.',
            'Yerel belge çözümleme, sürümlü şablon, uzman onayı ve izlenebilir DOCX/PDF çıktılı '
            'Windows rapor üreticisi.'),
  'fig': ('0.2.2', ('Windows release build', 'Windows derlemesi')),
  'title': ('Plan Forge — local-first planning report software',
            'Plan Forge — yerel çalışan planlama raporu yazılımı'),
  'desc': ('React and Python/FastAPI desktop software for parsing DOCX documents, freezing '
           'approved mappings and producing auditable DOCX/PDF reports.',
           'DOCX çözümleme, onaylı eşleştirmeleri dondurma ve denetlenebilir DOCX/PDF raporları '
           'için React ve Python/FastAPI masaüstü yazılımı.'),
  'deck': ('A planning report workflow that keeps source documents local and requires expert '
           'approval before draft content becomes a report.',
           'Kaynak belgeleri yerelde tutan ve taslağın rapora girmesinden önce uzman onayı isteyen '
           'planlama raporu akışı.'),
  'links': [],
  'tags': [('', ('Windows package', 'Windows paketi')),
           'v0.2.2',
           'React / FastAPI',
           ('', ('Private repository', 'Özel depo'))]}]

BY_SLUG = {p["slug"]: p for p in PROJECTS}
