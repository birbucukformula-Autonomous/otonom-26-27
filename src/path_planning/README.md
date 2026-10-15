# 🗺️ Path & Trajectory Planning (Yol ve Yörünge Planlama) Modülü

## 🎯 Kapsam
Bu modül, aracın başlangıç noktasından hedef noktasına çarpışmasız, güvenli ve kinematik olarak uygulanabilir bir yörünge çizmesini sağlar.

### Temel Çalışma Alanları
- **Global Rota Planlama:** A*, Dijkstra veya Search tabanlı algoritmalarla statik harita üzerinde en uygun yolun hesaplanması.
- **Lokal (Yerel) Planlama & Engelden Kaçma:** Dinamik engeller karşısında anlık yol güncellemesi (DWA, TEB, Lattice Planner).
- **Hız Profili & Yörünge Üretimi:** Kinematik kısıtlar (maksimum ivme, yanal savrulma sınırları) gözetilerek zamana bağlı hız profili atanması.
