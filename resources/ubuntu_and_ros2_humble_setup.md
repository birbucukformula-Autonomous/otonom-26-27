# 🐧 Ubuntu 22.04 & ROS 2 Humble Kurulum Kılavuzu

Bu kılavuz, otonom sistemler eğitim kampında kullanılacak olan **Ubuntu 22.04 LTS (Jammy)** ve **ROS 2 Humble Hawksbill** geliştirme ortamının sıfırdan kurulması için hazırlanmıştır.

---

## 1. İşletim Sistemi Tercihi

### Seçenek A: Doğrudan Ubuntu Kurulumu (Dual-Boot) — *Şiddetle Tavsiye Edilir*
* Bilgisayarınızın diskinde 50-100 GB alan ayırarak Windows'un yanına Ubuntu 22.04 LTS kurmak, özellikle kamera/GPU ve simülasyon araçları için en yüksek performansı ve sıfır sürücü uyumsuzluğunu sağlar.

### Seçenek B: Windows 11/10 Üzerinde WSL2
* Windows üzerinde PowerShell'i yönetici olarak açıp:
  ```powershell
  wsl --install -d Ubuntu-22.04
  ```
* WSL2 ile grafik arayüz (GUI - RViz, Turtlesim) desteği Windows 11'de yerleşik olarak (WSLg) gelir.

---

## 2. ROS 2 Humble Hawksbill Kurulum Adımları

Ubuntu terminalinizi (`Ctrl + Alt + T`) açın ve sırasıyla aşağıdaki komutları çalıştırın:

### Adım 1: Dil ve Bölge Ayarları (Locale)
```bash
sudo apt update && sudo apt install locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8
```

### Adım 2: Ubuntu Universe Deposunu Etkinleştirin
```bash
sudo apt install software-properties-common
sudo add-apt-repository universe
```

### Adım 3: ROS 2 GPG Anahtarını Ekleyin
```bash
sudo apt update && sudo apt install curl -y
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
```

### Adım 4: Depoyu Paket Listenize Ekleyin
```bash
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
```

### Adım 5: ROS 2 Humble Desktop Kurulumu
```bash
sudo apt update
sudo apt upgrade -y
sudo apt install ros-humble-desktop -y
```

### Adım 6: Geliştirme Araçları (Colcon, Rosdep, Python Araçları)
```bash
sudo apt install python3-colcon-common-extensions python3-rosdep python3-pip -y
sudo rosdep init
rosdep update
```

### Adım 7: Ortam Değişkenlerini Kalıcı Hale Getirin (Source)
Her yeni terminal açıldığında ROS 2 komutlarının otomatik tanınması için:
```bash
echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

---

## 3. Kurulum Doğrulama Testi

Terminalde şu komutları test edin:

```bash
# 1. ROS 2 doktor kontrolü:
ros2 doctor

# 2. Örnek Publisher & Subscriber Testi:
# Birinci terminalde:
ros2 run demo_nodes_cpp talker

# İkinci bir terminal açıp:
ros2 run demo_nodes_py listener
```
Eğer `listener` terminalinde "I heard: [Hello World: ...]" mesajlarını görüyorsanız, ROS 2 Humble başarıyla kurulmuştur!

---

## 4. Gerekli Python Kütüphaneleri
Otonom araç algılama ve planlama görevleri için gerekli paketleri kurun:
```bash
pip install --upgrade pip
pip install numpy opencv-python matplotlib ultralytics
```
