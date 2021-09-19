import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class PublisherNode(Node):

    def __init__(self):
        super().__init__() # Initialize node with name 
        self.publisher = self.create_publisher(String, 'topic_name', 10) #Create a publisher

        timer_period = 0.5  # How often the callback will be called
        self.timer = self.create_timer(timer_period, self.timer_callback) # Register callback for timer with period 'timer_period'

    def timer_callback(self):
        # Callback function for timer event.
        self.get_logger().info('Publishing message')
        # TODO: Create a message and publish it, also print a statement to console


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
