#!/usr/bin/env python

from rapp_DEVICE_api_audio import DeviceAudio
from rapp_DEVICE_api_motion import DeviceMotion
from rapp_DEVICE_api_sensors import DeviceSensors
from rapp_DEVICE_api_humanoid_motion import DeviceHumanoidMotion
from rapp_DEVICE_api_vision import DeviceVision

# The upper class (namespace), containing per-functionality modules
class RappRobot:
    def __init__(self):

        self.parameters = {}

        self.audio = DeviceAudio(self.parameters)
        self.motion = DeviceMotion(self.parameters)
        self.sensors = DeviceSensors(self.parameters)
        self.humanoid_motion = DeviceHumanoidMotion(self.parameters)
        self.vision = DeviceVision(self.parameters)
