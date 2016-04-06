#!/usr/bin/env python

from rapp_robot_api_motion import Motion

class DeviceMotion(Motion):

    def __init__(self, parameters):
        pass

    def enableMotors(self):
        return [None, "Not implemented yet"]
    
    def disableMotors(self):
        return [None, "Not implemented yet"]

    def moveByVelocity(self, x_vel, y_vel, theta_vel):
        return [None, "Not implemented yet"]

    def moveTo(self, x, y, theta):
        return [None, "Not implemented yet"]

    def stop(self):
        return [None, "Not implemented yet"]

    def getVelocities(self):
        return [None, "Not implemented yet"]


