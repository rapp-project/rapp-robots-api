#!/usr/bin/env python

from rapp_robot_api_audio import Audio

class DeviceAudio(Audio):

    def __init__(self, parameters):
        pass

    def speak(self, text): 
        return [None, "Not implemented yet"]

    def startRecording(self, filename, audio_type, samplerate, channels): 
        return [None, "Not implemented yet"]

    def stopRecording(self):
        return [None, "Not implemented yet"]

    def playFile(self, filename):
        return [None, "Not implemented yet"]

    def setVolume(self, volume):
        return [None, "Not implemented yet"]

    def record(self, filename, seconds, audio_type, samplerate, channels):
        return [None, "Not implemented yet"]

    def speechDetection(self, vocabulary, language, wait):
        return [None, "Not implemented yet"]

    def voiceEmotionAnalysis(self, wait):
        return [None, "Not implemented yet"]
