#!/usr/bin/env python

from rapp_robot_api_audio import Audio
from naoqi import ALProxy

class NAOAudio(Audio):

  def __init__(self, parameters):
    print "NAO audio initiated with parameters: " + str(parameters)
    
    # Intializing text to speech
    self.tts = ALProxy("ALTextToSpeech", parameters["nao_ip"], \
        int(parameters["nao_port"]))

  def speak(self, text):
    print "NAO robot speaks: \"" + str(text) + "\""
    self.tts.say(text)
