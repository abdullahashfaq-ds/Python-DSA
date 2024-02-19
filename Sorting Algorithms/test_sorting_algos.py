import unittest
from bubble_sort import bubble_sort
from selection_sort import selection_sort
from merge_sort import merge_sort


class TestSortingAlgorithms(unittest.TestCase):

    def _run_sort_test(self, sorting_func):
        test_cases = [
            ([], []),
            ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
            ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
            ([3, 1, 4, 2, 5], [1, 2, 3, 4, 5]),
            ([5, 4, 3, 4, 5], [3, 4, 4, 5, 5]),
        ]

        for input_list, expected_output in test_cases:
            with self.subTest(input_list=input_list):
                result = sorting_func(input_list)
                self.assertEqual(result, expected_output)

    def test_bubble_sort(self):
        self._run_sort_test(bubble_sort)

    def test_merge_sort(self):
        self._run_sort_test(merge_sort)

    def test_selection_sort(self):
        self._run_sort_test(selection_sort)


if __name__ == '__main__':
    unittest.main()
