import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class SubscriberNode(Node):

    def __init__(self):
        #TODO: setups subscriber 

        self.subscription  # prevent unused variable warning

    # TODO: Define callback function and log what is received 
    def listener_callback( PLACEHOLDER ):
        


def main(args=None):
    rclpy.init(args=args)

    subscriber_node = SubscriberNode()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    subscriber_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()