from database.db_controller import Database
from player.player import player
from prettytable import PrettyTable
from html.html_generator import HtmlGenerator

import os


class Ladder:
    file_name = ""
    table = []

    def __init__(self, ladder_name):
        self.ladder_name = ladder_name
        self.db = Database()
        self.table = self.db.get_leaderboard(ladder_name)

    def list_ladders(self):
        leaderboards = self.db.get_leaderboards()
        formatted_table = PrettyTable(["League Name"])

        for leagues in leaderboards:
            formatted_table.add_row([leagues])

        print formatted_table

    def print_ladder(self):
        formatted_table = PrettyTable(["Name", "Rank"])
        for player in self.table:
            formatted_table.add_row([player, self.table.index(player) + 1])
        formatted_table.title = self.ladder_name

        print formatted_table

    def add_new_score(self, winner_name, loser_name):
        winner_name, loser_name = winner_name.capitalize(), loser_name.capitalize()
        winner_pos, loser_pos = self.get_pos(winner_name), self.get_pos(loser_name)

        if (winner_pos and loser_pos) and (loser_pos < winner_pos):
            self.db.two_competing_player(self.ladder_name, winner_name, winner_pos + 1, loser_pos + 1)

        elif not winner_pos and not loser_pos:
            self.db.insert_two_new_players(self.ladder_name, winner_name, loser_name)

        elif winner_pos and not loser_pos:
            self.db.append_player(self.ladder_name, loser_name)

        elif loser_pos and not winner_pos:
            self.db.insert_winning_player(self.ladder_name, loser_pos + 1, winner_name)

        self.table = self.db.get_leaderboard(self.ladder_name)
        self.db.close()

    def in_leaderboard(self, name):
        return name in self.table

    def get_pos(self, name):
        try:
            if name in self.table:
                return self.table.index(name)
            else:
                return False
        except:
            return False


    def player_in_ladder(self, name):
        for player in self.table:
            if player.name == name:
                return True
            return False

    def read_state(self, ladder_name):
        self.file_name = "ladder/state/" + ladder_name + ".txt"
        try:
            with open(self.file_name) as f:
                contents = f.read().split("\n")
                for line in contents:
                    self.table.append(player(line))

        except:
            self.table = []
            print "Could not find populated state file."

    def write_state(self):
        html_generator = HtmlGenerator(self.ladder_name, self.table)

        with open(self.file_name, "w+") as f:
            f.truncate(0)
            for player in self.table:
                if self.table.index(player) == len(self.table) - 1:
                    f.write(player.name)
                else:
                    f.write(player.name + "\n")

        html_generator.write_html()

        return

