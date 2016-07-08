#!/usr/bin/env python

import rospy

from geometry_msgs.msg import Twist, TwistWithCovariance, Vector3
from nav_msgs.msg import Odometry
from kobuki_msgs.msgs import MotorPower

from rapp_robot_api_motion import Motion

class DeviceMotion(Motion):

    def __init__(self, parameters):
        self._motor_publisher = \
            rospy.Publisher("/mobile_base/commands/motor_power", MotorPower)
        self._velocity_publisher = \
            rospy.Publisher("/mobile_base/commands/velocity", Twist)

    def enableMotors(self):
        msg = MotorPower()
        msg.state = "1"
        self._motor_publisher.publish(msg)
        return {'response': 'Motors Enabled', 'error': ''}

    def disableMotors(self):
        msg = MotorPower()
        msg.state = "0"
        self._motor_publisher.publish(msg)
        return {'response': 'Motors Disabled', 'error': ''}

    def moveByVelocity(self, x_vel, y_vel, theta_vel):
        self._velocity_publisher.publish(
            Twist(Vector3(x_vel, y_vel, 0), Vector3(0, 0, theta_vel)))
        return {'response': 'Velocities set', 'error': ''}

    def moveTo(self, x, y, theta):
        return {'response': '', 'error': 'Not supported'}

    def stop(self):
        self._velocity_publisher.publish(
            Twist(Vector3(0, 0, 0), Vector3(0, 0, 0)))
        return {'response': 'Robot stopped', 'error': ''}

    def getVelocities(self):
        try:
            msg = rospy.wait_for_message("/odom", Odometry, timeout=5)
            vel = msg.twist.twist
            final_vel = [vel.linear.x, vel.linear.y, vel.angular.z]
            return {'velocities': final_vel, 'error': None}
        except (rospy.ROSException, rospy.ROSInterruptException) as rose:
            return {'velocities': None, 'error': rose.str()}
