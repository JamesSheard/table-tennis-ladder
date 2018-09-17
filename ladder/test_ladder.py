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
        expected_output = "+---------------+\n|  Test_Ladder  |\n+-------+-------+\n" \
                          "|  Name |  Rank |\n+-------+-------+\n|  Jim  |   1   |\n" \
                          "|  John |   2   |\n|  Bob  |   3   |\n|  Bill |   4   |\n" \
                          "|  Kev  |   5   |\n+-------+-------+\n"

        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_list_ladders(self):
        captured_output = StringIO.StringIO()
        sys.stdout = captured_output
        self.ladder.list_ladders()
        expected_output = "+-------------+\n| League Name |\n+-------------+\n" \
                          "|  taste_card |\n|     emis    |\n|    global   |\n" \
                          "+-------------+\n"

        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_get_pos(self):
        self.ladder.table = [
            "Jim",
            "John",
            "Bob",
            "Bill",
            "Kev"]

        test_cases = [
                        ["Bob", 2],
                        ["Gregory", False],
                        [233144, False]
                      ]

        for tc in test_cases:
            expected_output = tc[1]
            actual_output = self.ladder.get_pos(tc[0])
            self.assertEqual(expected_output, actual_output)


if __name__ == "__main__":
    unittest.main()
