#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
import cv2
import matplotlib.pyplot as plt
import numpy as np
from cv_bridge import CvBridge

def callback(data):
    rospy.loginfo('CALLINGBACK')
    bridge = CvBridge()
    # load ros image to open cv type
    cv_image = bridge.imgmsg_to_cv2(data, desired_encoding='passthrough')
    HSV_img = cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV)

    color = 'y' # set color for mask

    # mask b [0,30] g[30,60] y[60,100] r[110+]
    if color == 'r':
        lb=np.array([110,10,50])
        ub=np.array([180,255,255])
        mask=cv2.inRange(HSV_img,lb,ub)
    elif color == 'y':
        lb=np.array([60,10,50])
        ub=np.array([100,255,255])
        mask=cv2.inRange(HSV_img,lb,ub)
    elif color == 'g':
        lb=np.array([30,10,50])
        ub=np.array([60,255,255])
        mask=cv2.inRange(HSV_img,lb,ub)
    elif color == 'b':
        lb=np.array([0,10,50])
        ub=np.array([30,255,255])
        mask=cv2.inRange(HSV_img,lb,ub)

    #apply
    mask_img =np.uint8(cv2.bitwise_and(HSV_img,HSV_img, mask= mask))
    mask_img = cv2.cvtColor(mask_img, cv2.COLOR_HSV2BGR)
    mask_img = cv2.cvtColor(mask_img, cv2.COLOR_BGR2RGB)


    cv2.imshow('window1',mask_img)
    cv2.waitKey()


    rospy.sleep(1.)

    
    
    

def feed():
    rospy.init_node('image_feed', anonymous=False)
    rospy.Subscriber('/locobot/camera/color/image_raw', Image, callback)
    rospy.loginfo('END OF FEED')
    
    rospy.spin()
    
if __name__ == '__main__':
    feed()