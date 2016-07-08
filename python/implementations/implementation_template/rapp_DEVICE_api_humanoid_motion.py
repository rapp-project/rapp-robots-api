#!/usr/bin/env python

from rapp_robot_api_humanoid_motion import HumanoidMotion

class DeviceHumanoidMotion(HumanoidMotion):

    def __init__(self, parameters):
        pass

    def setJointAngles(self, joints, angles, speed):
        return {'error': 'Not implemented yet'}

    def getJointAngles(self, joints):
        return {'error': 'Not implemented yet'}

    def openHand(self, hand_name):
        return {'error': 'Not implemented yet'}

    def closeHand(self, hand_name):
        return {'error': 'Not implemented yet'}

    def goToPosture(self, posture, speed):
        return {'error': 'Not implemented yet'}

    def getPosture(self):
        return {'error': 'Not implemented yet'}
