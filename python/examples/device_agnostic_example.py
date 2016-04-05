#!/usr/bin/env python
import time

from rapp_robot_api import RappRobot

rh = RappRobot()

rh.audio.setVolume(30)
rh.audio.speak("Hello! I will record for 3 seconds")
rh.audio.startRecording("/home/nao/koukou.ogg")
time.sleep(3)
rh.audio.stopRecording()
rh.audio.playFile("/home/nao/koukou.ogg")
