from std_srvs.srv import Trigger
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Pose
import rclpy
from rclpy.node import Node


class TurtleDrawService(Node):

    def __init__(self):
        super().__init__('turtle_draw_circle_service')
        self.get_logger().info('Starting node')
        self.srv = self.create_service(Trigger, 'draw_circle', self.draw_circle)
        self.get_logger().info('Creating service')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.get_logger().info('Creating publisher')
        ##Placeholder
        ##Create subscribtion here, maybe a timer?



    
    def turtle_circle(self):
        #Placeholder code, create a subscribtion to pose to accuratly draw a full circle
        random_number = 10
        mv_cmd = Twist()
        mv_cmd.linear.x = random_number
        mv_cmd.angular.z = random_number
        self.publisher_.publish(mv_cmd)


    def draw_circle(self, request, response):
        self.get_logger().info('Drawing Circle')
        self.turtle_circle()
        response.success = True
        return response


def main(args=None):
    rclpy.init(args=args)

    turtle_draw = TurtleDrawService()

    rclpy.spin(turtle_draw)
   
    rclpy.shutdown()


if __name__ == '__main__':
    main()