#!/usr/bin/env python

from abc import ABCMeta, abstractmethod

class Audio:
    __metaclass__ = ABCMeta

    @abstractmethod
    def speak(self, text, language): 
        raise NotImplementedError()

    @abstractmethod 
    def startRecording(self, filename, audio_type, samplerate, channels): 
        raise NotImplementedError()

    @abstractmethod
    def stopRecording(self):
        raise NotImplementedError()

    @abstractmethod
    def playFile(self, filename):
        raise NotImplementedError()

    @abstractmethod
    def setVolume(self, volume):
        raise NotImplementedError()

    @abstractmethod 
    def record(self, filename, seconds, audio_type, samplerate, channels):
        raise NotImplementedError()

    @abstractmethod
    def speechDetection(self, vocabulary, wait, language):
        raise NotImplementedError()

