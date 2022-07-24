import math
import time
from interbotix_xs_modules.locobot import InterbotixLocobotXS


#predefined motions to pick up cube overhead
def pickup(bot):
    holdState = [-0, 0, 0, 0.778, 0, 0.756]
    pickUpState = [-0.08508286926685482, 0.5125083506364536, 0.6001356158147928, -3.1415826428907163, -0.4704778022578129, 3.055215286137077]
    bot.gripper.open()
    bot.arm.set_joint_positions(pickUpState)
    bot.gripper.close()
    bot.arm.set_joint_positions(holdState)


def comeHither(bot):
    state = [0.0, 0.0, -1/2, 0.0, -1, 0.0]
    bot.arm.go_to_home_pose()
    for i in range(3):
        bot.arm.set_joint_positions(state)
        bot.arm.go_to_home_pose()
        time.sleep(0.1)


def main():
    # set time allowed for robot arm to move and accelerate
    moving_time = 5
    accel_time = 2
    # pickUpState = [-0.08508286926685482, 0.5125083506364536, 0.6001356158147928, -3.1415826428907163, -0.4704778022578129, 3.055215286137077]
    locobot = InterbotixLocobotXS(robot_model="locobot_wx250s", arm_model="mobile_wx250s")
    locobot.arm.set_trajectory_time(moving_time,accel_time)
    # pickup(locobot)
    time.sleep(5)
    comeHither(locobot)
    

if __name__=='__main__':
    main()