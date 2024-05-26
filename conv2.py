import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import os 

class ImageSaver(Node):
    def __init__(self):
        super().__init__('image_saver')
        self.bridge = CvBridge()
        self.subscription = self.create_subscription(
            Image,
            '/raw_image',
            self.listener_callback,
            10)
        self.subscription 
        self.image_count = 0
        self.save_path = os.path.join(os.getcwd(), 'images')
        if not os.path.exists(self.save_path):
            os.makedirs(self.save_path)
        

    def listener_callback(self, msg):
        cv_image = self.bridge.imgmsg_to_cv2(msg) 
        cv2.imwrite(os.path.join(self.save_path, f'image_{self.image_count}.png'), cv_image)
        print("Saved imagae number: ", self.image_count)
        self.image_count += 1

def main(args=None):
    rclpy.init(args=args)
    image_saver = ImageSaver()
    rclpy.spin(image_saver)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
