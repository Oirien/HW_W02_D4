import unittest

from src.room import Room
from src.guest import Guest
from src.bar import Bar
from src.song import Song

class TestBar(unittest.TestCase):

    def setUp(self):
        self.bar1 = Bar("CC Karaoke")
        self.guest1 = Guest("John", "Chop Suey", 35)
        self.guest2 = Guest("Jim", "The Unforgiven", 35)
        self.guest3 = Guest("Jerry", "Bat Country", 35)
        self.guest4 = Guest("Joe", "My Heart will go on", 35)
        self.room1 = Room(1, 10, 5)
        self.room2 = Room(2, 5, 4)
        self.room3 = Room(3, 4, 3)
        self.room4 = Room(4, 4, 3)
        self.song1 = Song("Chop Suey")
        self.song2 = Song("The Unforgiven")

    def test_add_room_to_bar(self):
        self.bar1.add_room(self.room1)
        self.bar1.add_room(self.room2)
        self.bar1.add_room(self.room3)
        self.assertEqual([1, 2, 3], self.bar1.rooms)
