# 🚗 Otonom Araç Çekirdek Geliştirme Alanı (`src/`)

Bu dizin, **otonom-26-27** ekibinin ana otonom araç yazılım boru hattını (pipeline) geliştirdiği çalışma alanıdır. Sistem, endüstri standardı modüler otonom mimarisine uygun olarak alt disiplinlere ayrılmıştır.

---

## 🏗️ Alt Modüller ve Sorumluluk Alanları

* **[`perception/`](file:///home/zuzu/Desktop/otonom-26-27/src/perception/README.md):** Kamera ve LiDAR verilerini işleyen derin öğrenme tabanlı nesne tespiti, şerit/sınır tespiti ve zemin filtreleme algoritmaları.
* **[`localization/`](file:///home/zuzu/Desktop/otonom-26-27/src/localization/README.md):** GPS/RTK, IMU ve tekerlek odometrisi verilerini EKF ile birleştiren durum tahmini ve SLAM tabanlı haritalama sistemleri.
* **[`path_planning/`](file:///home/zuzu/Desktop/otonom-26-27/src/path_planning/README.md):** Küresel harita üzerinde rota hesaplayan global planlayıcılar ve dinamik engellerden kaçınan yerel (lokal) yörünge üreticileri.
* **[`motion_control/`](file:///home/zuzu/Desktop/otonom-26-27/src/motion_control/README.md):** Üretilen referans yolu takip eden Pure Pursuit, Stanley veya MPC gibi yanal ve boylamsal araç kontrolcüleri.
* **[`ros2_system/`](file:///home/zuzu/Desktop/otonom-26-27/src/ros2_system/README.md):** Ortak ROS 2 mesaj tanımları (`custom msgs`), launch dosyaları ve simülasyon (Gazebo / Webots / 2D) köprüleri.

---

## 📌 Geliştirme Kuralları
1. Yeni bir özellik veya algoritma geliştirirken ilgili alt modülün altında çalışınız.
2. Modüller arası haberleşme standart ROS 2 topic ve service arayüzleri üzerinden yürütülmelidir.
3. Her modül kendi bağımsız birim testlerine ve dökümantasyonuna sahip olmalıdır.
