#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
        self.tts_animated = ALProxy("ALAnimatedSpeech", self.nao_ip,
                                    self.nao_port)
        self.audio_rec = ALProxy("ALAudioRecorder", self.nao_ip, self.nao_port)
        self.audio_player = ALProxy("ALAudioPlayer", self.nao_ip, self.nao_port)
        self.audio_device = ALProxy("ALAudioDevice", self.nao_ip, self.nao_port)
        self.speech_recog = ALProxy("ALSpeechRecognition", self.nao_ip, self.nao_port)
        self.memory = ALProxy("ALMemory", self.nao_ip, self.nao_port)

    # Assistive function to return errors
    def ret_exc(self, text):
        print text
        return {'error': text}

    def speak(self, text, language='English', animated=False, speed=80):
        """
        Call to make NAO dictate a string. English is the default language.

        @type text: str
        @param text: The text to say

        @type language: str
        @param language: Language to use for TTS translation

        @type animated: bool
        @param animated: Enable animated speech

        @type speed: int
        @param speed: Voice speed. Values in range [0, 200]

        """
        if language in ['en', 'En', 'EN']:
            language = 'English'
        elif language in ['el', 'gr', 'Gr', 'GR']:
            language = 'Greek'
        # Check for supported languages
        supp_lang = ['French', 'Chinese', 'English', 'German', 'Italian',
                     'Japanese', 'Korean', 'Portuguese', 'Spanish', 'Greek']
        if language not in supp_lang:
            return self.ret_exc('audio.speak: Unsupported language')
        # If text is of type unicode, encode to utf8
        if isinstance(text, unicode):
            _text = text.encode('utf8')
        else:
            _text = text
        try:
            self.tts.setLanguage(language)
            self.tts.setParameter("speed", speed)
            if animated:
                self.tts_animated.say(_text,
                                      {"bodyLanguageMode": "contextual"})
            else:
                self.tts.say(_text)
        except Exception as e:
            return self.ret_exc(
                "audio.speak: Unrecognized exception: " + e.message)

        return {'error': None}

    # Call to make NAO start a recording. Supported audio types are wav (1-ch and
    # 4-ch) and ogg (1-ch). Default samplerate is 16kHz and default recording 
    # channel is the front. The filename's path must be absolute.
    def startRecording(self, \
            filename, \
            audio_type = 'ogg', \
            samplerate = 16000, \
            channels = [0, 0, 1, 0]):

        if filename == '' or '/' not in filename:
            return self.ret_exc("audio.startRecording: Invalid filename")
        if audio_type not in ['ogg', 'wav']:
            return self.ret_exc("audio.startRecording: Unsupported audio type")
        if samplerate <= 0 or not isinstance(samplerate, int):
            return self.ret_exc("audio.startRecording: Unsupported samplerate")
        if type(channels) is not list:
            return self.ret_exc("audio.startRecording: Not valid channels format")

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
            return self.ret_exc("audio.startRecording: Unrecognized exception: " + \
                e.message)

        return {'error': None}

    # Stops the recording. Must be called after a startRecording call.
    def stopRecording(self):
        try:
            self.audio_rec.stopMicrophonesRecording()
        except Exception as e:
            return self.ret_exc("audio.stopRecording: Unrecognized exception: " + \
                e.message)
        return {'error': None}

    # Plays a file stored in NAO. Filanema path must be absolute.
    def playFile(self, filename):
        try:
            self.audio_player.playFile(filename)
        except Exception as e:
            return self.ret_exc("audio.playFile: Unrecognized exception: " + \
                e.message)
        return {'error': None} 

    # Sets the NAO volume. The volume must be between 0 and 100, integer.
    def setVolume(self, volume):
        if type(volume) is not int or volume < 0 or volume > 100:
            return self.ret_exc("audio.setVolume: Wrong volume format or value")

        try:
            self.audio_device.setOutputVolume(volume)
        except Exception as e:
            return self.ret_exc("audio.setVolume: Unrecognized exception: " + \
                e.message)

        return {'error': None}

    # Performs recording. The inputs are the same as startRecording but this call
    # has the 'seconds' extra argument which must be a positive float number.
    def record(self, \
            filename, \
            seconds, \
            audio_type = 'ogg', \
            samplerate = 16000, \
            channels = [0,0,1,0]):

        if seconds <= 0.0:
            return self.ret_exc('audio.record: Negative time given')

        ret = \
                self.startRecording(filename, audio_type, samplerate, channels)
        if ret['error'] != None:
            return self.ret_exc('audio.record: ' + ret['error'])

        time.sleep(seconds)

        ret = self.stopRecording()
        if ret['error'] != None:
            return self.ret_exc('audio.record: ' + ret['error'])

        return {'error': None}

    # Performs speech detection with the NAO engine.
    # Vocabulary must be a list of strings
    # Since this is an event-based call, it waits 'wait' seconds for input
    # The default language is English
    def speechDetection(self, vocabulary, wait, language="English"):

        # Sanity checks
        if type(vocabulary) is not list:
            return self.ret_exc('audio.speechDetection: Vocabulary not a list')
        if type(wait) is not float and type(wait) is not int:
            return self.ret_exc('audio.speechDetection: Wait param not a number')
        if wait <= 0:
            return self.ret_exc('audio.speechDetection: Wait param negative value')

        if language in ['en', 'En', 'EN']:
            language = 'English'
        elif language in ['el', 'gr', 'Gr', 'GR']:
            language = 'Greek'
        # Check for supported languages
        supp_lang = ['French', 'Chinese', 'English', 'German', 'Italian',
                     'Japanese', 'Korean', 'Portuguese', 'Spanish', 'Greek']
        if language not in supp_lang:
            return self.ret_exc('audio.speak: Unsupported language')

        _vocabulary = []
        for idx, w in enumerate(vocabulary):
            if isinstance(w, unicode):
                _vocabulary.append(w.encode('utf8'))
            else:
                _vocabulary.append(w)
        # Setting language and activating the speech recognition
        try:
            self.speech_recog.setLanguage(language)
            self.speech_recog.setVocabulary(_vocabulary, False)
        except Exception as e:
            return self.ret_exc("audio.speechDetection: Unrecognized exception: " + \
                e.message)

        # Subscribing to the speech recognition event
        try:
            self.speech_recog.subscribe("rapp_speech_rec")
        except Exception as e:
            return self.ret_exc('audio.speechDetection: Not able to subscribe \
                to speech recognition system: ' + e.message)

        # Wait for 'wait' seconds
        try:
            iterations = wait / 0.1
            while self.memory.getData("WordRecognized")[0] == '' and iterations > 0:
                time.sleep(0.1)
                iterations -= 1
        except Exception as e:

            self.speech_recog.unsubscribe("rapp_speech_rec")
            return self.ret_exc('audio.speechDetection: Something wrong with \
                NAO memory proxy: ' + e.message)

        # If no speech detected return error
        if iterations <= 0:
            self.speech_recog.unsubscribe("rapp_speech_rec")
            return self.ret_exc("audio.speechDetection: Timeout without speech \
                detection")

        # Read the recognized words and return them
        try:
            [word, probability] = self.memory.getData("WordRecognized")
            self.speech_recog.unsubscribe("rapp_speech_rec")
        except Exception as e:
            self.speech_recog.unsubscribe("rapp_speech_rec")
            return self.ret_exc('audio.speechDetection: Error in unsubscription \
                from speech recognition: ' + e.message)

        return {
            'error': None,
            'word': word,
            'probability': probability
        }
