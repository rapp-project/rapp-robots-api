#!/usr/bin/env python

from rapp_robot_api_audio import Audio

class DeviceAudio(Audio):

    def __init__(self, parameters):
        pass

    def speak(self, text, language):
        return {'error': 'Not Supported'}

    def startRecording(self, filename, audio_type, samplerate, channels):
        return {'error': 'Not Supported'}

    def stopRecording(self):
        return {'error': 'Not Supported'}

    def playFile(self, filename):
        return {'error': 'Not Supported'}

    def setVolume(self, volume):
        return {'error': 'Not Supported'}

    def record(self, filename, seconds, audio_type, samplerate, channels):
        return {'error': 'Not Supported'}

    def speechDetection(self, vocabulary, wait, language):
        return {'error': 'Not Supported'}
