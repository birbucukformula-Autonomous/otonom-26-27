# 🎓 Otonom Sürüş — Yeni Üye Eğitim Programı (`training-program/`)

Bu dizin, otonom araç yazılım ekibimize katılan yeni üyelerin otonom sürüş boru hattını (pipeline) kavraması, algoritmik temelleri öğrenmesi ve simülasyon ortamlarında pratik yapması için hazırlanmış **eğitim ve oryantasyon programıdır**.

---

## 📋 Görev Listesi (Tasks)

Eğitim kampı 4 aşamalı bağımsız görevden oluşur. Her görev adayın araştırmasını teşvik edecek ve temel bir otonom alt disiplini deneyimlemesini sağlayacak şekilde kurgulanmıştır:

| Görev | Başlık | Odak Alanı | Teslimat Çıktısı |
| :--- | :--- | :--- | :--- |
| **[Task 01](file:///home/zuzu/Desktop/otonom-26-27/training-program/task-01-autonomous-pipeline-research/README.md)** | **Otonom Mimari & Alt Disiplinler Araştırması** | Algılama, SLAM, Planlama veya Kontrol | 5-8 slaytlık sunum (`sunum.pdf`) + `ozet.md` |
| **[Task 02](file:///home/zuzu/Desktop/otonom-26-27/training-program/task-02-ros2-communication-basics/README.md)** | **ROS 2 Temelleri & Simülatör Hareketi** | Node, Topic, Publisher/Subscriber, Twist mesajları | Python ROS 2 düğümü + Simülasyon & rqt grafiği |
| **[Task 03](file:///home/zuzu/Desktop/otonom-26-27/training-program/task-03-perception-yolo-training/README.md)** | **Perception: YOLO ile Etiketleme & Model Eğitimi** | Veri etiketleme, Roboflow/CVAT, Transfer Learning | Model kayıp grafiği + Bounding box tespit görseli |
| **[Task 04](file:///home/zuzu/Desktop/otonom-26-27/training-program/task-04-path-planning-and-motion/README.md)** | **Yol Takibi & Hareket Kontrolü** | Kinematik Bisiklet Modeli, Pure Pursuit / Stanley | Yol takip scripti + Yörünge ve hata grafikleri |

---

## 🚀 Görev Teslim (Submission) Kılavuzu

Takımımızda tüm teslimatlar profesyonel Git iş akışı (Branch & Pull Request) ile yapılır.

1. **Yeni Dal (Branch) Açın:**
   ```bash
   git checkout -b submission/<ad-soyad>/task-01
   ```
2. **Çalışmanızı İlgili Görevin Submissions Klasörüne Ekleyin:**
   * Dosyalarınızı **yalnızca** ilgili görevin altındaki `submissions/<ad_soyad>/` klasörüne ekleyiniz:
     ```text
     training-program/task-01-autonomous-pipeline-research/submissions/ahmet_yilmaz/
     ```
3. **Commit ve Push:**
   ```bash
   git add training-program/task-01-autonomous-pipeline-research/submissions/ahmet_yilmaz/
   git commit -m "feat(task-01): Ahmet Yılmaz araştırma teslimi"
   git push origin submission/<ad-soyad>/task-01
   ```
4. **Pull Request (PR) Açın:**
   * GitHub üzerinden `main` dalına doğru bir Pull Request açın.
   * Mentörler çalışmanızı inceleyip geri bildirim sağlayacaktır.
