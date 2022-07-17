import unittest

from src.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("Ray", "PassCode", "Metal")
        
    def test_room_set_up(self):
        self.assertEqual("Ray", self.song.name)    

    # the code above sets up a Song and tests it was created correctly
    