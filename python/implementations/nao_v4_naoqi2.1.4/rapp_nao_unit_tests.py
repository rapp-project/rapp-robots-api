#!/usr/bin/env python

import unittest

from rapp_robot_api import RappRobot

# Class to perform tests about the Audio functionalities
class RappNaoAPIAudioTests(unittest.TestCase):
    # Setting up the RappRobot class
    def setUp(self):
        self.robot = RappRobot()

    # function 'audio.speak' testing 'unsupported language'
    def test_speak_wrong_language(self):
        res = self.robot.audio.speak("test", 'Norwegian') 
        self.assertNotEqual(res[1], None)

    # function 'audio.speak' testing 'supported language'
    def test_speak_correct_language(self):
        res = self.robot.audio.speak("test", 'English') 
        self.assertEqual(res[1], None)

# class RappNaoAPIMotionTests (unittest.TestCase):
    # def test(self):
        # self.assertEqual(0, 0)

# class RappNaoAPIHumanoidMotionTests (unittest.TestCase):
    # def test(self):
        # self.assertEqual(0, 0)

# class RappNaoAPISensorsTests (unittest.TestCase):
    # def test(self):
        # self.assertEqual(0, 0)

# class RappNaoAPIVisionTests (unittest.TestCase):
    # def test(self):
        # self.assertEqual(0, 0)

if __name__ == "__main__":
    unittest.main()
