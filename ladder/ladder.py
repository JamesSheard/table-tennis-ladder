from prettytable import PrettyTable


class Ladder:
    file_name = ""
    table = []

    def __init__(self, ladder_name, db):
        self.ladder_name = ladder_name
        self.db = db
        self.table = self.db.get_leaderboard(ladder_name)

    def list_ladders(self):
        leaderboards = self.db.get_leaderboards()
        formatted_table = PrettyTable(["League Name"])

        for leagues in leaderboards:
            formatted_table.add_row([leagues])

        print formatted_table.get_string()

    def print_ladder(self):
        formatted_table = PrettyTable(["Name", "Rank"])
        for player in self.table:
            formatted_table.add_row([player, self.table.index(player) + 1])
        formatted_table.title = self.ladder_name

        print formatted_table.get_string()

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

    def get_pos(self, name):
        try:
            if name in self.table:
                return self.table.index(name)
            else:
                return False
        except:
            return False
