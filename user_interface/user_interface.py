import string
import sys
from ladder.ladder import Ladder
from database.db_controller import Database


class Interface:
    args = []

    def __init__(self, args):
        self.args = args

    def check_all_args(self, long_args, short_args):
        return (long_args in self.args) or (short_args in self.args)

    def check_first_arg(self, long_args, short_args):
        return self.args[1] == long_args or self.args[1] == short_args

    def record_result(self):
        try:
            return (self.args[1] == "--win" or self.args[1] == "-w") and (self.args[3] == "--lose" or self.args[3] == "-l")
        except:
            return False

    def with_leaderboard(self):
        try:
            return self.check_all_args("--leaderboard", "-lb")

        except:
            return False

    def get_leaderboard_pos(self):
        for index in range(0, len(self.args)):
            if self.args[index] == "--leaderboard" or self.args[index] == "-lb":
                return index + 1

    def is_list_ladders(self):
        try:
            return self.check_first_arg("--listladders", "-ll")

        except:
            return False
    
    def is_get_ladder(self):
        try:
            return self.check_first_arg("--getladder", "-gl")
        except:
            return False

    def is_get_help(self):
        try:
            return self.check_first_arg("--help", "-h")
        except:
            return False

    @staticmethod
    def print_help():
        f = open("help/help.txt")
        print f.read()
        f.close()

    @staticmethod
    def validate_input(name):
        invalid_chars = set(string.punctuation.replace("_", ""))

        if len(name) > 20:
            print "Your name is too long."
            return True

        if any(char in invalid_chars for char in name):
            print "Selection contains invalid characters. Please use only letters and underscores."
            return True
        else:
            return False

    def select_ladder(self):
        if self.with_leaderboard():
            lb_pos = self.get_leaderboard_pos()
            if self.validate_input(self.args[lb_pos]):
                sys.exit()
            return Ladder(self.args[lb_pos], Database(self.args[lb_pos]))
        else:
            return Ladder("global", Database("global"))
