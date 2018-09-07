import os
import sys


class player:
    def __init__(self, name):
        self.name = name


class ladder:
    table = []

    def __init__(self):
        self.read_state()

    def get_ladder(self):
        for player in self.table:
            print player.name + " " + str(self.table.index(player) + 1)

    def add_new_player(self, winner_name, loser_name):
        loser_pos = len(self.table)
        for play in self.table:
            if play.name == loser_name:
                loser_pos = self.table.index(play)

        if loser_pos == len(self.table):
            self.table.append(player(winner_name))
            self.table.append(player(loser_name))
        else:
            self.table.insert(loser_pos, player(winner_name))

    def player_in_ladder(self, name):
        if name in self.table:
            return True
        return False

    def read_state(self):
        f = open("ladder/ladder_state.txt")
        contents = f.read().split("\n")
        for line in contents:
            current_player = line.split()
            if current_player:
                self.table.append(player(current_player[0]))
        f.close()

    def write_state(self):
        f = open("ladder/ladder_state.txt", "w")
        f.truncate(0)
        for player in self.table:
            f.write(player.name + " " + str(self.table.index(player) + 1) + "\n")

        f.close()
        return


def main():
    ladd = ladder() #main.py --win john --lose barry
    if sys.argv[1] == "--win" and sys.argv[3] == "--lose":
        winner_name, loser_name = sys.argv[2], sys.argv[4]
        ladd.add_new_player(winner_name, loser_name)
        ladd.get_ladder()
        ladd.write_state()

    elif sys.argv[1] == "--getladder":
        ladd.get_ladder()

    else:
        print "incorrect parameters. `python main.py --win <name> --lose <name>`"


if __name__ == "__main__":
    main()