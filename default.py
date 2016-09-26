#! /usr/bin/env morseexec

"""
CPSELabs Sterela runway light inspection project
"""

from morse.builder import *
from sterela_runway.builder.sensors import PAC

# Runway
runway = PassiveObject("data/road.blend", "Plane")
## plane width is 2.5; length is 11
#runway.scale = ((4000/11),(60/2.5),1)
runway.scale = ((100./11),(20./2.5),1)

# Lights
for i in range(10):
    point = PassiveObject("data/lights2.blend", 'Point') 
    point.translate(x=i*10-50,y=5, z=0.21)
    outlight = PassiveObject("data/lights2.blend", "outlight")
    outlight.translate(x=i*10-50,y=5)
    
# Obstacle
for i in range(10):
    obstacle = PassiveObject("data/obstacle.blend", "Obstacle")
    obstacle.translate(x=i*10-49,y=5)

# 4MOB
robot = ATRV()
keyboard = Keyboard()
keyboard.properties(ControlType = 'Position')
keyboard.properties(Speed=2)
robot.append(keyboard)

# PAC sensor
pac = PAC()
pac.translate(z=0.65,y=-(1+1.3)/2)
robot.append(pac)

# Lasers
robot_laser = Sick()
robot_laser.translate(x=0.6,z=0.15)
robot_laser.properties(Visible_arc=False)
robot.append(robot_laser)
pac_laser = Sick()
pac_laser.translate(z=0.5,y=-(1+1.3)/2)
pac_laser.properties(Visible_arc=False)
robot.append(pac_laser)

#robot.add_default_interface('ros')

# set 'fastmode' to True to switch to wireframe mode
env = Environment('', fastmode = False)
env.set_camera_speed(8) # Increase camera speed for debugging purpose
env.set_camera_location([-18.0, -6.7, 10.8])
env.set_camera_rotation([1.09, 0, -1.14])

