class Database:
    def __init__(self, ladder_name, table):
        self.ladder_name = ladder_name
        self.table = table

    def get_leaderboard(self, ladder_name):
        return self.table

    def get_leaderboards(self):
        return ["taste_card", "emis", "global"]

    def db.two_competing_player(self.ladder_name, winner_name, winner_pos, loser_pos):
        return