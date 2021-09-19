import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class PublisherNode(Node):

    def __init__(self):
        super().__init__('minimal_publisher') # Initialize node with name 'minimal_publisher'
        self.publisher_ = self.create_publisher(String, 'topic_name', 10) #Create a publisher

        timer_period = 0.5  # How often the callback will be called
        self.timer = self.create_timer(timer_period, self.timer_callback) # Register callback for timer with period 'timer_period'
        self.i = 0

    def timer_callback(self):
        msg = String() #Create message type string
        msg.data = 'Hello World: %d' % self.i # Set the data to be contained withing the message
        self.publisher_.publish(msg) # Publish message
        self.get_logger().info('Publishing: "%s"' % msg.data) # Log to console
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    publisher_node = PublisherNode()

    rclpy.spin(publisher_node)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    publisher_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
