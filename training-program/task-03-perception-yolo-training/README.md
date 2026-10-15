# 👁️ Task 03: Perception — YOLO ile Etiketleme & Mini Model Eğitimi

## 🎯 Görevin Amacı & Açıklama
Otonom araçların pistteki trafik konilerini, yayaları, diğer araçları veya trafik işaretlerini ayırt edebilmesi için derin öğrenme tabanlı nesne tespiti (Object Detection) algoritmaları kullanılır.

Bu görevde amacınız; bilgisayarlı görü boru hattının en kritik aşamaları olan veri toplama, veri etiketleme (annotation) ve YOLO mimarisi ile mini bir modeli transfer learning yöntemiyle eğitme süreçlerini bağımsız olarak araştırıp uygulamaktır.

---

## 🔍 Araştırma Başlıkları & Yönlendirici Sorular

Görevi tamamlarken aşağıdaki konuları araştırmanız ve uygulamanız beklenmektedir:

* **Veri Etiketleme (Annotation) & Formatlar:** Nesne tespitinde kullanılan Bounding Box koordinatları YOLO formatında (`class x_center y_center width height`) nasıl normalize edilir?
* **Etiketleme Araçları:** Roboflow, CVAT veya Label Studio gibi araçlar üzerinden veri seti nasıl oluşturulur, etiketlenir ve Train / Validation setlerine nasıl ayrılır?
* **Transfer Learning & Model Eğitimi:** Önceden eğitilmiş bir temel model (`yolov8n.pt` veya benzeri hafif mimariler) kullanılarak kendi veri setiniz üzerinde model eğitimi Python API veya CLI üzerinden nasıl başlatılır? (İpucu: GPU imkanı olmayanlar Google Colab'dan faydalanabilir).
* **Model Başarım Metrikleri:** Nesne tespit modellerinin doğruluğunu ölçen **Precision**, **Recall** ve **mAP (Mean Average Precision)** metrikleri ne anlama gelir?

---

## 🛠️ Teknik Beklentiler

1. Otonom sürüşle ilişkili bir nesne sınıfı (Örn: trafik konisi, dur levhası veya araçlar) belirleyerek **15-25 adet görselden** oluşan mini bir veri seti hazırlayın ve etiketleyin.
2. Modeli bu veri seti üzerinde eğitin.
3. Eğitilen model ile daha önce modele gösterilmemiş en az bir test görseli üzerinde nesne tespiti çıkarımı (inference) yapın.

---

## 📤 Submission (Teslimat) Kısmı

### Beklenen Çıktılar
1. **`results.png`:** Model eğitiminin kayıp (loss) ve mAP metrik grafiği.
2. **`test_detection.jpg`:** Modelin test görseli üzerinde nesneyi kutu içine aldığı tespit çıktısı.
3. **`data.yaml`:** Veri kümesi sınıf ve yol yapılandırma dosyası.
4. **`README.md`:** Seçtiğiniz nesne sınıfını, eğitim sürecini, aldığınız mAP skorunu ve yorumlarınızı içeren kısa teknik rapor.

### Teslimat Formatı & Dizin Yapısı
Çalışmanızı sadece şu dizine ekleyiniz:
```text
training-program/task-03-perception-yolo-training/submissions/<ad_soyad>/
├── results.png
├── test_detection.jpg
├── data.yaml
└── README.md
```

### Git & PR Adımları
1. Yeni dal oluşturun:
   ```bash
   git checkout -b submission/<ad-soyad>/task-03
   ```
2. Dosyalarınızı kendi klasörünüze ekleyip commit atın:
   ```bash
   git add training-program/task-03-perception-yolo-training/submissions/<ad_soyad>/
   git commit -m "feat(task-03): <Ad Soyad> YOLO model eğitimi teslimi"
   ```
3. Dalınızı uzak sunucuya gönderip GitHub üzerinden `main` dalına Pull Request (PR) açın.
