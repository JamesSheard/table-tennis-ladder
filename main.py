import sys
from user_interface import Interface
from ladder import Ladder


def main():
    ladder = Ladder()
    user_interface = Interface(sys.argv)

    try:
        if user_interface.unix_args():
            winner_name, loser_name = sys.argv[2], sys.argv[4]

            if user_interface.validate_input(winner_name) or user_interface.validate_input(loser_name):
                return False

            ladder.add_new_player(winner_name, loser_name)
            ladder.get_ladder()
            ladder.write_state()

        elif user_interface.is_get_ladder():
            ladder.get_ladder()

        elif user_interface.is_get_help():
            user_interface.print_help()

        elif user_interface.is_interactive_mode():
            user_interface.interactive_mode(ladder)

        else:
            print "Incorrect parameters. Use `pythom main.py --help` to view commands"

    except:
        user_interface.print_help()


if __name__ == "__main__":
    main()