#!/usr/bin/env python3
"""
Task 04: 2D Yol Takibi ve Araç Simülasyonu (Kinematic Bicycle Model & Pure Pursuit)

Bu script, harici bir simülatöre ihtiyaç duymadan Python ve Matplotlib ile
kıvrımlı bir referans yolu takip eden basit bir otonom araç simülasyonudur.
"""

import math
import numpy as np
import matplotlib.pyplot as plt


class VehicleState:
    """
    Aracın 2D durum vektörü:
    x: X konumu (metre)
    y: Y konumu (metre)
    yaw: Yönelim açısı (radyan)
    v: İleri hız (m/s)
    """
    def __init__(self, x=0.0, y=0.0, yaw=0.0, v=2.0):
        self.x = x
        self.y = y
        self.yaw = yaw
        self.v = v


def generate_reference_path():
    """
    Simülasyon için kıvrımlı (sinüzoidal) bir referans yol üretir.
    """
    cx = np.linspace(0, 50, 200)
    cy = 5.0 * np.sin(cx / 4.0)
    return cx, cy


def find_target_index(state, cx, cy, lookahead_distance):
    """
    Araçtan belirli bir 'lookahead' mesafesi kadar ilerideki hedef noktanın indeksini bulur.
    """
    dx = cx - state.x
    dy = cy - state.y
    distances = np.hypot(dx, dy)
    closest_idx = np.argmin(distances)

    target_idx = closest_idx
    while target_idx < len(cx) - 1:
        dist = np.hypot(cx[target_idx] - state.x, cy[target_idx] - state.y)
        if dist >= lookahead_distance:
            break
        target_idx += 1

    return target_idx


def pure_pursuit_controller(state, target_x, target_y, wheelbase, lookahead_distance):
    """
    Hedef noktaya göre Pure Pursuit direksiyon açısını (delta) hesaplar.
    """
    # Aracın burnu ile hedef nokta arasındaki bağıl açı (alpha)
    angle_to_target = math.atan2(target_y - state.y, target_x - state.x)
    alpha = angle_to_target - state.yaw

    # Açıyı [-pi, pi] aralığına normalize et
    alpha = math.atan2(math.sin(alpha), math.cos(alpha))

    # Pure pursuit direksiyon açısı formülü: delta = atan2(2 * L * sin(alpha), ld)
    delta = math.atan2(2.0 * wheelbase * math.sin(alpha), lookahead_distance)

    # Maksimum direksiyon açısı kısıtlaması (+/- 35 derece)
    max_steer = math.radians(35.0)
    delta = max(-max_steer, min(max_steer, delta))

    return delta


def update_vehicle(state, delta, dt, wheelbase):
    """
    Kinematik Bisiklet Modeli (Bicycle Model) ile araç durumunu bir sonraki adıma günceller.
    """
    state.x += state.v * math.cos(state.yaw) * dt
    state.y += state.v * math.sin(state.yaw) * dt
    state.yaw += (state.v / wheelbase) * math.tan(delta) * dt
    return state


def run_simulation():
    # Simülasyon Parametreleri
    dt = 0.1                    # Zaman adımı (saniye)
    sim_time = 30.0             # Toplam simülasyon süresi (saniye)
    wheelbase = 1.5             # Dingil mesafesi (metre)
    lookahead_distance = 3.5    # İleri bakış mesafesi (metre) - BUNU DEĞİŞTİRİP ETKİSİNİ GÖZLEMLE!

    # Referans yol
    cx, cy = generate_reference_path()

    # Araç başlangıç durumu
    state = VehicleState(x=0.0, y=1.0, yaw=0.0, v=2.5)

    # Log kayıtları
    history_x = []
    history_y = []
    errors = []

    time = 0.0
    while time < sim_time and state.x < cx[-1]:
        target_idx = find_target_index(state, cx, cy, lookahead_distance)
        target_x = cx[target_idx]
        target_y = cy[target_idx]

        # Direksiyon açısını hesapla
        delta = pure_pursuit_controller(state, target_x, target_y, wheelbase, lookahead_distance)

        # Aracı güncelle
        state = update_vehicle(state, delta, dt, wheelbase)

        # Takip hatasını hesapla (en yakın yola dik mesafe)
        tracking_error = np.min(np.hypot(cx - state.x, cy - state.y))

        history_x.append(state.x)
        history_y.append(state.y)
        errors.append(tracking_error)

        time += dt

    # Sonuçları Görselleştir
    plt.figure(figsize=(12, 6))

    # 1. Grafik: Yörünge
    plt.subplot(1, 2, 1)
    plt.plot(cx, cy, "r--", label="Referans Yol", linewidth=2)
    plt.plot(history_x, history_y, "b-", label="Aracın İzlediği Yol", linewidth=1.5)
    plt.title("Otonom Yol Takip Yörüngesi (Pure Pursuit)")
    plt.xlabel("X [m]")
    plt.ylabel("Y [m]")
    plt.legend()
    plt.grid(True)
    plt.axis("equal")

    # 2. Grafik: Takip Hatası
    plt.subplot(1, 2, 2)
    plt.plot(np.linspace(0, time, len(errors)), errors, "g-", label="Yoldan Sapma Hatası")
    plt.title("Zamana Bağlı Takip Hatası (m)")
    plt.xlabel("Zaman [s]")
    plt.ylabel("Sapma Hatası [m]")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.savefig("starter_trajectory_plot.png", dpi=200)
    print("[+] Simülasyon tamamlandı! starter_trajectory_plot.png kaydedildi.")
    plt.show()


if __name__ == '__main__':
    run_simulation()
