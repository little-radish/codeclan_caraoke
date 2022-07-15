######################################################
###                                                ###
##  REMEMBER: start test function names with test   ##
###                                                ###
######################################################

import unittest

from src.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("Ray", "PassCode", "Metal")

    def test_blank(self):
        pass