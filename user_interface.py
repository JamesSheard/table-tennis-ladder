import string


class Interface:
    args = []

    def __init__(self, args):
        self.args = args

    def unix_args(self):
        try:
            if (self.args[1] == "--win" or self.args[1] == "-w") and (self.args[3] == "--lose" or self.args[3] == "-l"):
                return True
        except:
            return False

    def with_leaderboard(self):
        try:
            if ("--leaderboard" in self.args) or ("-lb" in self.args):
                return True
            else:
                return False
        except:
            return False

    def get_leaderboard_pos(self):
        for index in range(0, len(self.args)):
            if self.args[index] == "--leaderboard" or self.args[index] == "-lb":
                return index + 1

    def is_list_ladders(self):
        try:
            if self.args[1] == "--listladders" or self.args[1] == "-ll":
                return True
        except:
            return False
    
    def is_get_ladder(self):
        try:
            if self.args[1] == "--getladder" or self.args[1] == "-gl":
                return True
        except:
            return False

    def is_get_help(self):
        try:
            if self.args[1] == "--help" or self.args[1] == "-h":
                return True
        except:
            return False

    def print_help(self):
        f = open("help/help.txt")
        print f.read()
        f.close()

    def validate_input(self, name):
        invalid_chars = set(string.punctuation.replace("_", ""))

        if len(name) > 20:
            print "Your name is too long."
            return True

        if any(char in invalid_chars for char in name):
            print "Name contains invalid characters. Please use only letters, spaces and underscores."
            return True
        else:
            return False
