#! /usr/bin/env morseexec

"""
CPSELabs Sterela runway light inspection project
"""

from morse.builder import *

# Runway
runway = PassiveObject("./data/road.blend", "Plane")
## plane width is 2.5; length is 11
#runway.scale = ((4000/11),(60/2.5),1)
runway.scale = ((100./11),(20./2.5),1)

# 4MOB
robot = Morsy()
keyboard = Keyboard()
keyboard.properties(ControlType = 'Position')
robot.append(keyboard)

#robot.add_default_interface('ros')

# set 'fastmode' to True to switch to wireframe mode
env = Environment('', fastmode = False)
env.set_camera_location([-18.0, -6.7, 10.8])
env.set_camera_rotation([1.09, 0, -1.14])

