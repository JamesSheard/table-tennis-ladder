import unittest
from user_interface import Interface


class TestUserInterfaceMethods(unittest.TestCase):

    def setUp(self):
        self.user_interface = Interface([])

    def test_unix_args_true(self):
        self.user_interface.args = ["main.py", "--win", "James", "--lose", "Mike"]
        expected_output = True
        self.assertEqual(expected_output, self.user_interface.unix_args())

    def test_unix_args_false(self):
        self.user_interface.args = ["lolol", 12342, "HFVHWVFVW"]
        expected_output = False
        self.assertEqual(expected_output, self.user_interface.unix_args())

    def test_is_get_ladder_true(self):
        self.user_interface.args = ["main.py", "--getladder"]
        expected_output = True
        self.assertEqual(expected_output, self.user_interface.is_get_ladder())

    def test_is_get_ladder_false(self):
        self.user_interface.args = ["main.py", "011899961991"]
        expected_output = False
        self.assertEqual(expected_output, self.user_interface.is_get_ladder())

    def test_is_get_help_true(self):
        self.user_interface.args = ["main.py", "--help"]
        expected_output = True
        self.assertEqual(expected_output, self.user_interface.is_get_help())

    def test_is_get_help_false(self):
        self.user_interface.args = ["main.py", "ugfugf"]
        expected_output = False
        self.assertEqual(expected_output, self.user_interface.is_get_help())

    def test_interactive_mode_true(self):
        self.user_interface.args = ["main.py", "--interactive"]
        expected_output = True
        self.assertEqual(expected_output, self.user_interface.is_interactive_mode())

    def test_interactive_mode_false(self):
        self.user_interface.args = ["main.py", "Random"]
        expected_output = False
        self.assertEqual(expected_output, self.user_interface.is_interactive_mode())
  





if __name__ == '__main__':
    unittest.main()
