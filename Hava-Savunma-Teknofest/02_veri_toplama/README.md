# 2. Veri Toplama ve Hazırlama (`G2`)

## Alt Görevler
- [ ] Belirlenen objeler için eğitim fotoğraflarını topla ve YOLO formatında etiketle.
- [ ] Modelin yanılmaması için boş gökyüzü ve bulut fotoğrafları (negatif veri) ekle.
- [ ] Eğitim (`train`), doğrulama (`val`) ve test (`test`) setlerini birbirine karıştırmadan ayır.
- [ ] Gerekirse 3D modellerden sentetik fotoğraf üretip `synthetic/` içine koy.
- [ ] Video testlerinden gelen eksiklere göre yeni fotoğraflar ekleyip veri setini güncelle.

## Kurallar
- Tüm etiketler [configs/data.yaml](configs/data.yaml) içindeki sınıf ID'leriyle birebir aynı olmalıdır (`0: fuze`, `1: helikopter`, `2: f16`, `3: drone`, `4: balon`).
- Balonlar renk fark etmeksizin tek `balon` sınıfıyla etiketlenir; kırmızı/mavi (dost-düşman) ayrımı tespit sonrası OpenCV HSV ile yapılır.
- Boş (hedef içermeyen) gökyüzü/bulut kareleri için `labels/` altında boş `.txt` dosyası oluşturun.
- `04_video_test/test_videos/` içindeki videolardan alınan kareleri `dataset/train/` içine koymayın.

## Kontrol Komutu
```bash
python 02_veri_toplama/scripts/check_dataset.py
```
