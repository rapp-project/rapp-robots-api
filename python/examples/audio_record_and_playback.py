#!/usr/bin/env python
import time

from rapp_robot_api import RappRobot

rh = RappRobot()

# Lower the volume, record an audio and play it back
rh.audio.setVolume(30)
rh.audio.speak("Hello! I will record for 3 seconds")
rh.audio.record("/home/nao/temp.ogg",3)
rh.audio.playFile("/home/nao/temp.ogg")
