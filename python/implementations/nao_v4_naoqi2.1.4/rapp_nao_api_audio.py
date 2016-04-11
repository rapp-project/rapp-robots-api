#!/usr/bin/env python

import time

from rapp_robot_api_audio import Audio

from naoqi import ALProxy

# Handles the audio-related calls
class DeviceAudio(Audio):

    # Inialization of the NAO proxies needed to perform the calls
    def __init__(self, parameters):
        self.nao_ip = parameters["nao_ip"]
        self.nao_port = int(parameters["nao_port"])

        # Intializing NAOQi proxies
        self.tts = ALProxy("ALTextToSpeech", self.nao_ip, self.nao_port)
        self.audio_rec = ALProxy("ALAudioRecorder", self.nao_ip, self.nao_port)
        self.audio_player = ALProxy("ALAudioPlayer", self.nao_ip, self.nao_port)
        self.audio_device = ALProxy("ALAudioDevice", self.nao_ip, self.nao_port)
        self.speech_recog = ALProxy("ALSpeechRecognition", self.nao_ip, self.nao_port)
        self.memory = ALProxy("ALMemory", self.nao_ip, self.nao_port)

    # Call to make NAO dictate a string. English is the default language.
    def speak(self, text, language = 'English'):
        # Sanity conversion
        _text = str(text)

        # Check for supported languages
        supp_lang = ['French', 'Chinese', 'English', 'German', 'Italian',\
                'Japanese', 'Korean', 'Portuguese', 'Spanish', 'Greek']
        if language not in supp_lang:
            return [None, 'audio.speak: Unsupported language']
        try:
            self.tts.setLanguage(language)
            self.tts.say(_text)
        except Exception as e:
            error = "audio.speak: Unrecognized exception: " + e.message
            print error
            return [None, error]
        return [None, None]

    # Call to make NAO start a recording. Supported audio types are wav (1-ch and
    # 4-ch) and ogg (1-ch). Default samplerate is 16kHz and default recording 
    # channel is the front. The filename's path must be absolute.
    def startRecording(self, \
            filename, \
            audio_type = 'ogg', \
            samplerate = 16000, \
            channels = [0, 0, 1, 0]):

        if filename == '':
            error = "audio.startRecording: Invalid filename"
            print error
            return [None, error]
        if audio_type not in ['ogg', 'wav']:
            error = "audio.startRecording: Unsupported audio type"
            print error
            return [None, error]
        if samplerate <= 0 or not isinstance(samplerate, int):
            error = "audio.startRecording: Unsupported samplerate"
            print error
            return [None, error]
        if type(channels) is not list:
            error = "audio.startRecording: Not valid channels format"
            print error
            return [None, error]

        # Channels copy
        inner_channels = channels[:]

        # If channels are wrong for NAO, assume to record from the front
        if len(channels) != 4:
            inner_channels = [0, 0, 1, 0] 
        else:
            # Sort out the correct channels. NAO has left-right-front-rear
            # The robot-agnostic API assumes front-right-rear-left
            inner_channels[0] = channels[3]
            inner_channels[2] = channels[1]
            inner_channels[3] = channels[2]

        try:
            self.audio_rec.startMicrophonesRecording(filename, audio_type, \
                samplerate, inner_channels)
        except Exception as e:
            self.audio_rec.stopMicrophonesRecording()
            error = "audio.startRecording: Unrecognized exception: " + e.message
            print error
            return [None, error]

        return [None, None]

    # Stops the recording. Must be called after a startRecording call.
    def stopRecording(self):
        try:
            self.audio_rec.stopMicrophonesRecording()
        except Exception as e:
            error = "audio.stopRecording: Unrecognized exception: " + e.message
            print error
            return [None, error]
        return [None, None]

    # Plays a file stored in NAO. Filanema path must be absolute.
    def playFile(self, filename):
        try:
            self.audio_player.playFile(filename)
        except Exception as e:
            error = "audio.playFile: Unrecognized exception: " + e.message
            print error
            return [None, error]
        return [None, None]

    # Sets the NAO volume. The volume must be between 0 and 100, integer.
    def setVolume(self, volume):
        if type(volume) is not int or volume < 0 or volume > 100:
            error = "audio.setVolume: Wrong volume format or value"
            print error
            return [None, error]

        try:
            self.audio_device.setOutputVolume(volume)
        except Exception as e:
            error = "audio.setVolume: Unrecognized exception: " + e.message
            print error
            return [None, error]

        return [None, None]

    # Performs recording. The inputs are the same as startRecording but this call
    # has the 'seconds' extra argument which must be a positive float number.
    def record(self, \
            filename, \
            seconds, \
            audio_type = 'ogg', \
            samplerate = 16000, \
            channels = [0,0,1,0]):

        [ret, err] = \
                self.startRecording(filename, audio_type, samplerate, channels)
        if err != None:
            print err
            return [None, err]

        time.sleep(seconds)

        [ret, err] = self.stopRecording()
        if err != None:
            print err
            return [None, err]
        return [None, None]

    # Performs speech detection with the NAO engine. 
    # Vocabulary must be a list of strings
    # Since this is an event-based call, it waits 'wait' seconds for input
    # The default language is English
    def speechDetection(self, vocabulary, wait, language = "English"):

        # Sanity checks
        if type(vocabulary) is not list:
            error = 'audio.speechDetection: Vocabulary not a list'
            print error
            return [None, error]
        if type(wait) is not float and type(wait) is not int:
            error = 'audio.speechDetection: Wait param not a number'
            print error
            return [None, error]
        if wait <= 0:
            error = 'audio.speechDetection: Wait param negative value'
            print error
            return [None, error]

        # Setting language and activating the speech recognition
        try:
            self.speech_recog.setLanguage(language)
            self.speech_recog.setVocabulary(vocabulary, False)
        except Exception as e:
            error = "audio.speechDetection: Unrecognized exception: " + e.message
            print error
            return [None, error]
        
        # Subscribing to the speech recognition event
        try:
            self.speech_recog.subscribe("rapp_speech_rec")
        except Exception as e:
            error = 'audio.speechDetection: Not able to subscribe to speech \
                    recognition system: ' + e.message
            print error
            return [None, error]

        # Wait for 'wait' seconds
        try:
            iterations = wait / 0.1
            while self.memory.getData("WordRecognized")[0] == '' and iterations > 0:
                time.sleep(0.1)
                iterations -= 1
        except Exception as e:
            error = 'audio.speechDetection: Something wrong with NAO memory proxy: ' +\
                    e.message
            print error
            return [None, error]

        # If no speech detected return error
        if iterations <= 0:
            error = "audio.speechDetection: Timeout without speech detection"
            return [None, error]

        # Read the recognized words and return them
        try:
            [word, probability] = self.memory.getData("WordRecognized")
            self.speech_recog.unsubscribe("rapp_speech_rec")
        except Exception as e:
            error = 'audio.speechDetection: Error in unsubscription from speech \
                    recognition: ' + e.message
            print error
            return [None, error]

        return [[word, probability], None]

