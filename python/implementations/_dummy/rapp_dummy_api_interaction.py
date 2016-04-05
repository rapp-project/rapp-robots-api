#!/usr/bin/env python

from rapp_robot_api_interaction import Interaction

class DummyInteraction(Interaction):

  def speak(self, text):
    print "Dummy robot speaks: \"" + str(text) + "\""
