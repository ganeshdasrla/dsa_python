"""Start with bubble sort, then compare it with more efficient algorithms."""


def bubble_sort(values: list[int]) -> list[int]:
    """Return a sorted copy, preserving the input.

    Time: O(n squared) on average/worst case, O(n) when already sorted.
    Extra space: O(n) for the copy. Equal values retain their relative order.
    """
    result = values.copy()
    for end in range(len(result) - 1, 0, -1):
        swapped = False
        for index in range(end):
            if result[index] > result[index + 1]:
                result[index], result[index + 1] = result[index + 1], result[index]
                swapped = True
        if not swapped:
            break
    return result
