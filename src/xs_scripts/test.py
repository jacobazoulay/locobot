from interbotix_xs_modules.locobot import InterbotixLocobotXS

def move_test():
    joint_positions = [-1.0, 0.5 , 0.5, 0, -0.5, 1.57]
    locobot = InterbotixLocobotXS(robot_model="locobot_wx250s", arm_model="mobile_wx250s")
    locobot.arm.go_to_home_pose()
    locobot.arm.set_joint_positions(joint_positions)
    locobot.arm.go_to_home_pose()
    locobot.arm.go_to_sleep_pose()

    
