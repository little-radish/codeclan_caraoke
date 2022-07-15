######################################################
###                                                ###
##  REMEMBER: start test function names with test   ##
###                                                ###
######################################################

import unittest

from src.room import Room

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room_big = Room("Big Room", 10)
        self.room_small = Room("Wee Room", 2)
        
    def test_room_set_up(self):
        self.assertEqual("Big Room", self.room_big.name)
        self.assertEqual(10, self.room_big.max_capacity)        

