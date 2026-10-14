# 📑 Task 01: Sunum & Teknik Rapor Şablonu

Bu şablon, hazırlayacağınız 5-8 slaytlık sunumun ve `ozet.md` dosyasının iskeletini oluşturmanız için tasarlanmıştır.

---

## 🖼️ Önerilen Slayt Akışı (5-8 Slayt)

* **Slayt 1: Başlık & Giriş**
  * Konu Başlığı (Örn: *Otonom Araçlarda LiDAR Tabanlı 3D SLAM ve EKF Odometri Füzyonu*)
  * Adınız Soyadınız, Tarih, Takım İsmi
* **Slayt 2: Problem Tanımı & Motivasyon**
  * Neden bu teknolojiye ihtiyaç var? (Örn: *GPS tünellerde veya ormanlık arazilerde neden yetersiz kalır?*)
* **Slayt 3: Mimari & Veri Akışı (Blok Diyagram)**
  * Sensörden gelen veri nasıl işlenir? Hangi adımlardan geçer? (Ham veri -> Filtreleme -> Özellik Çıkarımı -> Karar)
* **Slayt 4: Popüler Algoritmalar & Yöntemler**
  * Sektörde ve otonom araç yarışmalarında en çok kullanılan 2-3 yaklaşımın karşılaştırması (Örn: *Pure Pursuit vs. MPC* veya *YOLO vs. Mask R-CNN*).
* **Slayt 5: Karşılaşılan Zorluklar (Edge Cases)**
  * Bu yöntemin zayıf olduğu durumlar nelerdir? (Hesaplama yükü, gecikme, sensör gürültüsü, hava şartları).
* **Slayt 6: Bizim Takım İçin Öneriler & Sonuç**
  * Biz simülasyonda veya aracımızda bu yöntemi nasıl uygulayabiliriz? Hangi ROS 2 paketleri kullanılabilir?
* **Slayt 7: Kaynakça**
  * İncelediğiniz makaleler, GitHub repoları, blog yazıları.

---

## 📄 `ozet.md` Rapor Formatı

Teslim edeceğiniz `ozet.md` dosyasında şu başlıkları doldurunuz:

```markdown
# [Konu Başlığı]

* **Yazar:** [Adınız Soyadınız]
* **Tarih:** [GG.AA.YYYY]
* **Seçilen Alan:** Perception / Localization & SLAM / Planning / Motion Control

## 1. Yönetici Özeti (Executive Summary)
[Konuyu ve amacını 3-4 cümleyle açıklayın]

## 2. Temel Kavramlar & Mimari
[Konunun temel yapı taşları, sensör/algoritma ilişkisi]

## 3. Avantajlar & Dezavantajlar
| Yöntem | Avantajları | Dezavantajları / Riskler |
| :--- | :--- | :--- |
| Yöntem A | ... | ... |
| Yöntem B | ... | ... |

## 4. Kullanılabilecek Açık Kaynak Araçlar & ROS 2 Paketleri
- Kütüphane / Paket 1 (Link)
- Kütüphane / Paket 2 (Link)

## 5. Kaynaklar
1. [Kaynak Adı](link)
```
