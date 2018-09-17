import sqlite3


class Database:
    #TODO:  Mike is very angry. Our SQL is injectable :D
    def __init__(self, ladder_name):
        self.conn = sqlite3.connect('database/table_tennis.db')

        if ladder_name not in self.get_leaderboards():
            self.create_league_table(ladder_name)

    def create_league_table(self, league_name):
        self.conn.execute("CREATE TABLE {league} (rank INTEGER, name TEXT)".format(league=league_name))
        self.commit()

    def insert_row_league(self, league_name, rank_num, player_name):
        self.conn.execute("INSERT INTO {league} VALUES "
                          "({rank}, '{player}')".format(league=league_name, player=player_name, rank=rank_num))

    def commit(self):
        self.conn.commit()

    def view_league_table(self, league_name):
        data = []

        for row in self.conn.execute("SELECT * FROM {league}".format(league=league_name)):
            data.append(row)

        return data

    def close(self):
        self.conn.close()

    def insert_winning_player(self, leaderboard, loser_pos, winner_name):
        query_one = "UPDATE {leaderboard} SET rank = rank + 1 WHERE rank >= {loser_pos};".format(
            leaderboard=leaderboard, loser_pos=loser_pos)
        query_two = "INSERT INTO {leaderboard} (rank, name) VALUES ({loser_pos},  '{winner_name}');".format(
            leaderboard=leaderboard, loser_pos=loser_pos, winner_name=winner_name)

        self.conn.execute(query_one)
        self.conn.execute(query_two)
        self.commit()

    def get_leaderboard(self, leaderboard):
        query = "SELECT * FROM {leaderboard} ORDER BY Rank ASC;"\
                .format(leaderboard=leaderboard)
        response = self.conn.execute(query)
        leaderboard = []

        for row in response:
            leaderboard.append(row[1])

        return leaderboard

    def get_leaderboards(self):
        query = "SELECT name FROM sqlite_master WHERE type='table';"
        response = self.conn.execute(query)
        leaderboards = []

        for row in response:
            leaderboards.append(row[0])

        return leaderboards

    def append_player(self, leaderboard, player_name):
        query = "INSERT INTO {leaderboard}(rank, name) VALUES " \
                "(((SELECT count(rank) FROM {leaderboard}) + 1), '{player_name}');".format(
                    leaderboard=leaderboard, player_name=player_name)

        self.conn.execute(query)
        self.commit()

    def insert_two_new_players(self, leaderboard, winner_name, loser_name):
        self.append_player(leaderboard, winner_name)
        self.append_player(leaderboard, loser_name)

    def two_competing_player(self, leaderboard, winner_name, winner_pos, loser_pos):
        query_one = "UPDATE {leaderboard} SET rank = rank + 1 WHERE rank >= {loser_pos};".format(
            leaderboard=leaderboard, loser_pos=loser_pos)
        query_two = "INSERT INTO {leaderboard} (rank, name) VALUES ({loser_pos}, '{winner_name}');".format(
            leaderboard=leaderboard, loser_pos=loser_pos, winner_name=winner_name)
        query_three = "DELETE FROM {leaderboard} WHERE rank = {winner_pos} + 1;".format(
            leaderboard=leaderboard, winner_pos=winner_pos)

        self.conn.execute(query_one)
        self.conn.execute(query_two)
        self.conn.execute(query_three)

        self.commit()
