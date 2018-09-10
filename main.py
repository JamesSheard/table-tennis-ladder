import sys
from prettytable import PrettyTable
import string


class player:
    def __init__(self, name):
        self.name = name


class ladder:
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

        if loser_pos == len(self.table):
            self.table.append(player(winner_name))
            self.table.append(player(loser_name))

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


def validate_input(name):
    invalid_chars = set(string.punctuation.replace("_", ""))
    if any(char in invalid_chars for char in name):
        print "Name contains invalid characters. Please use only letters, spaces and underscores."
        return True
    else:
        return False


def main():
    ladd = ladder()

    try:
        if sys.argv[1] == "--win" and sys.argv[3] == "--lose":
            winner_name, loser_name = sys.argv[2], sys.argv[4]

            if validate_input(winner_name) or validate_input(loser_name):
                return False

            ladd.add_new_player(winner_name, loser_name)
            ladd.get_ladder()
            ladd.write_state()

        elif sys.argv[1] == "--getladder":
            ladd.get_ladder()

        else:
            print "incorrect parameters. `python main.py --win <name> --lose <name>`"

    except:
        print "Would you like to: \n1. Show the ladder \n2. Add new game data"
        player_entered = raw_input("Please enter your selection:")

        if player_entered == "1":
            ladd.get_ladder()
        elif player_entered == "2":
            winner_name = raw_input("Please enter the winner: ").lower()
            loser_name = raw_input("Please enter the loser: ").lower()

            if validate_input(winner_name) or validate_input(loser_name):
                return False

            ladd.add_new_player(winner_name, loser_name)
            ladd.get_ladder()
            ladd.write_state()


if __name__ == "__main__":
    main()