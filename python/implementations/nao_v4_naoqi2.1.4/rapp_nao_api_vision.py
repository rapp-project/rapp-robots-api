#!/usr/bin/env python

from rapp_robot_api_vision import Vision

class DeviceVision(Vision):

    def __init__(self, parameters):
        pass

    def detectBlob(self, color_rgb, threshold, min_size, shape, wait): 
        return [None, "Not implemented yet"]

    def detectDarkness(self, threshold, wait): 
        return [None, "Not implemented yet"]

    def detectMovement(self, sensitivity, wait): 
        return [None, "Not implemented yet"]

    def capturePhoto(self, filepath, camera_id, resolution): 
        return [None, "Not implemented yet"]
