#!/usr/bin/env python

from rapp_robot_api_motion import Motion

from naoqi import ALProxy

# Handles the generic motion calls
class DeviceMotion(Motion):

    # Initialization of the needed NAO proxies
    def __init__(self, parameters):

        self.nao_ip = parameters["nao_ip"]
        self.nao_port = int(parameters["nao_port"])

        self.motion = ALProxy("ALMotion", self.nao_ip, self.nao_port)

    # Assistive function to return errors
    def ret_exc(self, text):
        print text
        return {'error': text}

    # Enables the NAO motors. The robot cannot move if its motors are not
    # enabled (a.k.a. stifness on).
    def enableMotors(self):
        try:
          self.motion.stiffnessInterpolation('Body', 1.0, 0.5)
        except Exception as e:
            return self.ret_exc("motion.enableMotors: Unrecognized exception: " + \
                e.message)

        return {'error': None}
  
    # Disables motors (a.k.a. stifness off)
    def disableMotors(self):
        try:
          self.motion.stiffnessInterpolation('Body', 0.0, 0.5)
        except Exception as e:
            return self.ret_exc("motion.disableMotors: Unrecognized exception: " + \
                e.message)

        return {'error': None}

    # Moves the NAO robot by velocities (all inputs are bounded to [-1,+1], where
    # +1 is the maximum positive speed and -1 is the maximum negative speed
    def moveByVelocity(self, x_vel, y_vel, theta_vel):

        if x_vel < -1 or x_vel > 1:
            return self.ret_exc('motion.moveByVelocity: x_vel out of bounds')
        if y_vel < -1 or y_vel > 1:
            return self.ret_exc('motion.moveByVelocity: y_vel out of bounds')
        if theta_vel < -1 or theta_vel > 1:
            return self.ret_exc('motion.moveByVelocity: theta_vel out of bounds')

        try:
            self.motion.moveToward(x_vel, y_vel, theta_vel)
        except Exception as e:
            return self.ret_exc("motion.moveByVelocity: Unrecognized exception: " + \
                e.message)

        return {'error': None}

    # Moves the NAO robot to the specified pose. x & y are meters, theta is
    # in radians
    def moveTo(self, x, y, theta):
    
        if type(x) not in [float, int]:
            return self.ret_exc('motion.moveTo: x not a number')
        if type(y) not in [float, int]:
            return self.ret_exc('motion.moveTo: y not a number')
        if type(theta) not in [float, int]:
            return self.ret_exc('motion.moveTo: theta not a number')

        try:
          self.motion.moveTo(x, y, theta)
        except Exception as e:
            return self.ret_exc("motion.moveTo: Unrecognized exception: " + \
                e.message)

        return {'error': None}

    # Stops the NAO motion. May be a bit harsh. It is suggested to use the
    # moveByVelocity(0,0,0) instead.
    def stop(self):
        try:
            self.motion.stopMove()
        except Exception as e:
            return self.ret_exc("motion.stop: Unrecognized exception: " + \
                e.message)

        return {'error': None}

    # Returns the NAO velocities in the three axes (x,y,theta)
    def getVelocities(self):
        try:
            data = self.motion.getRobotVelocity()
            return {'velocities': data, 'error': None}
        except Exception as e:
            return self.ret_exc("motion.getVelocities: Unrecognized exception: " + \
                e.message)



