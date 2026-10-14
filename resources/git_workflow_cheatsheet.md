# 🛠️ Git & GitHub Pratik İpuçları (Cheatsheet)

Bu belge, yeni üyelerin günlük çalışmalarda en çok ihtiyaç duyacağı Git komutlarını derler.

---

## 📌 En Çok Kullanılan Komutlar

| Komut | Açıklama |
| :--- | :--- |
| `git status` | Değiştirilen, eklenen veya silinen dosyaların anlık durumunu gösterir. |
| `git pull origin main` | Ana daldaki en güncel değişiklikleri yerel bilgisayarınıza çeker. |
| `git checkout -b <dal-adi>` | Yeni bir çalışma dalı (branch) oluşturur ve ona geçiş yapar. |
| `git checkout <dal-adi>` | Mevcut başka bir dala geçiş yapar. |
| `git add <dosya_veya_klasor>` | Belirtilen dosya veya klasörü commit aşamasına (staging) ekler. |
| `git commit -m "mesaj"` | Eklenen değişiklikleri kalıcı bir commit olarak kaydeder. |
| `git push origin <dal-adi>` | Yerel dalınızı GitHub'daki uzak depoya gönderir. |
| `git diff` | Henüz add edilmemiş dosyalardaki satır bazlı farkları gösterir. |
| `git log --oneline -n 5` | Son 5 commit'i özet olarak listeler. |

---

## ⚠️ Sık Karşılaşılan Durumlar ve Çözümleri

### 1. Yanlışlıkla `main` dalında kod yazdım, ne yapmalıyım?
Henüz commit atmadıysanız, hemen yeni dala geçebilirsiniz:
```bash
git checkout -b submission/<ad-soyad>/task-XX
# Değişiklikleriniz otomatik olarak yeni dala taşınır.
```

### 2. Kendi klasörüm dışında yanlış bir dosya ekledim:
```bash
# Yanlış eklenen dosyayı staging'den geri çekmek için:
git restore --staged <yanlis_dosya_yolu>
```

### 3. Uzak dal ile yerel dal senkronizasyonu:
Çalışmaya başlamadan önce her zaman ana dalın güncel olduğundan emin olun:
```bash
git checkout main
git pull origin main
git checkout submission/<ad-soyad>/task-XX
git merge main
```
