#!/usr/bin/env python

from rapp_robot_api_audio import Audio

class DeviceAudio(Audio):

    def __init__(self, parameters):
        pass

    def speak(self, text, language): 
        return {'response': '', 'error': 'Not implemented yet'}

    def startRecording(self, filename, audio_type, samplerate, channels): 
        return {'response': '', 'error': 'Not implemented yet'}

    def stopRecording(self):
        return {'response': '', 'error': 'Not implemented yet'}

    def playFile(self, filename):
        return {'response': '', 'error': 'Not implemented yet'}

    def setVolume(self, volume):
        return {'response': '', 'error': 'Not implemented yet'}

    def record(self, filename, seconds, audio_type, samplerate, channels):
        return {'response': '', 'error': 'Not implemented yet'}

    def speechDetection(self, vocabulary, wait, language):
        return {'response': '', 'error': 'Not implemented yet'}
