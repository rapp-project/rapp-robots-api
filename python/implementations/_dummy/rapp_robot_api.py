#!/usr/bin/env python

from rapp_dummy_api_interaction import DummyInteraction

# The upper class (namespace), containing per-functionality modules
class RappRobot:
    def __init__(self):
        self.interaction = DummyInteraction()
