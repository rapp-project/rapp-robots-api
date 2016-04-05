#!/usr/bin/env python

from abc import ABCMeta, abstractmethod

class Interaction:
  __metaclass__ = ABCMeta

  @abstractmethod
  def speak(self): pass
