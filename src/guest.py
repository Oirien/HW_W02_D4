class Guest:
    def __init__(self, name, favourite_song, wallet):
        self.name = name
        self.favourite_song = favourite_song
        self.wallet = wallet

    def pay_entry_fee(self, fee):
        self.wallet -= fee

    def does_this_room_have_my_song(self, room):
        for song in room.song_list:
            if song == self.favourite_song:
                return "Woo!"