import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.guest1 = Guest("John", "Chop Suey", 35)
        self.room1 = Room(1, 10, 5)
        self.song1 = Song("Chop Suey")
        self.song2 = Song("The Unforgiven")
    
    def test_guest_added(self):
        self.room1.guest_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
        self.room1.add_guest(self.guest1)
        self.assertEqual(["a", "b", "c", "d", "e", "f", "g", "h", "i", "John"], self.room1.guest_list)

    def test_guest_removed(self):
        self.room1.add_guest(self.guest1)
        self.room1.remove_guest(self.guest1)
        self.assertEqual([], self.room1.guest_list)

    def test_song_added(self):
        self.room1.add_song(self.song1)
        self.assertEqual(["Chop Suey"], self.room1.song_list)

    def test_entry_fee(self):
        self.room1.take_entry_fee(self.guest1)
        self.assertEqual(5, self.room1.till)
        self.assertEqual(30, self.guest1.wallet)