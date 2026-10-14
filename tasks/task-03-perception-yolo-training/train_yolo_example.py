#!/usr/bin/env python3
"""
Task 03: YOLO Model Eğitimi & Çıkarım (Inference) Örnek Scripti

Bu script Ultralytics YOLO kütüphanesi kullanarak mini bir veri setiyle
model eğitiminin ve test görseli üzerinde nesne tespitinin nasıl yapılacağını gösterir.
"""

import os
from ultralytics import YOLO


def train_mini_yolo(data_yaml_path='data.yaml', epochs=15, imgsz=640):
    """
    Önceden eğitilmiş (pretrained) yolov8n ağırlıkları üzerinden
    kendi özel veri setimizle transfer learning başlatır.
    """
    print(f"[*] YOLOv8 Nano modeli yükleniyor...")
    model = YOLO('yolov8n.pt')

    print(f"[*] Eğitim başlatılıyor ({epochs} epoch)...")
    results = model.train(
        data=data_yaml_path,
        epochs=epochs,
        imgsz=imgsz,
        project='yolo_runs',
        name='onboarding_experiment',
        exist_ok=True
    )
    print("[+] Eğitim başarıyla tamamlandı!")
    return model


def run_inference(weights_path, test_image_path):
    """
    Eğitilen en iyi model ağırlıklarıyla (best.pt) test görseli üzerinde tahmin yapar.
    """
    if not os.path.exists(weights_path):
        print(f"[-] Ağırlık dosyası bulunamadı: {weights_path}")
        return

    print(f"[*] Eğitilen model yükleniyor: {weights_path}")
    trained_model = YOLO(weights_path)

    print(f"[*] Test görselinde tespit yapılıyor: {test_image_path}")
    results = trained_model.predict(
        source=test_image_path,
        save=True,
        conf=0.25,
        project='yolo_runs',
        name='test_predictions'
    )
    print(f"[+] Çıkarım tamamlandı! Sonuçlar yolo_runs/test_predictions klasörüne kaydedildi.")


if __name__ == '__main__':
    # Örnek kullanım:
    # 1. Roboflow'dan indirdiğiniz data.yaml dosyasının yolunu belirtin:
    yaml_file = 'data.yaml'

    # Not: Gerçek veri setiniz hazır olduğunda aşağıdaki satırı çalıştırabilirsiniz:
    # model = train_mini_yolo(data_yaml_path=yaml_file, epochs=15)
    # run_inference('yolo_runs/onboarding_experiment/weights/best.pt', 'test_image.jpg')

    print("[i] YOLO eğitim scripti hazır. Veri setinizin data.yaml yolunu belirleyerek çalıştırabilirsiniz.")
