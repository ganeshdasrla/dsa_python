"""A last-in, first-out (LIFO) data structure backed by a Python list."""

from typing import Generic, TypeVar

T = TypeVar("T")


class Stack(Generic[T]):
    """Push is amortized O(1); pop, peek, and len are O(1)."""

    def __init__(self) -> None:
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        """Remove the latest item; raise IndexError when empty."""
        if not self._items:
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self) -> T:
        """Read the latest item; raise IndexError when empty."""
        if not self._items:
            raise IndexError("peek at empty stack")
        return self._items[-1]

    def __len__(self) -> int:
        return len(self._items)
