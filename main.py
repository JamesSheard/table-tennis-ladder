import os
import sys


class player:
    def __init__(self, name, position):
        self.name = name
        self.position = position


class ladder:
    table = [player("james", 1), player("mike", 2)]

    def __init__(self):
        self.table = []


    def get_ladder(self):
        return self.table

    def add_new_player(self, name, win):
        if name in self.table:
            return "player already in table"

        elif win:
            self.table.insert(player(name, ))
        else:
            self.table.append(player(name, len(self.table)+1))

    def modify_existing_player(self, player):


    def player_in_ladder(self, name):
        if name in self.table:
            return True
        return False


def main():
    ladd = ladder() #main.py --win john --lose barry
    if sys.argv[1] == "--win":
        winner_name = sys.argv[2]
        loser_name = sys.argv[4]

        if not ladder.player_in_ladder(winner_name):
            ladder.add_new_player(winner_name, True)
        if not ladder.player_in_ladder(loser_name):
            ladder.add_new_player(loser_name, False)

        if ladder.player_in_ladder(name):
            ladder.modify_existing_player(player)
        elif not ladder.player_in_ladder(name):
            ladder.add_new_player(name)

    elif sys.argv[1] == "--getladder":
        print ladd.get_ladder()


if __name__ == "__main__":
    main()