# 📚 Task 01: Otonom Sürüş Mimarisi & Alt Disiplinler Araştırması

## 🎯 Görevin Amacı & Açıklama
Bir otonom araç yazılım mühendisi olmanın ilk adımı, aracın beynini oluşturan katmanların birbiriyle nasıl konuştuğunu ve hangi problemleri çözdüğünü kavramaktır. 

Bu görevde, otonom sürüş mimarisinin temel disiplinlerinden birini seçerek bağımsız bir literatür ve sektör araştırması yapmanız, algoritmaların çalışma prensiplerini incelemeniz ve elde ettiğiniz bulguları takıma aktarmanız beklenmektedir.

---

## 🔍 Araştırma Başlıkları (Bir Alan Seçiniz)

Aşağıdaki 4 temel disiplinden ilgi duyduğunuz **biri** üzerine derinlemesine araştırma yapınız:

### 1. Algılama (Perception)
* Araç çevresini nasıl "görür" ve nesneleri (yayalar, araçlar, trafik işaretleri, koniler) nasıl tanır?
* Farklı sensör tiplerinin (Kamera, LiDAR, Radar) birbirine göre üstünlükleri ve zayıf yönleri nelerdir?
* Sensör Füzyonu (Sensor Fusion) neden gereklidir, tek bir sensör neden otonom sürüş için yeterli değildir?

### 2. Konumlandırma & Haritalama (Localization & SLAM)
* GPS/GNSS sinyalinin zayıfladığı veya kaybolduğu durumlarda araç santimetre hassasiyetinde nerede olduğunu nasıl hesaplar?
* Ataletsel ölçüm birimleri (IMU), tekerlek odometrisi ve harita bilgisi nasıl birleştirilir?
* SLAM (Simultaneous Localization and Mapping) yaklaşımının temel mantığı nedir?

### 3. Rota ve Yol Planlama (Path & Trajectory Planning)
* Global rota planlama ile lokal (yerel) engelden kaçma planlaması arasındaki farklar nelerdir?
* Statik ve dinamik (hareket eden) engeller karşısında yol planlayıcılar nasıl kararlar alır?
* Zaman, hız ve ivme kısıtları yörüngeye (trajectory) nasıl dahil edilir?

### 4. Araç & Hareket Kontrolü (Motion Control)
* Planlanan yol çizgisi üzerinde kalmak için direksiyon açısı ve gaz/fren torku nasıl hesaplanır?
* Geometrik kontrolcüler ile model tabanlı kontrol yaklaşımları arasındaki temel farklar ve kullanım alanları nelerdir?
* Acil durumlarda güvenlik frenlemesi ve sürüş dinamikleri nasıl yönetilir?

---

## 📤 Submission (Teslimat) Kısmı

### Beklenen Çıktılar
1. **Teknik Sunum (`sunum.pdf`):** Seçtiğiniz disiplini, karşılaşılan temel mühendislik problemlerini ve sektörde kullanılan popüler çözüm yöntemlerini özetleyen **5-8 slaytlık** sunum dosyası.
2. **Kısa Özet Raporu (`ozet.md`):** Araştırdığınız konuyu, öğrendiğiniz temel algoritmaları ve referans aldığınız kaynakları içeren 1 sayfalık Markdown notu.
3. **Takım İçi Sunum:** Hazırladığınız sunum, haftalık teknik toplantımızda takıma 5 dakikalık kısa bir oturumla sunulacaktır.

### Teslimat Formatı & Dizin Yapısı
Çalışmanızı sadece şu dizine ekleyiniz:
```text
tasks/task-01-autonomous-pipeline-research/submissions/<ad_soyad>/
├── sunum.pdf
└── ozet.md
```

### Git & PR Adımları
1. Yeni dal oluşturun:
   ```bash
   git checkout -b submission/<ad-soyad>/task-01
   ```
2. Dosyalarınızı kendi klasörünüze ekleyip commit atın:
   ```bash
   git add tasks/task-01-autonomous-pipeline-research/submissions/<ad_soyad>/
   git commit -m "feat(task-01): <Ad Soyad> araştırma teslimi"
   ```
3. Dalınızı uzak sunucuya gönderip GitHub üzerinden `main` dalına Pull Request (PR) açın.
