#!/usr/bin/env python
import time

from rapp_robot_api import RappRobot

rh = RappRobot()

rh.humanoid_motion.goToPosture("Stand", 0.7)
time.sleep(1)
rh.motion.moveTo(0.2, 0.0, 0.0)
time.sleep(1)
rh.motion.moveByVelocity(-0.5, 0.0, 0.2)
time.sleep(2)
print "Velocities: " + str(rh.motion.getVelocities())
time.sleep(2)
rh.motion.stop()
time.sleep(1)
rh.humanoid_motion.goToPosture("Sit", 0.7)

rh.humanoid_motion.setJointAngles(["HeadYaw", "HeadPitch"], [0.2, -0.2], 0.5)

rh.motion.disableMotors()
