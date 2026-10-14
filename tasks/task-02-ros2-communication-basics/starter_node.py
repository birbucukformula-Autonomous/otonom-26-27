#!/usr/bin/env python3
"""
Task 02: ROS 2 Humble Başlangıç Şablonu (Starter Node)

Bu düğüm, Turtlesim simülatörüne belirli bir periyotla (10 Hz)
hız komutları (Twist) publish eden örnek bir Python düğümüdür.
"""

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class TurtleCircleController(Node):
    """
    Turtlesim robotunu dairesel bir yörüngede hareket ettiren örnek düğüm.
    """

    def __init__(self):
        super().__init__('turtle_circle_controller')

        # 1. /turtle1/cmd_vel konusuna Twist mesajı basan bir Publisher oluşturuyoruz
        self.cmd_vel_pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)

        # 2. 10 Hz (saniyede 10 kez, 0.1 saniye aralıkla) çalışacak bir zamanlayıcı (Timer) kuruyoruz
        self.timer_period = 0.1  # saniye
        self.timer = self.create_timer(self.timer_period, self.timer_callback)

        self.get_logger().info('TurtleCircleController düğümü başlatıldı! Simülatör dinleniyor...')

    def timer_callback(self):
        """
        Zamanlayıcı her tetiklendiğinde çalışan fonksiyon.
        """
        msg = Twist()

        # Doğrusal hız (linear.x): İleri doğru hareket (m/s)
        msg.linear.x = 2.0
        msg.linear.y = 0.0
        msg.linear.z = 0.0

        # Açısal hız (angular.z): Dönüş hızı (rad/s)
        msg.angular.x = 0.0
        msg.angular.y = 0.0
        msg.angular.z = 1.0

        # Mesajı yayınla
        self.cmd_vel_pub.publish(msg)


def main(args=None):
    # ROS 2 iletişimini başlat
    rclpy.init(args=args)

    # Düğümü örneklendir
    node = TurtleCircleController()

    try:
        # Düğümü dinleme/çalışma döngüsüne sok
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Düğüm kullanıcı tarafından durduruldu (Ctrl+C).')
    finally:
        # Düğümü güvenle kapat ve kaynakları serbest bırak
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
