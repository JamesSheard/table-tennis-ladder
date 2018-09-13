import sqlite3


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
        query = "UPDATE {leaderboard} SET rank = rank + 1 WHERE rank > {loser_pos};" \
                "INSERT INTO {leaderboard} (rank, name) VALUES  ({loser_pos},  '{winner_name}');".format(leaderboard=leaderboard, loser_pos=loser_pos, winner_name=winner_name)

    def get_leaderboard(self, leaderboard):
        query = "SELECT * FROM {leaderboard} ORDER BY Rank ASC;".format(leaderboard=leaderboard)

    


if __name__ == "__main__":

    db = Database()
    db.create_league_table("TC")
    db.insert_row_league("TC", 1, "James")
    db.insert_row_league("TC", 2, "Mike")
    db.insert_row_league("TC", 3, "Bobby")
    db.insert_row_league("TC", 4, "Bill")
    db.insert_row_league("TC", 5, "Dan")

    db.commit()
    print db.view_league_table("TC")
    db.close()