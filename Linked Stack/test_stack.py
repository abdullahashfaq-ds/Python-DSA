import unittest
from stack import Stack


class StackTestCase(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_push(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)

        self.assertFalse(self.stack.is_empty())
        self.assertEqual(self.stack.get_count(), 3)
        self.assertEqual(
            str(self.stack),
            "Head -> 3 -> 2 -> 1 -> None"
        )

    def test_pop(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)

        popped_node = self.stack.pop()

        self.assertEqual(popped_node.value, 3)
        self.assertEqual(
            str(self.stack),
            "Head -> 2 -> 1 -> None"
        )

        popped_node = self.stack.pop()

        self.assertEqual(popped_node.value, 2)
        self.assertEqual(
            str(self.stack),
            "Head -> 1 -> None"
        )

    def test_pop_empty_stack(self):
        popped_value = self.stack.pop()

        self.assertIsNone(popped_value)
        self.assertTrue(self.stack.is_empty())
        self.assertEqual(self.stack.get_count(), 0)
        self.assertEqual(str(self.stack), "Empty Stack")


if __name__ == '__main__':
    unittest.main()
