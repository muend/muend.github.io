# Batı Antalya Tarımsal Kalkınma Rehberi (Agri-DSS Prototipi)

[![Durum](https://img.shields.io/badge/status-concept_&_prototype-green.svg)](https://)
[![Lisans](https://img.shields.io/badge/license-Özel_Lisans_(Tescilli)-red.svg)](#8--lisans)

Bu proje, Batı Antalya (Demre, Finike, Kaş, Kemer, Kumluca) koridorundaki çiftçiler ve tarım yatırımcıları için **veri-odaklı bir Karar Destek Sistemi (Decision Support System - DSS)** sunan bir SaaS (Software as a Service) prototipidir.

---

## 1. 🎯 Projenin Amacı ve Çözdüğü Sistemik Problem

### Problem: "Ortakların Trajedisi" (Tragedy of the Commons)
Tarımsal üretimde sıkça karşılaşılan bir problem, çiftçilerin birbirinden habersiz şekilde, o an kârlı görünen ürüne (örn: domates) yönelmesidir. Bu durum, hasat döneminde **arz fazlasına (piyasa çakılması)**, fiyatların maliyetin altına düşmesine, ürünlerin israf olmasına ve çiftçinin zarar etmesine yol açar.

### Çözüm: Veri-Odaklı Koordinasyon
Bu proje, "Hava durumu nasıl?" veya "Ne zaman gübre atılır?" gibi standart tarım uygulamalarının ötesine geçmeyi hedefler. Temel amacı, her mahalle/parsel için **kârlılığı optimize edecek** ürünü önermektir.

Bunu yaparken sadece toprağı ve iklimi değil, aynı zamanda **tahmini pazar fiyatlarını** ve bölgedeki **diğer üreticilerin eğilimlerini** (gelecek fazda) analiz ederek "Hangi ürünü ekersen, hasat zamanı hem yüksek verim alır hem de pazar fiyatı yüksek olacağı için maksimum kârı elde edersin?" sorusuna cevap arar.

## 2. ✨ Prototipin Temel Özellikleri

Mevcut prototip (bu repodaki `index.html`), sistemin kullanıcı arayüzünü (UI) ve temel iş mantığını *kavramsal verilerle* (mock data) göstermektedir:

* **Dinamik Bölge Seçimi:** İlçe ve mahalle bazında filtreleme.
* **Kısa Vadeli Tavsiyeler (Sezonluk):** Seçilen bölge için en uygun 3 adet sezonluk tarım ürününü (örn: Domates, Biber) gösterir.
    * Tahmini Verim (Yüksek/Orta/Düşük)
    * Tahmini Kârlılık (Yüksek/Orta/Düşük)
    * Sistem Notu (Neden bu ürünün seçildiğine dair agronomik/ekonomik gerekçe).
* **Uzun Vadeli Tavsiye (Yatırım):** Bölgenin iklim ve arazi yapısına uygun uzun vadeli yatırım ürünlerini (örn: Avokado, Zeytin, Badem) önerir.
* **Kavramsal Pazar Analizi:** Sistemin gelecekte sunacağı pazar açığı/fırsat analizini (örn: "Organik Biber", "Tıbbi Aromatik Bitkiler") simüle eder.
* **Yazdırılabilir Rapor:** Oluşturulan analizin, muhtarlık panoları veya kooperatifler için A4 formatında yazdırılabilmesini sağlar.

## 3. 📸 Ekran Görüntüleri

Prototipin ana arayüzü ve örnek bir analiz sonucu aşağıdadır.

**Bölge Seçim Ekranı:**
<img width="965" height="308" alt="image" src="https://github.com/user-attachments/assets/f18a34cc-6043-4fb6-b026-4fcd95faa859" />


**Örnek Analiz Sonuçları:**
<img width="973" height="783" alt="image" src="https://github.com/user-attachments/assets/fb0c624d-ca01-4135-bba3-e7982717e7da" />

<img width="930" height="799" alt="image" src="https://github.com/user-attachments/assets/e9c648dd-5d62-49d5-9fe5-ebee160397dd" />


## 4. 🏛️ Gelecek Vizyonu ve Hedeflenen Sistem Mimarisi

Bu prototip, aşağıda mimarisi çizilen tam teşekküllü, otonom bir SaaS platformunun ilk adımıdır.

### Hedeflenen Mimari (Kavramsal)

```
[KULLANICI (Çiftçi/Yatırımcı)]
       |
       v
[FRONTEND (Web/Mobil Uygulama)]
       |
       v
[BACKEND API (Python - FastAPI)]
       |
       +------------------+------------------+
       |                  |                  |
       v                  v                  v
[Abonelik/Kullanıcı]  [Veri Boru Hatları]  [ML Modelleri (MLOps)]
(PostgreSQL)          (Apache Airflow)     (Scikit-learn / Keras)
                          |                  |
                          v                  |
                  [VERİ KAYNAKLARI]          |
                  - MGM (İklim)              |
                  - Borsa/Hal (Fiyat)        |
                  - TARSİM (Risk)            |
                  - Sentinel (Uydu)          |
                  - IoT (Toprak Sensörleri)  |
                          |                  |
                          +------------------+
                                   |
                                   v
                      [ANALİZ MOTORU (Optimizasyon)]
                     (Kâr = (Fiyat x Verim) - Maliyet)
```

### Yol Haritası (Roadmap)

-   **[✔️] Faz 0: Konsept ve Prototip**
    -   Kullanıcı arayüzü (UI/UX) tasarımı.
    -   Kavramsal verilerle iş mantığının simülasyonu (Mevcut durum).

-   **[ ] Faz 1: MVP (Minimum Viable Product)**
    -   Gerçek veritabanı (PostgreSQL + PostGIS) kurulumu.
    -   Ziraat mühendisleri ve uzmanlarla **Kural Tabanlı Motor (Rule-Based Engine)** oluşturulması.
    -   Pilot bölgede (örn: Kumluca) ilk 20 pilot kullanıcı ile sistemin doğrulanması.

-   **[ ] Faz 2: Veri Altyapısı ve İlk ML Modeli**
    -   MGM (hava durumu) ve Borsa/Hal (fiyat) verileri için otomatik **Veri Boru Hatları (Data Pipelines)** kurulması.
    -   İlk **Verim Tahmin Modeli** (ML - örn: XGBoost) geliştirilmesi.

-   **[ ] Faz 3: Otonom SaaS ve MLOps**
    -   **Fiyat Tahmin Modeli** (Zaman Serisi - örn: LSTM) entegrasyonu.
    -   Modellerin yeni verilerle kendini otomatik güncellemesi için MLOps altyapısı.
    -   Abonelik (Stripe/Iyzico) ve kullanıcı yönetimi sisteminin eklenmesi.

-   **[ ] Faz 4: Ölçeklenme ve Ekosistem**
    -   Sistemin İzmir, Mersin gibi diğer tarım havzalarına genişletilmesi.
    -   Üreticilerle alıcıları (ihracatçılar, otel zincirleri) buluşturan bir **Pazar Yeri (Marketplace)** modülünün eklenmesi.
    -   Toprak nem/EC sensörleri için **IoT entegrasyonu**.

## 5. 💻 Kullanılan Teknolojiler

### Prototip (Mevcut)
* **Frontend:** HTML5, Tailwind CSS, JavaScript (ES6+)

### Hedeflenen (Gelecek)
* **Backend:** Python (FastAPI / Django)
* **Veritabanı:** PostgreSQL + PostGIS (Coğrafi veriler için)
* **Veri Bilimi (ML):** Pandas, Scikit-learn, TensorFlow/Keras
* **Veri Mühendisliği (ETL):** Apache Airflow
* **DevOps/MLOps:** Docker, Kubernetes, Kubeflow/MLflow

## 6. 🚀 Prototipi Yerel Olarak Çalıştırma

Bu prototip, sunucu taraflı bir dil veya derleme süreci gerektirmez.

1.  Bu repoyu klonlayın:
    ```bash
    git clone [https://github.com/muend.github.io](https://github.com/muend.github.io)
    ```

2.  Dizine gidin:
    ```bash
    cd muend.github.io
    ```
3.  `index.html` dosyasını tarayıcınızda açmanız yeterlidir.
4.  Görsellerin `README.md` dosyasında görünmesi için, klonladığınız dizin içinde `img` adında bir klasör oluşturun ve `selection_panel.png` ile `results_panel.png` dosyalarını bu klasörün içine taşıyın.

## 7. ✍️ Yazar

* **Muhammed Enes Duran**
    * [GitHub Profilim](https://github.com/muend)


## 8. 📄 Lisans

Copyright (c) 2025 muend. All rights reserved.

Tüm hakları saklıdır. Bu depodaki kaynak kodu, dokümanlar ve diğer materyaller ("Yazılım") üzerinde açıkça yazılı izin alınmaksızın kopyalama, değiştirme, dağıtma, alt lisanslama, satma, kiralama veya türev eser oluşturma hakları verilmez.

### Katkılar / Contributions
- Katkıları kabul ediyorum. Herhangi bir kişi bu depo için (pull request, issue, düzeltme, dokümantasyon, ikon/görsel vb. her türlü katkı) gönderdiğinde, katkıda bulunan şu hakları otomatik olarak muend'e (repo sahibi) verir:
  1) Bu katkıyı, türev dâhil olmak üzere, dünya çapında, süresiz, geri alınamaz, münhasır olmayan, telifsiz (royalty-free) bir lisans ile kullanma, kopyalama, değiştirme, birleştirme ve dağıtma hakkı;
  2) Bu katkının kodunu ticari veya ticari olmayan amaçlarla kullanma, alt lisanslama ve ticarileştirme hakkı.
- Katkıda bulunmadan önce sağduyulu davranılması ve eğer özel/telefonla/özgün bir sözleşme beklentisi varsa önce repo sahibiyle (medcoderz@hotmail.com) yazışılması önerilir.

### İzin talepleri / Lisans istisnaları
- Yazılımı kullanmak, kopyalamak veya değiştirmek için özel bir izin gerekiyorsa, lütfen medcoderz@hotmail.com adresinden yazılı olarak başvurun. Herhangi bir özel izin ancak yazılı olarak ve açık şekilde verildiğinde geçerli olacaktır.

### Sorumluluk reddi
- Bu Yazılım "OLDUĞU GİBİ" (AS IS) sağlanır; açık veya örtülü hiçbir garanti verilmez. Yazar/sağlayıcı, kullanım sonucu doğabilecek zararlardan sorumlu tutulamaz. Hukuki ve ticari sorumluluklar için lütfen hukuki danışmanlık alınız.
`

http://googleusercontent.com/immersive_entry_chip/0
