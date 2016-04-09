#!/usr/bin/env python

import time

from rapp_robot_api_audio import Audio

from naoqi import ALProxy

class DeviceAudio(Audio):

    def __init__(self, parameters):
        print "NAO audio initiated with parameters: " + str(parameters)

        self.nao_ip = parameters["nao_ip"]
        self.nao_port = int(parameters["nao_port"])

        # Intializing NAOQi proxies
        self.tts = ALProxy("ALTextToSpeech", self.nao_ip, self.nao_port)
        self.audio_rec = ALProxy("ALAudioRecorder", self.nao_ip, self.nao_port)
        self.audio_player = ALProxy("ALAudioPlayer", self.nao_ip, self.nao_port)
        self.audio_device = ALProxy("ALAudioDevice", self.nao_ip, self.nao_port)
        self.speech_recog = ALProxy("ALSpeechRecognition", self.nao_ip, self.nao_port)
        self.memory = ALProxy("ALMemory", self.nao_ip, self.nao_port)

    def speak(self, text, language):

        # Sanity conversion
        _text = str(text)

        # Check for supported languages
        supp_lang = ['French', 'Chinese', 'English', 'German', 'Italian',\
                'Japanese', 'Korean', 'Portuguese', 'Spanish', 'Greek']
        if _language not in supp_lang:
            return [None, 'Unsupported language']

        print "NAO robot speaks: \"" + str(_text) + "\""
        self.tts.setLanguage(_language)
        self.tts.say(_text)
        return [None, None]

    # Audio type: wav or ogg
    def startRecording(self, \
            filename, \
            audio_type = 'ogg', \
            samplerate = 16000, \
            channels = [0, 0, 1, 0]):

        inner_channels = channels.copy()

        # If channels are wrong for NAO, assume to record from the front
        if len(channels) != 4:
            inner_channels = [0, 0, 1, 0] 
        else:
            # Sort out the correct channels. NAO has left-right-front-rear
            # The robot-agnostic API assumes front-right-rear-left
            inner_channels[0] = channels[3]
            inner_channels[2] = channels[1]
            inner_channels[3] = channels[2]

        print "NAO start recording in file: " + str(filename)
        self.audio_rec.startMicrophonesRecording(filename, audio_type, \
                samplerate, inner_channels)
        return [None, None]

    def stopRecording(self):
        print "NAO stop recording"
        self.audio_rec.stopMicrophonesRecording()
        return [None, None]

    def playFile(self, filename):
        print "NAO to play file: " + str(filename)
        self.audio_player.playFile(filename)
        return [None, None]

    def setVolume(self, volume):
        print "Setting NAO volume: " + str(volume) + "%"
        self.audio_device.setOutputVolume(volume)
        return [None, None]

    def record(self, \
            filename, \
            seconds, \
            audio_type = 'ogg', \
            samplerate = 16000, \
            channels = [0,0,1,0]):
        print "NAO records for " + str(seconds) + " seconds in file: " + filename
        self.startRecording(filename, audio_type, samplerate, channels)
        time.sleep(seconds)
        self.stopRecording()
        return [None, None]

    def speechDetection(self, vocabulary, wait, language = "English"):
        print "Performing NAO speech detection in " + language + \
                " and vocabulary = " + str(vocabulary)

        self.speech_recog.setLanguage(language)
        self.speech_recog.setVocabulary(vocabulary, False)

        self.speech_recog.subscribe("rapp_speech_rec")
        iterations = wait / 0.1
        while self.memory.getData("WordRecognized")[0] == '' and iterations > 0:
            time.sleep(0.1)
            iterations -= 1

        error = None
        if iterations <= 0:
            error = "Timeout without speech detection"

        [word, probability] = self.memory.getData("WordRecognized")
        self.speech_recog.unsubscribe("rapp_speech_rec")

        return [[word, probability], error]

