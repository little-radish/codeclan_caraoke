######################################################
###                                                ###
##  REMEMBER: start test function names with test   ##
###                                                ###
######################################################

import unittest

from src.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song1 = Song("Ray", "PassCode", "Metal")

    def test_room_set_up(self):
        self.assertEqual("Ray", self.song1.name)
        self.assertEqual("PassCode", self.song1.artist)
        self.assertEqual("Metal", self.song1.genre)