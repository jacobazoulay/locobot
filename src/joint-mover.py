#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from __future__ import print_function
from six.moves import input
from math import pi, tau, dist, fabs, cos
from std_msgs.msg import String
from control_msgs.msg import JointTrajectoryControllerState
from moveit_commander.conversions import pose_to_list
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
import numpy as np



class MoveGroupPythonInterface(object):

    def __init__(self):
        super(MoveGroupPythonInterface, self).__init__()

        moveit_commander.roscpp_initialize(sys.argv)
        rospy.init_node("move_group_python_interface", anonymous=True)

        robot = moveit_commander.RobotCommander(robot_description="locobot/robot_description")

        scene = moveit_commander.PlanningSceneInterface(ns="locobot")

        group_name = "interbotix_arm"
        group_name_gripper = "interbotix_gripper"
        
        move_group = moveit_commander.MoveGroupCommander(robot_description="locobot/robot_description", ns="locobot", name=group_name)
        move_group_gripper = moveit_commander.MoveGroupCommander(robot_description="locobot/robot_description", ns="locobot", name=group_name_gripper)
        

        planning_frame = move_group.get_planning_frame()
        print("============ Planning frame: %s" % planning_frame)

        eef_link = move_group.get_end_effector_link()
        print("============ End effector link: %s" % eef_link)

        group_names = robot.get_group_names()
        print("============ Available Planning Groups:", robot.get_group_names())

        print("============ Printing robot state")
        print(robot.get_current_state())
        print("")

        # Misc variables
        self.box_name = ""
        self.robot = robot
        self.scene = scene
        self.move_group = move_group
        self.move_group_gripper = move_group_gripper
        self.planning_frame = planning_frame
        self.eef_link = eef_link
        self.group_names = group_names

        #vel and accel
        self.move_group.set_max_velocity_scaling_factor(1)
        self.move_group.set_max_acceleration_scaling_factor(1)
        
    
    def get_joints(self):
        #rospy.init_node('jointGet', anonymous=True)
        joints = rospy.wait_for_message('/locobot/arm_controller/state',JointTrajectoryControllerState )
        
        joints = str(joints).splitlines()[22]
        idx = joints.find('[')
        
        joints = joints[idx+1:-1].split(', ')
        joints = [float(x) for x in joints]
        return joints
    
    
    def get_joints_gripper(self):
        joints_gripper = rospy.wait_for_message('/locobot/gripper_controller/state',JointTrajectoryControllerState )
        joints_gripper = str(joints_gripper).splitlines()[18]
        idx = joints_gripper.find('[')
        
        joints_gripper = joints_gripper[idx+1:-1].split(', ')
        joints_gripper = [float(x) for x in joints_gripper]
        return joints_gripper

    
    def go_to_predefined_state(self,state):
        joint_goal = self.get_joints()

        joint_goal = state
        self.move_group.go(joint_goal, wait=True)
        self.move_group.stop()
        current_joints = self.get_joints()

        return all_close(joint_goal, current_joints, 0.01)
    
    
    def go_to_home_state(self):

        joint_goal = self.get_joints()
        
        # home
        joint_goal = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

        self.move_group.go(joint_goal, wait=True)

        self.move_group.stop()

        current_joints = self.get_joints()
        
        return all_close(joint_goal, current_joints, 0.01)
    
    
    def go_to_sleep_state(self):

        joint_goal = self.get_joints()
        
        #sleep
        joint_goal = [0.0, -1.1, 1.55, 0.0, 0.5, 0.0]

        self.move_group.go(joint_goal, wait=True)

        self.move_group.stop()

        current_joints = self.get_joints()
        
        return all_close(joint_goal, current_joints, 0.01)
    
    
    def go_to_hover_state(self):

        joint_goal = self.get_joints()
        
        #hovering above block
        joint_goal = [0.0, 0.86, -0.22, 0.0, 0.89, 0.0]

        self.move_group.go(joint_goal, wait=True)

        self.move_group.stop()

        current_joints = self.get_joints()
        
        return all_close(joint_goal, current_joints, 0.01)
    
    
    def close_gripper(self):
        joint_goal_gripper = self.get_joints_gripper()
        
        #close #original
        joint_goal_gripper = [0.016, -0.016]
        # joint_goal_gripper = [0.021, -0.0227]
        
        self.move_group_gripper.go(joint_goal_gripper, wait=True)

        self.move_group_gripper.stop()

        current_joints = self.get_joints_gripper()
        
        return all_close(joint_goal_gripper, current_joints, 0.01)
    
    
    def open_gripper(self):
        joint_goal_gripper = self.get_joints_gripper()
        
        #open
        joint_goal_gripper = [0.035, -0.035]
        
        self.move_group_gripper.go(joint_goal_gripper, wait=True)

        self.move_group_gripper.stop()

        current_joints = self.get_joints_gripper()
        
        return all_close(joint_goal_gripper, current_joints, 0.01)
    
    
    def go_to_pose_goal(self,x=0.5,y=0.0,z=0.1,qx=0.0,qy=0.0,qz=0.0,qw=0.5):
        
        pose_goal = geometry_msgs.msg.Pose()
        pose_goal.orientation.x = qx
        pose_goal.orientation.y = qy
        pose_goal.orientation.z = qz
        pose_goal.orientation.w = qw
        pose_goal.position.x = x
        pose_goal.position.y = y 
        pose_goal.position.z = z 

        self.move_group.set_pose_target(pose_goal)
        print(pose_goal)

        plan = self.move_group.go(wait=True)

        self.move_group.stop()

        self.move_group.clear_pose_targets()

        return
    

    def plan_cartesian_path(self, scale=1):
        waypoints = []

        wpose = self.move_group.get_current_pose().pose

        wpose.position.z -= scale * 0.1  # First move up (z)
        wpose.position.y += scale * 0.2  # and sideways (y)
        waypoints.append(copy.deepcopy(wpose))

        wpose.position.x += scale * 0.1  # Second move forward/backwards in (x)
        waypoints.append(copy.deepcopy(wpose))

        wpose.position.y -= scale * 0.1  # Third move sideways (y)
        waypoints.append(copy.deepcopy(wpose))

        (plan, fraction) = self.move_group.compute_cartesian_path(
            waypoints, 0.01, 0.0  # waypoints to follow  # eef_step
        )  # jump_threshold

        return plan, fraction


    def execute_plan(self, plan):
        self.move_group.execute(plan, wait=True)
        return

    # this is to tell people to come here
    def comeHither(self):
        
        print("point to ground")
        r = rospy.Rate(10)
        x = 1
        #hovering above block
        

        for i in range(3):
            self.go_to_home_state()
            
            
            joint_goal = self.get_joints()

            joint_goal = [0.0, 0.0, -x/2, 0.0, -x, 0.0]
            self.move_group.go(joint_goal, wait=True)

            self.move_group.stop()
            current_joints = self.get_joints()
            r.sleep()
        
        self.go_to_home_state()
        return all_close(joint_goal, current_joints, 0.01)

    # state for arm to securely hold block
    def holdBlock(self):
        joint_goal = self.get_joints()
        joint_goal = [-0, 0, 0, 0.778, 0, 0.756]

        self.move_group.go(joint_goal, wait=True)

        self.move_group.stop()
        current_joints = self.get_joints()
        return all_close(joint_goal, current_joints, 0.01)




def all_close(goal, actual, tolerance):
    """
    Convenience method for testing if the values in two lists are within a tolerance of each other.
    For Pose and PoseStamped inputs, the angle between the two quaternions is compared (the angle
    between the identical orientations q and -q is calculated correctly).
    @param: goal       A list of floats, a Pose or a PoseStamped
    @param: actual     A list of floats, a Pose or a PoseStamped
    @param: tolerance  A float
    @returns: bool
    """
    if type(goal) is list:
        for index in range(len(goal)):
            if abs(actual[index] - goal[index]) > tolerance:
                return False

    elif type(goal) is geometry_msgs.msg.PoseStamped:
        return all_close(goal.pose, actual.pose, tolerance)

    elif type(goal) is geometry_msgs.msg.Pose:
        x0, y0, z0, qx0, qy0, qz0, qw0 = pose_to_list(actual)
        x1, y1, z1, qx1, qy1, qz1, qw1 = pose_to_list(goal)
        # Euclidean distance
        d = dist((x1, y1, z1), (x0, y0, z0))
        # phi = angle between orientations
        cos_phi_half = fabs(qx0 * qx1 + qy0 * qy1 + qz0 * qz1 + qw0 * qw1)
        return d <= tolerance and cos_phi_half >= cos(tolerance / 2.0)

    return True


def tester():
    try:
        robotControl = MoveGroupPythonInterface()
        # robotControl.holdBlock()
        # robotControl.comeHither()
        # robotControl.go_to_sleep_state()
        # robotControl.go_to_pose_goal(x=0.5,y=0,z=0.05,w=0.0)
        
        robotControl.go_to_predefined_state([-0.08508286926685482, 0.5125083506364536, 0.6001356158147928, -3.1415826428907163, -0.4704778022578129, 3.055215286137077])
        
        robotControl.open_gripper()
        # robotControl.close_gripper()
        # robotControl.comeHither()
        # robotControl.holdBlock()
       
        # print(robotControl.get_joints())        
        # print(robotControl.get_joints_gripper())

    except rospy.ROSInterruptException:
        return
    except KeyboardInterrupt:
        return

def main():
    try:
        robotControl = MoveGroupPythonInterface()
#        input('Go to sleep state')
#        robotControl.go_to_sleep_state()
#        input('Go to home state')
        input('moving to home:')
        robotControl.go_to_home_state()
        input('moving to pose:')
        robotControl.go_to_pose_goal(x=0.4,y=0.0,z=0.1,qx=0.0, qy=0.5**0.5, qz=0.0, qw=0.5**0.5)
        input('getjoints:')
        print(robotControl.move_group.get_current_pose(robotControl.eef_link))
#        input('Open gripper')
#        robotControl.open_gripper()
##        input('Go to hover state')
#        robotControl.go_to_hover_state()
##        input('Close gripper')
#        robotControl.close_gripper()
##        input('Go to home state')
#        robotControl.go_to_home_state()
#
#        robotControl.go_to_sleep_state()
#        input('Go to pose goal')
#        robotControl.go_to_pose_goal()
#        input('Execute cartesian plan')
#        cartesian_plan, fraction = robotControl.plan_cartesian_path()
#        robotControl.execute_plan(cartesian_plan)

    except rospy.ROSInterruptException:
        return
    except KeyboardInterrupt:
        return

### JOINT POSITIONS FOR UPWARD GRABBING ###
# [-0.08508286926685482, 0.5125083506364536, 0.6001356158147928, -3.1415826428907163, -0.4704778022578129, 3.055215286137077]

### JOINT MESSAGE ###
# GOAL = [X Y Z A B C]
# Y = PITCH SHOULDER
# X = YAW ABOUT SHOULDER
# Z = PITCH ABOUT ELBOW
# A = ROLL ABOUT ELBOW
# B = PITCH ABOUT WRIST
# C = ROLL ABOUT WRIST 
if __name__ == "__main__":
    
    main()