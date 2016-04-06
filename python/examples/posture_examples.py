#!/usr/bin/env python
import time

from rapp_robot_api import RappRobot

rh = RappRobot()

[data, err] = rh.humanoid_motion.getPosture()
rh.audio.speak("My posture is " + data)

rh.humanoid_motion.goToPosture("Stand", 0.7)

time.sleep(3)

rh.audio.speak("My posture is " + \
        rh.humanoid_motion.getPosture()[0])
rh.humanoid_motion.goToPosture("Sit", 0.7)

rh.motion.disableMotors()
