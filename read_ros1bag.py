import os
import argparse

import cv2

import rosbag

from sensor_msgs.msg import Image, CompressedImage
from cv_bridge import CvBridge

save = False

def main():
    """Read from a rosbag file
    """
    bag_file = "/home/xmo/socialnav_xmo/feature_extractor/bagfiles/multiHuman2.bag"
    image_topic = "/camera/color/image_raw/compressed"
    output_dir = "/home/xmo/bagfiles/extract/"

    bag = rosbag.Bag(bag_file, "r")
    bridge = CvBridge()
    count = 0
    for topic, msg, t in bag.read_messages(topics=[image_topic]):

        cv_img = bridge.compressed_imgmsg_to_cv2(msg)

        cv2.imshow('RealSense RGB',cv_img)
        key = cv2.waitKey(5)
        if key == ord('q'):
            break

        if save:
            cv2.imwrite(os.path.join(output_dir, "frame%06i.png" % count), cv_img)
            print(f"Wrote image {count}")
        count += 1

    bag.close()


if __name__ == '__main__':
    main()