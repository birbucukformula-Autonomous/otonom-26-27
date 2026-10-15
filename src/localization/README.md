# 🧭 Localization & Mapping (Konumlandırma ve Haritalama) Modülü

## 🎯 Kapsam
Bu modül, aracın çevreye ve küresel koordinat sistemine göre nerede olduğunu yüksek hassasiyetle hesaplar ve harita oluşturur.

### Temel Çalışma Alanları
- **Durum Tahmini & Sensör Füzyonu:** GPS/GNSS, IMU (Ataletsel Ölçüm) ve Tekerlek Odometrisinin EKF (Extended Kalman Filter) ile birleştirilmesi.
- **SLAM (Simultaneous Localization and Mapping):** LiDAR ve Görsel (Visual) SLAM algoritmaları ile bilinmeyen ortamlarda eşzamanlı harita çıkarma ve konum kestirimi.
- **Harita Tabanlı Yerelleştirme:** Önceden çıkarılmış HD harita (HD Map) veya nokta bulutu haritası üzerinde yerelleştirme (NDT, ICP vb.).
