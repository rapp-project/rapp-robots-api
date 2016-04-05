#!/usr/bin/env python

from rapp_nao_api_audio import NAOAudio

# The upper class (namespace), containing per-functionality modules
class RappRobot:
    def __init__(self):
        self.parameters = {}

        # Per-device initialization to allow for flexibility
        #NOTE: These should be in an init file
        self.parameters["nao_ip"] = "192.168.0.101"
        self.parameters["nao_port"] = "9559"

        self.audio = NAOAudio(self.parameters)

