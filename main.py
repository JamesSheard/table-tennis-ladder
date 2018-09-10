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

        if user_interface.is_get_ladder():
            ladder.get_ladder()

        else:
            print "incorrect parameters. `python main.py --win <name> --lose <name>`"

    except:
        player_entered = user_interface.get_selection()

        if player_entered == "1":
            ladder.get_ladder()
        elif player_entered == "2":
            winner_name, loser_name, valid = user_interface.get_names()
            if valid != True:
                return False

            ladder.add_new_player(winner_name, loser_name)
            ladder.get_ladder()
            ladder.write_state()


if __name__ == "__main__":
    main()