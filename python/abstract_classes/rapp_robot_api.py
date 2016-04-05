#!/usr/bin/env python

from rapp_robot_api_interaction import Interaction

# The upper class (namespace), containing per-functionality modules
class RappRobot:
    def __init__(self):
        self.interaction = Interaction()
