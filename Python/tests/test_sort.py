from bubble_sort import bubble_sort
from hash_sort import hash_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from quick_sort import quick_sort, modified_quick_sort
from random_lists import create_random_list
from selection_sort import selection_sort
from shaker_sort import shaker_sort
from sort_functions import get_sort_function_names

from random import randint
import unittest


class TestSortingFunctions(unittest.TestCase):
    def setUp(self):
        self.sort_function_names = get_sort_function_names()

    def test_sorted(self):
        size = randint(2, 30)
        random_list = create_random_list(size)
        expected_list = sorted(random_list)

        for sort_function_name in self.sort_function_names:
            actual_list = self.sort_function_names[sort_function_name](random_list)

            self.assertEqual(expected_list, actual_list)

    def test_empty_list(self):
        empty_list = []
        expected_list = []

        for sort_function_name in self.sort_function_names:
            actual_list = self.sort_function_names[sort_function_name](empty_list)

            self.assertEqual(expected_list, actual_list)

if __name__ == '__main__':
    unittest.main()
