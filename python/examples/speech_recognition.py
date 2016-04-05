#!/usr/bin/env python
import time

from rapp_robot_api import RappRobot

rh = RappRobot()

# Lower the volume, record an audio and play it back
rh.audio.setVolume(60)
[word, prob] = rh.audio.speechDetection(['one', 'two'])
rh.audio.speak("You said " + word + " with a probability of " + \
        str(int(prob * 100)) + " percent")

