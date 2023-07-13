class Room:
    def __init__(self, room_number, size, price):
        self.room_number = room_number
        self.size = size
        self.price = price
        self.till = 0
        self.song_list = []
        self.guest_list = []

    def add_guest(self, guest):
        if len(self.guest_list) >= self.size:
            return "Room is full, try another room!"
        else:
            self.guest_list.append(guest.name)

    def remove_guest(self, guest):
        self.guest_list.remove(guest.name)

    def add_song(self, song):
        self.song_list.append(song.name)

    def increase_till(self):
        self.till += self.price

    def take_entry_fee(self, guest):
        self.increase_till()
        guest.pay_entry_fee(self.price)