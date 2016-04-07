#!/usr/bin/env python
import time

from rapp_robot_api import RappRobot

rh = RappRobot()

rh.humanoid_motion.openHand("Left")
rh.humanoid_motion.closeHand("Left")

rh.humanoid_motion.openHand("Right")
rh.humanoid_motion.closeHand("Right")

print rh.humanoid_motion.getJointAngles(["HeadPitch", "HeadYaw"])
