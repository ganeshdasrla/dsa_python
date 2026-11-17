import unittest

from dsa_python.searching import binary_search, linear_search


class SearchingTests(unittest.TestCase):
    def test_searches_cover_edge_cases(self) -> None:
        cases = [
            ([], 1), ([4], 4), ([4], 2), ([-5, -2, 0, 3], -2),
            ([1, 2, 2, 2, 5], 2), ([1, 3, 5], 0), ([1, 3, 5], 6),
        ]
        for search in (linear_search, binary_search):
            for values, target in cases:
                with self.subTest(search=search.__name__, values=values, target=target):
                    index = search(values, target)
                    if target in values:
                        self.assertGreaterEqual(index, 0)
                        self.assertLess(index, len(values))
                        self.assertEqual(values[index], target)
                    else:
                        self.assertEqual(index, -1)

    def test_linear_search_returns_first_match(self) -> None:
        self.assertEqual(linear_search([5, 2, 5], 5), 0)

    def test_linear_search_returns_minus_one_when_missing(self) -> None:
        self.assertEqual(linear_search([1, 2, 3], 4), -1)

    def test_binary_search_finds_first_and_last_items(self) -> None:
        values = [2, 4, 7, 10, 15]
        self.assertEqual(binary_search(values, 2), 0)
        self.assertEqual(binary_search(values, 15), 4)

    def test_binary_search_handles_empty_and_missing_values(self) -> None:
        self.assertEqual(binary_search([], 1), -1)
        self.assertEqual(binary_search([1, 3, 5], 4), -1)


if __name__ == "__main__":
    unittest.main()
