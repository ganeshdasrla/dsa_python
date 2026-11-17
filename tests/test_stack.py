import unittest

from dsa_python.stack import Stack


class StackTests(unittest.TestCase):
    def test_last_in_first_out_and_length(self) -> None:
        stack: Stack[int] = Stack()
        self.assertEqual(len(stack), 0)
        stack.push(10)
        stack.push(20)
        self.assertEqual(len(stack), 2)
        self.assertEqual(stack.pop(), 20)
        self.assertEqual(stack.pop(), 10)
        self.assertEqual(len(stack), 0)

    def test_peek_preserves_item(self) -> None:
        stack: Stack[str] = Stack()
        stack.push("hello")
        self.assertEqual(stack.peek(), "hello")
        self.assertEqual(len(stack), 1)
        self.assertEqual(stack.pop(), "hello")

    def test_empty_stack_operations_raise(self) -> None:
        stack: Stack[int] = Stack()
        with self.assertRaises(IndexError):
            stack.pop()
        with self.assertRaises(IndexError):
            stack.peek()


if __name__ == "__main__":
    unittest.main()
