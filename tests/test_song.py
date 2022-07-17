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
        self.song2 = Song("Can't Do Better", "Kim Petras", "Pop")
        self.song3 = Song("Welcome to the Black Parade", "My Chemical Romance", "Emo")
        self.song4 = Song("Feel Special", "TWICE", "K-Pop")
        

    def test_room_set_up(self):
        self.assertEqual("Ray", self.song1.name)
        self.assertEqual("PassCode", self.song1.artist)
        self.assertEqual("Metal", self.song1.genre)
import unittest

from src.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("Ray", "PassCode", "Metal")
        
    def test_room_set_up(self):
        self.assertEqual("Ray", self.song.name)    

    # the code above sets up a Song and tests it was created correctly
    
    