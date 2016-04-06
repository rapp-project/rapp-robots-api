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

Then you can invoke any of the following robot-agnostic calls. Each of these calls returns a predefined structure, being ```[data, error]```. ```data``` is call-specific, whereas the ```error``` field contains possible execution errors, or simply a message that this API call has not been implemented for a specific robot.

| RAPP Robot-agnostic Python API calls    | Description   |
| :------------------------------- | :----------- |
| ```rh.audio.speak(text)```  | The device dictates a ```text``` |
| ```rh.audio.startRecording(filename, audio_type, samplerate, channels)```  | The device starts recording using its microphones. The recording will be stored in ```filename``` (absolute path), having as ```audio_type``` one of [wav, ogg], with a specific ```samplerate``` and from specific ```channels```. The ```channels``` are in the form of [0,0,1..,0,1], where the size of the list is equal to the number of microphones and ```1``` is used to record the specific channel. |
| ```rh.audio.stopRecording()``` | The device stops the recording |
| ```rh.audio.playFile(filename)``` | The device plays the specific ```filename``` (absolute path) |
| ```rh.audio.setVolume(volume)``` | Sets the device's maste output volume. ```volume``` must be between [0,100] |
| ```rh.audio.record(filename, seconds, audio_type, samplerate, channels)``` | The device records to a ```filename```. The other parameters are the same as the ```startRecording``` call, but here the length in ```seconds``` must be specified |
| ```rh.audio.speechDetection(vocabulary, wait, language)``` | Performs vocabulary-based speech detection. The ```vocabulary``` must be a list of words (or sentenses) in a specific ```language```, and the call waits ```wait``` seconds |
| ```rh.motion.enableMotors()``` | Enables the device's motors (may not be needed in specific devices) |
| ```rh.motion.disableMotors()``` | Disables the device's motors |
| ```rh.motion.moveByVelocity(x_vel, y_vel, theta_vel)``` | Moves the device given the linear velocities by X,Y axis and the rotational (```theta_vel```)|
| ```rh.motion.moveTo(x, y, theta)``` | The device moves from its current position to the relative pose [x,y,theta] |
| ```rh.motion.stop()``` | Stops all motors activity |
| ```rh.motion.getVelocities()``` | Returns the current robot velocities in m/sec (x_vel, y_vel, theta_vel) |
| ```rh.humanoid_motion.setJointAngles(joints, angles, speed)``` | Sets a humanoid's joints in specific angles |
| ```rh.humanoid_motion.getJointAngles(joints)``` | Returns the requested joints' angles for a humanoid robot |
| ```rh.humanoid_motion.openHand(hand_name)``` | Opens a hand (name is [left, right]) |
| ```rh.humanoid_motion.closeHand(hand_name)``` | Closes a hand (name is [left, right]) |
| ```rh.humanoid_motion.goToPosture(posture, speed)``` | The humanoid goes to a predefined ```posture``` with the specific ```speed``` |
| ```rh.humanoid_motion.getPosture()``` | Returns the humanoid's posture. If it exists in an arbitrary posture ```Unknown``` is returned |
| ```rh.vision.detectBlob(color_rgb, threshold, min_size, shape, wait)``` | Detects a blob of color ```color_rgb``` denoted as [r,g,b] ranging between [0,255], with a ```threshold``` ranging from [0,255], having ```min_size``` pixels, or a predefined ```shape``` ([Circle, Unknown]). The call waits for events ```wait``` seconds |
| ```rh.vision.detectDarkness(threshold, wait)``` | Detects the existence of darkness, provided a threshold between [0,100]. The call waits for events ```wait``` seconds |
| ```rh.vision.detectMovement(sensitivity, wait)``` | Detects the existence of darkness, provided a sensitivity between [0.0,1.0]. The call waits for events ```wait``` seconds |
| ```rh.vision.capturePhoto(filepath, camera_id, resolution)``` | Captures an image with the specified ```resolution``` from a camera and stores it in the absolute ```filepath```. The ```camera_id``` can be one of [front, back, down, up, front-down, left, ... etc]. Each implementation must resolve this string to the proper device's cameras |
| ```rh.sensors.getBatteryLevels()``` | Returns the batteries names and levels |
| ```rh.getSonarsMeasurements()``` | Returns the sonar's measurements, along with their label |
| ```rh.getTactileMeasurements(wait)``` | Returns the tactile (touch) sensors measurements in a time frame of ```wait``` seconds |

TODO: Specify the return values


Nevertheless, since the actual robots have (or should have) their RAPP robot Python API installed, and there may be differences to each implementation (even extra functionalities), if you desire to execute applications to a single robot, please check its implementation:

[NAO v4, NAOQi 2.1.4 implementation](https://github.com/rapp-project/rapp-robots-api/tree/python_api/python/implementations/nao_v4_naoqi2.1.4)
