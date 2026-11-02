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
            (_("Period", "Dönem"), _("September 2026", "Eylül 2026")),
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

    # ======================================================== 07 neuron-to-gpt

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
