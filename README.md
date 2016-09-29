# Sterela 4MOB-PAC

## MORSE + ROS Simulation

### Install

* ROS install see http://wiki.ros.org/kinetic/Installation/Ubuntu
* sudo apt install ros-kinetic-desktop-full
* sudo pip3 install catkin-tools rospkg
* sudo apt install morse-simulator python3-morse-simulator

### Launch

* roscore
* morse run sterela_runway

## MAUVE control architecture

### Install

* Source ROS: source /opt/ros/kinetic/setup.bash
* Install OROCOS and RTT-ROS integration:
  * sudo apt install ruby-dev libreadline-dev
  * then follows: https://github.com/orocos/rtt_ros_integration#building-orocos-from-source
* Create a catkin workspace with MAUVE:
  * sudo apt install openjdk-8-{jdk,jre} scala
  * mkdir -p ~/catkin_ws/src
  * cd ~/catkin_ws/src
  * git clone http://mauve:mauve@git.onera.fr/mauve.git src/mauve
  * catkin_make
  * source devel/setup.sh
* Install the control architecture
  