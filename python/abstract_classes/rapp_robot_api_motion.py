#!/usr/bin/env python

from abc import ABCMeta, abstractmethod

class Motion:
    __metaclass__ = ABCMeta

    @abstractmethod
    def enableMotors(self):
        raise NotImplementedError()

    @abstractmethod
    def disableMotors(self):
        raise NotImplementedError()

    # Velocities [-1,1]
    @abstractmethod
    def moveByVelocity(self, x_vel, y_vel, theta_vel):
        raise NotImplementedError()

    # x,y in meters, theta in rads
    @abstractmethod
    def moveTo(self, x, y, theta):
        raise NotImplementedError()

    @abstractmethod
    def stop(self):
        raise NotImplementedError()

    @abstractmethod
    def getVelocities(self):
        raise NotImplementedError()


