import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class HelloNode(Node):

    def __init__(self):
        super().__init__('hello_world')
        self.publisher_ = self.create_publisher(String, 'greeting', 10)

        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = 'Hello World: %d' % self.i
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1


def main(args=None):
    rclpy.init(args=args)
    publisher_node = HelloNode()
    rclpy.spin(publisher_node)
    publisher_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
