# 3. Yapay Zeka Eğitimi — YOLOv11 (`G3`)

## Alt Görevler
- [ ] Eğitim ortamını kur (`Colab / Kaggle / PC`).
- [ ] İlk fotoğraflarla `yolo11n` ve `yolo11s` modellerini eğit.
- [ ] `dataset/test/` ile modelin öğrenme durumunu kontrol et.
- [ ] Video testlerinden gelen hatalara göre ayar/veri güncelleyip yeniden eğit (`v2`, `v3`).
- [ ] En iyi çalışan `best.pt` ağırlığını Orin NX'e hazır `.onnx` formatına dönüştür.

## Komutlar
```bash
python 03_yapay_zeka_egitimi/scripts/train.py --model yolo11s.pt --imgsz 640 --epochs 80 --name v1_yolo11s_640
python 03_yapay_zeka_egitimi/scripts/export_onnx.py --weights 03_yapay_zeka_egitimi/weights/best.pt --imgsz 640
```
