######################################################
###                                                ###
##  REMEMBER: start test function names with test   ##
###                                                ###
######################################################

import unittest

from src.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest1 = Guest("Edgeworth", 500)
        self.guest2 = Guest("Phoenix", 20)
        self.guest3 = Guest("Apollo", 10)
        self.guest4 = Guest("Gumshoe", 0)

    def test_guest_set_up(self):
        self.assertEqual("Edgeworth", self.guest1.name)
        self.assertEqual(500, self.guest1.wallet) 