"""Project pages added in October 2026, in both languages.

EatBetter (client work), PlaceTwin, neuron-to-gpt and Pixel LLM. Same rules as
pagebodies.py: every fact is transcribed from the project's own records, and
diagram labels stay in English.
"""
import shell
from shell import T as _
from build import project_page, svg, catalog
from pagebodies import fighead


def _video(name):
    """Site-relative path to a film or its poster, from a project page."""
    return f"{shell.rel('projects/x.html', shell.LANG)}assets/video/{name}"


def build():
    lang = shell.LANG

    # ======================================================== 00 EatBetter
    project_page(
        "eatbetter",
        spec_rows=[
            (_("Role", "Rol"), _("AI Engineer, contract", "Yapay Zekâ Mühendisi, sözleşmeli")),
            (_("Period", "Dönem"), _("August – October 2026", "Ağustos – Ekim 2026")),
            (_("Stack", "Yığın"), "Python · TypeScript / Node.js · PostgreSQL · Azure OpenAI"),
            (_("Shipped", "Teslim"), _("17 merged pull requests · +14.5k / −2.4k lines incl. tests",
                                       "Birleşen 17 PR · testler dahil +14,5 bin / −2,4 bin satır")),
            (_("Method", "Yöntem"),
             _("One engineer directing parallel AI coding agents from written task specs",
               "Yazılı görev tanımlarıyla paralel yapay zekâ kodlama ajanlarını yöneten tek mühendis")),
            (_("Source", "Kaynak"),
             _("Private client repositories; figures from the engagement's own records",
               "Özel müşteri depoları; sayılar işin kendi kayıtlarından")),
        ],
        sections=f"""
{shell.prose(_("Why", "Neden"),
  _("Measure first, then change", "Önce ölç, sonra değiştir"),
  _("<p>When the engagement started there was no versioned way to measure the production meal "
    "analysis against the company's own data. Whether one model or prompt was better than another "
    "could not be said with evidence. The food catalogue had been filled by model-generated "
    "writes, and the path that let defects in was still open.</p>"
    "<p>By handover there was a measurement platform anyone with the repository can "
    "run, a cleaned catalogue with its source closed, a pipeline that records and judges user "
    "corrections, and a fine-tuning dataset that matches the live call exactly. This page "
    "describes how each was built and what the measurements said, including the ones that said "
    "stop.</p>",
    "<p>İş başladığında, üretimdeki öğün analizini şirketin kendi verisiyle ölçen sürümlü bir yol "
    "yoktu. Bir modelin ya da istemin ötekinden daha iyi olup olmadığı kanıtla söylenemiyordu. "
    "Yemek kataloğu model üretimi yazımlarla dolmuştu ve kusurları içeri alan yol hâlâ açıktı.</p>"
    "<p>Devir anında, depoyu alan herkesin koşabildiği bir ölçüm platformu, kaynağı "
    "kapatılmış temiz bir katalog, kullanıcı düzeltmelerini kaydeden ve değerlendiren bir hat ve "
    "canlı çağrıyla birebir örtüşen bir ince ayar veri seti vardı. Bu sayfa her birinin nasıl "
    "kurulduğunu ve ölçümlerin ne dediğini anlatır; “dur” diyenler dahil.</p>"))}

{shell.figure(_("Fig. 01", "Şekil 01"),
  _("From production sample to release decision", "Üretim örnekleminden yayın kararına"),
  _("Labels are proposed by a three-model panel and settled by a human; model output is never "
    "treated as ground truth, and a model that helped propose labels cannot be evaluated as a "
    "candidate. Every comparison is paired on the same cases and resampled by user, because one "
    "person's meals are not independent observations.",
    "Etiketleri üç modelli bir panel önerir, son kararı insan verir; model çıktısı hiçbir zaman "
    "doğru kabul edilmez ve etiket önerisine katılan bir model aday olarak değerlendirilemez. Her "
    "karşılaştırma aynı vakalarda eşlenir ve kullanıcıya göre yeniden örneklenir; çünkü bir "
    "kişinin öğünleri birbirinden bağımsız gözlemler değildir."),
  shell.plate(_("Fig. 01", "Şekil 01"),
              _("Evaluation platform", "Değerlendirme platformu"), svg("eatbetter-eval.svg")))}

<section class="fig">
{fighead(_("Decisions", "Kararlar"), _("What the platform was used to decide",
                                       "Platformla verilen kararlar"))}
{catalog([
    (_("Costlier model", "Pahalı model"), _("−0.006", "−0,006"),
     _("ΔF1 against the live model, 95% CI [−0.023, +0.012], at about seven times the price. "
       "Retired.",
       "Canlı modele karşı ΔF1; %95 GA [−0,023, +0,012], yaklaşık yedi kat fiyata. Devreden "
       "çıkarıldı.")),
    (_("Candidate pipeline", "Aday hat"), "4 / 4",
     _("Comparisons lost to the bare model, at 12× the cost and 7× the latency. Shut down.",
       "Yalın modele karşı kaybedilen karşılaştırma; 12 kat maliyet ve 7 kat gecikmeyle. "
       "Kapatıldı.")),
    (_("Prompt gain", "İstem kazancı"), _("67%", "%67"),
     _("Share of the best prompt variant's apparent gain that came from label granularity rather "
       "than better recognition.",
       "En iyi istem varyantının görünen kazancının, daha iyi tanımadan değil etiket ayrıntı "
       "düzeyinden gelen payı.")),
    (_("LLM judge", "LLM hakemi"), _("0.82", "0,82"),
     _("Best agreement among five judge candidates on 80 hand-labelled meals; the existing rule "
       "path scored 0.66.",
       "Elle etiketlenmiş 80 öğünde beş hakem adayı arasındaki en yüksek uyum; mevcut kural yolu "
       "0,66 aldı.")),
])}
  <p class="fig-note">{_(
    "An error map drawn in the second week showed that two thirds of the best prompt's gain was "
    "not a vision improvement at all. That finding is what separates a higher score from a better "
    "system, and it changed how every later target was written.",
    "İkinci haftada çıkarılan hata haritası, en iyi istemin kazancının üçte ikisinin hiç de bir "
    "görme iyileşmesi olmadığını gösterdi. “Daha yüksek skor” ile “daha iyi sistem”i ayıran bulgu "
    "budur; sonraki her hedefin nasıl yazıldığını değiştirdi.")}</p>
</section>

{shell.figure(_("Fig. 02", "Şekil 02"),
  _("One permitted path to production", "Üretime giden tek izinli yol"),
  _("Only a human connected to the live database. Each change was planned locally from a "
    "read-only export, rehearsed inside a transaction that was rolled back, and committed only "
    "when the affected row count matched the prediction. The write gate at the source went live "
    "before the cleanup, so cleaned rows could not return.",
    "Canlı veritabanına yalnız insan bağlandı. Her değişiklik salt okunur bir dışa aktarımdan "
    "yerelde planlandı, geri alınan bir işlem içinde prova edildi ve yalnızca etkilenen satır "
    "sayısı öngörüyle tuttuğunda yazıldı. Kaynaktaki yazma kapısı temizlikten önce canlıya "
    "alındı; böylece temizlenen satırlar geri gelemedi."),
  shell.plate(_("Fig. 02", "Şekil 02"),
              _("Guarded writes and the write gate", "Korumalı yazım ve yazma kapısı"),
              svg("eatbetter-write.svg")))}

<section class="fig">
{fighead(_("Catalogue", "Katalog"), _("What changed in the live database",
                                      "Canlı veritabanında ne değişti"))}
  <p>{_("Percentages are of the 387,668-row catalogue export taken before the cleanup. Deletion "
        "went by content group, not by a target number: one-off compositions, numbered copies and "
        "broken slugs were removed, while searchable generic names were only unpublished.",
        "Yüzdeler, temizlikten önce alınan 387.668 satırlık katalog dışa aktarımına göredir. Silme "
        "bir sayı hedefine göre değil, içerik grubuna göre yapıldı: tek seferlik bileşimler, sayı "
        "ekli kopyalar ve bozuk slug'lar silindi; aranabilir genel adlar yalnızca yayından "
        "çekildi.")}</p>
{catalog([
    (_("Soft-deleted", "Yumuşak silinen"), _("88,970", "88.970"),
     _("23.0% of the catalogue, each row recoverable from its undo file.",
       "Kataloğun %23,0'ı; her satır geri alma dosyasından kurtarılabilir.")),
    (_("Unpublished", "Yayından çekilen"), _("90,735", "90.735"),
     _("23.4%, kept in the database but taken out of publication.",
       "%23,4; veritabanında tutuldu, yayından çıkarıldı.")),
    (_("Popularity re-derived", "Popülerliği düzeltilen"), _("292,113", "292.113"),
     _("75.4%: model-invented popularity replaced with real usage.",
       "%75,4: modelin uydurduğu popülerlik gerçek kullanımla değiştirildi.")),
    (_("Link and brand repairs", "Bağlantı ve marka onarımı"), _("35,979", "35.979"),
     _("Row operations: chains flattened, wrong merges split, junk brands cleared.",
       "Satır işlemi: zincirler düzleştirildi, yanlış birleştirmeler ayrıldı, çöp "
       "markalar boşaltıldı.")),
])}
{shell.note(_("A mistake, and its repair", "Bir hata ve onarımı"),
  _("During the cleanup the first version of a duplicate-merge script wrote one of two merge fields "
    "and broke 1,845 redirects. It was repaired the same day from current live values, verified "
    "with a health query, and the script gained a root-quality filter. One other step skipped its "
    "separate rollback rehearsal; the count matched the prediction exactly and the deviation was "
    "logged. Both are in the engagement's records, which is where they belong.",
    "Temizlik sırasında kopya birleştirme betiğinin ilk sürümü birleştirmenin iki alanından yalnızca "
    "birini yazdı ve 1.845 yönlendirmeyi kırdı. Aynı gün canlıdaki güncel değerlerle onarıldı, bir "
    "sağlık sorgusuyla doğrulandı ve betiğe kök kalite süzgeci eklendi. Bir başka adımda ayrı "
    "ROLLBACK provası atlandı; sayı öngörüyle birebir tuttu ve sapma kayda geçti. İkisi de işin "
    "kayıtlarında duruyor; olması gereken yer de orası."), warn=True)}
</section>

{shell.prose(_("Assistant safety", "Asistan güvenliği"),
  _("A scorecard built from real failures", "Gerçek hatalardan kurulan bir karne"),
  _("<p>The in-app assistant keeps a memory of each user. In a stress test that adds more than "
    "thirty synthetic memory entries to a real profile, an older allergy record stopped reaching "
    "the answer. A pre-registered scorecard measured it: 400 frozen cases, 6,000 generations and "
    "24,000 judge slots across two judge models and two orderings.</p>"
    "<p>A fix that places allergy, medication and condition records first in the prompt cut the "
    "paired veto rate from 96.4% to 2.1% over 172 pairs (Holm-corrected p = 0.0001). It was the "
    "only one of ten candidates to pass the acceptance gate, and was delivered behind a flag that "
    "switches on without a deploy.</p>"
    "<p>The lesson came the day before. A 24-variant tournament found no verified improvement, "
    "because the control arm already scored 97–98% and the test set never stressed the real "
    "mechanism. The scorecard that found the win was built only from cases the current version "
    "actually got wrong, at about a quarter of the cost. Safety results are advisory: there was "
    "no dietitian on the team.</p>",
    "<p>Uygulama içi asistan her kullanıcı için bir bellek tutar. Gerçek bir profile otuzdan "
    "fazla sentetik bellek kaydı ekleyen bir stres testinde, eski bir alerji kaydı cevaba "
    "ulaşmaz hâle geldi. Bunu ön kayıtlı bir karne ölçtü: 400 dondurulmuş vaka, 6.000 üretim ve "
    "iki hakem modeli ile iki sıralama üzerinden 24.000 hakem slotu.</p>"
    "<p>Alerji, ilaç ve hastalık kayıtlarını istemde öne alan düzeltme, eşlenmiş veto oranını 172 "
    "çiftte %96,4'ten %2,1'e indirdi (Holm düzeltmeli p = 0,0001). Kabul kapısını geçen, on aday "
    "arasındaki tek düzeltme oldu ve yeniden dağıtım gerektirmeden açılan bir bayrağın arkasında "
    "teslim edildi.</p>"
    "<p>Ders bir gün önce çıkmıştı. 24 varyantlı bir turnuva doğrulanmış bir iyileşme bulamadı; "
    "çünkü kontrol kolu zaten %97–98'deydi ve test seti asıl mekanizmayı hiç zorlamıyordu. "
    "Kazancı bulan karne, yalnızca mevcut sürümün gerçekten hata yaptığı vakalardan kuruldu ve "
    "yaklaşık dörtte bir maliyete çıktı. Güvenlik sonuçları tavsiye niteliğindedir: ekipte "
    "diyetisyen yoktu.</p>"))}

<section class="fig">
{fighead(_("Pipelines", "Hatlar"), _("Data and pipelines delivered alongside",
                                     "Yanında teslim edilen veri ve hatlar"))}
{catalog([
    (_("Nutrient verification", "Besin değeri doğrulaması"), _("242,707", "242.707"),
     _("Foods checked independently by three models. The 215,584-food correction package carries "
       "a per-row “write only if unchanged” guard and undo SQL, and was rehearsed on a local copy "
       "of the live export.",
       "Üç modelle bağımsız kontrol edilen yemek. 215.584 yemeklik düzeltme paketi satır başına "
       "“eski değer hâlâ buysa yaz” koruması ve geri alma SQL'i taşır; canlı dışa aktarımın yerel "
       "kopyasında prova edildi.")),
    (_("Image runner", "Görsel üretim hattı"), _("≈29 / min", "≈29 / dk"),
     _("Persistent, budget-capped jobs over a three-endpoint pool with AIMD rate control, at the "
       "ceiling of the provider quota; about 250k food images (estimate).",
       "Üç uç noktalı bir havuz üzerinde, bütçe tavanlı kalıcı işler ve AIMD hız kontrolü; "
       "sağlayıcı kotasının tavanında. Yaklaşık 250 bin yemek görseli (tahmini).")),
    (_("Fine-tuning dataset", "İnce ayar veri seti"), _("561,314", "561.314"),
     _("Versioned records for Qwen3-VL with a leakage audit against sealed sets, PII scan, "
       "deduplication and per-user splits; 0 template or tokenizer errors over 638,493 records.",
       "Qwen3-VL için sürümlü kayıt: mühürlü setlere karşı sızıntı denetimi, kişisel veri taraması, "
       "tekrar temizliği ve kullanıcıya göre bölme; 638.493 kayıtta 0 şablon ya da tokenizer "
       "hatası.")),
    (_("Tool-use dialogues", "Araç kullanım sohbeti"), _("38,417", "38.417"),
     _("Synthetic assistant conversations in six languages covering all 15 tools; 89% passed "
       "every code check. No real user chats were used.",
       "Altı dilde, 15 aracın tamamını kapsayan sentetik asistan sohbeti; %89'u bütün kod "
       "kontrollerinden geçti. Gerçek kullanıcı sohbeti kullanılmadı.")),
    (_("Meal notes labelled", "Etiketlenen öğün notu"), _("259,986", "259.986"),
     _("Real meal notes labelled through the live contract, after a six-arm teacher benchmark "
       "weighed label quality against cost.",
       "Canlı sözleşmeyle etiketlenen gerçek öğün notu; öncesinde altı kollu bir öğretmen "
       "kıyaslaması etiket kalitesini maliyete karşı tarttı.")),
    (_("Corrections loop", "Düzeltme döngüsü"), _("3 PRs", "3 PR"),
     _("Lost user corrections are now recorded and the model's first answer preserved; personal "
       "habits and a spend-capped LLM judge sit behind flags.",
       "Kaybolan kullanıcı düzeltmeleri artık kaydediliyor ve modelin ilk cevabı korunuyor; "
       "kişisel alışkanlıklar ve harcama tavanlı LLM hakemi bayrak arkasında.")),
])}
  <p class="fig-note">{_(
    "At handover the nutrient package was approved and waiting for an off-peak "
    "write, the safety fix was waiting for its flag, and the image total was an estimate still "
    "to be confirmed from the job table.",
    "Devir anında besin değeri paketi onaylıydı ve düşük trafikte yazılmayı bekliyordu, "
    "güvenlik düzeltmesi bayrağının açılmasını bekliyordu, görsel toplamı ise iş tablosundan "
    "doğrulanması gereken bir tahmindi.")}</p>
</section>

{shell.prose(_("Negative results", "Olumsuz sonuçlar"),
  _("Stopped on evidence", "Kanıtla durdurulanlar"),
  _("<p>Work that a measurement or a review ended is listed with the same weight as work that "
    "shipped. Most of it set the direction of what came next.</p>"
    "<ul>"
    "<li><strong>Candidate recognition pipeline.</strong> Worse than the bare model in four of "
    "four comparisons, at 12× the cost. Closed.</li>"
    "<li><strong>Prompt-module set.</strong> A measured +0.04 F1, significant in three repeats, "
    "was judged too small to be visible to users. Archived without a pull request.</li>"
    "<li><strong>Costlier teacher candidate.</strong> 9% worse than the live model at 20× the "
    "price. The live baseline stayed.</li>"
    "<li><strong>Corrections loop, first design.</strong> 20 commits and 724 tests, rejected in "
    "review: the personal hint read only the note, while half of all scans were photos. Rebuilt "
    "as three small, conflict-free pull requests that merged two days later.</li>"
    "<li><strong>24-variant tournament.</strong> No verified improvement. Its measurement "
    "harness was reused for the scorecard that found one.</li>"
    "</ul>",
    "<p>Bir ölçümün ya da incelemenin sonlandırdığı iş, yayına çıkan işle aynı ağırlıkta "
    "listelenir. Çoğu, sonraki işin yönünü belirledi.</p>"
    "<ul>"
    "<li><strong>Aday tanıma hattı.</strong> Dört karşılaştırmanın dördünde yalın modelden kötü; "
    "12 kat maliyetle. Kapatıldı.</li>"
    "<li><strong>İstem modülü seti.</strong> Üç tekrarda da anlamlı çıkan +0,04 F1, kullanıcıya "
    "görünür bir fayda için fazla küçük bulundu. PR açılmadan arşivlendi.</li>"
    "<li><strong>Daha pahalı öğretmen adayı.</strong> Canlı modelden %9 kötü, 20 kat pahalı. "
    "Canlı taban çizgisi korundu.</li>"
    "<li><strong>Düzeltme döngüsü, ilk tasarım.</strong> 20 commit ve 724 test; incelemede "
    "reddedildi: kişisel ipucu yalnızca nota bakıyordu, oysa taramaların yarısı fotoğraflıydı. "
    "İki gün sonra birleşen, birbiriyle çakışmayan üç küçük PR olarak yeniden kuruldu.</li>"
    "<li><strong>24 varyantlı turnuva.</strong> Doğrulanmış bir iyileşme yok. Ölçüm düzeni, "
    "iyileşmeyi bulan karnede yeniden kullanıldı.</li>"
    "</ul>"))}

{shell.prose(_("Way of working", "Çalışma yöntemi"),
  _("One engineer, many agents, fixed rules", "Tek mühendis, çok ajan, değişmez kurallar"),
  _("<p>The work was done by one engineer directing several AI coding agents in parallel. "
    "Decisions, rules and every step that touched production stayed with the human; agents "
    "worked from 94 written task specifications with limited permissions, each in its own "
    "worktree.</p>"
    "<ul>"
    "<li>Only a human writes to the live database: rehearse with ROLLBACK, then COMMIT, always "
    "with an undo file.</li>"
    "<li>Behaviour changes sit behind a flag whose default is today's behaviour, so rollback "
    "needs no deploy.</li>"
    "<li>Pull requests are conflict-free by design, checked with a merge-tree matrix against the "
    "main branches and each other.</li>"
    "<li>Adversarial multi-agent review before a pull request opens: 44 agents on one change "
    "produced 19 verified findings.</li>"
    "<li>Mutation testing, pre-registration, Holm correction and user-clustered bootstrap for "
    "anything claimed as a result.</li>"
    "</ul>"
    "<p>The handover was a set of decision records, daily notes and a delivery manifest listing "
    "each artefact with its SHA-256.</p>",
    "<p>İş, birden çok yapay zekâ kodlama ajanını paralel yöneten tek bir mühendisle yürüdü. "
    "Kararlar, kurallar ve üretime dokunan her adım insanda kaldı; ajanlar 94 yazılı görev "
    "tanımıyla, sınırlı yetkiyle ve her biri kendi worktree'sinde çalıştı.</p>"
    "<ul>"
    "<li>Canlı veritabanına yalnız insan yazar: önce ROLLBACK ile prova, sonra COMMIT, her "
    "zaman bir geri alma dosyasıyla.</li>"
    "<li>Davranış değişiklikleri, varsayılanı bugünkü davranış olan bir bayrağın arkasındadır; "
    "geri dönüş dağıtım gerektirmez.</li>"
    "<li>PR'lar tasarım gereği çakışmasızdır; ana dallara ve birbirlerine karşı merge-tree "
    "matrisiyle denetlenir.</li>"
    "<li>PR açılmadan önce çok ajanlı karşıt inceleme: tek bir değişiklikte 44 ajan, 19 "
    "doğrulanmış bulgu üretti.</li>"
    "<li>Sonuç diye öne sürülen her şey için mutasyon testi, ön kayıt, Holm düzeltmesi ve "
    "kullanıcı kümeli bootstrap.</li>"
    "</ul>"
    "<p>Devir; karar kayıtları, günlük notlar ve her çıktıyı SHA-256 özetiyle listeleyen bir "
    "teslim tutanağından oluştu.</p>"))}

{shell.note(_("Scope", "Kapsam"),
  _("<strong>Client work.</strong> The repositories and data are private, so nothing on this "
    "page links out, and product internals are described only as far as the method needs. "
    "Figures are transcribed from the engagement's own records at handover; items "
    "delivered but not yet live at handover are stated as such.",
    "<strong>Müşteri işi.</strong> Depolar ve veri özeldir; bu yüzden bu sayfadaki hiçbir şey "
    "dışarıya bağlanmaz ve ürünün iç yapısı yalnızca yöntemin gerektirdiği kadar anlatılır. "
    "Sayılar, işin devir anındaki kendi kayıtlarından aktarılmıştır; teslim edilmiş ama "
    "devir anında henüz canlıya alınmamış kalemler öyle belirtilmiştir."))}
""")

    # ======================================================== 06 PlaceTwin
    project_page(
        "placetwin",
        spec_rows=[
            (_("Context", "Bağlam"),
             _("Urban design studio, İzmir Institute of Technology, Fall 2026",
               "Kentsel tasarım stüdyosu, İzmir Yüksek Teknoloji Enstitüsü, Güz 2026")),
            (_("Study areas", "Çalışma alanları"),
             _("A2 21.67 ha, 106 buildings · B2 21.94 ha, 590 buildings",
               "A2 21,67 ha, 106 bina · B2 21,94 ha, 590 bina")),
            (_("Delivery", "Teslim"),
             _("Offline single file (≈3.6 MB) · team panel · gated site",
               "Çevrimdışı tek dosya (≈3,6 MB) · ekip paneli · girişli site")),
            (_("Export CRS", "Dışa aktarım"),
             _("TUREF / TM27 (EPSG:5254), within 0.13 mm of an independent implementation",
               "TUREF / TM27 (EPSG:5254), bağımsız bir uygulamaya göre fark en çok 0,13 mm")),
            (_("Stack", "Yığın"), "three.js · vanilla JS · Node · Cloudflare Pages + D1 · Claude"),
            (_("Tests", "Test"), _("512 for the twin · 75 for panel and site",
                                   "İkiz için 512 · panel ve site için 75")),
        ],
        sections=f"""
{shell.prose(_("Why", "Neden"),
  _("A model that admits what it does not know", "Bilmediğini kabul eden bir model"),
  _("<p>Studio models usually draw every building with the same confidence. Here the height of 49 "
    "buildings comes from title deeds, 7 from OpenStreetMap, and the remaining 640 are estimates "
    "with a stated range. The twin says which is which, on every building, and a field survey "
    "promotes a building to the highest class.</p>"
    "<p>Nothing in the scene is decoration. There are no representative cars, street lamps or "
    "façade materials: if it is not data, it is not drawn. Counts that depend on incomplete "
    "cadastral coverage are shown as lower bounds and labelled provisional until the coverage "
    "threshold is met.</p>",
    "<p>Stüdyo modelleri çoğu zaman her binayı aynı güvenle çizer. Burada 49 binanın yüksekliği "
    "tapu kaydından, 7 binanınki OpenStreetMap'ten gelir; kalan 640 bina aralığı belirtilmiş "
    "tahmindir. İkiz hangisinin hangisi olduğunu her binada söyler; saha çalışması bir binayı en "
    "üst sınıfa taşır.</p>"
    "<p>Sahnede süs yoktur. Temsili araba, sokak lambası ya da cephe malzemesi çizilmez: veri "
    "değilse çizilmez. Eksik kadastro kapsamına bağlı sayılar alt sınır olarak gösterilir ve "
    "kapsam eşiği sağlanana kadar “geçici” diye işaretlenir.</p>"))}

{shell.figure(_("Fig. 01", "Şekil 01"),
  _("From sources to studio", "Kaynaklardan stüdyoya"),
  _("A deterministic build turns open and official sources into one data file and one summary. "
    "The panel, the site and the assistant all read that same summary, so the numbers a student "
    "sees in three places cannot disagree.",
    "Deterministik bir derleme, açık ve resmî kaynakları tek bir veri dosyasına ve tek bir özete "
    "çevirir. Panel, site ve asistan aynı özeti okur; böylece bir öğrencinin üç ayrı yerde "
    "gördüğü sayılar birbiriyle çelişemez."),
  shell.plate(_("Fig. 01", "Şekil 01"),
              _("Source-to-studio chain", "Kaynaktan stüdyoya zincir"), svg("placetwin.svg")))}

<section class="fig">
{fighead(_("Evidence", "Kanıt"), _("What the twin measures", "İkizin ölçtükleri"))}
  <p>{_("Two study areas in one scene: A2, the slipway and the old bus station, and B2, the "
        "historic customs house, Cumhuriyet Square, the old khans and the Potamos stream.",
        "Tek sahnede iki çalışma alanı: A2, Kızak ve Eski Otogar; B2, Tarihi Gümrük, Cumhuriyet "
        "Meydanı, Eski Hanlar ve Potamos.")}</p>
{catalog([
    (_("Buildings", "Bina"), "696",
     _("106 in A2 and 590 in B2, each with source, confidence class and parcel link.",
       "A2'de 106, B2'de 590; her biri kaynağı, güven sınıfı ve parsel bağlantısıyla.")),
    (_("Cadastral parcels", "Kadastro parseli"), "669",
     _("95 and 574, queried one by one at a rate the public service allows.",
       "95 ve 574; kamu servisinin izin verdiği hızda tek tek sorgulandı.")),
    (_("Winter sun", "Kış güneşi"), _("5.6 / 2.4 h", "5,6 / 2,4 sa"),
     _("Mean direct sunlight in open space on 21 December, A2 against B2.",
       "21 Aralık'ta açık alanda ortalama doğrudan güneş; A2'ye karşı B2.")),
    (_("No sea view", "Denizi görmeyen"), _("66% / 81%", "%66 / %81"),
     _("Share of open space with no view of the sea at eye level.",
       "Göz hizasında denizi görmeyen açık alan payı.")),
    (_("Possible missing buildings", "Olası eksik yapı"), "232",
     _("Footprints in an independent dataset but absent from OpenStreetMap, queued for field "
       "checks.",
       "Bağımsız bir veri setinde olup OpenStreetMap'te bulunmayan izler; saha denetimi "
       "kuyruğunda.")),
    (_("Sourced planning rules", "Kaynaklı plan kuralı"), "35",
     _("18 for A2 and 17 for B2, compiled with citations. Informational, not an official plan.",
       "A2 için 18, B2 için 17; atıflarıyla derlendi. Bilgi amaçlıdır, resmî plan değildir.")),
])}
</section>

{shell.prose(_("Assistant", "Asistan"),
  _("Answers come from the twin, not from memory", "Yanıtlar bellekten değil, ikizden gelir"),
  _("<p>The studio panel has a Claude assistant with ten tools. Eight of them read and manage the "
    "panel itself: the sixteen-week calendar, tasks, assignments, deliverables and the decision "
    "log. The other two are the grounding.</p>"
    "<ul>"
    "<li><strong>Building lookup.</strong> Finds up to five buildings by number, name or "
    "block and parcel, and returns area, storeys, height, the data's confidence class and source, "
    "the parcel and any field record.</li>"
    "<li><strong>Plan and policy lookup.</strong> Searches a sourced compilation of plans, zoning "
    "and conservation rules, decision authority, actors and disputes, and cites what it "
    "returns.</li>"
    "</ul>"
    "<p>Selecting a building in the 3D scene and choosing “ask the assistant” carries that "
    "selection into the conversation as context, so the question starts from the place rather "
    "than from a description of it.</p>",
    "<p>Stüdyo panelinde on araçlı bir Claude asistanı var. Sekizi panelin kendisini okur ve "
    "yönetir: on altı haftalık takvim, görevler, atamalar, teslimler ve karar defteri. Öteki "
    "ikisi yanıtların dayanağıdır.</p>"
    "<ul>"
    "<li><strong>Yapı arama.</strong> Bina numarası, adı ya da ada ve parsel ile en çok beş "
    "yapı bulur; alanı, kat sayısını, yüksekliği, verinin güven sınıfını ve kaynağını, parseli "
    "ve varsa saha kaydını döndürür.</li>"
    "<li><strong>Plan ve politika arama.</strong> Planlar, imar ve koruma kuralları, karar "
    "yetkisi, aktörler ve tartışmalardan oluşan kaynaklı bir derlemede arar ve döndürdüğünün "
    "kaynağını gösterir.</li>"
    "</ul>"
    "<p>3B sahnede bir bina seçip “asistana sor” demek, o seçimi bağlam olarak sohbete taşır; "
    "soru bir yerin tarifinden değil, yerin kendisinden başlar.</p>"))}

<section class="fig">
{fighead(_("Film", "Film"), _("Sixty seconds through the twin", "İkizde altmış saniye"))}
  <p>{_("The introduction film made for the studio. Every number on screen matches the twin's "
        "summary file. The panel ships under the name Kızak; narration text is in Turkish.",
        "Stüdyo için hazırlanan tanıtım filmi. Ekrandaki her sayı ikizin özet dosyasıyla aynıdır. "
        "Panel “Kızak” adıyla yayımlanır.")}</p>
{shell.film(_video("placetwin-film.mp4"), _video("placetwin-film.jpg"),
            _("Introduction film · 60 s", "Tanıtım filmi · 60 sn"))}
</section>

{shell.note(_("Limits", "Sınırlar"),
  _("An <strong>information tool, not an official plan document</strong>. Risk layers are "
    "open-data screening, not hazard maps. 640 of 696 building heights are estimates. Official "
    "data still missing: seismic design parameters, the base map, the conservation plan, the "
    "listed-building register and an approved shoreline. The repository is private and the site "
    "sits behind a login, so nothing here links out.",
    "<strong>Bilgi aracıdır, resmî plan belgesi değildir</strong>. Risk katmanları açık veriden "
    "taramadır, tehlike haritası değildir. 696 bina yüksekliğinin 640'ı tahmindir. Hâlâ eksik "
    "olan resmî veriler: deprem tasarım parametreleri, halihazır harita, koruma planı, tescil "
    "listesi ve onaylı kıyı kenar çizgisi. Depo özeldir ve site giriş kapısının arkasındadır; bu "
    "yüzden buradaki hiçbir şey dışarıya bağlanmaz."), warn=True)}
""")

    # ======================================================== 07 neuron-to-gpt
    project_page(
        "neuron-to-gpt",
        spec_rows=[
            (_("Scope", "Kapsam"), _("8 weeks, one runnable directory each",
                                    "8 hafta, her biri çalıştırılabilir ayrı bir dizin")),
            (_("Model", "Model"), _("6 blocks · 8 heads · width 256 · context 256",
                                    "6 blok · 8 kafa · 256 genişlik · 256 bağlam")),
            (_("Parameters", "Parametre"), _("4,833,345 English · 4,860,534 Turkish",
                                             "4.833.345 İngilizce · 4.860.534 Türkçe")),
            (_("Training", "Eğitim"),
             _("5,000 updates · BF16 · NVIDIA A100 · ≈7.3 min per model",
               "5.000 güncelleme · BF16 · NVIDIA A100 · model başına ≈7,3 dk")),
            (_("Validation NLL", "Doğrulama NLL"),
             _("1.4723 Shakespeare · 1.6239 Turkish", "1,4723 Shakespeare · 1,6239 Türkçe")),
            (_("Tests", "Test"), _("31, incl. exact checkpoint continuation",
                                   "31; kontrol noktasından birebir devam dahil")),
        ],
        sections=f"""
{shell.prose(_("Why", "Neden"),
  _("Know the machine you evaluate", "Değerlendirdiğin makineyi tanı"),
  _("<p>Evaluating language models for a living without ever having built one leaves a gap. "
    "This journal closes it the slow way: a neuron, a loss, a gradient, then an autograd engine "
    "written with nothing but the standard library, and only then PyTorch.</p>"
    "<p>From week three each new layer is rebuilt by hand before the framework version is "
    "trusted: the bigram counts before the neural bigram, manual backpropagation before "
    "<code>backward()</code>, a custom BatchNorm before LayerNorm, causal averaging before "
    "attention. The Week 8 model was written before the finished reference was consulted.</p>",
    "<p>Hiç dil modeli kurmadan, işi dil modellerini değerlendirmek olan biri için bir boşluk "
    "kalır. Bu günlük o boşluğu yavaş yoldan kapatır: bir nöron, bir kayıp, bir gradyan; sonra "
    "yalnızca standart kütüphaneyle yazılmış bir otomatik türev motoru; PyTorch ancak ondan "
    "sonra.</p>"
    "<p>Üçüncü haftadan itibaren her yeni katman, çerçevedeki sürümüne güvenilmeden önce elle "
    "yeniden kurulur: sinirsel bigramdan önce bigram sayımları, <code>backward()</code>'dan önce "
    "elle geri yayılım, LayerNorm'dan önce özel bir BatchNorm, dikkatten önce nedensel ortalama. "
    "8. hafta modeli, bitmiş referansa bakılmadan önce yazıldı.</p>"))}

{shell.figure(_("Fig. 01", "Şekil 01"),
  _("Eight weeks, then a measured comparison", "Sekiz hafta, ardından ölçülmüş bir karşılaştırma"),
  _("The six-stage comparison holds the corpus, split, seed and iteration budget fixed and adds "
    "one idea at a time. Each step improved in this run; the repository says plainly that "
    "improvement is not guaranteed for every configuration.",
    "Altı aşamalı karşılaştırma külliyatı, ayrımı, tohumu ve yineleme bütçesini sabit tutar ve "
    "her seferinde tek bir fikir ekler. Bu koşuda her adım iyileşme getirdi; depo, iyileşmenin "
    "her yapılandırmada garanti olmadığını açıkça söyler."),
  shell.plate(_("Fig. 01", "Şekil 01"),
              _("Path and measured stages", "Yol ve ölçülen aşamalar"), svg("neuron.svg")))}

<section class="fig">
{fighead(_("Results", "Sonuçlar"), _("What the trained models reached",
                                     "Eğitilen modellerin ulaştığı değerler"))}
{catalog([
    (_("Architecture gain", "Mimari kazancı"), _("−0.627", "−0,627"),
     _("Nats per character from bigram to the completed block, at a fixed CPU budget.",
       "Sabit CPU bütçesinde, bigramdan tamamlanmış bloğa karakter başına nat.")),
    (_("Shakespeare", "Shakespeare"), _("1.4723", "1,4723"),
     _("Final validation NLL after 5,000 updates; best sampled checkpoint 1.4657 at step 4,500.",
       "5.000 güncelleme sonrası son doğrulama NLL'si; örneklenen en iyi kontrol noktası 4.500. "
       "adımda 1,4657.")),
    (_("Turkish corpus", "Türkçe külliyat"), _("1.6239", "1,6239"),
     _("A 1.9M-character Nâzım Hikmet collection with a 118-character vocabulary. Not a ranking "
       "against English.",
       "118 karakterlik sözlüğe sahip, 1,9 milyon karakterlik bir Nâzım Hikmet derlemesi. "
       "İngilizceye karşı bir sıralama değildir.")),
    (_("Live inference", "Canlı çıkarım"), "Gradio",
     _("An optional panel loads the trained checkpoints and generates text next to the recorded "
       "evidence.",
       "İsteğe bağlı bir panel eğitilmiş kontrol noktalarını yükler ve kayıtlı kanıtın yanında "
       "metin üretir.")),
])}
  <p class="fig-note">{_(
    "The Turkish corpus was prepared from three user-selected PDFs with layout-aware extraction "
    "and OCR recovery of 243 pages. Raw texts, PDFs and checkpoints stay out of Git; only "
    "metrics, loss histories, plots and samples are published.",
    "Türkçe külliyat, kullanıcının seçtiği üç PDF'ten, sayfa düzenini gözeten çıkarım ve 243 "
    "sayfanın OCR ile kurtarılmasıyla hazırlandı. Ham metinler, PDF'ler ve kontrol noktaları "
    "Git'e girmez; yalnızca metrikler, kayıp geçmişleri, grafikler ve örnekler yayımlanır.")}</p>
</section>

{shell.prose(_("Sample", "Örnek"),
  _("What 4.8 million parameters can and cannot do", "4,8 milyon parametre neyi yapar, neyi yapamaz"),
  _("<p>An unedited excerpt generated by the Shakespeare model, not a quotation:</p>"
    "<p><code>KING RICHARD II: Shall I, be made to be exceeding?</code><br>"
    "<code>QUEEN ELIZABETH: My hard will I be?</code></p>"
    "<p>The model has learned speaker labels, line structure and plausible vocabulary. It has "
    "not learned meaning. A low character loss does not guarantee coherent writing, and the "
    "repository states that next to the samples.</p>",
    "<p>Shakespeare modelinin ürettiği, düzeltilmemiş bir kesit; alıntı değildir:</p>"
    "<p><code>KING RICHARD II: Shall I, be made to be exceeding?</code><br>"
    "<code>QUEEN ELIZABETH: My hard will I be?</code></p>"
    "<p>Model konuşmacı etiketlerini, dize yapısını ve akla yatkın bir söz dağarcığını öğrendi. "
    "Anlamı öğrenmedi. Düşük karakter kaybı tutarlı bir yazıyı garanti etmez; depo bunu "
    "örneklerin hemen yanında belirtir.</p>"))}

{shell.note(_("Limitations", "Sınırlar"),
  _("Educational scale, and stated as such. The larger runs change width, depth, context, "
    "training budget and precision together, so they are <strong>not an ablation</strong>; the "
    "six-stage CPU table is the controlled comparison, and it is not parameter-matched. The "
    "reported GPU losses were validated for internal consistency against the returned histories, "
    "not re-evaluated independently. The sequence follows Andrej Karpathy's lecture series.",
    "Eğitim amaçlı bir ölçek; öyle de belirtiliyor. Büyük koşular genişliği, derinliği, bağlamı, "
    "eğitim bütçesini ve hassasiyeti birlikte değiştirir; bu yüzden <strong>bir ablasyon "
    "değildir</strong>. Kontrollü karşılaştırma altı aşamalı CPU tablosudur ve parametre eşlemeli "
    "değildir. Raporlanan GPU kayıpları, dönen geçmiş kayıtlarına karşı iç tutarlılık açısından "
    "doğrulandı; bağımsız olarak yeniden değerlendirilmedi. Sıralama, Andrej Karpathy'nin ders "
    "serisini izler."))}
""")

    # ======================================================== 08 Pixel LLM
    project_page(
        "pixel-llm",
        spec_rows=[
            (_("Engine", "Motor"), "Godot 4.7.1 · GDScript"),
            (_("Structure", "Yapı"), _("One run = one model, ten stages",
                                      "Bir koşu = bir model, on aşama")),
            (_("Tiers", "Kademeler"),
             _("Intern ≈15 min · Researcher ≈25 min · Frontier ≈35 min",
               "Intern ≈15 dk · Researcher ≈25 dk · Frontier ≈35 dk")),
            (_("Languages", "Diller"), _("English and Turkish", "İngilizce ve Türkçe")),
            (_("Targets", "Hedefler"), _("Web demo first, then desktop",
                                        "Önce web demosu, sonra masaüstü")),
            (_("Status", "Durum"),
             _("In development · internal builds 0.2.0 · not yet released",
               "Geliştiriliyor · iç derleme 0.2.0 · henüz yayımlanmadı")),
        ],
        sections=f"""
{shell.prose(_("Why", "Neden"),
  _("The pipeline is the game", "Hat, oyunun kendisi"),
  _("<p>Most people meet a language model as a chat box. Everything that decides how it behaves "
    "happened earlier: which data was collected, what was filtered out, how text was cut into "
    "tokens, how large the network is, what it was rewarded for.</p>"
    "<p>Pixel LLM makes those ten stages playable and, more importantly, makes them depend on "
    "each other. A corpus cleaned carelessly in stage two produces noisier patterns in "
    "pre-training and a blurred view of the questions at evaluation. A small corpus cannot feed "
    "a large architecture. The player learns the pipeline by living with its consequences.</p>",
    "<p>Çoğu insan bir dil modeliyle bir sohbet kutusu olarak tanışır. Nasıl davranacağını "
    "belirleyen her şey ondan önce olmuştur: hangi verinin toplandığı, neyin süzüldüğü, metnin "
    "tokenlara nasıl bölündüğü, ağın ne kadar büyük olduğu, neyle ödüllendirildiği.</p>"
    "<p>Pixel LLM bu on aşamayı oynanabilir kılar ve daha da önemlisi birbirine bağlar. İkinci "
    "aşamada özensiz temizlenen bir külliyat, ön eğitimde daha gürültülü örüntüler ve "
    "değerlendirmede sorulara bulanık bir bakış üretir. Küçük bir külliyat büyük bir mimariyi "
    "besleyemez. Oyuncu hattı, sonuçlarıyla yaşayarak öğrenir.</p>"))}

{shell.figure(_("Fig. 01", "Şekil 01"),
  _("Ten stages, one model card", "On aşama, tek model kartı"),
  _("Stages do not know about each other. Each receives the model's profile, returns a validated "
    "result, and the run controller applies it. That contract is what lets a decision in stage "
    "one still matter in stage ten.",
    "Aşamalar birbirini bilmez. Her biri modelin profilini alır, doğrulanmış bir sonuç döndürür "
    "ve koşu denetleyicisi bunu işler. Birinci aşamadaki bir kararın onuncu aşamada hâlâ önem "
    "taşımasını sağlayan şey bu sözleşmedir."),
  shell.plate(_("Fig. 01", "Şekil 01"),
              _("Run structure and carry-over", "Koşu yapısı ve taşınan etkiler"),
              svg("pixel.svg")))}

<section class="fig">
{fighead(_("Design", "Tasarım"), _("How a run is shaped", "Bir koşu nasıl biçimlenir"))}
{catalog([
    (_("Stages", "Aşama"), "10",
     _("Data, cleaning, tokeniser, architecture, pre-training, evaluation, SFT, RLHF, red team, "
       "launch.",
       "Veri, temizleme, tokenizer, mimari, ön eğitim, değerlendirme, SFT, RLHF, kırmızı takım, "
       "lansman.")),
    (_("Tiers", "Kademe"), "3",
     _("Intern is correct but simple, Researcher adds real tensions, Frontier stays close to "
       "real practice.",
       "Intern doğru ama sade, Researcher gerçek gerilimleri ekler, Frontier gerçek pratiğe çok "
       "yakındır.")),
    (_("Run length", "Koşu süresi"), _("15–35 min", "15–35 dk"),
     _("Short enough to replay, so a different decision can be tried the same evening.",
       "Yeniden oynanacak kadar kısa; farklı bir karar aynı akşam denenebilir.")),
    (_("Ending", "Bitiş"), _("Model card", "Model kartı"),
     _("Generated from the stats and traits the run accumulated; each stage closes on one of at "
       "least three archetypes.",
       "Koşunun biriktirdiği stat ve etiketlerden üretilir; her aşama en az üç arketipten "
       "biriyle kapanır.")),
])}
</section>

{shell.prose(_("Engineering", "Mühendislik"),
  _("Game logic that runs without the engine", "Motor olmadan çalışan oyun mantığı"),
  _("<p>Rules, formulas and the economy live in engine-independent code with no scene "
    "dependencies, so they can be unit-tested and rebalanced without launching the game. Scenes "
    "handle presentation and input only.</p>"
    "<ul>"
    "<li>Balance values sit in JSON tables validated against a schema at load, not in code.</li>"
    "<li>Every stage extends one base contract and returns a result that validates itself at "
    "its boundary.</li>"
    "<li>Saves are written atomically with an automatic backup and a migration hook.</li>"
    "<li>All player text goes through translation keys from the first day, English first.</li>"
    "</ul>",
    "<p>Kurallar, formüller ve ekonomi, sahne bağımlılığı olmayan, motordan bağımsız kodda "
    "durur; böylece oyun açılmadan birim testi yapılabilir ve denge ayarlanabilir. Sahneler "
    "yalnızca sunumu ve girdiyi yönetir.</p>"
    "<ul>"
    "<li>Denge değerleri kodda değil, yüklenirken şemaya karşı doğrulanan JSON tablolarında "
    "durur.</li>"
    "<li>Her aşama tek bir temel sözleşmeyi genişletir ve kendi sınırında kendini doğrulayan bir "
    "sonuç döndürür.</li>"
    "<li>Kayıtlar atomik yazılır; otomatik yedek ve sürüm geçiş kancası vardır.</li>"
    "<li>Bütün oyuncu metinleri ilk günden çeviri anahtarlarından geçer; önce İngilizce.</li>"
    "</ul>"))}

<section class="fig">
{fighead(_("Film", "Film"), _("Trailer and a minute of play", "Fragman ve bir dakikalık oynanış"))}
  <p>{_("Captured from the current internal build.", "Güncel iç derlemeden çekildi.")}</p>
{shell.films(
    shell.film(_video(f"pixel-trailer-{lang}.mp4"), _video(f"pixel-trailer-{lang}.jpg"),
               _("Trailer · 20 s", "Fragman · 20 sn")),
    shell.film(_video(f"pixel-demo-{lang}.mp4"), _video(f"pixel-demo-{lang}.jpg"),
               _("Gameplay · 60 s", "Oynanış · 60 sn")))}
</section>

{shell.note(_("Status", "Durum"),
  _("<strong>In development under a working title.</strong> Internal web and Windows builds "
    "exist, external playtesting comes next, and no store page is live. The repository is "
    "private, so nothing here links out. The game teaches the pipeline; it does not train a "
    "real model.",
    "<strong>Geçici bir adla geliştiriliyor.</strong> İç web ve Windows derlemeleri var, sırada "
    "dış oyuncu testi bulunuyor ve yayında bir mağaza sayfası yok. Depo özeldir; bu yüzden "
    "buradaki hiçbir şey dışarıya bağlanmaz. Oyun hattı öğretir; gerçek bir model eğitmez."),
  warn=True)}
""")
