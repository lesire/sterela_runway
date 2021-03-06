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
  * cd ~/catkin_ws/
  * git clone http://mauve:mauve@git.onera.fr/mauve.git src/mauve
  * catkin_make
  * source devel/setup.sh
* Install the control architecture
  * cd ~/catkin_ws/
  * git clone https://github.com/lesire/mauve_sterela.git src/mauve_sterela
  * catkin_make
  * source devel/setup.sh
  
### Launch

* roslaunch sterela ObstacleDeployment.launch

## Monitors

### Install

* cd ~/catkin_ws/
* git clone https://github.com/lesire/sterela_monitors.git src/sterela_monitors
* catkin_make
* source devel/setup.sh

### Launch

Will launch the monitor itself (scripts/monitor.py) + topic connections between MAUVE, MORSE and the monitor.

* roslaunch sterela_monitors monitor.launch