#!/usr/bin/env python

import time

from rapp_robot_api_sensors import Sensors

from naoqi import ALProxy

class DeviceSensors(Sensors):

    def __init__(self, parameters):

        self.nao_ip = parameters["nao_ip"]
        self.nao_port = int(parameters["nao_port"])

        # Intializing NAOQi proxies
        self.battery = ALProxy("ALBattery", self.nao_ip, self.nao_port)
        self.memory = ALProxy("ALMemory", self.nao_ip, self.nao_port)
        self.sonars = ALProxy("ALSonar", self.nao_ip, self.nao_port)
        self.sonars.subscribe("rapp_sonars_subscriber")

    def getBatteryLevels(self): 
        level = self.battery.getBatteryCharge()
        return [[level], None]

    def getSonarsMeasurements(self):
        left = self.memory.getData("Device/SubDeviceList/US/Left/Sensor/Value")
        right = self.memory.getData("Device/SubDeviceList/US/Right/Sensor/Value")
        data = {}
        data['front_left'] = left
        data['front_right'] = right
        return [data, None]

    def getTactileMeasurements(self, wait, get_history = False):
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
        iterations = wait / 0.1
        while iterations > 0:
            time.sleep(0.1)
            iterations -= 1
            hef = self.memory.getData("Device/SubDeviceList/Head/Touch/Front/Sensor/Value")
            her = self.memory.getData("Device/SubDeviceList/Head/Touch/Rear/Sensor/Value")
            hem = self.memory.getData("Device/SubDeviceList/Head/Touch/Middle/Sensor/Value")

            lhb = self.memory.getData("Device/SubDeviceList/LHand/Touch/Back/Sensor/Value")
            lhl = self.memory.getData("Device/SubDeviceList/LHand/Touch/Left/Sensor/Value")
            lhr = self.memory.getData("Device/SubDeviceList/LHand/Touch/Right/Sensor/Value")

            rhb = self.memory.getData("Device/SubDeviceList/RHand/Touch/Back/Sensor/Value")
            rhl = self.memory.getData("Device/SubDeviceList/RHand/Touch/Left/Sensor/Value")
            rhr = self.memory.getData("Device/SubDeviceList/RHand/Touch/Right/Sensor/Value")

            fl = self.memory.getData("Device/SubDeviceList/LFoot/Bumper/Left/Sensor/Value")
            fr = self.memory.getData("Device/SubDeviceList/RFoot/Bumper/Right/Sensor/Value")

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
        return [data, None]

