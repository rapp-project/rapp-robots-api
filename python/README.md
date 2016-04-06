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
| ```rh.audio.startRecording(filename, audio_type, samplerate, channels)```  | The device starts recording using its microphones. The recording will be stored in ```filename```, having as ```audio_type``` one of [wav, ogg], with a specific ```samplerate``` and from specific ```channels```. The ```channels``` are in the form of [0,0,1..,0,1], where the size of the list is equal to the number of microphones and ```1``` is used to record the specific channel. |
| ```rh.audio.stopRecording()``` | The device stops the recording |

Nevertheless, since the actual robots have (or should have) their RAPP robot Python API installed, and there may be differences to each implementation (even extra functionalities), if you desire to execute applications to a single robot, please check its implementation:

[NAO v4, NAOQi 2.1.4 implementation](https://github.com/rapp-project/rapp-robots-api/tree/python_api/python/implementations/nao_v4_naoqi2.1.4)
