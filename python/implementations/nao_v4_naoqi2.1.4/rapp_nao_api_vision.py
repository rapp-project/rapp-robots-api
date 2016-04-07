#!/usr/bin/env python

import time
import os

from rapp_robot_api_vision import Vision

from naoqi import ALProxy

class DeviceVision(Vision):

    def __init__(self, parameters):
        print "NAO vision initiated with parameters: " + str(parameters)

        self.nao_ip = parameters["nao_ip"]
        self.nao_port = int(parameters["nao_port"])

        # Intializing NAOQi proxies
        self.photo = ALProxy("ALPhotoCapture", self.nao_ip, self.nao_port)
        self.video = ALProxy("ALVideoDevice", self.nao_ip, self.nao_port)

    def capturePhoto(self, filepath, camera_id, resolution): 
        head, tail = os.path.split(filepath)
        cam_id = -1
        if camera_id == "front":
            cam_id = 0
        elif camera_id == "front_down":
            cam_id = 1
        else:
            return [None, "Camera id not supported"]

        if resolution not in ['40x30', '80x60', '160x120', '320x240', \
                '640x480', '1280x960']:
            return [None, "Resolution id not supported"]

        resol = {}
        resol['40x30'] = 8
        resol['80x60'] = 7
        resol['160x120'] = 0
        resol['320x240'] = 1
        resol['640x480'] = 2
        resol['1280x960'] = 3

        self.photo.setCameraID(cam_id)
        self.photo.setResolution(resol[resolution])
        self.photo.takePicture(head, tail)

        return [None, "Not implemented yet"]

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

