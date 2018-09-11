import sys
import unittest
from ladder import Ladder
from player import player
import StringIO


class TestLadderMethods(unittest.TestCase):

    def setUp(self):
        self.ladder = Ladder()
        self.ladder.table = [
            player("Jim"),
            player("John"),
            player("Bob"),
            player("Bill"),
            player("Kev")]

    def test_player_in_ladder(self):
        self.assertEqual(self.ladder.player_in_ladder("Jim"), True)
        self.assertEqual(self.ladder.player_in_ladder("Gavin"), False)

    def test_add_two_new_players(self):
        self.ladder.table = [
            player("Jim"),
            player("John"),
            player("Bob"),
            player("Bill"),
            player("Kev")]

        expected_table = [
            player("Jim"),
            player("John"),
            player("Bob"),
            player("Bill"),
            player("Kev"),
            player("Gazza"),
            player("Carlson")]

        self.ladder.add_new_score("Gazza", "Carlson")

        for x in range(0, len(self.ladder.table)):
            self.assertEqual(self.ladder.table[x].name, expected_table[x].name)

    def test_add_one_new_winning_player(self):
        self.ladder.table = [
            player("Jim"),
            player("John"),
            player("Bob"),
            player("Bill"),
            player("Kev")]

        expected_table = [
            player("Jim"),
            player("John"),
            player("Bob"),
            player("Gazza"),
            player("Bill"),
            player("Kev")]

        self.ladder.add_new_score("Gazza", "Bill")

        for x in range(0, len(self.ladder.table)):
            self.assertEqual(self.ladder.table[x].name, expected_table[x].name)

    def test_add_one_new_losing_player(self):
        self.ladder.table = [
            player("Jim"),
            player("John"),
            player("Bob"),
            player("Bill"),
            player("Kev")]

        expected_table = [
            player("Jim"),
            player("John"),
            player("Bob"),
            player("Bill"),
            player("Kev"),
            player("Gazza")]

        self.ladder.add_new_score("John", "Gazza")

        for x in range(0, len(self.ladder.table)):
            self.assertEqual(self.ladder.table[x].name, expected_table[x].name)

    def test_existing_competing_players(self):
        self.ladder.table = [
            player("Jim"),
            player("John"),
            player("Bob"),
            player("Bill"),
            player("Kev")]

        expected_table = [
            player("Jim"),
            player("Bill"),
            player("John"),
            player("Bob"),
            player("Kev")]

        self.ladder.add_new_score("Bill", "John")

        for x in range(0, len(self.ladder.table)):
            self.assertEqual(self.ladder.table[x].name, expected_table[x].name)

    def test_print_ladder(self):
        captured_output = StringIO.StringIO()
        sys.stdout = captured_output
        self.ladder.print_ladder()
        expected_len = 144
        # 144 is the number of characters in the leaderboard
        # TODO: This is properly shonk.


        self.assertEqual(len(captured_output.getvalue()), expected_len)


if __name__ == "__main__":
    unittest.main()
