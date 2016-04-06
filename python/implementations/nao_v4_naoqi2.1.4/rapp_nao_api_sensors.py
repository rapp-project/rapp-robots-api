#!/usr/bin/env python

from rapp_robot_api_sensors import Sensors

class DeviceSensors(Sensors):

    def __init__(self, parameters):
        pass

    def getBatteryLevels(self, levels): 
        return [None, "Not implemented yet"]

    def getSonarsMeasurements(self): 
        return [None, "Not implemented yet"]

    def getTactileMeasurements(self, wait): 
        return [None, "Not implemented yet"]

