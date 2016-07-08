#!/usr/bin/env python

from rapp_robot_api_vision import Vision

class DeviceVision(Vision):

    def __init__(self, parameters):
        pass

    def capturePhoto(self, filepath, camera_id, resolution): 
        return {'error': 'Not implemented yet'}
