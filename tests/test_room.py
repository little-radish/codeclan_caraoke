######################################################
###                                                ###
##  REMEMBER: start test function names with test   ##
###                                                ###
######################################################


import unittest

from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):


    def setUp(self):
        self.room = Room("Big Room", 10)
        
    def test_room_set_up(self):
        self.assertEqual("Big Room", self.room.name)
        self.assertEqual(10, self.room.max_capacity)      

    def test_check_guest_into_room(self):
        guest_large_wallet = Guest("Edgeworth", 500)
        guest_small_wallet = Guest("Gumshoe", 9)

        self.room.check_guest_into_room(guest_large_wallet)
        self.assertEqual(490, self.room.occupants[0].wallet)
        
        self.room.check_guest_into_room(guest_small_wallet)
        self.assertEqual("I'm sorry, entry is £10.", self.room.check_guest_into_room(guest_small_wallet))

        self.room.occupants.clear()
        self.room.max_capacity = 0

        self.room.check_guest_into_room(guest_large_wallet)
        self.assertEqual("I'm sorry, that room can host 0 guests and there are 0 people in there.", self.room.check_guest_into_room(guest_large_wallet))





    def test_add_song_to_playlist(self):
        song = Song("Ray", "Passcode", "Metal")
        self.room.add_song_to_playlist(song)
        self.assertEqual("Ray", self.room.playlist[0].name)
