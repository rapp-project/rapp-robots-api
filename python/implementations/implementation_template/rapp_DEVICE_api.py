#!/usr/bin/env python

from rapp_DEVICE_api_audio import DeviceAudio
from rapp_DEVICE_api_motion import DeviceMotion
from rapp_DEVICE_api_sensors import DeviceSensors
from rapp_DEVICE_api_humanoid_motion import DeviceHumanoidMotion
from rapp_DEVICE_api_vision import DeviceVision

# The upper class (namespace), containing per-functionality modules
class RappRobot:
    def __init__(self):
        self.audio = DeviceAudio()
        self.motion = DeviceMotion()
        self.sensors = DeviceSensors()
        self.humanoid_motion = DeviceHumanoidMotion()
        self.vision = DeviceVision()
