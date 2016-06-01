#!/usr/bin/env python

import unittest

from rapp_robot_api import RappRobot

# Class to perform tests about the Audio functionalities
class RappNaoAPIAudioTests(unittest.TestCase):
    # Setting up the RappRobot class
    def setUp(self):
        self.robot = RappRobot()
        self.robot.audio.setVolume(10)

    # Should produce an error
    def test_speak_wrong_language(self):
        res = self.robot.audio.speak("test", 'Norwegian') 
        self.assertNotEqual(res['error'], None)

    def test_speak_no_language(self):
        res = self.robot.audio.speak("test") 
        self.assertEqual(res['error'], None)

    def test_speak_wrong_text_format(self):
        res = self.robot.audio.speak([1,2,3], 'English') 
        self.assertEqual(res['error'], None)

    def test_speak_correct_language(self):
        res = self.robot.audio.speak("Cuku", 'English') 
        self.assertEqual(res['error'], None)

    ###########################################################################

    def test_startRecording_no_filename(self):
        res = self.robot.audio.startRecording("") 
        self.robot.audio.stopRecording()
        self.assertNotEqual(res['error'], None)

    def test_startRecording_wrong_audiotype(self):
        res = self.robot.audio.startRecording("/home/nao/test.wav", "mp3") 
        self.robot.audio.stopRecording()
        self.assertNotEqual(res['error'], None)

    def test_startRecording_wrong_filepath(self):
        res = self.robot.audio.startRecording("/hme/na/test.wav", "wav") 
        self.robot.audio.stopRecording()
        self.assertNotEqual(res['error'], None)

    def test_startRecording_wrong_samplerate(self):
        res = self.robot.audio.startRecording("/home/nao/test.wav", "wav", -16000) 
        self.robot.audio.stopRecording()
        self.assertNotEqual(res['error'], None)

    def test_startRecording_wrong_channels(self):
        res = self.robot.audio.startRecording("/home/nao/test.wav", "wav", 16000, "test") 
        self.robot.audio.stopRecording()
        self.assertNotEqual(res['error'], None)

    ###########################################################################

    def test_play_non_existent_file(self):
        res = self.robot.audio.playFile("/home/nao/tesssssssst.wav") 
        self.assertNotEqual(res['error'], None)

    ###########################################################################

    def test_set_volume(self):
        res = self.robot.audio.setVolume(200)
        self.assertNotEqual(res['error'], None)
        res = self.robot.audio.setVolume(-100)
        self.assertNotEqual(res['error'], None)
        res = self.robot.audio.setVolume(50)
        self.assertEqual(res['error'], None)

    ###########################################################################

    def test_record_wrong_filepath(self):
        res = self.robot.audio.record("koukou", 1.0)
        self.assertNotEqual(res['error'], None)
        res = self.robot.audio.record("/koukou", 2.0)
        self.assertNotEqual(res['error'], None)

    def test_record_wrong_seconds(self):
        res = self.robot.audio.record("/home/nao/test.wav", -1.0)
        self.assertNotEqual(res['error'], None)

    ###########################################################################

    def test_speech_detection_wrong_voc(self):
        res = self.robot.audio.speechDetection(3, 3)
        self.assertNotEqual(res['error'], None)

    def test_speech_detection_empty_voc(self):
        res = self.robot.audio.speechDetection([], 3)
        self.assertNotEqual(res['error'], None)

    def test_speech_detection_wrong_wait(self):
        res = self.robot.audio.speechDetection(['a'], -3.0)
        self.assertNotEqual(res['error'], None)

###############################################################################

# Class to perform tests about the humanoid motion functionalities
class RappNaoAPIHumanoidMotionTests(unittest.TestCase):
    # Setting up the RappRobot class
    def setUp(self):
        self.robot = RappRobot()

    def test_set_joint_angles_no_joints(self):
        res = self.robot.humanoid_motion.setJointAngles([], [], 1.0)
        self.assertNotEqual(res['error'], None)

    def test_set_joint_angles_joint_is_not_a_list(self):
        res = self.robot.humanoid_motion.setJointAngles(3.0, [], 1.0)
        self.assertNotEqual(res['error'], None)

    def test_set_joint_angles_joint_is_not_a_string(self):
        res = self.robot.humanoid_motion.setJointAngles([3.0], [3.0], 1.0)
        self.assertNotEqual(res['error'], None)
    
    def test_set_joint_angles_angle_is_a_string(self):
        res = self.robot.humanoid_motion.setJointAngles(['HeadYaw'], ['3.0'], 1.0)
        self.assertNotEqual(res['error'], None)
 
    def test_set_joint_angles_wrong_speed(self):
        res = self.robot.humanoid_motion.setJointAngles(['HeadYaw'], [0.3], 1.1)
        self.assertNotEqual(res['error'], None)
        res = self.robot.humanoid_motion.setJointAngles(['HeadYaw'], [0.3], -0.1)
        self.assertNotEqual(res['error'], None)
        res = self.robot.humanoid_motion.setJointAngles(['HeadYaw'], [0.3], '1.1')
        self.assertNotEqual(res['error'], None)

    def test_set_joint_angles_wrong_joint(self):
        res = self.robot.humanoid_motion.setJointAngles(['Head'], [0.3], 1.0)
        self.assertNotEqual(res['error'], None)

    ###########################################################################
    
    def test_open_hand_wrong_hand_number(self):
        res = self.robot.humanoid_motion.openHand(3.0)
        self.assertNotEqual(res['error'], None)

    def test_open_hand_wrong_hand_string(self):
        res = self.robot.humanoid_motion.openHand('Middle')
        self.assertNotEqual(res['error'], None)

    def test_close_hand_wrong_hand_number(self):
        res = self.robot.humanoid_motion.closeHand(3.0)
        self.assertNotEqual(res['error'], None)

    def test_close_hand_wrong_hand_string(self):
        res = self.robot.humanoid_motion.closeHand('Middle')
        self.assertNotEqual(res['error'], None)

    ###########################################################################

    def test_go_to_posture_wrong_posture_string(self):
        res = self.robot.humanoid_motion.goToPosture('Middle', 1.0)
        self.assertNotEqual(res['error'], None)

    def test_go_to_posture_wrong_posture_number(self):
        res = self.robot.humanoid_motion.goToPosture(0.3, 1.0)
        self.assertNotEqual(res['error'], None)

    def test_go_to_posture_wrong_speed(self):
        res = self.robot.humanoid_motion.goToPosture('Sit', 1.1)
        self.assertNotEqual(res['error'], None)
        res = self.robot.humanoid_motion.goToPosture('Sit', -1.1)
        self.assertNotEqual(res['error'], None)
        res = self.robot.humanoid_motion.goToPosture('Sit', '0.3')
        self.assertNotEqual(res['error'], None)

# Class to perform tests about the motion functionalities
class RappNaoAPIMotionTests(unittest.TestCase):
    # Setting up the RappRobot class
    def setUp(self):
        self.robot = RappRobot()

    def test_move_velocity_string_inputs(self):
        ret = self.robot.motion.moveByVelocity('a', 0.1, 0.1)
        self.assertNotEqual(ret['error'], None)
        ret = self.robot.motion.moveByVelocity(0.1, '0.1', 0.1)
        self.assertNotEqual(ret['error'], None)
        ret = self.robot.motion.moveByVelocity(0.1, 0.1, '0.1')
        self.assertNotEqual(ret['error'], None)

    def test_move_velocity_out_of_bounds(self):
        ret = self.robot.motion.moveByVelocity(1.1, 0.1, 0.1)
        self.assertNotEqual(ret['error'], None)
        ret = self.robot.motion.moveByVelocity(0.1, 1.1, 0.1)
        self.assertNotEqual(ret['error'], None)
        ret = self.robot.motion.moveByVelocity(0.1, 0.1, 1.1)
        self.assertNotEqual(ret['error'], None)
        ret = self.robot.motion.moveByVelocity(-1.1, 0.1, 0.1)
        self.assertNotEqual(ret['error'], None)
        ret = self.robot.motion.moveByVelocity(0.1, -1.1, 0.1)
        self.assertNotEqual(ret['error'], None)
        ret = self.robot.motion.moveByVelocity(0.1, 0.1, -1.1)
        self.assertNotEqual(ret['error'], None)

    ###########################################################################

    def test_move_to_string_inputs(self):
        ret = self.robot.motion.moveTo('a', 0.1, 0.1)
        self.assertNotEqual(ret['error'], None)
        ret = self.robot.motion.moveTo(0.1, '0.1', 0.1)
        self.assertNotEqual(ret['error'], None)
        ret = self.robot.motion.moveTo(0.1, 0.1, '0.1')
        self.assertNotEqual(ret['error'], None)

        ret = self.robot.motion.moveTo([0.1], 0.1, 0.1)
        self.assertNotEqual(ret['error'], None)
        ret = self.robot.motion.moveTo(0.1, [0.1], 0.1)
        self.assertNotEqual(ret['error'], None)
        ret = self.robot.motion.moveTo(0.1, 0.1, [0.1])
        self.assertNotEqual(ret['error'], None)

###############################################################################

# Class to perform tests about the sensors functionalities
class RappNaoAPISensorsTests(unittest.TestCase):
    # Setting up the RappRobot class
    def setUp(self):
        self.robot = RappRobot()

    def test_tactile_wait_not_a_number(self):
        ret = self.robot.sensors.getTactileMeasurements('1')
        self.assertNotEqual(ret['error'], None)
        ret = self.robot.sensors.getTactileMeasurements([1])
        self.assertNotEqual(ret['error'], None)

    def test_tactile_get_history_not_bool(self):
        ret = self.robot.sensors.getTactileMeasurements(1.0, 3)
        self.assertNotEqual(ret['error'], None)
        ret = self.robot.sensors.getTactileMeasurements(1.0, '4')
        self.assertNotEqual(ret['error'], None)

###############################################################################

# Class to perform tests about the vision functionalities
class RappNaoAPIVisionTests(unittest.TestCase):
    # Setting up the RappRobot class
    def setUp(self):
        self.robot = RappRobot()

    def test_vision_capture_wrong_path(self):
        ret = self.robot.vision.capturePhoto('test.gif')
        self.assertNotEqual(ret['error'], None)
        ret = self.robot.vision.capturePhoto('')
        self.assertNotEqual(ret['error'], None)
        ret = self.robot.vision.capturePhoto('/test.gif')
        self.assertNotEqual(ret['error'], None)

if __name__ == "__main__":
    unittest.main()
