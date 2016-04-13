#!/usr/bin/env python
import time
import os.path

from rapp_robot_api import RappRobot

rh = RappRobot()

rh.audio.setVolume(70)
rh.audio.speak("This is 60% of the volume")
rh.audio.setVolume(40)
rh.audio.speak("This is 40% of the volume")

rh.audio.speak('Testing start recording for 3 seconds')
rh.audio.startRecording('/home/nao/temp.ogg')
time.sleep(3.0)
rh.audio.speak('Testing stop recording')
rh.audio.stopRecording()

rh.audio.speak('Testing playing file')
rh.audio.playFile('/home/nao/temp.ogg')

rh.audio.speak('Testing record for 5 seconds')
rh.audio.record('/home/nao/temp.ogg', 5)
rh.audio.playFile('/home/nao/temp.ogg')

rh.audio.speak('Testing speech detection for 5 seconds. The words are in and out')
[r,e] = rh.audio.speechDetection(['in', 'out'], 5)
rh.audio.speak('The word captured was ' + str(r[0]))

###############################################################################

rh.audio.speak('Testing set joint angles. The head should move')
rh.motion.enableMotors()
rh.humanoid_motion.setJointAngles(['HeadYaw'], [0.3], 0.5)
[r,e] = rh.humanoid_motion.getJointAngles(['HeadYaw'])
rh.audio.speak('The head yaw is equal to ' + r[0] + ' rads')
rh.audio.speak('Testing opening and closing the hands')
rh.humanoid_motion.openHand('Right')
rh.humanoid_motion.closeHand('Right')
rh.humanoid_motion.openHand('Left')
rh.humanoid_motion.closeHand('Left')
rh.audio.speak('Trying some postures')
rh.humanoid_motion.goToPosture('Stand', 0.7)
[r,e] = rh.humanoid_motion.getPosture()
rh.audio.speak('The posture is ' + r)
rh.humanoid_motion.goToPosture('Sit', 0.7)
[r,e] = rh.humanoid_motion.getPosture()
rh.audio.speak('The posture is ' + r)

rh.humanoid_motion.goToPosture('Stand', 1.0)
rh.audio.speak('Trying some movement. Moving sideways for 3 seconds')
rh.motion.moveByVelocity(0.5, 0.5, 0)
time.sleep(1.5)
[r,e] = rh.motion.getVelocities()
time.sleep(1.5)
rh.motion.moveByVelocity(0, 0, 0)
rh.audio.speak('During movement my velocities were ' + r[0] + ' ' + r[1] + ' ' + r[2])
rh.audio.speak('Testing moving to a point. Goind backwards 0.2 meters and turning a bit')
rh.motion.moveTo(-0.2, -0.2, 0.7)
rh.humanoid_motion.goToPosture('Sit', 1.0)
rh.motion.disableMotors()
rh.audio.speak('Motors are disabled')

###############################################################################

[r,e] = rh.sensors.getBatteryLevels()
rh.audio.speak('My battery level is ' + r + ' %')
[r,e] = rh.sensors.getSonarsMeasurements()
rh.audio.speak('The sonars measurements are ' + r['front_left'] + ' meters and ' +\
        r['front_left'] + ' meters')
rh.audio.speak('Trying the touch sensors for 10 seconds. Touch something')
[r,e] = rh.sensors.getTactileMeasurements(10.0)
touched = ''
for i in r.iterkeys():
    if r[i] > 0:
        touched += ' ' + i
rh.audio.speak('You touched the following: ' + touched)

###############################################################################

rh.audio.speak('Trying to capture an image')
rh.vision.capturePhoto('/home/nao/temp.jpg')
if os.path.isfile('/home/nao/temp.jpg'):
    rh.audio.speak('OK, the picture exists')
else
    rh.audio.speak('hm, there was a problem')

###############################################################################

rh.audio.speak('Ok, i am done!')

