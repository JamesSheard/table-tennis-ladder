

class Tournament:
    def __init__(self, num_players):
        self.num_players = num_players
        self.players = []

    def get_players(self):
        for index, p in self.num_players():
            self.players.append(self.get_entry(index))

    def get_entry(self, index):
        print "Adding player: " + index + "/" + self.num_players + "\n"
        return raw_input("Name:").lower()

    def tournament_mode(self):
        self.get_players()
