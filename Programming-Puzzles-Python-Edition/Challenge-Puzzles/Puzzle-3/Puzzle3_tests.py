import unittest
import Puzzle3


class Puzzle3TestCase(unittest.TestCase):
    def test_function_returns_sum_if_all_numbers_even(self):
        self.assertEqual(150, Puzzle3.sum_even([10, 20, 30, 40, 50]))

    def test_function_returns_zero_if_all_numbers_odd(self):
        self.assertEqual(0, Puzzle3.sum_even([9, 7, 5, 3, 1]))

    def test_function_returns_correct_sum_if_numbers_are_odd_and_even(self):
        self.assertEqual(30, Puzzle3.sum_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

    def test_function_returns_zero_with_empty_list(self):
        self.assertEqual(0, Puzzle3.sum_even([]))


if __name__ == '__main__':
    unittest.main()
