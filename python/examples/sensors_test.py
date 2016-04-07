#!/usr/bin/env python
import time

from rapp_robot_api import RappRobot

rh = RappRobot()

print rh.sensors.getBatteryLevels()
print rh.sensors.getSonarsMeasurements()
print rh.sensors.getTactileMeasurements(10.00, False)
