#!/usr/bin/env python

from abc import ABCMeta, abstractmethod

class Vision:
    __metaclass__ = ABCMeta

    @abstractmethod
    def detectBlob(self, color_rgb, threshold, min_size, shape, wait): 
        raise NotImplementedError()

    @abstractmethod
    def detectDarkness(self, threshold, wait): 
        raise NotImplementedError()

    @abstractmethod
    def detectMovement(self, sensitivity, wait): 
        raise NotImplementedError()

    @abstractmethod
    def capturePhoto(self, filepath, camera_id, resolution): 
        raise NotImplementedError()
