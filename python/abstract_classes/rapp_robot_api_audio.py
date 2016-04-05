#!/usr/bin/env python

from abc import ABCMeta, abstractmethod

class Audio:
  __metaclass__ = ABCMeta

  @abstractmethod
  def speak(self): pass
