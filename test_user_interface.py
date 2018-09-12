import unittest
from user_interface import Interface
import StringIO
import sys


class TestUserInterfaceMethods(unittest.TestCase):

    def setUp(self):
        self.user_interface = Interface([])

    def test_unix_args(self):
        test_cases = [
            [["main.py", "--win", "James", "--lose", "mike"], True],
            [["main.py", "-w", "James", "-l", "mike"], True],
            [["main.py", "-w", "James", "--lose", "mike"], True],
            [["foo", 0123, "bar"], False],
            [[0123, 4385], False]
        ]

        for tc in test_cases:
            self.user_interface.args = tc[0]
            expected = tc[1]
            self.assertEqual(expected, self.user_interface.unix_args())

    def test_is_get_ladder(self):
        test_cases = [
            [["main.py", "--getladder"], True],
            [["main.py", "-gl"], True],
            [["foo", "bar"], False]
        ]

        for tc in test_cases:
            self.user_interface.args = tc[0]
            expected = tc[1]
            self.assertEqual(expected, self.user_interface.is_get_ladder())

    def test_is_get_help(self):
        test_cases = [
            [["main.py", "--help"], True],
            [["main.py", "-h"], True],
            [["foo", "bar"], False]
        ]

        for tc in test_cases:
            self.user_interface.args = tc[0]
            expected = tc[1]
            self.assertEqual(expected, self.user_interface.is_get_help())


    def test_print_help(self):
        captured_output = StringIO.StringIO()
        sys.stdout = captured_output
        self.user_interface.print_help()
        expected = 722
        # 722 is the length of the help file.
        # TODO: This is properly shonk.

        self.assertEqual(len(captured_output.getvalue()), expected)

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


if __name__ == '__main__':
    unittest.main()