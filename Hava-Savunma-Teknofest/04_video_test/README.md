# 4. Object Detection — Video Test ve Revizyon (`G4`)

Kamera ve Jetson gelene kadar eğitilen modeller bu klasördeki gerçek test videolarıyla doğrulanır.

## Alt Görevler
- [ ] Eğitimde hiç kullanılmamış test videolarını `test_videos/` içine koy.
- [ ] `scripts/test_video.py` ile videolar üzerinde tespit çalıştırıp `outputs/` içini incele.
- [ ] Kaçırılan küçük hedefleri ve yanlış alarmları [revizyon_notlari.md](revizyon_notlari.md) dosyasına yaz.

## Komut
```bash
python 04_video_test/scripts/test_video.py --weights 03_yapay_zeka_egitimi/weights/best.pt --conf 0.35 --imgsz 640
```
