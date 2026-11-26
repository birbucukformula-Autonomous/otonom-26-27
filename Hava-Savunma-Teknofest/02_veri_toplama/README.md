# 2. Veri Toplama ve Hazırlama (`G2`)

Bu klasör; toplanan görüntülerin ham halinden temizlenip **eğitim (`train`), doğrulama (`val`) ve test (`test`)** setlerine ayrıldığı alandır.

---

## 📁 Nereye Ne Konulur? (Klasör ve Dosya Rehberi)

| Yol | Ne İşe Yarar? / Nereye Ne Konulur? | GitHub'a Gider mi? |
| :--- | :--- | :---: |
| [configs/data.yaml](configs/data.yaml) | Ortak sınıf ID listesi (`0: fuze`, `1: helikopter`, `2: f16`, `3: drone`, `4: balon`). Tüm ekip aynı ID'leri kullanır. | ✅ Evet |
| `raw/` | Roboflow, Kaggle vb. yerlerden indirilen **ham, henüz ayrılmamış** fotoğraf ve etiketlerin geçici olarak toplandığı klasör. | ❌ Hayır (yerel) |
| `synthetic/` | 3D modellerden (Blender veya `gazebo_sim` üzerinden) üretilen **sentetik** görsel ve etiketlerin konulduğu klasör. | ❌ Hayır (yerel) |
| `dataset/train/images/` | **Eğitim (~%70):** Modelin öğrenmesi için kullanılan fotoğraflar buraya konur. | ❌ Hayır (yerel) |
| `dataset/train/labels/` | **Eğitim etiketleri:** `train/images/` içindeki her fotoğrafla **aynı isimdeki** `.txt` YOLO etiketleri buraya konur (`ornek.jpg` → `ornek.txt`). | ❌ Hayır (yerel) |
| `dataset/val/images/` | **Doğrulama (~%20):** Eğitim sırasında modelin her turdaki başarısını ölçen fotoğraflar (eğitimdekilerden farklı olmalıdır). | ❌ Hayır (yerel) |
| `dataset/val/labels/` | **Doğrulama etiketleri:** `val/images/` fotoğraflarına karşılık gelen `.txt` etiketleri. | ❌ Hayır (yerel) |
| `dataset/test/images/` | **Son Test (~%10):** Eğitim tamamen bittikten sonra modelin gerçek performansını ölçmek için ayrılan fotoğraflar. | ❌ Hayır (yerel) |
| `dataset/test/labels/` | **Son Test etiketleri:** `test/images/` fotoğraflarına karşılık gelen `.txt` etiketleri. | ❌ Hayır (yerel) |
| [scripts/check_dataset.py](scripts/check_dataset.py) | `dataset/` içindeki eksik/hatalı etiketleri, sınıf sayılarını ve `train/val/test` arası dosya adı çakışmalarını kontrol eder. | ✅ Evet |

> **Not:** Klasörlerin içindeki `.gitkeep` dosyaları boş klasörlerin GitHub'da görünmesini sağlar; silmeyin. Büyük görsel/etiket dosyaları `.gitignore` ile bilinçli olarak GitHub dışında tutulur.

---

## 📝 Etiket (`.txt`) Formatı Nasıl Olmalı?
Her fotoğraf için aynı isimde bir `.txt` dosyası bulunur ve her satır bir hedefi gösterir:
```text
<sinif_id> <x_merkez> <y_merkez> <genislik> <yukseklik>
```
Örnek (`drone` sınıfı = `3`):
```text
3 0.512000 0.340000 0.085000 0.060000
```
- Boş gökyüzü / bulut (negatif) fotoğraflarda hedef olmadığı için `.txt` dosyasını **tamamen boş** bırakın.

---

## ✅ Alt Görevler
- [ ] Belirlenen objeler için eğitim fotoğraflarını topla ve YOLO formatında etiketle.
- [ ] Modelin yanılmaması için boş gökyüzü ve bulut fotoğrafları (negatif veri) ekle.
- [ ] Eğitim (`train`), doğrulama (`val`) ve test (`test`) setlerini birbirine karıştırmadan ayır.
- [ ] Gerekirse 3D modellerden sentetik fotoğraf üretip `synthetic/` içine koy.
- [ ] Video testlerinden gelen eksiklere göre yeni fotoğraflar ekleyip veri setini güncelle.

## ⚠️ Kurallar
- Tüm etiketler [configs/data.yaml](configs/data.yaml) içindeki sınıf ID'leriyle birebir aynı olmalıdır (`0: fuze`, `1: helikopter`, `2: f16`, `3: drone`, `4: balon`).
- Balonlar renk fark etmeksizin tek `balon` sınıfıyla etiketlenir; kırmızı/mavi (dost-düşman) ayrımı tespit sonrası OpenCV HSV ile yapılır.
- `04_video_test/test_videos/` içindeki videolardan alınan kareleri `dataset/train/` içine koymayın.

## 🔍 Kontrol Komutu
Veri ekledikten sonra mutlaka çalıştırın:
```bash
python3 02_veri_toplama/scripts/check_dataset.py
```
