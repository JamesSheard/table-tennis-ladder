from player import player
from prettytable import PrettyTable
import os

class Ladder:
    file_name = ""
    table = []

    def __init__(self, ladder_name):
        self.ladder_name = ladder_name
        self.read_state(ladder_name)

    def list_ladders(self):
        files = os.listdir("ladder/")
        ladder_names = [x[:-4] for x in files]
        ladders_table = PrettyTable(["Ladder Names"])
        for name in ladder_names:
            ladders_table.add_row([name])

        print ladders_table

    def print_ladder(self):
        formatted_table = PrettyTable(["Name", "Rank"])
        for player in self.table:
            formatted_table.add_row([player.name, self.table.index(player) + 1])
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
        self.file_name = "ladder/" + ladder_name + ".txt"
        try:
            f = open(self.file_name)
            contents = f.read().split("\n")
            for line in contents:
                self.table.append(player(line))
            f.close()

        except:
            self.table = []
            print "Could not find populated state file."

    def write_state(self):
        f = open(self.file_name, "w+")
        f.truncate(0)
        for player in self.table:
            if self.table.index(player) == len(self.table) - 1:
                f.write(player.name)
            else:
                f.write(player.name + "\n")

        f.close()

        self.write_to_html()

        return

    def write_to_html(self):
        html = "<head>\n" \
                "</head>\n" \
                "<table style=\"width:25%\" border=10 bordercolor=\"#D3D3D3\">" \
                "\n\t<tr>" \
                "\n\t\t<th>Name</th>" \
                "\n\t\t<th>Rank</th>" \
                "\n\t</tr>\n"

        for p in self.table:
            html = html + "\t<tr>\n"
            html = html + "\t\t<td>" + p.name + "</td>\n"
            html = html + "\t\t<td>" + str(self.table.index(p) + 1) + "</td>\n"
            html = html + "\t</tr>\n"
        html += "</table>\n"


        f = open(self.ladder_name + ".html", "w+")
        f.truncate(0)
        f.write(html)
