# 👁️ Task 03: Perception — YOLO ile Veri Etiketleme & Mini Model Eğitimi

## 🎯 Görevin Amacı
Otonom araçların çevresindeki araçları, yayaları, trafik levhalarını veya pistteki trafik konilerini ayırt edebilmesi için derin öğrenme tabanlı nesne tespiti (Object Detection) modelleri kullanılır.

Bu görevin amacı:
1. Gerçek dünya veya simülasyon ortamından toplanan görseller üzerinde **etiketleme (annotation)** mantığını öğrenmek.
2. Roboflow, CVAT veya Label Studio gibi modern bir etiketleme aracı kullanarak mini bir veri seti (15-25 görsel) hazırlamak.
3. Hazırlanan veri seti ile Google Colab (ücretsiz GPU) veya yerel bilgisayarınızda **Ultralytics YOLO (YOLOv8 veya YOLOv11)** kullanarak transfer learning ile mini bir model eğitmek.
4. Eğitilen modeli yeni bir test görseli üzerinde çalıştırıp tespit sonuçlarını (bounding box ve doğruluk skoru) görselleştirmek.

---

## 🛠️ Ön Hazırlık
Gerekli Python kütüphanelerini kurun:
```bash
pip install ultralytics opencv-python matplotlib
```
*Not: Model eğitimi için güçlü bir GPU'nuz yoksa [Google Colab](https://colab.research.google.com/) üzerinden ücretsiz T4 GPU kullanarak 2-3 dakikada modelinizi eğitebilirsiniz.*

---

## 📝 Görev Adımları

### 1. Adım: Veri Seti Konusunu Seçin & Görselleri Toplayın
Aşağıdaki sınıflardan birini seçebilirsiniz:
* **Trafik Konileri (Önerilen):** Sarı, mavi veya turuncu koniler.
* **Trafik İşaretleri / Levhalar:** Dur levhası, hız sınırı, yaya geçidi.
* **Yol Engelleri / Araçlar:** Oyuncak arabalar, yayalar vb.

İnternetten veya [sample_images/](file:///home/zuzu/Desktop/otonom-26-27/tasks/task-03-perception-yolo-training/sample_images/README.md) rehberindeki açık kaynak veri setlerinden **15 ila 25 adet görsel** belirleyin.

### 2. Adım: Veri Etiketleme (Annotation)
1. [Roboflow](https://roboflow.com/) veya [CVAT](https://www.cvat.ai/) üzerinde ücretsiz bir hesap açın.
2. Görsellerinizi yükleyin ve nesnelerin etrafına Bounding Box (Kutu) çizerek sınıf adını (örn: `cone`, `car`, `sign`) belirleyin.
3. Veri setinizi **YOLOv8 formatında** dışa aktarın (Train: %80, Val: %20 oranında bölünmüş olmalıdır). Roboflow size bir `data.yaml` dosyası ve görsel/etiket klasörleri verecektir.

### 3. Adım: Modeli Eğitin (Training)
[train_yolo_example.py](file:///home/zuzu/Desktop/otonom-26-27/tasks/task-03-perception-yolo-training/train_yolo_example.py) scriptini veya Google Colab notebook'unu kullanarak modeli eğitin:

```python
from ultralytics import YOLO

# Hafif nano model ile transfer learning başlatıyoruz
model = YOLO('yolov8n.pt')

# Modeli 15 epoch eğitiyoruz
results = model.train(data='data.yaml', epochs=15, imgsz=640)
```

### 4. Adım: Test ve Çıkarım (Inference)
Eğitilen `best.pt` ağırlıklarını kullanarak daha önce modele gösterilmemiş 1-2 test görseli üzerinde tahmin yapın:

```python
# Eğitilen modelle tahmin
model = YOLO('runs/detect/train/weights/best.pt')
results = model('test_image.jpg', save=True)
```

---

## 📤 Teslimat Formatı

Kendi adınıza açtığınız dalda (`submission/<ad-soyad>/task-03`), dosyalarınızı şu dizine ekleyin:

```text
tasks/task-03-perception-yolo-training/submissions/<ad_soyad>/
├── results.png                # Model eğitiminin loss/mAP metrik grafiği (runs/.../results.png)
├── test_detection_1.jpg       # Modelin tahmin yapıp kutu çizdiği test görseli 1
├── test_detection_2.jpg       # Modelin tahmin yapıp kutu çizdiği test görseli 2
├── data_sample.yaml           # Roboflow'dan aldığınız yapılandırma dosyası
└── README.md                  # Hangi sınıfı etiketlediğinizi ve mAP skorunuzu açıklayan rapor
```

---

## 💡 İpuçları
* Nano model (`yolov8n.pt` veya `yolo11n.pt`) çok hafiftir ve az sayıda görselle dahi 10-15 epoch'ta makul sonuçlar verir.
* Doğruluk metriği olarak **mAP50** (Mean Average Precision) değerine dikkat edin.
