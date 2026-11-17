"""Heap sort using a max heap."""


def _sift_down(
    values: list[int], root: int, heap_size: int, *, trace: bool = False
) -> None:
    """Restore the max-heap property below root."""
    while True:
        largest = root
        left_child = 2 * root + 1
        right_child = 2 * root + 2

        if trace:
            print(
                f"  Inspect index {root} (value {values[root]}) "
                f"in heap {values[:heap_size]}"
            )

        if left_child < heap_size:
            if trace:
                print(
                    f"    Compare left child: {values[left_child]} "
                    f"with current largest: {values[largest]}"
                )
            if values[left_child] > values[largest]:
                largest = left_child

        if right_child < heap_size:
            if trace:
                print(
                    f"    Compare right child: {values[right_child]} "
                    f"with current largest: {values[largest]}"
                )
            if values[right_child] > values[largest]:
                largest = right_child

        if largest == root:
            if trace:
                print("    No swap needed; this part is already a max heap.")
            return

        if trace:
            print(
                f"    Swap {values[root]} at index {root} with "
                f"{values[largest]} at index {largest}"
            )
        values[root], values[largest] = values[largest], values[root]
        if trace:
            print(f"    Array after swap: {values}")
        root = largest


def max_heap_sort(values: list[int], *, trace: bool = False) -> list[int]:
    """Return an ascending sorted copy using a max heap.

    Time: O(n log n). Extra space: O(n) because the input is copied.
    Set trace=True to print each important comparison and swap.
    """
    result = values.copy()

    if trace:
        print(f"Starting array: {result}")
        print("\nPHASE 1: Build a max heap")

    # Turn the list into a max heap. Leaf nodes are already valid heaps.
    for root in range(len(result) // 2 - 1, -1, -1):
        if trace:
            print(f"\nStart sifting from index {root}:")
        _sift_down(result, root, len(result), trace=trace)

    if trace:
        print(f"\nMax heap completed: {result}")
        print("\nPHASE 2: Move each maximum into its final position")

    # Move the maximum to the end, then repair the remaining heap.
    for end in range(len(result) - 1, 0, -1):
        if trace:
            print(
                f"\nMove maximum {result[0]} from index 0 "
                f"to final index {end}."
            )
        result[0], result[end] = result[end], result[0]
        if trace:
            print(f"  After moving maximum: {result}")
            print(f"  Unsorted heap: {result[:end]} | Sorted: {result[end:]}")
        _sift_down(result, 0, end, trace=trace)
        if trace:
            print(f"  Heap repaired: {result[:end]} | Sorted: {result[end:]}")

    if trace:
        print(f"\nSorting complete: {result}")

    return result


def main() -> None:
    """Run an example when this file is executed directly."""
    values = [12, 11, 13, 5, 6, 7]
    sorted_values = max_heap_sort(values, trace=True)
    print(f"\nReturned result: {sorted_values}")


if __name__ == "__main__":
    main()
