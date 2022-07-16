class Room:

    def __init__(self, name, max_capacity):
        self.name = name
        self.max_capacity = max_capacity
        self.playlist = []
        self.occupants = []
        self.entry_fee = 10

    def check_guest_into_room(self, guest):
                if len(self.occupants) < self.max_capacity:

                    if guest.wallet >= self.entry_fee:
                        guest.wallet -= self.entry_fee
                        self.occupants.append(guest)

                    else:
                        return f"I'm sorry, entry is £{self.entry_fee}."

                else:
                    return f"I'm sorry, that room can host {self.max_capacity} guests and there are {len(self.occupants)} people in there."

    def add_song_to_playlist(self, song):
        self.playlist.append(song)