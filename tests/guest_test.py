import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest1 = Guest("John", "Chop Suey", 35)
        self.room1 = Room(1, 10, 5)
        self.song1 = Song("Chop Suey")
        self.song2 = Song("The Unforgiven")

    def test_if_guest_favourite_song_is_in_room(self):
        self.room1.add_song(self.song1)
        self.assertEqual("Woo!", self.guest1.does_this_room_have_my_song(self.room1))