#! /usr/bin/env morseexec

"""
CPSELabs Sterela runway light inspection project
"""

from morse.builder import *
from sterela_runway.builder.sensors import PAC
import math, os, bpy

# Runway
runway = Plane("Runway")
runway.scale = (50, 10, 1)
runway._bpy_object.game.physics_type = 'STATIC'

# Sun
scene = bpy.context.scene
lamp_data = bpy.data.lamps.new(name="Sun", type='SUN')
lamp_object = bpy.data.objects.new(name="Sun", object_data=lamp_data)
scene.objects.link(lamp_object)
lamp_object.location = (0, 0, 10.0)

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
pose = Pose()
robot.append(pose)

# PAC sensor
pac = PAC()
pac.translate(z=0.65,y=(1+1.3)/2)
robot.append(pac)

# Lasers
robot_laser = Hokuyo()
robot_laser.translate(x=.6,y=.4,z=0.15)
robot_laser.properties(Visible_arc=False)
robot_laser.properties(scan_window=270)
robot.append(robot_laser)

pac_laser = Sick()
pac_laser.translate(z=0.5,y=(1+1.3)/2)
pac_laser.properties(Visible_arc=False)
pac_laser.properties(scan_window=90)
robot.append(pac_laser)

# V,W control
control = MotionVW()
robot.append(control)

# Init robot: start of line
robot.translate(x=-45,y=3.85)
robot.add_default_interface('ros')
#robot.add_default_interface('socket')

# set 'fastmode' to True to switch to wireframe mode
env = Environment('', fastmode = False)
env.set_camera_speed(8) # Increase camera speed for debugging purpose
env.set_camera_location([-18.0, -6.7, 10.8])
env.set_camera_rotation([1.09, 0, -1.14])
env.show_framerate()
env.show_debug_properties()

