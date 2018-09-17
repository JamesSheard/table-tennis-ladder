import sys
import unittest
from ladder import Ladder
import StringIO
from mocks.mock_db import Database


class TestLadderMethods(unittest.TestCase):
    def setUp(self):
        mock_db = Database("Test_Ladder", [
            "Jim",
            "John",
            "Bob",
            "Bill",
            "Kev"])

        self.ladder = Ladder("Test_Ladder", mock_db)
        self.ladder.table = [
            "Jim",
            "John",
            "Bob",
            "Bill",
            "Kev"]

    def test_player_in_ladder(self):
        self.assertEqual(self.ladder.player_in_ladder("Jim"), True)
        self.assertEqual(self.ladder.player_in_ladder("Gavin"), False)

    def test_add_two_new_players(self):
        self.ladder.table = [
            "Jim",
            "John",
            "Bob",
            "Bill",
            "Kev"]

        expected_table = [
            "Jim",
            "John",
            "Bob",
            "Bill",
            "Kev",
            "Gazza",
            "Carlson"]

        self.ladder.add_new_score("Gazza", "Carlson")

        for x in range(0, len(self.ladder.table)):
            self.assertEqual(self.ladder.table[x], expected_table[x])

    def test_add_one_new_winning_player(self):
        self.ladder.table = [
            "Jim",
            "John",
            "Bob",
            "Bill",
            "Kev"]

        expected_table = [
            "Jim",
            "John",
            "Bob",
            "Gazza",
            "Bill",
            "Kev"]

        self.ladder.add_new_score("Gazza", "Bill")

        for x in range(0, len(self.ladder.table)):
            self.assertEqual(self.ladder.table[x], expected_table[x])

    def test_add_one_new_losing_player(self):
        self.ladder.table = [
            "Jim",
            "John",
            "Bob",
            "Bill",
            "Kev"]

        expected_table = [
            "Jim",
            "John",
            "Bob",
            "Bill",
            "Kev",
            "Gazza"]

        self.ladder.add_new_score("John", "Gazza")

        for x in range(0, len(self.ladder.table)):
            self.assertEqual(self.ladder.table[x], expected_table[x])

    def test_existing_competing_players(self):
        self.ladder.table = [
            "Jim",
            "John",
            "Bob",
            "Bill",
            "Kev"]

        expected_table = [
            "Jim",
            "Bill",
            "John",
            "Bob",
            "Kev"]

        self.ladder.add_new_score("Bill", "John")

        for x in range(0, len(self.ladder.table)):
            self.assertEqual(self.ladder.table[x], expected_table[x])

    def test_print_ladder(self):
        captured_output = StringIO.StringIO()
        sys.stdout = captured_output
        self.ladder.print_ladder()
        expected_len = 198
        # 198 is the number of characters in the leaderboard
        # TODO: This is properly shonk.

        self.assertEqual(len(captured_output.getvalue()), expected_len)

    def test_list_ladders(self):
        captured_output = StringIO.StringIO()
        sys.stdout = captured_output
        self.ladder.list_ladders()
        expected_output = "+-------------+\n| League Name |\n+-------------+\n" \
                          "|  taste_card |\n|     emis    |\n|    global   |\n+-------------+\n"
        # 198 is the number of characters in the leaderboard
        # TODO: This is properly shonk.

        self.assertEqual(captured_output.getvalue(), expected_output)

if __name__ == "__main__":
    unittest.main()
