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

    def add_new_player(self, winner_name, loser_name, win):

        loser_pos = self.table.index(player(loser_name, ))

        if name in self.table:
            return "player already in table"

        elif win:
            player(winner_name, loser_pos)
            self.table.insert(loser_pos, winner_name)
        else:
            self.table.append(player(loser_name, len(self.table)+1))

    #def modify_existing_player(self, player):


    def player_in_ladder(self, name):
        if name in self.table:
            return True
        return False


def main():
    ladd = ladder() #main.py --win john --lose barry
    if sys.argv[1] == "--win":
        winner_name = sys.argv[2]
        loser_name = sys.argv[4]

        if ladd.player_in_ladder(winner_name) != True:
            ladd.add_new_player(winner_name, loser_name, True)
        if not ladd.player_in_ladder(loser_name):
            ladd.add_new_player(loser_name, False)

        if ladd.player_in_ladder(name):
            ladd.modify_existing_player(player)
        elif not ladd.player_in_ladder(name):
            ladd.add_new_player(name)

    elif sys.argv[1] == "--getladder":
        print ladd.get_ladder()


if __name__ == "__main__":
    main()