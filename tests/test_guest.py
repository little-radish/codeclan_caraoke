import unittest

from src.guest import Guest
from src.song import Song
from src.room import Room

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Edgeworth", 500, Song("Welcome to the Black Parade", "My Chemical Romance", "Emo"))

    def test_guest_set_up(self):
        self.assertEqual("Edgeworth", self.guest.name)

    def test_guest_reaction(self):

        room = Room("The Big Room", 10)
        test_playlist = [Song("Ray", "PassCode", "Metal"), Song("Can't Do Better", "Kim Petras", "Pop"), Song("Welcome to the Black Parade", "My Chemical Romance", "Emo")]
        for song in test_playlist:
            room.add_song_to_playlist(song)
        # setting up local test data, creating a room and adding songs to its playlist


        self.guest.guest_reaction(room)
        self.assertEqual("Woohoo", self.guest.guest_reaction(room))
        # testing against first guest whose favourite song is in the playlist

        guest2 = Guest("Gumshoe", "9", Song("Feel Special", "TWICE", "K-Pop"))
        # creating a second guest whose favourite song is NOT in the playlist

        guest2.guest_reaction(room)
        self.assertEqual("thanks, what time do you close? soon, right?", guest2.guest_reaction(room))