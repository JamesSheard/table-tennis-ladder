from player import player
from prettytable import PrettyTable


class Ladder:
    table = []

    def __init__(self):
        self.read_state()

    def get_ladder(self):
        formatted_table = PrettyTable(["Name", "Rank"])
        for player in self.table:
            formatted_table.add_row([player.name, self.table.index(player) + 1])
        print formatted_table

    def add_new_player(self, winner_name, loser_name):
        loser_pos, winner_pos = len(self.table), len(self.table)
        winner_name, loser_name = winner_name.capitalize(), loser_name.capitalize()

        for play in self.table:
            if play.name == loser_name:
                loser_pos = self.table.index(play)
            if play.name == winner_name:
                winner_pos = self.table.index(play)

        if loser_pos == len(self.table) and winner_pos == len(self.table):
            self.table.append(player(winner_name))
            self.table.append(player(loser_name))

        elif winner_pos == len(self.table):
            self.table.insert(loser_pos, player(winner_name))

        else:
            self.table.insert(loser_pos, player(winner_name))
            self.table.pop(winner_pos + 1)

    def player_in_ladder(self, name):
        if name in self.table:
            return True
        return False

    def read_state(self):
        try:
            f = open("ladder/ladder_state.txt")
            contents = f.read().split("\n")
            for line in contents:
                self.table.append(player(line))
            f.close()

        except:
            self.table = []
            print "Could not find populated state file."

    def write_state(self):
        f = open("ladder/ladder_state.txt", "w+")
        f.truncate(0)
        for player in self.table:
            if self.table.index(player) == len(self.table) - 1:
                f.write(player.name)
            else:
                f.write(player.name + "\n")

        f.close()
        return
