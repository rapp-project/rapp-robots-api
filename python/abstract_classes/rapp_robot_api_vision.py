#!/usr/bin/env python

from abc import ABCMeta, abstractmethod

class Vision:
    __metaclass__ = ABCMeta

    @abstractmethod
    def capturePhoto(self, filepath, camera_id, resolution): 
        raise NotImplementedError()
