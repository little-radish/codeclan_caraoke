class Guest:

    def __init__(self, name, wallet, favourite_song):
        self.name = name
        self.wallet = wallet
        self.favourite_song = favourite_song


    def guest_reaction(self, room):

        for song in room.playlist:

                if song.name == self.favourite_song.name:
                    return "Woohoo"
                
        if self.favourite_song.name == "Stairway To Heaven":
            return "No Stairway? Denied??"

        return "thanks, what time do you close? soon, right?"