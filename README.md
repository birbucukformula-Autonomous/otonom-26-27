# 🚗 Otonom Sürüş Sistemleri — Yeni Üye Oryantasyon & Eğitim Kampı

> **Hoş Geldin!** Bu repo, otonom araç yazılım ekibimize katılan yeni üyelerin otonom sürüş mimarisini teorik ve uygulamalı olarak öğrenmesi, simülasyon araçlarına alışması ve profesyonel Git iş akışını deneyimlemesi için tasarlanmış bir **eğitim ve oryantasyon (training sandbox)** merkezidir.

Buradaki görevleri başarıyla tamamlayan üyeler, ekibimizin ana geliştirme repolarına ve ileri düzey simülasyon / araç projelerine dahil edilir.

---

## 🧭 Otonom Sürüş Mimarisine Genel Bakış

Bir otonom aracın karar verip hareket edebilmesi için veri akışı şu temel katmanlardan geçer:

```text
  [1. SENSÖRLER]          Kamera, LiDAR, Radar, IMU, GNSS, Odometri
        │
        ▼
  [2. ALGILAMA (Perception)]       Nesne Tespiti (YOLO), Şerit Takibi, Zemin Filtreleme
        │
        ▼
  [3. KONUMLANDIRMA & HARİTALAMA]  SLAM, EKF Sensör Füzyonu, Durum Tahmini
        │
        ▼
  [4. YOL PLANLAMA (Planning)]     Global Rota (A*, Dijkstra) & Lokal Engelden Kaçma
        │
        ▼
  [5. HAREKET KONTROLÜ (Motion)]   Hız & Direksiyon Kontrolü (Pure Pursuit, PID, MPC)
        │
        ▼
  [6. ARAÇ / SİMÜLASYON]  Gazebo, RViz2, Webots, 2D Dinamik Simülatörler
```

---

## 🛠️ Ön Hazırlık & Çalışma Ortamı

Bu repodaki görevler fiziksel araç gerektirmez; **tamamen simülasyon ve yazılım odaklıdır**. Görevlere başlamadan önce geliştirme ortamınızı hazırlamanız gerekmektedir:

### 1. İşletim Sistemi
* **Önerilen:** **Ubuntu 22.04 LTS (Jammy Jellyfish)**
* *Windows kullanıcıları için:* İkinci işletim sistemi (Dual Boot) en yüksek performansı verir. Alternatif olarak **WSL2 (Windows Subsystem for Linux)** üzerine Ubuntu 22.04 kurulabilir.

### 2. Çekirdek Yazılımlar
* **ROS 2:** **Humble Hawksbill** (LTS sürümü)
  * Kurulum adımları için [resources/ubuntu_and_ros2_humble_setup.md](file:///home/zuzu/Desktop/otonom-26-27/resources/ubuntu_and_ros2_humble_setup.md) kılavuzunu inceleyebilirsiniz.
* **Python:** Python 3.10+
* **Temel Kütüphaneler:**
  ```bash
  pip install numpy opencv-python matplotlib ultralytics
  ```
* **Kod Editörü:** Visual Studio Code (Önerilen eklentiler: *Python*, *ROS*, *C/C++*, *GitLens*)

---

## 📋 Eğitim Programı & Görev Haritası

Eğitim kampı 4 ana görevden oluşur. Her üyenin görevleri sırasıyla tamamlaması beklenir:

| Görev | Başlık | Odak Alanı | Çıktı / Teslim |
| :--- | :--- | :--- | :--- |
| [Task 01](file:///home/zuzu/Desktop/otonom-26-27/tasks/task-01-autonomous-pipeline-research/README.md) | **Otonom Boru Hattı Araştırması & Sunum** | Algılama, SLAM, Planlama veya Kontrol | 5-7 slaytlık sunum + 5 dk takım içi sunum |
| [Task 02](file:///home/zuzu/Desktop/otonom-26-27/tasks/task-02-ros2-communication-basics/README.md) | **ROS 2 Humble Temelleri & Simülatör Hareketi** | Node, Topic, Publisher/Subscriber, Twist mesajları | Python ROS 2 düğümü + Simülasyon ekran görüntüsü |
| [Task 03](file:///home/zuzu/Desktop/otonom-26-27/tasks/task-03-perception-yolo-training/README.md) | **Perception: YOLO ile Etiketleme & Mini Model Eğitimi** | Bilgisayarlı Görü, Roboflow/CVAT, YOLO eğitimi | Eğitim metrikleri grafiği + Bounding box tespit görseli |
| [Task 04](file:///home/zuzu/Desktop/otonom-26-27/tasks/task-04-path-planning-and-motion/README.md) | **Yol Takibi & Hareket Kontrolü (Planning & Motion)** | Waypoints, Rota Takibi, Pure Pursuit / PID mantığı | Rota takip kodu + Yörünge grafiği / simülasyon çıktısı |

---

## 🚀 Görev Teslim (Submission) Süreci

Takımımızda kod ve rapor teslimleri endüstri standardı olan **Git Pull Request (PR)** yöntemiyle yapılır.

1. **Repoyu Klonlayın:**
   ```bash
   git clone https://github.com/birbucukformula-Autonomous/otonom-26-27.git
   cd otonom-26-27
   ```
2. **Kendi Dalınızı (Branch) Oluşturun:**
   ```bash
   git checkout -b submission/<ad-soyad>/task-01
   # Örnek: git checkout -b submission/ahmet-yilmaz/task-01
   ```
3. **Çalışmanızı İlgili Klasöre Ekleyin:**
   * Dosyalarınızı **yalnızca** ilgili görevin altındaki `submissions/<ad_soyad>/` dizinine ekleyin:
     ```text
     tasks/task-01-autonomous-pipeline-research/submissions/ahmet_yilmaz/
     ```
   * *Not: Bu kural, başka üyelerin dosyalarıyla çakışma (merge conflict) yaşanmasını engeller.*
4. **Commit & Push:**
   ```bash
   git add tasks/task-01-autonomous-pipeline-research/submissions/ahmet_yilmaz/
   git commit -m "feat(task-01): Ahmet Yilmaz sunum teslimi"
   git push origin submission/ahmet-yilmaz/task-01
   ```
5. **Pull Request (PR) Açın:**
   * GitHub üzerinden `main` dalına doğru PR açın.
   * PR açıklamasındaki kontrol listesini doldurun. Mentörünüz PR'ı inceleyip geri bildirim verecektir.

Ayrıntılı rehber için [CONTRIBUTING.md](file:///home/zuzu/Desktop/otonom-26-27/CONTRIBUTING.md) belgesini inceleyin.

---

## ❓ Sıkça Sorulan Sorular & İletişim

* **S: Bilgisayarım Ubuntu kaldırmıyor, ne yapmalıyım?**  
  *C:* Windows 10/11 üzerinde WSL2 (Ubuntu 22.04) kurarak çalışabilirsiniz. Task 03 (YOLO) için ise ücretsiz Google Colab GPU'larını kullanabilirsiniz.
* **S: Takıldığım yerlerde kimden yardım alabilirim?**  
  *C:* Takım Discord/Slack kanalımızdaki `#otonom-onboarding` kanalından sorularınızı sorabilir veya takım liderlerine ulaşabilirsiniz.