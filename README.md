# 🚗 Otonom 26-27 — Otonom Sürüş Sistemleri Ana Deposu

> **Otonom 26-27**, 2026-2027 sezonu için otonom araç yazılım sistemlerinin (algılama, konumlandırma, planlama ve kontrol) geliştirildiği, simüle edildiği ve yeni üyelerin yetiştirildiği merkezi çalışma alanıdır.

Bu repo hem ekibin **ana otonom yazılım geliştirme ortamını (`src/`)** hem de ekibe yeni katılan üyelerin oryantasyonunu sağlayan **eğitim programını (`training-program/`)** bünyesinde barındırır.

---

## 🧭 Otonom Sürüş Mimarisi

Sistemimiz modüler bir boru hattı (pipeline) yapısında çalışır. Veri akışı aşağıdaki katmanlar üzerinden yürütülür:

```text
  ┌─────────────────────────────────────────────────────────────┐
  │ 1. SENSÖRLER (Kamera, LiDAR, Radar, IMU, GNSS, Odometri)   │
  └──────────────────────────────┬──────────────────────────────┘
                                 │
                                 ▼
  ┌─────────────────────────────────────────────────────────────┐
  │ 2. ALGILAMA (src/perception)                                │
  │    Nesne Tespiti (YOLO), Şerit Takibi, Zemin Filtreleme     │
  └──────────────────────────────┬──────────────────────────────┘
                                 │
                                 ▼
  ┌─────────────────────────────────────────────────────────────┐
  │ 3. KONUMLANDIRMA & HARİTALAMA (src/localization)            │
  │    SLAM, EKF Sensör Füzyonu, Durum Kestirimi (State Est.)   │
  └──────────────────────────────┬──────────────────────────────┘
                                 │
                                 ▼
  ┌─────────────────────────────────────────────────────────────┐
  │ 4. YOL PLANLAMA (src/path_planning)                         │
  │    Global Rota (A*, Dijkstra) & Dinamik Engelden Kaçma      │
  └──────────────────────────────┬──────────────────────────────┘
                                 │
                                 ▼
  ┌─────────────────────────────────────────────────────────────┐
  │ 5. HAREKET KONTROLÜ (src/motion_control)                    │
  │    Pure Pursuit, Stanley, PID & MPC ile Araç Dinamiği       │
  └──────────────────────────────┬──────────────────────────────┘
                                 │
                                 ▼
  ┌─────────────────────────────────────────────────────────────┐
  │ 6. SİSTEM & SİMÜLASYON (src/ros2_system)                    │
  │    ROS 2 Humble Düğümleri, Mesajlar, Gazebo / 2D Simülatör  │
  └─────────────────────────────────────────────────────────────┘
```

---

## 📁 Depo Dizin Yapısı (Architecture)

Proje iki ana bölüme ayrılmıştır:

```text
otonom-26-27/
├── README.md                      # Proje genel tanıtımı ve mimari kılavuz
├── LICENSE                        # Proje açık kaynak lisansı
│
├── training-program/              # 🎓 Yeni Üye Eğitim & Oryantasyon Kampı
│   ├── README.md                  # Eğitim programı kılavuzu ve teslim kuralları
│   ├── task-01-autonomous-pipeline-research/  # Otonom mimari araştırması ve sunum
│   ├── task-02-ros2-communication-basics/     # ROS 2 düğüm temelleri ve Turtlesim
│   ├── task-03-perception-yolo-training/      # YOLO ile etiketleme ve model eğitimi
│   └── task-04-path-planning-and-motion/      # Yol takip ve hareket kontrol simülasyonu
│
└── src/                           # 🚀 Çekirdek Otonom Araç Geliştirme Alanı
    ├── README.md                  # Çekirdek yazılım mimarisi
    ├── perception/                # Kamera, LiDAR işleme ve nesne tespiti
    ├── localization/              # Haritalama (SLAM), sensör füzyonu ve odometri
    ├── path_planning/             # Global rota ve lokal yörünge planlayıcılar
    ├── motion_control/            # Yanal ve boylamsal araç kontrolcüleri
    └── ros2_system/               # Özel ROS 2 mesajları, launch dosyaları ve simülasyon
```

---

## 🛠️ Teknoloji Yığını & Geliştirme Ortamı

* **İşletim Sistemi:** Ubuntu 22.04 LTS (Jammy Jellyfish) *(veya Windows WSL2)*
* **Robotik Ara Katmanı:** ROS 2 Humble Hawksbill (LTS)
* **Programlama Dilleri:** Python 3.10+, C++17/20
* **Kütüphaneler:** NumPy, OpenCV, PyTorch / Ultralytics YOLO, Matplotlib
* **Simülasyon Araçları:** Turtlesim, RViz2, Gazebo / Webots

---

## 🚀 Başlarken

### 1. Yeni Üyeler İçin (Eğitim Kampı)
Ekibe yeni katıldıysanız doğrudan **[`training-program/`](file:///home/zuzu/Desktop/otonom-26-27/training-program/README.md)** dizinine geçiş yapın. Buradaki görevleri sırasıyla tamamlayarak pull request (PR) açmanız beklenmektedir.

### 2. Çekirdek Geliştiriciler İçin (Ana Sistem)
Aracın ana algoritmaları üzerinde çalışmak için **[`src/`](file:///home/zuzu/Desktop/otonom-26-27/src/README.md)** dizinindeki ilgili modülü seçip standart Git akışıyla dal açarak katkıda bulunabilirsiniz.