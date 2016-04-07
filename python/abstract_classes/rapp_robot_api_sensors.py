#!/usr/bin/env python

from abc import ABCMeta, abstractmethod

class Sensors:
    __metaclass__ = ABCMeta

    @abstractmethod
    def getBatteryLevels(self): 
        raise NotImplementedError()

    @abstractmethod
    def getSonarsMeasurements(self): 
        raise NotImplementedError()

    @abstractmethod
    def getTactileMeasurements(self, wait, get_history): 
        raise NotImplementedError()

