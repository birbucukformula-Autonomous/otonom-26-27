# 🤖 Task 02: ROS 2 Humble Temelleri & Simülatör Hareketi

## 🎯 Görevin Amacı & Açıklama
Robot İşletim Sistemi (ROS 2), modern otonom araç yazılımlarının omurgasıdır. Algılama, planlama ve kontrol modülleri birbirleriyle ROS 2 düğümleri (nodes) ve konuları (topics) üzerinden haberleşir.

Bu görevde amacınız; ROS 2'nin temel haberleşme mekanizmalarını araştırarak kendi Python düğümünüzü yazmak ve ROS 2'nin dahili 2D simülatörü olan **Turtlesim** üzerinde robotu otonom olarak hareket ettirmektir.

---

## 🔍 Araştırma Başlıkları & Yönlendirici Sorular

Görevi tamamlayabilmek için aşağıdaki konuları araştırmanız ve uygulamanız beklenmektedir:

* **ROS 2 Düğüm Mimarisi:** Python ile (`rclpy` istemci kütüphanesi) bir düğüm (Node) nasıl tanımlanır ve döngüsel (timer/callback) olarak nasıl çalıştırılır?
* **Haberleşme & Mesaj Tipleri:** Robotun hızını belirlemek için hangi standart ROS 2 mesaj tipi (`geometry_msgs/msg/Twist`) kullanılır? Doğrusal (`linear`) ve açısal (`angular`) hız bileşenleri robotun hareketini nasıl etkiler?
* **Subscriber Yapısı (Opsiyonel / İleri Seviye):** Robotun mevcut konumunu (`/turtle1/pose`) dinleyip ekrandaki sınırlara yaklaştığında otomatik yön değiştirmesi nasıl sağlanabilir?
* **Grafik & Hata Ayıklama Araçları:** Çalışan düğümler ve konular arasındaki veri akışını görselleştirmek için `rqt_graph` ve `ros2 topic` araçları nasıl kullanılır?

---

## 🛠️ Teknik Beklentiler

1. Yazacağınız Python kontrolcü düğümü simülatördeki robotu belirli bir kural dahilinde hareket ettirmelidir (Örn: geometrik bir şekil çizme, spiral hareket veya duvara çarpmadan sınır kontrolü).
2. Sistemin çalıştığı ve haberleşmenin kurulduğu `rqt_graph` grafiği ile doğrulanmalıdır.

---

## 📤 Submission (Teslimat) Kısmı

### Beklenen Çıktılar
1. **`motion_controller.py`:** Kendi geliştirdiğiniz Python ROS 2 düğüm dosyası.
2. **`screenshot.png`:** Simülatörün çizdiği hareket rotasını gösteren ekran görüntüsü.
3. **`rqt_graph.png`:** Düğüm ve konu bağlantılarını gösteren `rqt_graph` şeması.
4. **`README.md`:** Kodunuzun çalışma mantığını, kullandığınız konuları ve karşılaştığınız zorlukları özetleyen kısa rapor.

### Teslimat Formatı & Dizin Yapısı
Çalışmanızı sadece şu dizine ekleyiniz:
```text
training-program/task-02-ros2-communication-basics/submissions/<ad_soyad>/
├── motion_controller.py
├── screenshot.png
├── rqt_graph.png
└── README.md
```

### Git & PR Adımları
1. Yeni dal oluşturun:
   ```bash
   git checkout -b submission/<ad-soyad>/task-02
   ```
2. Dosyalarınızı kendi klasörünüze ekleyip commit atın:
   ```bash
   git add training-program/task-02-ros2-communication-basics/submissions/<ad_soyad>/
   git commit -m "feat(task-02): <Ad Soyad> ROS 2 simülasyon teslimi"
   ```
3. Dalınızı uzak sunucuya gönderip GitHub üzerinden `main` dalına Pull Request (PR) açın.
