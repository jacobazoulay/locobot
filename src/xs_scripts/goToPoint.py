#!/usr/bin/env python

import rospy
import numpy as np
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
from geometry_msgs.msg import Point, Twist
from math import atan2

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

        self.linVel = 0.6
        self.angVel = 1
        

        # initialize node
        rospy.init_node('PositionMeasurement', anonymous=False)
        self.r = rospy.Rate(10)
        self.pub = rospy.Publisher('/locobot/mobile_base/commands/velocity', Twist, queue_size=1)
        self.sub = rospy.wait_for_message('/locobot/odom', Odometry)
        self.odomCallback(self.sub)

        # what to call on shutdown
        rospy.on_shutdown(self.shutdown)


    # subscribes to get odom messages
    # publishes to velocity topic
    def subscribeToOdom(self):
        print('Subscribed')
        self.sub = rospy.Subscriber('/locobot/odom', Odometry, self.odomCallback)
        
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

    
    def shutdown(self):
        self.pub.publish(Twist())
        print('Interrupt command recieved')


# <--- OUT OF CLASS --> #




def main(): 

    #make odomGet object
    myOdom = odomGet()
    
    #get data
    myOdom.subscribeToOdom()
    myOdom.goToGoal(1.25,2)
    myOdom.rotateToPoint(1.25,0)

    myOdom.goToGoal(0,0)
    myOdom.rotateToPoint(1,0)

## tester script
def tester():

    # current tester rotates bot to take orientation measurements with respect to desired point
    print('Running testing function')

    myOdom = odomGet()
    myOdom.subscribeToOdom()
    turning = True
    rotate = Twist()
    rotate.angular.z = 1
    while not rospy.is_shutdown():
        
        inc_x = (1 - myOdom.xpos)
        inc_y = (0 - myOdom.ypos)

        goalAngle = atan2(inc_y,inc_x)
        print('angle to goal: ',goalAngle)
        print('bot orientation: ',myOdom.theta)
        inc_theta = goalAngle - myOdom.theta
        mod_theta = (inc_theta+(2*np.pi)) % (2*np.pi)
        print('mod difference: ',mod_theta)

        if abs(inc_theta) > 0.1:
            if mod_theta < np.pi and turning:
                rotate.angular.z = 0.5
                print('LEFT')
                turning = False
            elif turning:
                rotate.angular.z = -0.5
                print('RIGHT')
                turning = False
        else:
            rotate.angular.z = 0
            turning = True
        myOdom.pub.publish(rotate)
        myOdom.r.sleep()


if __name__ == '__main__':

    main()
    # tester()

