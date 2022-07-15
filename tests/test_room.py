######################################################
###                                                ###
##  REMEMBER: start test function names with test   ##
###                                                ###
######################################################

import unittest

from src.room import Room

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.roombig = Room("Big Room", 10)
        self.roomsmall = Room("Wee Room", 2)
        
    def test_blank(self):
        pass