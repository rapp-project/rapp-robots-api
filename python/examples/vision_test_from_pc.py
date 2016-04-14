#!/usr/bin/env python
import time

from rapp_robot_api import RappRobot

rh = RappRobot()

rh.vision.capturePhoto("/home/nao/aoua.jpg", "front", '1280x960')
rh.utilities.moveFileToPC('/home/nao/aoua.jpg', 'aoua.jpg')
rh.utilities.moveFileToNAO('/home/nao/aoua2.jpg', 'aoua.jpg')
