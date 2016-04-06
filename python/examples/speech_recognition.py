#!/usr/bin/env python
import time

from rapp_robot_api import RappRobot

rh = RappRobot()

# Lower the volume, record an audio and play it back
rh.audio.setVolume(30)
[[word, prob], error] = rh.audio.speechDetection(['one', 'two'], 5.0)
if error == None:
    rh.audio.speak("You said " + word + " with a probability of " + \
        str(int(prob * 100)) + " percent")
else:
    rh.audio.speak(error)
