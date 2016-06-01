This folder contains the NAO-specific rapp-robot-api implementation. For information concerning the entirety of the calls, please visit the [generic README file](https://github.com/rapp-project/rapp-robots-api/tree/master/python), as here specific information about the NAO implementation exist. 

If you want to utilize the API remotely, your PC must be in the same LAN as the NAO and you have to declare NAO's IP in [this file](https://github.com/rapp-project/rapp-robots-api/blob/master/python/implementations/nao_v4_naoqi2.1.4/nao_connectivity). If you want to install the API in the real robot and execute the applications there, you have to move the API in the readl NAO under the ```PATH_TO_API``` folder, change the IP to ```127.0.0.1``` and add the following lines to the ```~/.bash_profile``` file:

```
export PYTHONPATH=$PYTHONPATH:PATH_TO_API/python/abstract_classes
export PYTHONPATH=$PYTHONPATH:PATH_TO_API/python/implementations/nao_v4_naoqi2.1.4
```

## Special considerations concerning the generic API calls

NOTE: Where the "default" value is mentioned, it means that if you do not provide this input parameter at all, this value will be automatically set.

#### Audio calls
- ```audio.speak```: The default ```language``` value is 'English' and the supported languages are ['French', 'Chinese', 'English', 'German', 'Italian', 'Japanese', 'Korean', 'Portuguese', 'Spanish', 'Greek']. Nevertheless, NAO can contain only two installed languages, thus this call may not work if the given language is not installed in the real NAO. Conclusively, for the English language you can invoke is as such: ```audio.speak("Hello")```
- ```audio.startRecording```: The default ```audio_type``` is 'ogg', the default ```samplerate``` is 16000 and the default ```channels``` is [0,0,1,0], i.e. if only the ```filename``` is provided, NAO will start recording an ogg file, 16kHz single-channel from the front microphone.
- ```audio.record```: Has the same default values as the ```startRecording```.
- ```audio.speechDetection```: The default ```language``` value is 'English'

#### Humanoid motion calls
- The ```joints``` parameter can take the following values: ```['HeadYaw', 'LShoulderPitch', 'LHipYawPitch1', 'RHipYawPitch1', 'RShoulderPitch', 'HeadPitch', 'LShoulderRoll', 'LHipRoll', 'RHipRoll', 'RShoulderRoll', 'LElbowYaw', 'LHipPitch', 'RHipPitch', 'RElbowYaw', 'LElbowRoll', 'LKneePitch', 'RKneePitch', 'RElbowRoll', 'LWristYaw2', 'LAnklePitch', 'RAnklePitch', 'RWristYaw2', 'LHand2', 'RAnkleRoll', 'LAnkleRoll', 'RHand2']```
- The ```hand_name``` parameters can take values from ```['Right', 'Left']```
- The ```posture``` parameter can take values from ```["Crouch", "LyingBack", "LyingBelly", "Sit", "SitRelax", "Stand", "StandInit", "StandZero"]```

#### Motion calls
- ```motion.moveByVelocity```: The input parameters values **are not** in m/sec but bounded between [-1,1], where 1 is the maximum speed and -1 the maximum negative speed.
- ```motion.stop```: It is advisable not to use this call when NAO is walking as it abruptly stops its motors, thus making a fall possible. The ```motion.moveByVelocity(0,0,0)``` can be called instead.

#### Sensors calls
- ```sensors.getBatteryLevels```: NAO contains only one battery, thus the result will be a list with lenght equal to one (1).
- ```sensors.getSonarsMeasurements```: A dictionary with two values is returned. The key values are ```front_left``` and ```front_right```.
- ```sensors.getTactileMeasurements```: A dictionary with the following key values is returned: ```'head_front', 'head_rear', 'head_middle', 'left_hand_left', 'left_hand_right', 'left_hand_back', 'right_hand_back', 'right_hand_right', 'right_hand_left', 'left_foot', 'right_foot'```. Each of these contain 0 if not triggered and 1 if triggered.

#### Vision calls
- ```vision.capturePhoto```: The default ```camera_id``` value is 'front' and the default resolution is ```640x480```. The ```filepath``` must be **absolute** in the NAO OS.

## NAO specific calls

### Utilities API calls

Since the NAO applications can be remotely executed and the API calls producing files store these in the NAO, the ```utilities``` calls were implemented to enable file transfer from NAO to the PC and vice versa.

###rh.utilities.moveFileToPC(nao_file, pc_file)

**Description**: Performs an scp call to NAO transferring a file from NAO to the PC.

**Inputs**:
- ```nao_file```: A string containing the absolute path of the file to be transferred
- ```pc_file```: A string containing the target path in the PC

**Example input**: ```rh.utilities.moveFileToPC("/home/nao/img.jpg", "~/temp/test.jpg")```
**Call Output**: ```{'error': None}```
**Expected Output**: The file is transferred from the NAO to the PC

***

###rh.utilities.moveFileToNAO(nao_file, pc_file)

**Description**: Performs an scp call to NAO transferring a file from PC to the NAO.

**Inputs**:
- ```nao_file```: A string containing the absolute target path in NAO
- ```pc_file```: A string containing the path of the file to be transferred in the PC

**Example input**: ```rh.utilities.moveFileToNAO("/home/nao/img.jpg", "~/temp/test.jpg")```
**Call Output**: ```{'error': None}```
**Expected Output**: The file is transferred from the PC to the NAO
