#!/usr/bin/env python

import time

from rapp_robot_api_sensors import Sensors

from naoqi import ALProxy

# Handles the NAO sensors input
class DeviceSensors(Sensors):

    # Initialization of NAO procies
    def __init__(self, parameters):

        self.nao_ip = parameters["nao_ip"]
        self.nao_port = int(parameters["nao_port"])

        # Intializing NAOQi proxies
        self.battery = ALProxy("ALBattery", self.nao_ip, self.nao_port)
        self.memory = ALProxy("ALMemory", self.nao_ip, self.nao_port)
        self.sonars = ALProxy("ALSonar", self.nao_ip, self.nao_port)
        self.leds = ALProxy("ALLeds", self.nao_ip, self.nao_port)
        self.sonars.subscribe("rapp_sonars_subscriber")

    # Assistive function to return errors
    def ret_exc(self, text):
        print text
        return {'error': text}

    # Returns the battery levels in percentage form
    def getBatteryLevels(self): 
        try:
            level = self.battery.getBatteryCharge()
            return {'levels': [level], 'error': None}
        except Exception as e:
            return eelf.ret_exc("sensors.getBatteryCharge: Unrecognized exception: " + \
                e.message)
 
    # Returns the two sonars measurements in meters. The result is a python
    # dictionary containing 'front_left' and 'front_right'
    def getSonarsMeasurements(self):
        try:
            left = self.memory.getData("Device/SubDeviceList/US/Left/Sensor/Value")
            right = self.memory.getData("Device/SubDeviceList/US/Right/Sensor/Value")
        except Exception as e:
            return self.ret_exc("sensors.getSonarsMeasurements: Unrecognized exception: " + \
                e.message)

        data = {}
        data['front_left'] = left
        data['front_right'] = right
        return {'sonars': data, 'error': None}

    # Returns the NAO tactiles and bumpers readings. Since this is an event-based
    # call, the user must provide a delay of 'wait' seconds
    # The result is a python dictionary including the following keys:
    # 'head_front', 'head_rear', 'head_middle', 'left_hand_left', 'left_hand_right'
    # 'left_hand_back', 'right_hand_back', 'right_hand_right', 'right_hand_left'
    # 'left_foot', 'right_foot'
    # The 'get_history' input variable is by default False. When False the 
    # result is just a dictionary containing the aforementioned values. When
    # it is True the returning value is a list of dictionaries containing
    # a snapshot of measurements every 0.1 seconds.
    def getTactileMeasurements(self, wait, get_history = False):

        if type(wait) not in [int, float]:
            return self.ret_exc('sensors.getTactileMeasurements: Wait not a number')

        if type(get_history) is not bool:
            return self.ret_exc('sensors.getTactileMeasurements: get_history not bool')

        data = {}
        data['head_front'] = 0
        data['head_rear'] = 0
        data['head_middle'] = 0

        data['left_hand_back'] = 0
        data['left_hand_left'] = 0
        data['left_hand_right'] = 0

        data['right_hand_back'] = 0
        data['right_hand_left'] = 0
        data['right_hand_right'] = 0
        
        data['left_foot'] = 0
        data['right_foot'] = 0

        ret = []

        if wait < 0.0:
            return self.ret_exc('sensors.getTactileMeasurements: Waiting value is \
                negative')

        iterations = wait / 0.1
        while iterations > 0:
            time.sleep(0.1)
            iterations -= 1

            try:
                hef = self.memory.getData(\
                    "Device/SubDeviceList/Head/Touch/Front/Sensor/Value")
                her = self.memory.getData(\
                    "Device/SubDeviceList/Head/Touch/Rear/Sensor/Value")
                hem = self.memory.getData(\
                    "Device/SubDeviceList/Head/Touch/Middle/Sensor/Value")

                lhb = self.memory.getData(\
                    "Device/SubDeviceList/LHand/Touch/Back/Sensor/Value")
                lhl = self.memory.getData(\
                    "Device/SubDeviceList/LHand/Touch/Left/Sensor/Value")
                lhr = self.memory.getData(\
                    "Device/SubDeviceList/LHand/Touch/Right/Sensor/Value")

                rhb = self.memory.getData(\
                    "Device/SubDeviceList/RHand/Touch/Back/Sensor/Value")
                rhl = self.memory.getData(\
                    "Device/SubDeviceList/RHand/Touch/Left/Sensor/Value")
                rhr = self.memory.getData(\
                    "Device/SubDeviceList/RHand/Touch/Right/Sensor/Value")

                fl = self.memory.getData(\
                    "Device/SubDeviceList/LFoot/Bumper/Left/Sensor/Value")
                fr = self.memory.getData(\
                    "Device/SubDeviceList/RFoot/Bumper/Right/Sensor/Value")
            except Exception as e:
                return self.ret_exc("sensors.getTactileMeasurements: Unrecognized \
                    exception: " + e.message)

            if get_history:
                data['head_front'] = int(hef)
                data['head_rear'] = int(her)
                data['head_middle'] = int(hem)

                data['left_hand_right'] = int(lhr)
                data['left_hand_left'] = int(lhl)
                data['left_hand_back'] = int(lhb)

                data['right_hand_right'] = int(rhr)
                data['right_hand_left'] = int(rhl)
                data['right_hand_back'] = int(rhb)

                data['left_foot'] = int(fl)
                data['right_foot'] = int(fr)

                ret.append(data.copy())
            else:
                data['head_front'] = data['head_front'] or hef
                data['head_rear'] = data['head_rear'] or her
                data['head_middle'] = data['head_middle'] or hem

                data['left_hand_back'] = data['left_hand_back'] or lhb
                data['left_hand_right'] = data['left_hand_right'] or lhr
                data['left_hand_left'] = data['left_hand_left'] or lhl

                data['right_hand_back'] = data['right_hand_back'] or rhb
                data['right_hand_right'] = data['right_hand_right'] or rhr
                data['right_hand_left'] = data['right_hand_left'] or rhl

                data['left_foot'] = data['left_foot'] or fl
                data['right_foot'] = data['right_foot'] or fr

        if get_history:
            data = ret 
        return {'tactiles': data, 'error': None}

    def rastaLedsOn(self, duration=10):
        """
        Launch a green/yellow/red rasta animation on all body.

        @type duration: Float
        @param duration: Approximate duration of the animation in seconds.

        @returns Task id to control/stop the rasta leds task.
        """
        try:
            taskId = self.leds.post.rasta(duration)
        except Exception as e:
            self.ret_exc("sensors.rastaLedsOn: {0}".format(e.message))
        else:
            return taskId

    def rastaLedsOff(self, taskId):
        """
        Command the ALLeds proxy to stop the rasta leds task. Previously
        obtained taskId, from calling rastaLedsOn must be provided as
        argument

        @param taskId: The rasta leds on task id obtained from calling
            rastaLedsOn()
        """
        try:
            self.leds.stop(taskId)
        except Exception as e:
            self.ret_exc("sensors.rastaLedsOff: {0}".format(e.message))
        else:
            return 1

    def randomEyesOn(self, duration=10):
        try:
            self.leds.post.randomEyes(duration)
        except Exception as e:
            self.ret_exc("sensors.randomEyesOn: {0}".format(e.message))
        else:
            return 1

    def randomEyesOff(self, taskId):
        try:
            self.leds.stop(taskId)
        except Exception as e:
            self.ret_exc("sensors.randomEyesOff: {0}".format(e.message))
        else:
            return 1
