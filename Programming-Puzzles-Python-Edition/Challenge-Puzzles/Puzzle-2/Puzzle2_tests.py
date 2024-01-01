import unittest
import Puzzle2


class Puzzle2TestCase(unittest.TestCase):
    def test_sum_is_returned_if_less_fifty(self):
        self.assertEqual(25, Puzzle2.sum_if_less_than_fifty(10, 15))

    def test_sum_is_returned_if_it_is_forty_nine(self):
        self.assertEqual(49, Puzzle2.sum_if_less_than_fifty(40, 9))

    def test_None_is_returned_if_sum_is_fifty(self):
        self.assertEqual(None, Puzzle2.sum_if_less_than_fifty(25, 25))

    def test_None_is_returned_if_sum_is_greater_than_fifty(self):
        self.assertEqual(None, Puzzle2.sum_if_less_than_fifty(30, 30))

    def test_function_can_handle_negative_numbers(self):
        self.assertEqual(-10, Puzzle2.sum_if_less_than_fifty(-5, -5))

    def test_function_can_handle_zero(self):
        self.assertEqual(0, Puzzle2.sum_if_less_than_fifty(0, 0))


if __name__ == '__main__':
    unittest.main()
