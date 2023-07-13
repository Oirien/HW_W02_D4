class Bar:
    def __init__(self, name):
        self.name = name
        self.safe = 0
        self.lobby = []
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room.room_number)