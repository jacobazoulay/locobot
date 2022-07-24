import rospy
import numpy as np 
from geometry_msgs.msg import Twist

class square():
    def __init__(self):
        # initiliaze
        rospy.init_node('Square', anonymous=False)

        # What function to call when you ctrl + c    
        rospy.on_shutdown(self.shutdown)

        # Create a publisher
        self.cmd_vel = rospy.Publisher('/locobot/mobile_base/commands/velocity', Twist, queue_size=100)


        # move forward command
        mv_forward = Twist()
        mv_forward.linear.x = 0.2

        # rotate command
        rotate90 = Twist()
        rotate90.angular.z = np.pi/10

        #execution
        rospy.sleep(1.)
        rospy.loginfo("block1")
        self.cmd_vel.publish(Twist())
        self.cmd_vel.publish(mv_forward)
        rospy.sleep(5.)
        self.cmd_vel.publish(Twist())
        self.cmd_vel.publish(rotate90)
        rospy.sleep(5.)
        self.cmd_vel.publish(Twist())

        rospy.loginfo("block2")
        self.cmd_vel.publish(mv_forward)
        rospy.sleep(5.)
        self.cmd_vel.publish(Twist())
        self.cmd_vel.publish(rotate90)
        rospy.sleep(5.)
        self.cmd_vel.publish(Twist())

        rospy.loginfo("block3")
        self.cmd_vel.publish(mv_forward)
        rospy.sleep(5.)
        self.cmd_vel.publish(Twist())
        self.cmd_vel.publish(rotate90)
        rospy.sleep(5.)
        self.cmd_vel.publish(Twist())

        rospy.loginfo("block4")
        self.cmd_vel.publish(mv_forward)
        rospy.sleep(5.)
        self.cmd_vel.publish(Twist())
        self.cmd_vel.publish(rotate90)
        rospy.sleep(5.)
        self.cmd_vel.publish(Twist())



    def shutdown(self):
        
        self.cmd_vel.publish(Twist())
	    # sleep just makes sure TurtleBot receives the stop command prior to shutting down the script
        rospy.sleep(1)

if __name__ == '__main__':
    try:
        square()
    except:
        rospy.loginfo("square node terminated.")
