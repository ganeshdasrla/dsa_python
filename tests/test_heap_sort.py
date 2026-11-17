import unittest

from dsa_python.heap_sort import max_heap_sort


class MaxHeapSortTests(unittest.TestCase):
    def test_sorts_common_cases_without_changing_input(self) -> None:
        cases = [
            [],
            [1],
            [1, 2, 3],
            [3, 2, 1],
            [12, 11, 13, 5, 6, 7],
            [3, -1, 3, 0],
        ]

        for values in cases:
            with self.subTest(values=values):
                original = values.copy()
                self.assertEqual(max_heap_sort(values), sorted(original))
                self.assertEqual(values, original)


if __name__ == "__main__":
    unittest.main()
