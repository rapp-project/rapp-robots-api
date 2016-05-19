#!/usr/bin/env python

from rapp_nao_api_audio import DeviceAudio
from rapp_nao_api_motion import DeviceMotion
from rapp_nao_api_sensors import DeviceSensors
from rapp_nao_api_humanoid_motion import DeviceHumanoidMotion
from rapp_nao_api_vision import DeviceVision
from rapp_nao_api_utilities import Utilities

import os

# The upper class (namespace), containing per-functionality modules
class RappRobot:
    def __init__(self, ip = "", port = ""):

        self.parameters = {}

        self.configuration = []

        curr_path = os.path.dirname(os.path.realpath(__file__))
        with open(curr_path + "/nao_connectivity") as f:
            self.configuration = f.readlines()

        # Per-device initialization to allow for flexibility
        if ip == "" or port == "":
            self.parameters["nao_ip"] = self.configuration[0].replace('\n', '')
            self.parameters["nao_port"] = self.configuration[1].replace('\n', '')
        else:
            self.parameters["nao_ip"] = ip
            self.parameters["nao_port"] = port

        try:
          self.audio = DeviceAudio(self.parameters)
          self.motion = DeviceMotion(self.parameters)
          self.sensors = DeviceSensors(self.parameters)
          self.humanoid_motion = DeviceHumanoidMotion(self.parameters)
          self.vision = DeviceVision(self.parameters)
          self.utilities = Utilities(self.parameters)
        except:
          print "rapp_robot_api: Not able to connect to proxies (" + str(self.parameters) + ". Check the NAO connection"

