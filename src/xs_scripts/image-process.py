#!/usr/bin/env python

# script that will pilot different functions on our robot 
import rospy
from sensor_msgs.msg import Image
import cv2
import matplotlib.pyplot as plt
import numpy as np
import pyrealsense2 as rs
from cv_bridge import CvBridge

class colorImageGet:

    # constructor initializes object with empty maskImg field
    def __init__(self):
        self.maskImg = []
        self.maskGet = False
        self.data = []
        # rospy.init_node('colorImageGet', anonymous=False)
        print('Color Image object initialized')

        

    #get our depth image data
    def subscribeToDepth(self):
        print('sub to depth image')

        self.depth = rospy.wait_for_message('/locobot/camera/depth/image_rect_raw', Image)
        self.depthCallBack()
        

    # get our mask
    def subscribeToColor(self,color):

        print('Subscribe to image_raw topic')
        
        # self.sub = rospy.Subscriber('/locobot/camera/color/image_raw', Image, self.colorCallBack)
        self.data = rospy.wait_for_message('/locobot/camera/color/image_raw', Image)
        self.colorCallBack(color)

    #apply our mask to our depth image CALL SUBSCRIBETOCOLOR FIRST
    def depthCallBack(self):
        bridge = CvBridge()
        cv_image=bridge.imgmsg_to_cv2(self.depth, desired_encoding='passthrough')
        self.depth_img = cv_image
        self.depth_img = np.array(self.depth_img, dtype=np.float32)
        self.depth_img = np.multiply(self.depth_img,self.maskImgBool) 
        # pc = rs.pointcloud()
        # self.points = pc.calculate(self.depth_img)
        # print(self.points)
        # print('showimg')
        # cv2.imshow('window1',self.depth_img)
        # cv2.waitKey()

    #call back that generates mask
    def colorCallBack(self,color):
        rospy.loginfo('CALLINGBACK')
        bridge = CvBridge()
        # load ros image to open cv type
        cv_image = bridge.imgmsg_to_cv2(self.data, desired_encoding='passthrough')
        HSV_img = cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV)

        maskColor = color

        # mask b [0,30] g[30,60] y[60,100] r[110+]
        if maskColor == 'r':
            lb=np.array([110,50,50])
            ub=np.array([180,255,255])
            mask=cv2.inRange(HSV_img,lb,ub)
        elif maskColor == 'y':
            lb=np.array([60,10,50])
            ub=np.array([100,255,255])
            mask=cv2.inRange(HSV_img,lb,ub)
        elif maskColor == 'g':
            lb=np.array([30,10,50])
            ub=np.array([60,255,255])
            mask=cv2.inRange(HSV_img,lb,ub)
        elif maskColor == 'b':
            lb=np.array([0,10,50])
            ub=np.array([30,255,255])
            mask=cv2.inRange(HSV_img,lb,ub)

        #apply
        mask_img =np.uint8(cv2.bitwise_and(HSV_img,HSV_img, mask= mask))
        mask_img = cv2.cvtColor(mask_img, cv2.COLOR_HSV2BGR)
        mask_img = cv2.cvtColor(mask_img, cv2.COLOR_BGR2RGB)
        # [ret,thresh] = cv2.threshold(mask_img,5,255,cv2.THRESH_BINARY)
        
        self.maskImg = mask_img
        self.maskImgBool = self.maskImg[:,:,0] !=0
        print('showimg')
        cv2.imshow('window1',self.maskImg)
        cv2.waitKey()


def main():
    # initialize master node for all objects
    rospy.init_node('PilotNode',anonymous=False)
    # go to desired point
    myImg = colorImageGet()
    myImg.subscribeToColor('r')
    myImg.subscribeToDepth()
    
    rows, cols = np.nonzero(myImg.depth_img)
    print(myImg.depth_img[rows,cols])
    print(np.mean(myImg.depth_img[rows,cols]))




   



if __name__ == '__main__':
    main()
    