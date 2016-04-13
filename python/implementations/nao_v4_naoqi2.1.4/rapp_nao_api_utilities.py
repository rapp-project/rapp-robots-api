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
        return [None, text]

    # This function helps to move files from the NAO robot to a PC, in case
    # the application is remotely executed in the PC
    def moveFile(self, nao_file, pc_file):
        try:
            command = "scp -p 'nao' nao@" + self.nao_ip + ":" + nao_file + " " + pc_file
            print command
            os.system(command)
        except Exception as e:
            return self.ret_exc('utilities.moveFile: Unknown exception: ' + \
                    e.message)
