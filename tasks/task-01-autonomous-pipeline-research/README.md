# 📚 Task 01: Otonom Sürüş Mimarisi & Alt Disiplinler Araştırması

## 🎯 Görevin Amacı
Bir otonom araç yazılım mühendisi olmanın ilk adımı, aracın beynini oluşturan katmanların birbiriyle nasıl konuştuğunu anlamaktır. Bu görevin amacı; otonom sürüşün temel disiplinlerinden birini seçerek derinlemesine araştırma yapmak, sektörde kullanılan algoritmaları incelemek ve elde edilen bulguları takıma 5 dakikalık bir teknik sunum ile aktarmaktır.

---

## 🧭 Araştırma Alanları (Birini Seçiniz)

Aşağıdaki 4 temel disiplinden ilgi duyduğunuz **en az birini** seçiniz:

### 1. Algılama (Perception & Computer Vision)
* **Temel Soru:** Araç çevresini nasıl "görür" ve nesneleri nasıl tanır?
* **Araştırma Başlıkları:**
  * Kamera vs. LiDAR vs. Radar sensörlerinin avantajları, menzilleri ve kötü hava koşullarındaki (yağmur, sis, gece) performansları.
  * 2D Nesne Tespiti (YOLO, Faster R-CNN) ile 3D Point Cloud Segmentasyonu arasındaki farklar.
  * Sensör Füzyonu (Sensor Fusion) nedir ve neden tek bir sensör yeterli değildir?

### 2. Konumlandırma & Haritalama (Localization & SLAM)
* **Temel Soru:** GPS sinyali kaybolduğunda (tünel, kapalı alan, yüksek binalar) araç nerede olduğunu santimetre hassasiyetinde nasıl bilir?
* **Araştırma Başlıkları:**
  * GNSS/RTK + IMU (Ataletsel Ölçüm Birimi) ve Tekerlek Odometrisi nasıl birleştirilir? (Genişletilmiş Kalman Filtresi - EKF).
  * SLAM (Simultaneous Localization and Mapping) mantığı nedir? LiDAR SLAM (Cartographer, FAST-LIO) nasıl çalışır?

### 3. Yol ve Rota Planlama (Path & Trajectory Planning)
* **Temel Soru:** Araç A noktasından B noktasına giderken engellere çarpmadan en uygun rotayı nasıl çizer?
* **Araştırma Başlıkları:**
  * Global Planlama (A*, Dijkstra) ile Lokal Planlama (DWA - Dynamic Window Approach, TEB, Lattice Planner) farkları.
  * Statik engeller ile dinamik (hareket eden yaya, diğer araçlar) engellerden kaçma stratejileri.

### 4. Hareket & Araç Kontrolü (Motion Control & Vehicle Dynamics)
* **Temel Soru:** Planlanan çizgi üzerinde kalmak için direksiyon açısı ve gaz/fren torku nasıl hesaplanır?
* **Araştırma Başlıkları:**
  * Geometrik Kontrolcüler (Pure Pursuit, Stanley Algoritması) nasıl çalışır?
  * Model Tabanlı Kontrolcüler (PID Kontrol, MPC - Model Predictive Control) nedir?
  * Acil Durum Frenleme (AEB / ASB) sistemleri ve güvenlik prensipleri.

---

## 📝 Görev Çıktısı & Teslimat Formatı

1. **Sunum Dosyası:** Seçtiğiniz konuyu anlatan **5 ila 8 slaytlık** bir sunum hazırlayın (`.pdf` veya `.pptx` formatında).
   * Sunumda teorik açıklamaların yanında en az 2 adet şematik diyagram, mimari görsel veya algoritma akış şeması bulunmalıdır.
   * [presentation_template.md](file:///home/zuzu/Desktop/otonom-26-27/tasks/task-01-autonomous-pipeline-research/presentation_template.md) dosyasındaki yapıyı referans alabilirsiniz.
2. **Kısa Özet Raporu:** `ozet.md` adında 1 sayfalık teknik özet çıkarın (Seçtiğiniz konu, karşılaşılan temel zorluklar, kullanılan kütüphaneler/araçlar).
3. **Takım İçi Sunum:** Hazırladığınız sunumu haftalık teknik toplantımızda takıma 5 dakika süreyle sunacaksınız.

---

## 📤 Teslim Adımları

1. Kendi adınıza dal açın:
   ```bash
   git checkout -b submission/<ad-soyad>/task-01
   ```
2. Dosyalarınızı yalnızca şu dizine yükleyin:
   ```text
   tasks/task-01-autonomous-pipeline-research/submissions/<ad_soyad>/
   ├── sunum.pdf
   └── ozet.md
   ```
3. Commit atıp uzak sunucuya pushlayın ve Pull Request (PR) açın:
   ```bash
   git add tasks/task-01-autonomous-pipeline-research/submissions/<ad_soyad>/
   git commit -m "feat(task-01): <Ad Soyad> mimari araştırma teslimi"
   git push origin submission/<ad-soyad>/task-01
   ```
