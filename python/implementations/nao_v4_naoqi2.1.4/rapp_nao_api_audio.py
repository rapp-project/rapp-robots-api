#!/usr/bin/env python

from rapp_robot_api_audio import Audio
from naoqi import ALProxy

class NAOAudio(Audio):

    def __init__(self, parameters):
        print "NAO audio initiated with parameters: " + str(parameters)

        self.nao_ip = parameters["nao_ip"]
        self.nao_port = int(parameters["nao_port"])

        # Intializing NAOQi proxies
        self.tts = ALProxy("ALTextToSpeech", self.nao_ip, self.nao_port)
        self.audio_rec = ALProxy("ALAudioRecorder", self.nao_ip, self.nao_port)
        self.audio_player = ALProxy("ALAudioPlayer", self.nao_ip, self.nao_port)
        self.audio_device = ALProxy("ALAudioDevice", self.nao_ip, self.nao_port)

    def speak(self, text):
        print "NAO robot speaks: \"" + str(text) + "\""
        self.tts.say(text)

    # Audio type: wav or ogg
    def startRecording(self, \
            filename, \
            audio_type = 'ogg', \
            samplerate = 16000, \
            channels = [0,0,1,0]):
        print "NAO start recording in file: " + str(filename)
        self.audio_rec.startMicrophonesRecording(filename, audio_type, \
                samplerate, channels)

    def stopRecording(self):
        print "NAO stop recording"
        self.audio_rec.stopMicrophonesRecording()

    def playFile(self, filename):
        print "NAO to play file: " + str(filename)
        self.audio_player.playFile(filename)

    # Volume is between [0, 100]
    def setVolume(self, volume):
        print "Setting NAO volume: " + str(volume) + "%"
        self.audio_device.setOutputVolume(volume)

