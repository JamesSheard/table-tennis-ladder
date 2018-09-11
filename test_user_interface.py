import unittest
from user_interface import Interface


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

    def test_interactive_mode(self):
        test_cases = [
            [["main.py", "--interactive"], True],
            [["main.py", "-i"], True],
            [["foo", "bar"], False]
        ]

        for tc in test_cases:
            self.user_interface.args = tc[0]
            expected = tc[1]
            self.assertEqual(expected, self.user_interface.is_interactive_mode())


if __name__ == '__main__':
    unittest.main()