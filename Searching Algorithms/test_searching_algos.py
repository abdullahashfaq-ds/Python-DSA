import unittest
from linear_search import linear_search_iterative, linear_search_recursive
from binary_search import binary_search_iterative, binary_search_recursive


class TestSearchingAlgorithms(unittest.TestCase):

    def _run_search_test(self, searching_func):
        test_cases = [
            ([], 5, -1),
            ([1], 1, 0),
            ([1], 5, -1),
            ([1, 2, 3, 4, 5], 1, 0),
            ([1, 2, 3, 4, 5], 5, 4),
            ([1, 2, 3, 4, 5, 6, 7, 8], 5, 4),
            ([1, 2, 3, 4, 5, 6, 7, 8], 9, -1),
            ([1, 2, 3, 4, 5, 6, 7, 8], 3, 2),
            ([1, 2, 3, 4, 5, 6, 7, 8], 10, -1),
        ]

        for arr, target, expected_output in test_cases:
            with self.subTest(arr=arr, target=target):
                result = searching_func(arr, target)
                self.assertEqual(result, expected_output)

    def test_linear_search_iterative(self):
        self._run_search_test(linear_search_iterative)

    def test_linear_search_recursive(self):
        self._run_search_test(linear_search_recursive)

    def test_binary_search_iterative(self):
        self._run_search_test(binary_search_iterative)

    def testbinaryr_search_recursive(self):
        self._run_search_test(binary_search_recursive)


if __name__ == '__main__':
    unittest.main()
