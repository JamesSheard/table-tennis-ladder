import string


class Interface:
    args = []

    def __init__(self, args):
        self.args = args

    def unix_args(self):
        if self.args[1] == "--win" and self.args[3] == "--lose":
            return True
        return False

    def is_get_ladder(self):
        if self.args[1] == "--getladder":
            return True
        return False

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
