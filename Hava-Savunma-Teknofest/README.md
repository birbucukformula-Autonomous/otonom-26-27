# 🛡️ Hava Savunma Teknofest — Nesne Tespiti (YOLOv11) Çalışma Alanı

TEKNOFEST Hava Savunma Sistemleri yarışması için donanım öncesi fazda **araştırma, veri toplama, YOLOv11 model eğitimi ve video üzerinde tespit/revizyon** süreçlerinin yürütüldüğü proje klasörüdür.

---

## 📁 Klasör Yapısı

```text
Hava-Savunma-Teknofest/
├── README.md
├── requirements.txt
├── .gitignore
│
├── 01_arastirma/                      # G1: Hava savunma araştırması ve ortak sınıf tanımları
│   └── README.md
│
├── 02_veri_toplama/                   # G2: Eğitim & test fotoğrafları ve doğrulama araçları
│   ├── configs/
│   │   └── data.yaml                  # Ortak sınıf isimleri (tüm ekip burayı kullanır)
│   ├── dataset/
│   │   ├── train/{images,labels}/
│   │   ├── val/{images,labels}/
│   │   └── test/{images,labels}/
│   ├── raw/                           # Ham indirilen görseller (git dışı)
│   ├── synthetic/                     # 3D modellerden üretilen sentetik veriler (git dışı)
│   └── scripts/
│       └── check_dataset.py           # Etiket, sınıf dağılımı ve sızıntı kontrolü
│
├── 03_yapay_zeka_egitimi/             # G3: YOLOv11 eğitim ve .onnx export scriptleri
│   ├── README.md
│   ├── experiments/                   # Eğitim metrik ve revizyon notları
│   ├── weights/                       # best.pt / best.onnx dosyaları (git dışı)
│   └── scripts/
│       ├── train.py
│       └── export_onnx.py
│
└── 04_video_test/                     # G4: Kamera gelene kadar video üzerinde tespit & revizyon
    ├── README.md
    ├── revizyon_notlari.md            # Video hataları ve iyileştirme kayıtları
    ├── test_videos/                   # Eğitime girmemiş test videoları (git dışı)
    ├── outputs/                       # Tespit çıktı videoları (git dışı)
    └── scripts/
        └── test_video.py
```

---

## 🚀 Hızlı Başlangıç

```bash
pip install -r requirements.txt

# 1. Veri setini ve etiketleri kontrol et
python 02_veri_toplama/scripts/check_dataset.py

# 2. YOLOv11 modelini eğit
python 03_yapay_zeka_egitimi/scripts/train.py --model yolo11s.pt --imgsz 640 --epochs 80

# 3. Test videolarında çalıştır
python 04_video_test/scripts/test_video.py --weights 03_yapay_zeka_egitimi/weights/best.pt

# 4. Orin NX'e hazır .onnx çıktısı al
python 03_yapay_zeka_egitimi/scripts/export_onnx.py --weights 03_yapay_zeka_egitimi/weights/best.pt
```

> **Kural:** `04_video_test/test_videos/` içindeki videolardan alınan kareler kesinlikle `02_veri_toplama/dataset/train/` içerisine eklenmemelidir.
