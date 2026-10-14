# 🤖 Task 02: ROS 2 Humble Temelleri & Simülatör Hareketi

## 🎯 Görevin Amacı
Robot İşletim Sistemi (ROS 2), otonom araç yazılımlarının omurgasıdır. Farklı sensörler, algoritmalar ve kontrolcüler birbirleriyle ROS 2 düğümleri (nodes) ve konuları (topics) üzerinden haberleşir.

Bu görevin amacı:
1. ROS 2'de bir **Publisher** ve **Subscriber** düğümü yazmak.
2. ROS 2'nin yerleşik 2D simülatörü olan **Turtlesim** üzerinde robotu `geometry_msgs/msg/Twist` mesajları kullanarak otonom olarak (örneğin daire çizdirerek veya duvara çarpmadan dönmesini sağlayarak) hareket ettirmek.
3. Çalışan sistemin düğüm grafiğini (`rqt_graph`) ve simülasyon hareketini belgelemek.

---

## 🛠️ Ön Hazırlık
Görevi yapabilmek için ROS 2 Humble ortamının kurulu ve source edilmiş olması gerekir:
```bash
source /opt/ros/humble/setup.bash
```
Simülatörü test etmek için:
```bash
# Terminal 1: Simülatör penceresini açar
ros2 run turtlesim turtlesim_node

# Terminal 2: Robotun anlık konumunu dinler
ros2 topic echo /turtle1/pose
```

---

## 📝 Görev Adımları

### 1. Adım: Başlangıç Kodunu İnceleyin
Bu klasörde yer alan [starter_node.py](file:///home/zuzu/Desktop/otonom-26-27/tasks/task-02-ros2-communication-basics/starter_node.py) dosyasını inceleyin. Bu şablon, `rclpy` (Python ROS 2 istemci kütüphanesi) kullanarak bir düğüm oluşturur ve `/turtle1/cmd_vel` konusuna hız komutları basar.

### 2. Adım: Otonom Hareket Kontrolcüsü Geliştirin (`motion_controller.py`)
Şablon kodu referans alarak kendi kontrolcü düğümünüzü yazın. Düğümünüz aşağıdaki şartlardan **en az birini** yerine getirmelidir:
* **Seçenek A (Geometrik Rota):** Robotun önce düz gidip, ardından 90 derece dönerek bir kare çizmesini sağlamak.
* **Seçenek B (Dinamik Hız & Açı):** Robotun yarıçapı giderek büyüyen bir spiral çizmesini sağlamak (linear.x sabit, angular.z zamanla azalan).
* **Seçenek C (Geri Beslemeli Sürüş - Bonus):** `/turtle1/pose` konusuna abone (Subscriber) olup robot ekranın sınırlarına (x < 1.5 veya x > 9.5) yaklaştığında otomatik geri dönmesini sağlamak.

### 3. Adım: Sistemi Çalıştırın ve Kanıt Toplayın
1. `ros2 run turtlesim turtlesim_node` ile simülatörü başlatın.
2. Yazdığınız Python scriptini çalıştırın:
   ```bash
   python3 motion_controller.py
   ```
3. Başka bir terminalde düğüm ve konu grafiğini açın:
   ```bash
   rqt_graph
   ```
4. Simülasyonun çizdiği rotanın ve `rqt_graph` penceresinin ekran görüntüsünü (`screenshot.png` ve `rqt_graph.png`) kaydedin.

---

## 📤 Teslimat Formatı

Kendi adınıza açtığınız dalda (`submission/<ad-soyad>/task-02`), dosyalarınızı şu yapıda teslim edin:

```text
tasks/task-02-ros2-communication-basics/submissions/<ad_soyad>/
├── motion_controller.py       # Yazdığınız Python ROS 2 düğüm kodu
├── screenshot.png             # Simülatör hareketinin ekran görüntüsü
├── rqt_graph.png              # rqt_graph düğüm haberleşme şeması
└── README.md                  # Kodunuzun nasıl çalıştığını açıklayan kısa not
```

---

## 💡 İpuçları & Kaynaklar
* `geometry_msgs/msg/Twist`:
  * `linear.x`: İleri/geri hız (m/s)
  * `angular.z`: Kendi etrafında dönüş hızı (rad/s)
* [ROS 2 Humble Dökümantasyonu - rclpy Düğümleri](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Py-Publisher-And-Subscriber.html)
