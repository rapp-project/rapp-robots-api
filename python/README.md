- [Setup](https://github.com/rapp-project/rapp-robots-api/tree/master/python#setup)
- RAPP Python API calls
  - [Audio RAPP Python API calls](https://github.com/rapp-project/rapp-robots-api/tree/master/python#audio-rapp-python-api-calls)
    - [rh.audio.speak](https://github.com/rapp-project/rapp-robots-api/tree/master/python#rhaudiospeaktext-language)
    - [rh.audio.startRecording](https://github.com/rapp-project/rapp-robots-api/tree/master/python#rhaudiostartrecordingfilename-audio_type-samplerate-channels)
    - [rh.audio.stopRecording](https://github.com/rapp-project/rapp-robots-api/tree/master/python#rhaudiostoprecording)
    - [rh.audio.playFile](https://github.com/rapp-project/rapp-robots-api/tree/master/python#rhaudioplayfilefilename)
    - [rh.audio.setVolume](https://github.com/rapp-project/rapp-robots-api/tree/master/python#rhaudiosetvolumevolume)
    - [rh.audio.record](https://github.com/rapp-project/rapp-robots-api/tree/master/python#rhaudiorecordfilename-seconds-audio_type-sample_rate-channels)
    - [rh.audio.speechDetection](https://github.com/rapp-project/rapp-robots-api/tree/master/python#rhaudiospeechdetectionvocabulary-wait-language)
  - [Motion RAPP Python API calls](https://github.com/rapp-project/rapp-robots-api/tree/master/python#motion-rapp-python-api-calls)
    - [rh.motion.enableMotors](https://github.com/rapp-project/rapp-robots-api/tree/master/python#rhmotionenablemotors)
    - [rh.motion.disableMotors](https://github.com/rapp-project/rapp-robots-api/tree/master/python#rhmotiondisablemotors)
    - [rh.motion.moveByVelocity](https://github.com/rapp-project/rapp-robots-api/tree/master/python#rhmotionmovebyvelocityx_vel-y_vel-theta_vel)
    - [rh.motion.moveTo](https://github.com/rapp-project/rapp-robots-api/tree/master/python#rhmotionmovetox-y-theta)
    - [rh.motion.stop](https://github.com/rapp-project/rapp-robots-api/tree/master/python#rhmotionstop)
    - [rh.motion.getVelocities](https://github.com/rapp-project/rapp-robots-api/tree/master/python#rhmotiongetvelocities)
  - [Humanoid motion RAPP Python API calls](https://github.com/rapp-project/rapp-robots-api/tree/master/python#humanoid-motion-rapp-python-api-calls)
    - [rh.humanoid_motion.setJointAngles](https://github.com/rapp-project/rapp-robots-api/tree/master/python#rhhumanoid_motionsetjointanglesjoints-angles-speed)
    - [rh.humanoid_motion.getJointAngles](https://github.com/rapp-project/rapp-robots-api/tree/master/python#rhhumanoid_motiongetjointanglesjoints)
    - [rh.humanoid_motion.openHand](https://github.com/rapp-project/rapp-robots-api/tree/master/python#rhhumanoid_motionopenhandhand_name)
    - [rh.humanoid_motion.closeHand](https://github.com/rapp-project/rapp-robots-api/tree/master/python#rhhumanoid_motionclosehandhand_name)
    - [rh.humanoid_motion.goToPosture](https://github.com/rapp-project/rapp-robots-api/tree/master/python#rhhumanoid_motiongotopostureposture-speed)
    - [rh.humanoid_motion.getPosture](https://github.com/rapp-project/rapp-robots-api/tree/master/python#rhhumanoid_motiongetposture)
  - [Sensors RAPP Python API calls](https://github.com/rapp-project/rapp-robots-api/tree/master/python#sensors-rapp-python-api-calls)
    - [rh.sensors.getBatteryLevels](https://github.com/rapp-project/rapp-robots-api/tree/master/python#rhsensorsgetbatterylevels)
    - [rh.sensors.getSonarsMeasurements](https://github.com/rapp-project/rapp-robots-api/tree/master/python#rhsensorsgetsonarsmeasurements)
    - [rh.sensors.getTactileMeasurements](https://github.com/rapp-project/rapp-robots-api/tree/master/python#rhsensorsgettactilemeasurementswait-get_history)
  - [Vision RAPP Python API calls](https://github.com/rapp-project/rapp-robots-api/tree/master/python#vision-rapp-python-api-calls)
    - [rh.vision.capturePhoto](https://github.com/rapp-project/rapp-robots-api/tree/master/python#rhvisioncapturephotofilepath-camera_id-resolution) 
- [Compatibility table](https://github.com/rapp-project/rapp-robots-api/tree/master/python#compatibility-table)

#Setup

In any device for which you want to use the device-agnostic Python API, you must add the path of the ```abstract_classes``` folder and the implementation you want in ```PYTHONPATH```. For example for the NAO case:

```
export PYTHONPATH=$PYTHONPATH:/home/nao/rapp-robots-api/python/abstract_classes
export PYTHONPATH=$PYTHONPATH:/home/nao/rapp-robots-api/python/implementations/nao_v4_naoqi2.1.4
```

Then any python-based application can be executed using the rapp-robot-api implementation for NAO.

In order to use the RAPP robot-agnostic API in an application, you should add to your implementation the following:
```
from rapp_robot_api import RappRobot
rh = RappRobot()
```

Then you can invoke any of the following robot-agnostic calls. Each of these calls returns a Python dictionary.

Nevertheless, since the actual robots have (or should have) their RAPP robot Python API installed, and there may be differences to each implementation (even extra functionalities), if you desire to execute applications to a single robot, please check its implementation:

- [NAO v4, NAOQi 2.1.4 implementation](https://github.com/rapp-project/rapp-robots-api/tree/python_api/python/implementations/nao_v4_naoqi2.1.4)

#Audio RAPP Python API calls

###rh.audio.speak(text, language)

**Description**: The device dictates a ```text```

**Inputs**:
- ```text```: A string containing the text to be dictated by the device
- ```language```: A string containing the language

**Example input**: ```rh.audio.speak("Hello there", "English")```
**Call Output**: ```{'error': None}```
**Expected Output**: The device dictates "Hello there"

***

###rh.audio.startRecording(filename, audio_type, samplerate, channels)

**Description**: The device starts recording using its microphones

**Inputs**:
- ```filename```: An *absolute* file path for the audio to be stored
- ```audio_type```: One of ["wav", "ogg"]
- ```sample_rate```: Integer value defining the sample rate (e.g. 16000)
- ```channels```: Defines which microphones will be recorded. This is a list containing 0 by default and 1 at the microphones to be included as channels (e.g. [0,0,0,1]). This of course is device-specific, thus any API implementation must resolve the arbitrary input.

**Example input**: ```rh.audio.startRecording("/home/device/test.ogg", "ogg", 16000, [0,0,1,0])```

**Call Output**: ```{'error': None}```

**Expected Output**: The audio is captured using one microphone (thus the file contains one channel) and the file exists at ```/home/device/test.ogg```

***
###rh.audio.stopRecording()

**Description**: The device stops the recording. This must be used after a ```startRecording``` invocation.
***
###rh.audio.playFile(filename)

**Description**: The device plays a stored audio file

**Inputs**:
- ```filename```: An *absolute* file path for the audio to be played

**Example input**: ```rh.audio.playFile("/home/device/test.ogg")```

**Call Output**: ```{'error': None}```

**Expected Output**: The device plays the ```/home/device/test.ogg``` file from the speakers
***

###rh.audio.setVolume(volume)

**Description**: Changes the master volume level of the device

**Inputs**:
- ```volume```: The volume level which must be between [0,100]

**Example input**: ```rh.audio.setVolume(50)```

**Call Output**: ```{'error': None}```

**Expected Output**: Nothing interesting. The results will be apparent when NAO plays a file or speaks

***

###rh.audio.record(filename, seconds, audio_type, sample_rate, channels

**Description**: Implements the joined functionality of ```startRecording``` and ```stopRecording```

**Inputs**:
- ```filename```: An *absolute* file path for the audio to be stored
- ```seconds```: Duration of the recording in seconds
- ```audio_type```: One of ["wav", "ogg"]
- ```sample_rate```: Integer value defining the sample rate (e.g. 16000)
- ```channels```: Defines which microphones will be recorded. This is a list containing 0 by default and 1 at the microphones to be included as channels (e.g. [0,0,0,1]). This of course is device-specific, thus any API implementation must resolve the arbitrary input. The first channel is assumed to be the Front one and the next follow in a clockwise fashion (e.g. front-right-rear-left)

**Example input**: ```rh.audio.record("/home/device/test.ogg", 10, "ogg", 16000, [0,0,1,0])```

**Call Output**: ```{'error': None}```

**Expected Output**: The audio is captured using one microphone (thus the file contains one channel) and the file exists at ```/home/device/test.ogg```. The audio file has a duration of 10 seconds.

***

###rh.audio.speechDetection(vocabulary, wait, language)

**Description**: Performs vocabulary-based speech detection

**Inputs**:
- ```vocabulary```: A list of words or sentences to be recognized
- ```wait```: The call waits for N seconds trying to capture voice. If the voice is captured before the expiration of this time duration the call is interrupted.
- ```language```: The full name of the language (e.g. "English")

**Example input**: ```rh.audio.speechDetection(["yes", "no", "maybe"], 10.0, "English")```

**Call Output**: 
- ```{'word': "yes", 'probability': 0.59, 'error': None}``` if "yes" is detected successfully with a probability of 59%
- ```{'error': "Timeout without speech detection"}``` if no speech existed during the time frame

**Expected Output**: No device output.

***
#Motion RAPP Python API calls

###rh.motion.enableMotors()

**Description**: Enables the device's motors (may not be needed in specific devices)

**Inputs**: None

**Example input**: ```rh.motion.enableMotors()```

**Call Output**: ```{'error': None}```

**Expected Output**: All motors' stiffness is enabled

***

###rh.motion.disableMotors()

**Description**: Disables the device's motors (may not be needed in specific devices)

**Inputs**: None

**Example input**: ```rh.motion.disableMotors()```

**Call Output**: ```{'error': None}```

**Expected Output**: All motors' stiffness is removed

***

###rh.motion.moveByVelocity(x_vel, y_vel, theta_vel)

**Description**: Moves the device given the linear and rotational velocities

**Inputs**:
- ```x_vel```: Linear velocity in the X axis (in front of the robot) in m/sec
- ```y_vel```: Linear velocity in the Y axis (right side of the robot) in m/sec
- ```theta_vel```: Rotational velocity in rad/sec

**Example input**: ```rh.motion.moveByVelocity(0.10, 0.0, 0.0)```

**Call Output**: ```{'error': None}```

**Expected Output**: The device walks directly ahead till someone stops it (either another command, an obstacle or a cliff)

***

###rh.motion.moveTo(x, y, theta)

**Description**: The device moves from its current position to the relative pose given

**Inputs**:
- ```x```: The relative pose in the X axis in meters
- ```y```: The relative pose in the Y axis in meters
- ```theta```: The relative rotation in rads

**Example input**: ```rh.motion.moveTo(0.50, 0.0, 0.785)```

**Call Output**: ```{'error': None}```

**Expected Output**: The device walks ahead for 0.5 meters and has eventually has an orientation of 90 degrees

***

###rh.motion.stop()

**Description**: Stops all motion

***

###rh.motion.getVelocities()

**Description**: Returns the current robot velocities

**Inputs**: None

**Example input**: ```rh.motion.getVelocities()```

**Call Output**: ```{'velocities': [0.1, 0.2, 0.3], 'error': None}```: the device as a x_vel=0.1 m/s, y_vel=0.2 m/s and theta_vel=0.3 rad/s

**Expected Output**: No device output

***

#Humanoid Motion RAPP Python API calls

###rh.humanoid_motion.setJointAngles(joints, angles, speed)

**Description**: Sets angles for a humanoid robot's joints

**Inputs**:
- ```joints```: The joints names as a list. The nomenclature used is the one of the [NAO robot](http://doc.aldebaran.com/2-1/family/robots/bodyparts.html#nao-chains)
- ```angles```: A list of the desired angles
- ```speed```: The motion speed ranging from [0.0, 1.0]

**Example input**: ```rh.humanoid_motion.setJointAngles(["HeadYaw", "HeadPitch"], [0.1, 0.2], 0.5)```

**Call Output**: ```{'error': None}```

**Expected Output**: The humanoid moves its head according to the input angles

***

###rh.humanoid_motion.getJointAngles(joints)

**Description**: Gets the angles for a humanoid robot's joints

**Inputs**:
- ```joints```: The joints names as a list. The nomenclature used is the one of the [NAO robot](http://doc.aldebaran.com/2-1/family/robots/bodyparts.html#nao-chains)

**Example input**: ```rh.humanoid_motion.getJointAngles(["HeadYaw", "HeadPitch"])```

**Call Output**: ```{'angles': [0.1, 0.2], 'error': None}```

**Expected Output**: No device output

***

###rh.humanoid_motion.openHand(hand_name)

**Description**: The humanoid opens a hand

**Inputs**:
- ```hand_name```: The name of the hand to be opened ("Right" or "Left")

**Example input**: ```rh.humanoid_motion.openHand("Right")```

**Call Output**: ```{'error': None}```

**Expected Output**: The humanoid opens the right hand

***

###rh.humanoid_motion.closeHand(hand_name)

**Description**: The humanoid closes a hand

**Inputs**:
- ```hand_name```: The name of the hand to be closed ("Right" or "Left")

**Example input**: ```rh.humanoid_motion.closeHand("Right")```

**Call Output**: ```{'error': None}```

**Expected Output**: The humanoid closes the right hand

***

###rh.humanoid_motion.goToPosture(posture, speed)

**Description**: The humanoid goes to a predefined ```posture```

**Inputs**:
- ```posture```: The name of the posture. The nomenclature used is the one of the [NAO robot](http://doc.aldebaran.com/2-1/naoqi/motion/alrobotposture.html#term-predefined-postures)
- ```speed```: The speech of the movement ranging between [0,1], where 1 is the maximum speed.

**Example input**: ```rh.humanoid_motion.goToPosture("Stand")```

**Call Output**: ```{'error': None}```

**Expected Output**: The humanoid stands up

***
###rh.humanoid_motion.getPosture()

**Description**: Returns the current humanoid's posture.

**Inputs**: None

**Example input**: ```rh.humanoid_motion.getPosture()```

**Call Output**: ```{'posture': "Sit", 'error': None}```. If the robot has no predefined posture, ```Unknown``` is returned.

**Expected Output**: None visible

***
#Sensors RAPP Python API calls

###rh.sensors.getBatteryLevels()

**Description**: Returns the batteries' levels in a percentage form

**Inputs**: None

**Example input**: ```rh.sensors.getBatteryLevels()```

**Call Output**: ```{'levels': [50, 80], 'error': None}``` - The robot has two batteries charged 50% and 80%

**Expected Output**: None visible

***
###rh.sensors.getSonarsMeasurements()

**Description**: Returns the sonar's measurements, along with their label. The labels are arbitrarily set using the "front", "rear", "left", "right", "up", "down" words, as well as their combinations, divided by an underscore.

**Inputs**: None

**Example input**: ```rh.sensors.getSonarsMeasurements()```

**Call Output**: ```{'sonars': {'front_left': 1.2, 'front_right': 0.24}, 'error': None}``` - This example is for the NAO robot

**Expected Output**: None visible

***

###rh.sensors.getTactileMeasurements(wait, get_history)

**Description**: Returns the tactile (touch) sensors measurements in a time frame of ```wait``` seconds. This call is robot-specific, since different robots have tactile sensors in various places. For now **only a NAO implementation** makes sense.

**Inputs**: 
- ```wait```: Waits for ```wait``` seconds and if a tactile is touched during this timespan 1.0 is returned
- ```get_history```: The call stores the tactiles' history every 0.1 seconds and returns it

**Example input**: ```rh.sensors.getTactileMeasurements(1.0, False)```

**Call Output**: ```{'tactiles': {'head_middle': 0.0, 'left_hand_back': 0.0, 'left_hand_right': 0.0, 'right_hand_right': 0.0, 'head_front': 0.0, 'right_hand_left': 0.0, 'left_hand_left': 0.0, 'head_rear': 0.0, 'left_foot': 1.0, 'right_hand_back': 0.0, 'right_foot': 1.0}, 'error': None}```. This means that the left Foot and the right Foot bumpers were triggered during the 1.0 second.

**Example input**: ```rh.sensors.getTactileMeasurements(5.0, True)```

**Call Output**: 
```{'tactiles': [{'head_front': 0, 'head_middle': 0, 'head_rear': 0}, {'head_front': 0, 'head_middle': 0, 'head_rear': 0}, {'head_front': 0, 'head_middle': 0, 'head_rear': 0}, {'head_front': 0, 'head_middle': 0, 'head_rear': 0}, {'head_front': 0, 'head_middle': 0, 'head_rear': 0}, {'head_front': 0, 'head_middle': 0, 'head_rear': 0}, {'head_front': 0, 'head_middle': 0, 'head_rear': 0}, {'head_front': 0, 'head_middle': 0, 'head_rear': 0}, {'head_front': 0, 'head_middle': 0, 'head_rear': 0}, {'head_front': 0, 'head_middle': 0, 'head_rear': 0}, {'head_front': 0, 'head_middle': 0, 'head_rear': 0}, {'head_front': 0, 'head_middle': 0, 'head_rear': 0}, {'head_front': 0, 'head_middle': 0, 'head_rear': 0}, {'head_front': 0, 'head_middle': 0, 'head_rear': 0}, {'head_front': 0, 'head_middle': 0, 'head_rear': 0}, {'head_front': 0, 'head_middle': 0, 'head_rear': 0}, {'head_front': 0, 'head_middle': 0, 'head_rear': 0}, {'head_front': 0, 'head_middle': 0, 'head_rear': 0}, {'head_front': 0, 'head_middle': 0, 'head_rear': 0}, {'head_front': 0, 'head_middle': 0, 'head_rear': 0}, {'head_front': 0, 'head_middle': 0, 'head_rear': 0}, {'head_front': 0, 'head_middle': 0, 'head_rear': 0}, {'head_front': 0, 'head_middle': 0, 'head_rear': 0}, {'head_front': 0, 'head_middle': 0, 'head_rear': 0}, {'head_front': 0, 'head_middle': 0, 'head_rear': 0}, {'head_front': 0, 'head_middle': 0, 'head_rear': 0}, {'head_front': 0, 'head_middle': 0, 'head_rear': 0}, {'head_front': 0, 'head_middle': 0, 'head_rear': 0}, {'head_front': 0, 'head_middle': 0, 'head_rear': 0}, {'head_front': 0, 'head_middle': 0, 'head_rear': 0}, {'head_front': 0, 'head_middle': 0, 'head_rear': 0}, {'head_front': 0, 'head_middle': 0, 'head_rear': 0}, {'head_front': 0, 'head_middle': 0, 'head_rear': 0}, {'head_front': 0, 'head_middle': 0, 'head_rear': 0}, {'head_front': 0, 'head_middle': 0, 'head_rear': 0}, {'head_front': 1, 'head_middle': 0, 'head_rear': 0}, {'head_front': 1, 'head_middle': 0, 'head_rear': 0}, {'head_front': 1, 'head_middle': 0, 'head_rear': 0}, {'head_front': 1, 'head_middle': 0, 'head_rear': 0}, {'head_front': 1, 'head_middle': 0, 'head_rear': 0}, {'head_front': 1, 'head_middle': 0, 'head_rear': 0}, {'head_front': 1, 'head_middle': 0, 'head_rear': 0}, {'head_front': 1, 'head_middle': 0, 'head_rear': 0}, {'head_front': 0, 'head_middle': 0, 'head_rear': 0}, {'head_front': 0, 'head_middle': 0, 'head_rear': 0}, {'head_front': 0, 'head_middle': 0, 'head_rear': 0}, {'head_front': 0, 'head_middle': 0, 'head_rear': 0}, {'head_front': 0, 'head_middle': 0, 'head_rear': 0}, {'head_front': 0, 'head_middle': 0, 'head_rear': 0}, {'head_front': 0, 'head_middle': 0, 'head_rear': 0}], 'error': None}```: The front head sensors was touched for 0.8 seconds (8 times visible)

**Expected Output**: None visible

***
#Vision RAPP Python API calls

###rh.vision.capturePhoto(filepath, camera_id, resolution)

**Description**: Returns the tactile (touch) sensors measurements in a time frame of ```wait``` seconds. This call is robot-specific, since different robots have tactile sensors in various places. For now **only a NAO implementation** makes sense.

**Inputs**: 
- ```filepath```: The absolute path of the picture to be stored (including the postfix)
- ```camera_id```: The camera "name". The labels are arbitrarily set using the "front", "rear", "left", "right", "up", "down" words, as well as their combinations, divided by an underscore. The per-device implementation must sort this out.
- ```resolution```: The camera resolution. The supported values are one of '40x30', '80x60', '160x120', '320x240', '640x480', '1280x960'. Again the per-device implementation must sort these inputs out.

**Example input**: ```rh.vision.capturePhoto("/home/nao/test.jpg", "front", "1280x960")```

**Call Output**: ```{'error': None}```

**Expected Output**: The image must exist at "/home/nao/test.jpg"

***

#Compatibility table

|API call | NAO v4 |
| :--------: | :--------: |
| rh.audio.speak | ✓ |
| rh.audio.startRecording | ✓ |
| rh.audio.stopRecording | ✓ |
| rh.audio.playFile | ✓ |
| rh.audio.setVolume | ✓ |
| rh.audio.record | ✓ |
| rh.audio.speechDetection | ✓ |
| rh.motion.enableMotors | ✓ |
| rh.motion.disableMotors | ✓ |
| rh.motion.moveByVelocity | ✓ |
| rh.motion.moveTo | ✓ |
| rh.motion.stop | ✓ |
| rh.humanoid_motion.getVelocities | ✓ |
| rh.humanoid_motion.setJointAngles | ✓ |
| rh.humanoid_motion.getJointAngles | ✓ |
| rh.humanoid_motion.openHand | ✓ |
| rh.humanoid_motion.closeHand | ✓ |
| rh.humanoid_motion.goToPosture | ✓ |
| rh.humanoid_motion.getPosture | ✓ |
| rh.sensors.getBatteryLevels | ✓ |
| rh.sensors.getSonarsMeasurements | ✓ |
| rh.sensors.getTactileMeasurements | ✓ |
| rh.vision.capturePhoto | ✓ |


