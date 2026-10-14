# 🛣️ Task 04: Yol Takibi & Hareket Kontrolü (Path Planning & Motion Control)

## 🎯 Görevin Amacı
Otonom sürüş boru hattında algılama (perception) katmanı çevredeki engelleri ve sınırları tespit ettikten sonra, planlama (planning) ve kontrol (control) katmanları devreye girer:
1. **Planlama (Planning):** Güvenli, çarpışmasız bir referans yol (waypoint listesi: $x, y$ koordinatları) oluşturur.
2. **Kontrol (Motion Control):** Aracın mevcut konumu ile referans yol arasındaki sapmayı (lateral ve heading error) hesaplayarak direksiyon açısını ve hızı belirler.

Bu görevin amacı; harici ağır simülatörlere ihtiyaç duymadan, Python ve Matplotlib ile çalışan saf 2D bir araç simülasyonunda temel bir yol takip algoritmasının (**Pure Pursuit** veya basit **Orantısal PID Kontrol**) mantığını kavramak ve parametre ayarlaması (tuning) yapmaktır.

---

## 🛠️ Ön Hazırlık
Gerekli kütüphaneleri kurun:
```bash
pip install numpy matplotlib
```

---

## 📝 Görev Adımları

### 1. Adım: Başlangıç Kodunu İnceleyin
Bu klasörde yer alan [starter_planner.py](file:///home/zuzu/Desktop/otonom-26-27/tasks/task-04-path-planning-and-motion/starter_planner.py) scriptini çalıştırın:
```bash
python3 starter_planner.py
```
Bu script:
* Sinüzoidal (kıvrımlı) bir referans yol üretir.
* Basit bir bisiklet modeli (Kinematic Bicycle Model) ile aracın hareketini simüle eder.
* Araç için bir **"Lookahead Distance" (İleri Bakış Mesafesi)** noktası seçip direksiyon açısını hesaplar.
* Sonuçları bir Matplotlib grafiğinde (Referans Yol vs. Aracın İzlediği Yol ve Hata Grafiği) görselleştirir.

### 2. Adım: Kontrolcü Parametrelerini İyileştirin (Tuning)
`starter_planner.py` dosyasındaki parametreleri inceleyin:
* `lookahead_distance` (İleri bakış mesafesi) çok küçük olursa araç yolda yalpalama (salınım) yapar.
* Çok büyük olursa virajları erken keser veya yoldan çıkar.
* Kontrol kazancını (`kp_steering`) ve ileri bakış mesafesini optimize ederek aracın referans rotayı minimum hatayla takip etmesini sağlayın.

### 3. Adım: Kendi Özel Rotanızı Ekleyin (Mini Meydan Okuma)
Script içerisindeki referans yol fonksiyonunu değiştirerek:
* İster bir S virajı (şikan),
* İster bir yarış pisti / oval parkur,
* İster keskin 90 derecelik bir dönüş ekleyin.
Aracınızın bu yeni rotayı başarıyla tamamladığını doğrulayın.

---

## 📤 Teslimat Formatı

Kendi adınıza açtığınız dalda (`submission/<ad-soyad>/task-04`), dosyalarınızı şu dizine ekleyin:

```text
tasks/task-04-path-planning-and-motion/submissions/<ad_soyad>/
├── path_follower.py          # İyileştirdiğiniz ve kendi rotanızı eklediğiniz Python scripti
├── trajectory_plot.png       # Matplotlib tarafından üretilen yörünge takip grafiği
├── error_plot.png            # Aracın rotadan sapma miktarını (Tracking Error) gösteren grafik
└── README.md                 # Parametre seçimlerinizi ve yaptığınız değişiklikleri açıklayan kısa rapor
```

---

## 💡 İpuçları
* **Pure Pursuit Formülü:** $\delta = \arctan\left(\frac{2 L \sin(\alpha)}{l_d}\right)$
  * $L$: Aracın dingil mesafesi (Wheelbase)
  * $\alpha$: Aracın burnu ile hedef nokta arasındaki açı
  * $l_d$: Lookahead mesafesi
  * $\delta$: Ön tekerlek direksiyon açısı
