# Colaborative Robotic Resource Gathering Locobot
The goal of this project was to develop an autonomous control algorithm and decision-making framework for a 6 DOF mobile-base arm manipulator robot (wx250s Locobot by Trossen Robotics), enabling identification and collection of specified colored objects. The colaborative task required the Locobot to cooperate with another team's Locobot, relying on visual cues and environment mapping as digital communication between the robots was not allowed.


## Scripts

This repo contains Python scripts which can be called with rosrun. These include scripts for controling the movement of the mobile-base, processing the image stream recieved from the Intel® RealSense™ Depth Camera D435, moving the robotic arm and end-effector gripper, and detecting april tags. These can be found in the [src](https://github.com/jacobazoulay/locobot/tree/main/src "src") directory.

These scripts can be run in simulation and on the physical robot. They work on top of the Interbotix ROS packages which provide functionality for SLAM, mobile-base control, navigation control, inverse kinematics for the robotic arm, and various other functions.


## Directory Structure

- **assets**: images for documentation
- **gazebo_worlds**: Gazebo world models for different applications.
- **launch**: ROS launch files for interfacing with the robot.
- **src**: Python scrips for higher level control algorithms and image processing.

## Project Details
### Gazebo Simulation
![Gazeob_Sim](/assets/images/gazebo-locobot.png)

### MoveIt Arm and Gripper Control
![MoveIt_Commander](/assets/images/rviz_locobot.png)

### Trossen Robotics

More information on the Locobot used in the project can be found [here](https://www.trossenrobotics.com/locobot-wx250-6-degree-of-freedom.aspx "trossen").
