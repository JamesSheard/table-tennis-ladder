import sys
from user_interface import Interface
from ladder import Ladder


def main():
    ladder = None
    user_interface = Interface(sys.argv)

    if user_interface.with_leaderboard():
        lb_pos = user_interface.get_leaderboard_pos()
        ladder = Ladder(sys.argv[lb_pos])
    else:
        ladder = Ladder("ladder_state")

    try:
        if user_interface.is_get_ladder():
            ladder.print_ladder()
            exit_code(0)

        elif user_interface.is_get_help():
            user_interface.print_help()
            exit_code(0)

        elif user_interface.is_list_ladders():
            ladder.list_ladders()
            exit_code(0)

        elif user_interface.unix_args():
            winner_name, loser_name = sys.argv[2], sys.argv[4]

            if winner_name == loser_name:
                print "Error: You have entered the same name twice."
                return False

            if user_interface.validate_input(winner_name) or user_interface.validate_input(loser_name):
                return False

            ladder.add_new_score(winner_name, loser_name)
            ladder.print_ladder()
            ladder.write_state()
            exit_code(0)

        else:
            print "Incorrect parameters. Use `pythom main.py --help` to view commands"
            exit_code(1)

    except:
        user_interface.print_help()
        exit_code(0)


def exit_code(code):
    if code < 0 or code > 3:
        print "invalid exit code"
    print "Program quit with exit code: " + str(code)


if __name__ == "__main__":
    main()