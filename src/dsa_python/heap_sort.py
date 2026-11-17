"""Heap sort using a max heap."""


def _sift_down(values: list[int], root: int, heap_size: int) -> None:
    """Restore the max-heap property below root."""
    while True:
        largest = root
        left_child = 2 * root + 1
        right_child = 2 * root + 2

        if left_child < heap_size and values[left_child] > values[largest]:
            largest = left_child
        if right_child < heap_size and values[right_child] > values[largest]:
            largest = right_child

        if largest == root:
            return

        values[root], values[largest] = values[largest], values[root]
        root = largest


def max_heap_sort(values: list[int]) -> list[int]:
    """Return an ascending sorted copy using a max heap.

    Time: O(n log n). Extra space: O(n) because the input is copied.
    """
    result = values.copy()

    # Turn the list into a max heap. Leaf nodes are already valid heaps.
    for root in range(len(result) // 2 - 1, -1, -1):
        _sift_down(result, root, len(result))

    # Move the maximum to the end, then repair the remaining heap.
    for end in range(len(result) - 1, 0, -1):
        result[0], result[end] = result[end], result[0]
        _sift_down(result, 0, end)

    return result


def main() -> None:
    """Run an example when this file is executed directly."""
    values = [12, 11, 13, 5, 6, 7]
    print(f"Before: {values}")
    print(f"After:  {max_heap_sort(values)}")


if __name__ == "__main__":
    main()
