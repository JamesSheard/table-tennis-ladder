import sqlite3

from prettytable import PrettyTable


class Database:
    #TODO:  Mike is very angry. Our SQL is injectable :D
    def __init__(self):
        self.conn = sqlite3.connect('database/table_tennis.db')

    def create_league_table(self, league_name):
        self.conn.execute("CREATE TABLE {league} (rank INTEGER, name TEXT)"
                          .format(league=league_name))

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
        print "Into winning player\n\n\n"
        query = "UPDATE {leaderboard} SET rank = rank + 1 WHERE rank > {loser_pos};" \
                "INSERT INTO {leaderboard} (rank, name) VALUES  ({loser_pos},  '{winner_name}');"\
                .format(leaderboard=leaderboard, loser_pos=loser_pos, winner_name=winner_name)
        print self.conn.execute(query)

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
                "(((SELECT count(rank) FROM {leaderboard}) + 1), {player_name});"\
                .format(leaderboard=leaderboard, player_name=player_name)
        self.conn.execute(query)

    def insert_two_new_players(self, leaderboard, winner_name, loser_name):
        self.append_player(leaderboard, winner_name)
        self.append_player(leaderboard, loser_name)

    def two_competing_player(self, leaderboard, winner_name, winner_pos, loser_pos):
        query = "UPDATE {leaderboard} SET rank = rank + 1 WHERE rank > {loser_pos};" \
                "INSERT INTO {leaderboard} (rank, name) VALUES ({loser_pos}, '{winner_name}');" \
                "DELETE FROM {leaderboard} WHERE rank = {winner_pos};"\
                .format(leaderboard=leaderboard,
                        winner_name=winner_name,
                        loser_pos=loser_pos,
                        winner_pos=winner_pos + 1)  # TODO: Check this logic.
        self.conn.execute(query)


if __name__ == "__main__":
    db = Database()
    db.create_league_table("TC")
    db.insert_row_league("TC", 1, "James")
    db.insert_row_league("TC", 2, "Mike")
    db.insert_row_league("TC", 3, "Bobby")
    db.insert_row_league("TC", 4, "Bill")
    db.insert_row_league("TC", 5, "Dan")

    db.commit()
    # cache = db.view_league_table("TC")

    table = db.get_leaderboard("TC")

    formatted_table = PrettyTable(["Name", "Rank"])
    for player in table:
        formatted_table.add_row([player, table.index(player) + 1])
    formatted_table.title = "taste card"
    print formatted_table

    db.close()