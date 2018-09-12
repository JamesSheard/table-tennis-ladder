import sys
from user_interface import Interface
from ladder import Ladder


def main():
    ladder = None
    user_interface = Interface(sys.argv)

    try:
        if user_interface.unix_args():
            if user_interface.with_leaderboard():
                ladder = Ladder(sys.argv[6])
            else:
                ladder = Ladder("ladder_state")
                print "No ladder selected. Defaulting to global leaderboard..."

            winner_name, loser_name = sys.argv[2], sys.argv[4]
            if winner_name == loser_name:
                print "Error: You have entered the same name twice."
                return False
            if user_interface.validate_input(winner_name) or user_interface.validate_input(loser_name):
                return False

            ladder.add_new_score(winner_name, loser_name)
            ladder.print_ladder()
            ladder.write_state()

        elif user_interface.is_get_ladder():
            ladder.print_ladder()

        elif user_interface.is_get_help():
            user_interface.print_help()

        elif user_interface.is_interactive_mode():
            user_interface.interactive_mode(ladder)

        else:
            print "Incorrect parameters. Use `pythom main.py --help` to view commands"

    except:
        user_interface.print_help()

def exit_code(code):
    if code < 0 or code > 3:
        print "invalid exit code"
    print ""


if __name__ == "__main__":
    main()