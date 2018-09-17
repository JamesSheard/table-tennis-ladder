from database.db_controller import Database
from player.player import player
from prettytable import PrettyTable
from html.html_generator import HtmlGenerator


class Ladder:
    file_name = ""
    table = []

    def __init__(self, ladder_name):
        self.ladder_name = ladder_name
        self.db = Database(ladder_name)
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

        # Winning player is lower in ladder than losing player
        if winner_pos is not False and loser_pos is not False:
            if loser_pos < winner_pos:
                self.db.two_competing_player(self.ladder_name, winner_name, winner_pos + 1, loser_pos + 1)

        # Losing player is not in the ladder
        elif winner_pos is not False and loser_pos is False:
            self.db.append_player(self.ladder_name, loser_name)

        # Winning player is not in the ladder
        elif loser_pos is not False and winner_pos is False:
            self.db.insert_winning_player(self.ladder_name, loser_pos + 1, winner_name)

        # Neither player is in ladder
        elif winner_pos is False and loser_pos is False:
            self.db.insert_two_new_players(self.ladder_name, winner_name, loser_name)

        self.table = self.db.get_leaderboard(self.ladder_name)
        self.db.close()

        html = HtmlGenerator(self.ladder_name, self.table)
        html.write_html()

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
