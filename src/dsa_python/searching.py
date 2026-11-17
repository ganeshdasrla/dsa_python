"""Searching algorithms for sorted and unsorted sequences."""


def linear_search(values: list[int], target: int) -> int:
    """Return the first match, or -1. Time: O(n); extra space: O(1)."""
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1


def binary_search(values: list[int], target: int) -> int:
    """Return a matching index, or -1. Time: O(log n); extra space: O(1).

    The caller must supply values sorted in ascending order. If duplicates
    exist, any matching index may be returned.
    """
    left = 0
    right = len(values) - 1

    while left <= right:
        middle = (left + right) // 2
        if values[middle] == target:
            return middle
        if values[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1
