#!/usr/bin/env python

import unittest

from rapp_robot_api import RappRobot

# Class to perform tests about the Audio functionalities
class RappNaoAPIAudioTests(unittest.TestCase):
    # Setting up the RappRobot class
    def setUp(self):
        self.robot = RappRobot()

    # Should produce an error
    def test_speak_wrong_language(self):
        res = self.robot.audio.speak("test", 'Norwegian') 
        self.assertNotEqual(res[1], None)

    def test_speak_no_language(self):
        res = self.robot.audio.speak("test") 
        self.assertEqual(res[1], None)

    def test_speak_wrong_text_format(self):
        res = self.robot.audio.speak([1,2,3], 'English') 
        self.assertEqual(res[1], None)

    def test_speak_correct_language(self):
        res = self.robot.audio.speak("test", 'English') 
        self.assertEqual(res[1], None)

    ###########################################################################

    def test_startRecording_no_filename(self):
        res = self.robot.audio.startRecording("") 
        self.robot.audio.stopRecording()
        self.assertNotEqual(res[1], None)

    def test_startRecording_wrong_audiotype(self):
        res = self.robot.audio.startRecording("/home/nao/test.wav", "mp3") 
        self.robot.audio.stopRecording()
        self.assertNotEqual(res[1], None)

    def test_startRecording_wrong_filepath(self):
        res = self.robot.audio.startRecording("/hme/na/test.wav", "wav") 
        self.robot.audio.stopRecording()
        self.assertNotEqual(res[1], None)

    def test_startRecording_wrong_samplerate(self):
        res = self.robot.audio.startRecording("/home/nao/test.wav", "wav", -16000) 
        self.robot.audio.stopRecording()
        self.assertNotEqual(res[1], None)

    def test_startRecording_wrong_channels(self):
        res = self.robot.audio.startRecording("/home/nao/test.wav", "wav", 16000, "test") 
        self.robot.audio.stopRecording()
        self.assertNotEqual(res[1], None)

    ###########################################################################

    def test_play_non_existent_file(self):
        res = self.robot.audio.playFile("/home/nao/tesssssssst.wav") 
        self.assertNotEqual(res[1], None)


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
