#!/usr/bin/env python

# script that will pilot different functions on our robot 
import rospy
from sensor_msgs.msg import Image
import cv2
import matplotlib.pyplot as plt
import numpy as np
from cv_bridge import CvBridge

from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
from geometry_msgs.msg import Point, Twist
from math import atan2

import math
import time
from interbotix_xs_modules.locobot import InterbotixLocobotXS


# from goToPoint import odomGet
# from proccessImage import colorImageGet


## ---responsible for making masks--- ##
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
            lb=np.array([30,50,50])
            ub=np.array([60,255,255])
            mask=cv2.inRange(HSV_img,lb,ub)
        elif maskColor == 'b':
            lb=np.array([0,10,50])
            ub=np.array([30,255,255])
            mask=cv2.inRange(HSV_img,lb,ub)

        #apply
        mask_img =np.uint8(cv2.bitwise_and(HSV_img,HSV_img, mask= mask))
        mask_img = cv2.cvtColor(mask_img, cv2.COLOR_HSV2BGR)
        self.gray_img = cv2.cvtColor(mask_img, cv2.COLOR_BGR2GRAY)
        mask_img = cv2.cvtColor(mask_img, cv2.COLOR_BGR2RGB)
        
        [self.ret,self.thresh] = cv2.threshold(self.gray_img,5,255,cv2.THRESH_BINARY)
        
        self.maskImg = mask_img
        self.maskImgBool = self.maskImg[:,:,0] !=0

        print('got img')
        # cv2.imshow('window1',self.maskImg)
        # cv2.waitKey()
    
    def findContours(self):
        contours, _= cv2.findContours(self.thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        # for cnt in contours:
        #     M = cv2.moments(cnt)
        #     x_cam = int(M['m10']/M['m00'])
        #     y_cam = int(M['m01']/M['m00'])
        #     print(x_cam)
        #     print(y_cam)
        #     cv2.circle(self.maskImg, (x_cam,y_cam),5, (255,255,255),-1)
            
        # cv2.imshow('title',self.maskImg)
        # cv2.waitKey()
        cnt = contours[0]
        M = cv2.moments(cnt)
        x_cam = int(M['m10']/M['m00'])
        y_cam = int(M['m01']/M['m00'])
        print(x_cam)
        print(y_cam)
        cv2.circle(self.maskImg, (x_cam,y_cam),5, (255,255,255),-1)
        # cv2.imshow('title',self.maskImg)
        # cv2.waitKey()
        self.x_cam = x_cam
        self.y_cam = y_cam

    def averageBin(self):
        idx = np.nonzero(self.maskImgBool)
        # print(idx)
        self.avgRow = np.mean(idx[0])
        self.avgCol = np.mean(idx[1])

    

## --- responsible for driving robot -- ##
class odomGet:

    #constructor
    def __init__(self):
        self.xpos = 0
        self.ypos = 0
        self.zpos = 0
        self.roll = 0
        self.pitch = 0
        
        self.sub = None
        self.pub = None

        self.linVel = 0.5
        self.angVel = 1
        

        # initialize node
        # rospy.init_node('PositionMeasurement', anonymous=False)
        self.r = rospy.Rate(10)
        self.pub = rospy.Publisher('/locobot/mobile_base/commands/velocity', Twist, queue_size=1)
        self.sub = rospy.wait_for_message('/locobot/mobile_base/odom', Odometry)
        self.odomCallback(self.sub)

        # what to call on shutdown
        rospy.on_shutdown(self.shutdown)


    # subscribes to get odom messages
    # publishes to velocity topic
    def subscribeToOdom(self):
        print('Subscribed')
        self.sub = rospy.Subscriber('/locobot/mobile_base/odom', Odometry, self.odomCallback)
        
        # self.sub = rospy.wait_for_message('/locobot/odom', Odometry)
        # self.odomCallback(self.sub)

    
    # call back to get data from odom msgs
    def odomCallback(self,msg):
        self.xpos = msg.pose.pose.position.x
        self.ypos = msg.pose.pose.position.y 

        rot_q = msg.pose.pose.orientation
        self.roll, self.pitch, self.theta = euler_from_quaternion([rot_q.x, rot_q.y, rot_q.z, rot_q.w])


    # function called to get to goal x y
    def goToGoal(self,x,y):
        
        speed = Twist() 
        turning = True
        inc_x = (x - self.xpos)
        inc_y = (y - self.ypos)


        thresh = 0.1

        # keep moving while not at goal
        while abs(inc_x) > thresh or abs(inc_y) > thresh:
            
            inc_x = (x - self.xpos)
            inc_y = (y - self.ypos)
            goalAngle = atan2(inc_y,inc_x)


            inc_theta = goalAngle - self.theta
            mod_theta = (inc_theta+(2*np.pi)) % (2*np.pi)
    
            

            # check our orientation and rotate to goal point
            if abs(inc_theta) > 0.1:
                # speed.linear.x = 0.0
                if mod_theta < np.pi and turning:
                    speed.angular.z = self.angVel
                    print('LEFT')
                    turning = False
                elif turning:
                    speed.angular.z = -self.angVel
                    print('RIGHT')
                    turning = False
            # else go to goal
            else:
                print('FORWARD')
                speed.linear.x = self.linVel
                speed.angular.z = 0.0
                turning = True
            
            self.pub.publish(speed)
            self.r.sleep()
        #stop moving
        self.pub.publish(Twist())

    def rotateToPoint(self,x,y):
        turning = True
        rotate = Twist()
        rotate.angular.z = 1
        inc_x = (x - self.xpos)
        inc_y = (y - self.ypos)
        goalAngle = atan2(inc_y,inc_x)
        inc_theta = goalAngle - self.theta
        while abs(inc_theta) > 0.1:
            
            inc_x = (x - self.xpos)
            inc_y = (y - self.ypos)

            goalAngle = atan2(inc_y,inc_x)
            inc_theta = goalAngle - self.theta
            mod_theta = (inc_theta+(2*np.pi)) % (2*np.pi)
    

            
            if mod_theta < np.pi and turning:
                rotate.angular.z = self.angVel
                print('LEFT')
                turning = False
            elif turning:
                rotate.angular.z = -self.angVel
                print('RIGHT')
                turning = False
            self.pub.publish(rotate)
            self.r.sleep()
        
        self.pub.publish(Twist())

    def alignToBlock(self,obj,color):
        print('align')
        move = Twist()
        move.linear.x = 0.1
        sign = True
        imgCenter = round(obj.maskImg.shape[0]/2)
        while abs(obj.avgRow-imgCenter)>5:
            print('In while2')
            if obj.avgRow-imgCenter >0 and sign:
                move.linear.x = -move.linear.x
                sign = False
            self.pub.publish(move)
            self.r.sleep()
            obj.subscribeToColor(color)
            obj.averageBin()
        self.pub.publish(Twist())

        imgCenter = round(obj.maskImg.shape[1]/2)
        
        rotate = Twist()
        rotate.angular.z = 0.2
        sign = True
        while abs(obj.avgCol-imgCenter) > 10:
            print('IN WHILE')
            print(obj.avgCol,imgCenter)
            if obj.avgCol-imgCenter > 0 and sign:
                rotate.angular.z = -rotate.angular.z
                sign = False
            self.pub.publish(rotate)
            self.r.sleep()
            obj.subscribeToColor(color)
            obj.averageBin()
        self.pub.publish(Twist())

        move = Twist()
        move.linear.x = 0.1
        sign = True
        imgCenter = round(obj.maskImg.shape[0]/2)
        while abs(obj.avgRow-imgCenter)>5:
            print('In while2')
            if obj.avgRow-imgCenter >0 and sign:
                move.linear.x = -move.linear.x
                sign = False
            self.pub.publish(move)
            self.r.sleep()
            obj.subscribeToColor(color)
            obj.averageBin()
        self.pub.publish(Twist())

        imgCenter = round(obj.maskImg.shape[1]/2)

        imgCenter = round(obj.maskImg.shape[1]/2)
        
        rotate = Twist()
        rotate.angular.z = 0.2
        sign = True
        while abs(obj.avgCol-imgCenter) > 10:
            print('IN WHILE')
            print(obj.avgCol,imgCenter)
            if obj.avgCol-imgCenter > 0 and sign:
                rotate.angular.z = -rotate.angular.z
                sign = False
            self.pub.publish(rotate)
            self.r.sleep()
            obj.subscribeToColor(color)
            obj.averageBin()
        self.pub.publish(Twist())



    # def goToObject(self,z):

    
    def shutdown(self):
        self.pub.publish(Twist())
        print('Interrupt command recieved')







    # <--- OUT OF CLASS --> #
def comeHither(bot):
    state = [0.0, 0.0, -1/2, 0.0, -1, 0.0]
    bot.arm.go_to_home_pose()
    for i in range(3):
        bot.arm.set_joint_positions(state)
        bot.arm.go_to_home_pose()
        time.sleep(0.1)

def main():
    # initialize master node for all objects
    locobot = InterbotixLocobotXS(robot_model='locobot_wx250s', arm_model='mobile_wx250s')
    # rospy.init_node('PilotNode',anonymous=False)
    # go to desired point
    locobot.camera.pan_tilt_move(0,0.756252)
    locobot.arm.go_to_sleep_pose()
    locobot.gripper.open()
    print('going to point')
    myOdom = odomGet()
    
    # myOdom.goToGoal(1,0)
    
    myOdom.subscribeToOdom()
    myOdom.rotateToPoint(0,1)
    myOdom.rotateToPoint(1,0)
    myImg = colorImageGet()
    myImg.subscribeToColor('r')
    # cv2.imshow('window1',myImg.maskImg)
    # cv2.waitKey()
    myImg.averageBin()
    myOdom.alignToBlock(myImg,'r')
    # myImg.subscribeToColor('r')
    cv2.imshow('window1',myImg.maskImg)
    cv2.waitKey()
    # locobot = InterbotixLocobotXS(robot_model='locobot_wx250s', arm_model='mobile_wx250s')
    locobot.arm.set_ee_pose_components(x=0.52,y=0.068,z=-0.03,pitch=0)
    locobot.gripper.close()
    holdState = [-0, 0, 0, 0.778, 0, 0.756]
    locobot.arm.set_joint_positions(holdState)
    locobot.arm.go_to_sleep_pose()
    myImg.subscribeToColor('g')
    myImg.averageBin()
    cv2.imshow('window1',myImg.maskImg)
    cv2.waitKey()
    myOdom.alignToBlock(myImg,'g')
    locobot.arm.set_ee_pose_components(x=0.52,y=0.06985,z=-0.01,pitch=0)
    locobot.gripper.open()

    comeHither(locobot)
    
    
    # myOdom.rotateToPoint(-2,4)




   



if __name__ == '__main__':
    main()
    