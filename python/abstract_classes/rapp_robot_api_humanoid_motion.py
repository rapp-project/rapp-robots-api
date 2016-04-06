#!/usr/bin/env python

from abc import ABCMeta, abstractmethod

class HumanoidMotion:
    __metaclass__ = ABCMeta

    @abstractmethod
    def setJointAngles(self, joints, angles, speed):
        raise NotImplementedError()

    @abstractmethod
    def getJointAngles(self, joints):
        raise NotImplementedError()

    @abstractmethod
    def openHand(self, hand_name):
        raise NotImplementedError()

    @abstractmethod
    def closeHand(self, hand_name):
        raise NotImplementedError()

    @abstractmethod
    def goToPosture(self, posture, speed):
        raise NotImplementedError()

    @abstractmethod
    def getPosture(self):
        raise NotImplementedError()

