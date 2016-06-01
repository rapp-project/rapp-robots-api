#!/usr/bin/env python

from rapp_robot_api_humanoid_motion import HumanoidMotion

from naoqi import ALProxy

# Handles the humanoid-specific motion calls
class DeviceHumanoidMotion(HumanoidMotion):
    
    # Initialization of NAO proxies
    def __init__(self, parameters):

        self.nao_ip = parameters["nao_ip"]
        self.nao_port = int(parameters["nao_port"])

        self.posture = ALProxy("ALRobotPosture", self.nao_ip, self.nao_port)
        self.motion = ALProxy("ALMotion", self.nao_ip, self.nao_port)

        self.allowed_joints = ['HeadYaw', 'LShoulderPitch', 'LHipYawPitch1', \
                'RHipYawPitch1', 'RShoulderPitch', 'HeadPitch', 'LShoulderRoll', \
                'LHipRoll', 'RHipRoll', 'RShoulderRoll', \
                'LElbowYaw', 'LHipPitch', 'RHipPitch', 'RElbowYaw', \
                'LElbowRoll', 'LKneePitch', 'RKneePitch', 'RElbowRoll', \
                'LWristYaw2', 'LAnklePitch', 'RAnklePitch', 'RWristYaw2', \
                'LHand2', 'RAnkleRoll', 'LAnkleRoll', 'RHand2']

    # Assistive function to return errors
    def ret_exc(self, text):
        print text
        return {'error': text}

    # Sets a humanoid robot's joints. 'joints' are the names of the joints.
    # The nonmeclature used is the one of the NAO robot:
    # http://doc.aldebaran.com/2-1/family/robots/bodyparts.html#nao-chains
    # Angles are in rads.
    # Speed must be between [0,1], where 1 is the maximum nominal speed
    def setJointAngles(self, joints, angles, speed):
 
        if type(joints) != list or type(angles) != list:
            return self.ret_exc('humanoid_motion.setJointAngles: Joints or angles \
                    not lists')
        if len(joints) == 0 or len(angles) == 0:
            return self.ret_exc('humanoid_motion.setJointAngles: Empty joints \
                    or angles')

        for j in joints:
            if type(j) != str:
                return self.ret_exc('humanoid_motion.setJointAngles: A joint is \
                        not string')
            if j not in self.allowed_joints:
                return self.ret_exc('hunanoid_motion.setJointAngles: Not a valid \
                        joint: ' + str(j))
        if speed <= 0 or speed > 1:
            return self.ret_exc('humanoid_motion.setJointAngles: Speed out of bounds')

        for a in angles:
            if type(a) not in [float, int]:
                return self.ret_exc('humanoid_motion.setJointAngles: Angle not a number')

        try:
            self.motion.setAngles(joints, angles, speed)
        except Exception as e:
            return self.ret_exc("humanoid_motion.setJointAngles: Unrecognized exception: "\
                    + e.message)

        return {'error': None}

    # Returns the joint angles of a humanoid. Again 'joints' are the joints'
    # names, which can be found here:
    # http://doc.aldebaran.com/2-1/family/robots/bodyparts.html#nao-chains
    def getJointAngles(self, joints):
        for i in joints:
            if i not in self.allowed_joints:
                return self.ret_exc('hunanoid_motion.getJointAngles: Not a valid \
                        joint: ' + str(j))

        try:
            data = self.motion.getAngles(joints, False) 
        except Exception as e:
            return self.ret_exc("humanoid_motion.setJointAngles: Unrecognized exception: "\
                    + e.message)

        return {'angles': data, 'error': None}

    # Opens a hand of a humanoid robot. The input must be 'Right' or 'Left'
    def openHand(self, hand_name):
        if hand_name not in ['Right', 'Left']:
            return self.ret_exc('humanoid_motion.openHand: Unsupported hand name: ' +\
                    str(hand_name))
        try:
            if hand_name == "Right":
                self.motion.openHand('RHand')
            elif hand_name == "Left":
                self.motion.openHand('LHand')
        except Exception as e:
            return self.ret_exc("humanoid_motion.openHand: Unrecognized exception: "\
                    + e.message)

        return {'error': None}

    # Closes a NAO's hand. The input must be 'Right' or 'Left'
    def closeHand(self, hand_name):
        if hand_name not in ['Right', 'Left']:
            return self.ret_exc('humanoid_motion.closeHand: Unsupported hand name: ' +\
                    str(hand_name))

        if hand_name == "Right":
            self.motion.closeHand('RHand')
        elif hand_name == "Left":
            self.motion.closeHand('LHand')

        return {'error': None}

    # Forces NAO to go to a predefined posture. The supported postures are here:
    # http://doc.aldebaran.com/2-1/naoqi/motion/alrobotposture.html#term-predefined-postures
    def goToPosture(self, posture, speed):
        if posture not in ["Crouch", "LyingBack", "LyingBelly", "Sit", "SitRelax",\
                "Stand", "StandInit", "StandZero"]:
            return self.ret_exc("humanoid_motion.goToPosture: Not supported posture: " +\
                    str(posture))

        if speed <= 0.0 or speed > 1.0:
            return self.ret_exc('humanoid_motion.goToPosture: Speed out of bounds')

        try:
            self.posture.goToPosture(posture, speed)
        except Exception as e:
            return self.ret_exc("humanoid_motion.goToPosture: Unrecognized exception: "\
                    + e.message)

        return {'error': None}

    # Returns the NAO's posture. If the robot has no predefined posture it will
    # return 'unknown'
    def getPosture(self):
        try:
            ans = self.posture.getPosture()
            return {'posture': ans, 'error': None}
        except Exception as e:
            return self.ret_exc("humanoid_motion.getPosture: Unrecognized exception: "\
                    + e.message)


