#!/usr/bin/env python

from rapp_robot_api_motion import Motion

from naoqi import ALProxy

class DeviceMotion(Motion):

    def __init__(self, parameters):
        print "NAO motion initiated with parameters: " + str(parameters)

        self.nao_ip = parameters["nao_ip"]
        self.nao_port = int(parameters["nao_port"])

        self.motion = ALProxy("ALMotion", self.nao_ip, self.nao_port)

    def enableMotors(self):
        self.motion.stiffnessInterpolation('Body', 1.0, 0.5)
        return [None, None]

    def disableMotors(self):
        self.motion.stiffnessInterpolation('Body', 0.0, 0.5)
        return [None, None]

    def moveByVelocity(self, x_vel, y_vel, theta_vel):
        self.motion.moveToward(x_vel, y_vel, theta_vel)
        return [None, None]

    def moveTo(self, x, y, theta):
        self.motion.moveTo(x, y, theta)
        return [None, None]

    def stop(self):
        self.motion.stopMove()
        return [None, None]

    def getVelocities(self):
        data = self.motion.getRobotVelocity()
        return [data, None]


