class Database:
    def __init__(self, ladder_name, table):
        self.ladder_name = ladder_name
        self.table = table

    def get_leaderboard(self, ladder_name):
        return self.table

    def get_leaderboards(self):
        return ["taste_card", "emis", "global"]

    def two_competing_player(self, ladder_name, winner_name, winner_pos, loser_pos):
        self.table = [
            "Jim",
            "Bill",
            "John",
            "Bob",
            "Kev"]

    def append_player(self, ladder_name, loser_name):
        self.table = [
            "Jim",
            "John",
            "Bob",
            "Bill",
            "Kev",
            "Gazza"]

    def insert_winning_player(self, ladder_name, loser_pos, winner_name):
        self.table = [
            "Jim",
            "John",
            "Bob",
            "Gazza",
            "Bill",
            "Kev"]

    def insert_two_new_players(self, ladder_name, winner_name, loser_name):
        self.table = [
            "Jim",
            "John",
            "Bob",
            "Bill",
            "Kev",
            "Gazza",
            "Carlson"]

    def close(self):
        return True
