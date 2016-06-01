#!/usr/bin/env python

import os

from naoqi import ALProxy

# Handles the vision modules of NAO
class Utilities:

    # Initialization of NAO proxies
    def __init__(self, parameters):

        self.nao_ip = parameters["nao_ip"]
        self.nao_port = int(parameters["nao_port"])

    # Assistive function to return errors
    def ret_exc(self, text):
        print text
        return {'error': text}

    # This function helps to move files from the NAO robot to a PC, in case
    # the application is remotely executed in the PC
    def moveFileToPC(self, nao_file, pc_file):
        try:
            command = 'sshpass -p "nao" scp nao@' + self.nao_ip + ":" + \
                    nao_file + " " + pc_file
            os.system(command)
        except Exception as e:
            return self.ret_exc('utilities.moveFile: Unknown exception: ' + \
                    e.message)
        return {'error': None}

    # This function helps to move files from the PC to a NAO robot, in case
    # the application is remotely executed in the PC
    def moveFileToNAO(self, nao_file, pc_file):
        try:
            command = 'sshpass -p "nao" scp ' + pc_file + \
                    ' nao@' + self.nao_ip + ":" + nao_file
            os.system(command)
        except Exception as e:
            return self.ret_exc('utilities.moveFile: Unknown exception: ' + \
                    e.message)
        return {'error': None}
