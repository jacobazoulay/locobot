#!/usr/bin/env python

# script that will pilot different functions on our robot 
import rospy
from sensor_msgs.msg import Image
import cv2
import matplotlib.pyplot as plt
import numpy as np
from cv_bridge import CvBridge

class colorImageGet:

    # constructor initializes object with empty maskImg field
    def __init__(self,color='r'):
        self.maskImg = []
        self.maskGet = False
        self.maskColor = color
        rospy.init_node('colorImageGet', anonymous=False)
        print('Color Image object initialized')

        

    #function responsbile for initializing subscriber node to pull sensor_msg
    def subscribeToColor(self):

        print('Subscribe to image_raw topic')
        
        # self.sub = rospy.Subscriber('/locobot/camera/color/image_raw', Image, self.colorCallBack)
        self.sub = rospy.wait_for_message('/locobot/camera/color/image_raw', Image, self.colorCallBack)

    #call back that generates mask
    def colorCallBack(self, data):
        rospy.loginfo('CALLINGBACK')
        bridge = CvBridge()
        # load ros image to open cv type
        cv_image = bridge.imgmsg_to_cv2(data, desired_encoding='passthrough')
        HSV_img = cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV)

        

        # mask b [0,30] g[30,60] y[60,100] r[110+]
        if self.maskColor == 'r':
            lb=np.array([110,10,50])
            ub=np.array([180,255,255])
            mask=cv2.inRange(HSV_img,lb,ub)
        elif self.maskColor == 'y':
            lb=np.array([60,10,50])
            ub=np.array([100,255,255])
            mask=cv2.inRange(HSV_img,lb,ub)
        elif self.maskColor == 'g':
            lb=np.array([30,10,50])
            ub=np.array([60,255,255])
            mask=cv2.inRange(HSV_img,lb,ub)
        elif self.maskColor == 'b':
            lb=np.array([0,10,50])
            ub=np.array([30,255,255])
            mask=cv2.inRange(HSV_img,lb,ub)

        #apply
        mask_img =np.uint8(cv2.bitwise_and(HSV_img,HSV_img, mask= mask))
        mask_img = cv2.cvtColor(mask_img, cv2.COLOR_HSV2BGR)
        mask_img = cv2.cvtColor(mask_img, cv2.COLOR_BGR2RGB)
        
        self.maskImg = mask_img
        print('showimg')
        #self.sub.unregister()

        self.maskGet = True
        # rospy.on_shutdown(self.hook)

        cv2.imshow('window1',self.maskImg)
        cv2.waitKey()
        
    def hook(self):
        print('shuttingdown')

    

    

def main():
    # Initializes color image node
    # ic = colorImageGet()
    # rospy.init_node('colorImageGet', anonymous=True)
    # try:
    #     rospy.loginfo('spinning')
    #     rospy.spin()
        

    # except KeyboardInterrupt:
    #     rospy.loginfo('Shutting down pilot node')
    
    myColorImg = colorImageGet('y')
    while not(myColorImg.maskGet):
        myColorImg.subscribeToColor()
    
    myColorImg.sub.unregister()
        
    rospy.loginfo(myColorImg.maskImg)
    rospy.loginfo(myColorImg.maskGet)

    #cv2.imshow('window1',myColorImg.maskImg)
    #cv2.waitKey()
if __name__ == '__main__':
    main()
    