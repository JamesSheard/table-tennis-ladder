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
        self.read_state(ladder_name)
        self.db = Database()

    def list_ladders(self):
        leaderboards = self.db.get_leaderboards()
        formatted_table = PrettyTable(["League Name"])

        for leagues in leaderboards:
            formatted_table.add_row([leagues])

        print formatted_table


    def print_ladder(self):
        table = self.db.get_leaderboard(self.ladder_name)
        formatted_table = PrettyTable(["Name", "Rank"])

        for player in table:
            formatted_table.add_row([player, table.index(player) + 1])
        formatted_table.title = self.ladder_name

        print formatted_table

    def add_new_score(self, winner_name, loser_name):
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

        elif loser_pos == len(self.table) and winner_pos != len(self.table):
            self.table.append(player(loser_name))

        else:
            self.table.insert(loser_pos, player(winner_name))
            self.table.pop(winner_pos + 1)

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

