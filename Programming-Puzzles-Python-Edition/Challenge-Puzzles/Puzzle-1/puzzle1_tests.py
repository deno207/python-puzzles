import unittest
import Puzzle1


class Puzzle1TestCase(unittest.TestCase):
    def test_filters_out_strings_without_a(self):
        returned_list = Puzzle1.filter_strings_containing_a(["apple", "banana", "cherry", "date"])
        self.assertEqual(["apple", "banana", "date"], returned_list)  # add assertion here

    def test_funtion_can_handle_empty_list(self):
        filtered_list = Puzzle1.filter_strings_containing_a([])
        self.assertEqual([], filtered_list)

    def test_function_can_return_empty_list(self):
        filtered_list = Puzzle1.filter_strings_containing_a(["bbbb", "cccc"])
        self.assertEqual([], filtered_list)

    def test_function_only_filters_lower_case_a(self):
        filtered_list = Puzzle1.filter_strings_containing_a(["aaaa", "AAAA"])
        self.assertEqual(["aaaa"], filtered_list)


if __name__ == '__main__':
    unittest.main()
