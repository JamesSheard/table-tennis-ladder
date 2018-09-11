import string


class Interface:
    args = []

    def __init__(self, args):
        self.args = args

    def unix_args(self):
        if (self.args[1] == "--win" or self.args[1] == "-w") and (self.args[3] == "--lose" or self.args[3] == "-l"):
            return True
        return False

    def is_get_ladder(self):
        if self.args[1] == "--getladder" or self.args[1] == "-gl":
            return True
        return False

    def is_get_help(self):
        if self.args[1] == "--help" or self.args[1] == "-h":
            return True
        return False

    def is_interactive_mode(self):
        if self.args[1] == "--interactive" or self.args[1] == "-i":
            return True
        return False

    def print_help(self):
        f = open("help/help.txt")
        print f.read()
        f.close()

    def validate_input(self, name):
        invalid_chars = set(string.punctuation.replace("_", ""))
        if any(char in invalid_chars for char in name):
            print "Name contains invalid characters. Please use only letters, spaces and underscores."
            return True
        else:
            return False

    def get_selection(self):
        print "Would you like to: \n1. Show the ladder \n2. Add new game data"
        return raw_input("Please enter your selection:")

    def get_names(self):
        winner_name = raw_input("Please enter the winner: ").lower()
        loser_name = raw_input("Please enter the loser: ").lower()

        if self.validate_input(winner_name) or self.validate_input(loser_name):
            return winner_name, loser_name, False

        return winner_name, loser_name, True

    def interactive_mode(self, ladder):
        player_entered = self.get_selection()

        if player_entered == "1":
            ladder.get_ladder()
        elif player_entered == "2":
            winner_name, loser_name, valid = self.get_names()
            if valid != True:
                return False

            ladder.add_new_player(winner_name, loser_name)
            ladder.get_ladder()
            ladder.write_state()
