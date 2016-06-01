#!/usr/bin/env python

import time
import os

from rapp_robot_api_vision import Vision

from naoqi import ALProxy

# Handles the vision modules of NAO
class DeviceVision(Vision):

    # Initialization of NAO proxies
    def __init__(self, parameters):

        self.nao_ip = parameters["nao_ip"]
        self.nao_port = int(parameters["nao_port"])

        # Intializing NAOQi proxies
        self.photo = ALProxy("ALPhotoCapture", self.nao_ip, self.nao_port)
        self.video = ALProxy("ALVideoDevice", self.nao_ip, self.nao_port)

    # Assistive function to return errors
    def ret_exc(self, text):
        print text
        return {'error': text}

    # Captures a photo and stores it LOCALLY in NAO.
    # The filepath must be absolute (not relative)
    # The camera_id must be one of ['front', 'front_down']. If it is anything
    # else the 'front' camera is assumed, which is the default value.
    # Resolution must be one of '40x30', '80x60', '160x120', '320x240', '640x480'
    # and '1280x960'. If it is anything else '640x480 is assumed, being the
    # default value.
    def capturePhoto(self, filepath, camera_id = 'front', resolution = '640x480'): 

        if '/home/nao/' not in filepath:
            return self.ret_exc('vision.capturePhoto: Erroneous filepath')

        head, tail = os.path.split(filepath)
        cam_id = 0
        if camera_id not in ['front', 'front_down']:
            cam_id = 0
        if camera_id == "front_down":
            cam_id = 1
        l_resolution = resolution
        if resolution not in ['40x30', '80x60', '160x120', '320x240', \
                '640x480', '1280x960']:
            l_resolution = '640x480'

        resol = {}
        resol['40x30'] = 8
        resol['80x60'] = 7
        resol['160x120'] = 0
        resol['320x240'] = 1
        resol['640x480'] = 2
        resol['1280x960'] = 3

        try:
            self.photo.setCameraID(cam_id)
            self.photo.setResolution(resol[l_resolution])
            self.photo.takePicture(head, tail)
        except Exception as e:
            return self.ret_exc("vision.capturePhoto: Unrecognized exception: " + \
                e.message)

        return {'error': None}

    #def setActiveCamera(self, camera_id):
        #cam_id = -1
        #if camera_id == "Front":
            #cam_id = 0
        #elif camera_id == "FrontDown":
            #cam_id = 1
        #else:
            #return [None, "Camera id not supported"]
        #self.video.setActiveCamera(cam_id)

    #def setResolution(self, resolution):
        #resol = {}
        #resol['40x30'] = 8
        #resol['80x60'] = 7
        #resol['160x120'] = 0
        #resol['320x240'] = 1
        #resol['640x480'] = 2
        #resol['1280x960'] = 3

        #if resolution not in ['40x30', '80x60', '160x120', '320x240', \
                #'640x480', '1280x960']:
            #return [None, "Resolution id not supported"]

        #self.video.setResolution("rapp_video_handler", resol[resolution])

