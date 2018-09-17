import unittest
from user_interface import Interface
import StringIO
import sys
from ladder.ladder import Ladder
from database.db_controller import Database


class TestUserInterfaceMethods(unittest.TestCase):

    def setUp(self):
        self.user_interface = Interface([])

    def test_record_results(self):
        test_cases = [
            [["main.py", "--win", "James", "--lose", "mike"], True],
            [["main.py", "-w", "James", "-l", "mike"], True],
            [["main.py", "-w", "James", "--lose", "mike"], True],
            [["foo", "0123", "bar"], False],
            [["0123", "4385"], False]
        ]

        for tc in test_cases:
            self.user_interface.args = tc[0]
            expected = tc[1]
            self.assertEqual(expected, self.user_interface.record_result())

    def test_check_all_args(self):
        test_cases = [
            [["--leaderboard", "-lb"], ["main.py", "-lb"], True],
            [["--leaderboard", "-lb"], ["main.py", "-ll"], False],
            [["--leaderboard", "-lb"], ["main.py", "foo", "-lb"], True]
        ]

        for tc in test_cases:
            self.user_interface.args = tc[1]
            expected_output = tc[2]
            self.assertEqual(self.user_interface.check_all_args(tc[0][0], tc[0][1]), expected_output)


    def test_check_first_arg(self):
        test_cases = [
            [["--leaderboard", "-lb"], ["main.py", "-lb"], True],
            [["--leaderboard", "-lb"], ["main.py", "-ll"], False],
            [["--leaderboard", "-lb"], ["main.py", "foo", "-lb"], False]
        ]

        for tc in test_cases:
            self.user_interface.args = tc[1]
            expected_output = tc[2]
            self.assertEqual(self.user_interface.check_first_arg(tc[0][0], tc[0][1]), expected_output)

    def test_get_leaderboard_pos(self):
        test_cases = [
            [["main.py", "--leaderboard"], 2],
            [["main.py", "-lb"], 2],
            [["main.py", "foo", "bar", "--leaderboard"], 4],
            [["main.py", "foo", "-lb", "bar"], 3]
        ]

        for tc in test_cases:
            self.user_interface.args = tc[0]
            expected_output = tc[1]
            self.assertEqual(expected_output, self.user_interface.get_leaderboard_pos())

    def test_is_list_ladders(self):
        test_cases = [
            [["main.py", "--listladders"], True],
            [["main.py", "-ll"], True],
            [["foo", "bar"], False],
            [["-ll"], False]
        ]

        for tc in test_cases:
            self.user_interface.args = tc[0]
            expected = tc[1]
            self.assertEqual(expected, self.user_interface.is_list_ladders())


    def test_is_get_ladder(self):
        test_cases = [
            [["main.py", "--getladder"], True],
            [["main.py", "-gl"], True],
            [["foo", "bar"], False],
            [["-gl"], False]
        ]

        for tc in test_cases:
            self.user_interface.args = tc[0]
            expected = tc[1]
            self.assertEqual(expected, self.user_interface.is_get_ladder())

    def test_is_get_help(self):
        test_cases = [
            [["main.py", "--help"], True],
            [["main.py", "-h"], True],
            [["foo", "bar"], False],
            [["-h"], False]
        ]

        for tc in test_cases:
            self.user_interface.args = tc[0]
            expected = tc[1]
            self.assertEqual(expected, self.user_interface.is_get_help())

    def test_print_help(self):
        captured_output = StringIO.StringIO()
        sys.stdout = captured_output
        self.user_interface.print_help()
        expected_output = "--- Welcome to Table Tennis Tracker ---"

        self.assertIn(expected_output, captured_output.getvalue())

    def test_validate_input(self):
        test_cases = [
            ["Harry", False],
            ["Jam<e>s", True],
            ["Tom_Dick_and_Harry", False],
            ["Tom Dick and Harry", False],
            ["Tom_Dick_Harry_and_James", True],
            ["123123321321", False]
        ]

        for tc in test_cases:
            input = tc[0]
            expected = tc[1]
            actual = self.user_interface.validate_input(input)
            self.assertEqual(expected, actual)

    def test_select_ladder(self):
        test_cases = [
            [["main.py", "-lb", "taste_card"], "taste_card"],
            [["main.py", "-lb", "emis"], "emis"],
            [["main.py", "--leaderboard", "emis"], "emis"],
            [["main.py"], "global"]
        ]

        for tc in test_cases:
            self.user_interface.args = tc[0]

            self.assertEqual(
                self.user_interface.select_ladder().ladder_name,
                Ladder(tc[1], Database(tc[1])).ladder_name
            )

    def test_select_ladder_raises_expection(self):
        self.user_interface.args = ["main.py", "-lb", "!@%!"]

        with self.assertRaises(SystemExit) as cm:
            self.user_interface.select_ladder()
            self.assertEqual(cm.exception, "Error")


if __name__ == '__main__':
    unittest.main()