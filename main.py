"""Run a small demo of the algorithms in this project."""

from dsa_python.searching import binary_search, linear_search
from dsa_python.sorting import bubble_sort
from dsa_python.stack import Stack


def main() -> None:
    numbers = [2, 4, 7, 10, 15, 21]
    target = 10
    result = binary_search(numbers, target)
    print(f"Binary search: {target} is at index {result}.")
    print(f"Linear search: {target} is at index {linear_search(numbers, target)}.")

    unsorted_numbers = [7, 2, 10, 4, 2]
    print(f"Bubble sort: {unsorted_numbers} -> {bubble_sort(unsorted_numbers)}")

    stack: Stack[str] = Stack()
    stack.push("first")
    stack.push("second")
    print(f"Stack: popped {stack.pop()!r}; next item is {stack.peek()!r}.")


if __name__ == "__main__":
    main()
