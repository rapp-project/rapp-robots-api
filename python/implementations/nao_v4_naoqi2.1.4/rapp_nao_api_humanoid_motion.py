#!/usr/bin/env python

from rapp_robot_api_humanoid_motion import HumanoidMotion

from naoqi import ALProxy

class DeviceHumanoidMotion(HumanoidMotion):

    def __init__(self, parameters):
        print "NAO humanoid motion initiated with parameters: " + str(parameters)

        self.nao_ip = parameters["nao_ip"]
        self.nao_port = int(parameters["nao_port"])

        self.posture = ALProxy("ALRobotPosture", self.nao_ip, self.nao_port)
        self.motion = ALProxy("ALMotion", self.nao_ip, self.nao_port)

    def setJointAngles(self, joints, angles, speed):
        self.motion.setAngles(joints, angles, speed)
        return [None, None]

    def getJointAngles(self, joints):
        data = self.motion.getAngles(joints) # Not tested
        return [data, None]

    def openHand(self, hand_name):
        return [None, "Not implemented yet"]

    def closeHand(self, hand_name):
        return [None, "Not implemented yet"]

    def goToPosture(self, posture, speed):
        if posture not in ["Crouch", "LyingBack", "LyingBelly", "Sit", "SitRelax",\
                "Stand", "StandInit", "StandZero"]:
            return [None, "Not supported posture"]

        if speed <= 0.0 or speed > 1.0:
            return [None, "Speed out of bounds"]

        self.posture.goToPosture(posture, speed)
        return [None, None]

    def getPosture(self):
        ans = self.posture.getPosture()
        return [ans, None]

