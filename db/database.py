import sqlite3

class Database:
    #TODO:  Mike is very angry. Our SQL is injectable :D
    def __init__(self):
        self.conn = sqlite3.connect('./table_tennis.db')

    def create_league_table(self, league_name):
        self.conn.execute("CREATE TABLE "+league_name+" (player_id NOT NULL INTEGER, rank NOT NULL INTEGER, name text, FOREIGN KEY(player_id) REFERENCES player_table(id))")

    def create_player_table(self):
        self.conn.execute('''CREATE TABLE player_table
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
         name TEXT)''')

    def insert_row_league(self, league_name, player_name):
        self.conn.execute("INSERT INTO ? VALUES ('SELECT id from player_table WHERE name=?)", (league_name, player_name))

    def commit(self):
        self.conn.commit()

    def select(self, league_name):
        data = []


        for row in self.conn.execute("SELECT * FROM ?", (league_name)):
            data.append(row)
        return data


    def create_player(self, player_name):
        self.conn.execute("INSERT INTO player_table VALUES (NULL, '"+player_name+"')")

    def close(self):
        self.conn.close()

if __name__ == "__main__":

    db = Database()
    db.create_league_table("TC")
    db.insert_row_league("TC", "Mike")
    #db.create_player_table()

    db.commit()
    print db.select("TC")
    db.close()