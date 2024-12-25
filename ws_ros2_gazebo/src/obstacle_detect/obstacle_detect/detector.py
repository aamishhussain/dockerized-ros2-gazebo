import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from std_msgs.msg import String

class ObstacleDetector(Node):
    def __init__(self):
        super().__init__('obstacle_detector')
        self.subscription = self.create_subscription(
            LaserScan,
            '/scan',
            self.scan_callback,
            10)
        self.publisher = self.create_publisher(String, '/obstacle_alert', 10)
        self.get_logger().info("Obstacle Detector Node has started")

    def scan_callback(self, msg):
        min_distance = min(msg.ranges)
        if min_distance < 0.5:  # Threshold for obstacle detection
            alert_msg = String()
            alert_msg.data = f"Obstacle detected at {min_distance:.2f} meters!"
            self.publisher.publish(alert_msg)
            self.get_logger().warn(alert_msg.data)

def main(args=None):
    rclpy.init(args=args)
    node = ObstacleDetector()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
