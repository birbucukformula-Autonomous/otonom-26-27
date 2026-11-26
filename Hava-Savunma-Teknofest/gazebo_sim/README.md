# Gazebo Simülasyonu (TEKNOFEST 3D Modelleri)

`/home/zuzu/Downloads/Modeller` içindeki 3MF `.model` dosyalarını **Ignition Gazebo 6 (`ign gazebo`)** içinde açmak ve test etmek için hazırlanmıştır.

## 1. Modelleri `.stl` Formatına Çevirme
*(Büyük `.stl` dosyaları git'e eklenmediği için ilk seferde bu komutu çalıştırın:)*
```bash
python3 gazebo_sim/scripts/convert_3mf_to_stl.py
```

## 2. Gazebo'da Açma
```bash
bash gazebo_sim/launch_gazebo.sh
```
Sahne içinde 4 hedef model (`fuze`, `helikopter`, `f16`, `drone`) havada dizili gelir. Sağ üstteki eklenti menüsünden **Image Display** açıp `/air_defense_camera/image` konusunu seçerseniz yerdeki sanal kameranın gördüğü görüntüyü de canlı izleyebilirsiniz.
