# 🛣️ Task 04: Yol Takibi & Hareket Kontrolü (Path Following & Motion Control)

## 🎯 Görevin Amacı & Açıklama
Otonom araç yazılım boru hattında algılama katmanı çevreyi tanımladıktan sonra, planlama katmanı güvenli bir referans yol (waypoint listesi) oluşturur. Hareket kontrolü (Motion Control) katmanı ise aracın mevcut konumu ile referans yol arasındaki sapmayı hesaplayarak direksiyon açısını ve hızı yönetir.

Bu görevde amacınız; Python ortamında temel yol takip kontrol algoritmalarını araştırmak, kendi kontrolcü algoritmanızı geliştirmek ve aracın belirlenen referans rotayı minimum sapmayla takip etmesini sağlamaktır.

---

## 🔍 Araştırma Başlıkları & Yönlendirici Sorular

Görevi tamamlarken aşağıdaki konuları araştırmanız ve uygulamanız beklenmektedir:

* **Yol Takip Kontrolcüleri:** Otonom sürüşte yaygın olarak kullanılan **Pure Pursuit**, **Stanley Algoritması** veya **PID tabanlı yanal kontrol** yaklaşımları nasıl çalışır? Matematiksel prensipleri nelerdir?
* **Araç Kinematiği:** Basit araç hareketlerini modellemek için kullanılan **Kinematik Bisiklet Modeli (Kinematic Bicycle Model)** yönelim ($\theta$), hız ve dingil mesafesi (wheelbase) değişkenlerini nasıl ilişkilendirir?
* **Lookahead Distance (İleri Bakış Mesafesi):** Kontrolcünün hedef aldığı ileri bakış mesafesi parametresinin araç kararlılığı ve viraj alma performansı üzerindeki etkisi nedir? (Çok küçük veya çok büyük seçilirse araç nasıl tepki verir?)
* **Hata Analizi:** Yanal sapma hatası (Cross-Track / Lateral Error) nasıl hesaplanır ve optimize edilir?

---

## 🛠️ Teknik Beklentiler

1. Python (NumPy ve Matplotlib kullanarak) ile bir referans rota (kıvrımlı bir yol, S virajı veya kapalı bir parkur) tanımlayın.
2. Seçtiğiniz yol takip kontrolcüsünü kodlayarak aracı bu rota boyunca simüle edin.
3. Parametreleri ayarlayarak (tuning) aracın rotayı başarıyla tamamlamasını sağlayın.
4. Aracın izlediği yörüngeyi ve oluşan hata miktarını grafik olarak görselleştirin.

---

## 📤 Submission (Teslimat) Kısmı

### Beklenen Çıktılar
1. **`path_follower.py`:** Kendi geliştirdiğiniz kontrolcü ve simülasyon Python scripti.
2. **`trajectory_plot.png`:** Referans rota ile aracın izlediği gerçek yörüngeyi gösteren grafik.
3. **`error_plot.png`:** Simülasyon boyunca oluşan rotadan sapma (Tracking Error) grafiği.
4. **`README.md`:** Seçtiğiniz algoritmayı, parametre seçimlerinizi ve hata grafiği analizlerinizi açıklayan kısa teknik rapor.

### Teslimat Formatı & Dizin Yapısı
Çalışmanızı sadece şu dizine ekleyiniz:
```text
training-program/task-04-path-planning-and-motion/submissions/<ad_soyad>/
├── path_follower.py
├── trajectory_plot.png
├── error_plot.png
└── README.md
```

### Git & PR Adımları
1. Yeni dal oluşturun:
   ```bash
   git checkout -b submission/<ad-soyad>/task-04
   ```
2. Dosyalarınızı kendi klasörünüze ekleyip commit atın:
   ```bash
   git add training-program/task-04-path-planning-and-motion/submissions/<ad_soyad>/
   git commit -m "feat(task-04): <Ad Soyad> yol takibi simülasyon teslimi"
   ```
3. Dalınızı uzak sunucuya gönderip GitHub üzerinden `main` dalına Pull Request (PR) açın.
