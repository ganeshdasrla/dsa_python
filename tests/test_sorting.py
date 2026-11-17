import unittest

from dsa_python.sorting import bubble_sort


class SortingTests(unittest.TestCase):
    def test_sorts_common_cases_without_changing_input(self) -> None:
        for values in ([], [1], [1, 2, 3], [3, 2, 1], [3, -1, 3, 0]):
            with self.subTest(values=values):
                original = values.copy()
                result = bubble_sort(values)
                self.assertEqual(result, sorted(original))
                self.assertEqual(values, original)
                self.assertIsNot(result, values)


if __name__ == "__main__":
    unittest.main()
