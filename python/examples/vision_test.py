#!/usr/bin/env python
import time

from rapp_robot_api import RappRobot

rh = RappRobot()

#rh.vision.setActiveCamera("FrontDown")
rh.vision.capturePhoto("/home/nao/aoua.jpg", "front", '1280x960')
#rh.vision.setActiveCamera("Front")
#rh.vision.setResolution("1280x960")
