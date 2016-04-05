#!/usr/bin/env python

from abc import ABCMeta, abstractmethod

class Audio:
  __metaclass__ = ABCMeta

  @abstractmethod
  def speak(self, text): pass

  @abstractmethod 
  def startRecording(self, filename, audio_type, samplerate, channels): pass

  @abstractmethod
  def stopRecording(self): pass

  @abstractmethod
  def playFile(self, filename): pass

  @abstractmethod
  def setVolume(self, volume): pass
  
  @abstractmethod 
  def record(self, filename, seconds, audio_type, samplerate, channels): pass

