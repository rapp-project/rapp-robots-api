#!/usr/bin/env python

from rapp_nao_api_audio import DeviceAudio
from rapp_nao_api_motion import DeviceMotion
from rapp_nao_api_sensors import DeviceSensors
from rapp_nao_api_humanoid_motion import DeviceHumanoidMotion
from rapp_nao_api_vision import DeviceVision

# The upper class (namespace), containing per-functionality modules
class RappRobot:
    def __init__(self):

        self.parameters = {}

        self.configuration = []
        with open("nao_connectivity") as f:
            self.configuration = f.readlines()

        # Per-device initialization to allow for flexibility
        self.parameters["nao_ip"] = self.configuration[0]
        self.parameters["nao_port"] = self.configuration[1]

        self.audio = DeviceAudio(self.parameters)
        self.motion = DeviceMotion(self.parameters)
        self.sensors = DeviceSensors(self.parameters)
        self.humanoid_motion = DeviceHumanoidMotion(self.parameters)
        self.vision = DeviceVision(self.parameters)
