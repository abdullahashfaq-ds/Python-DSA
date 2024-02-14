import sys
import unittest
from io import StringIO
from binary_search_tree import BinarySearchTree


class TestBinarySearchTree(unittest.TestCase):
    def setUp(self):
        self.tree = BinarySearchTree()

        self.tree.insert(5)
        self.tree.insert(3)
        self.tree.insert(7)
        self.tree.insert(4)
        self.tree.insert(6)

    def tearDown(self):
        """Reset stdout after each test"""
        sys.stdout = sys.__stdout__

    def _test_display(self, traversal_method, expected_output):
        captured_output = StringIO()
        sys.stdout = captured_output

        self.tree.display(traversal_method)
        output = captured_output.getvalue().strip()
        self.assertEqual(output, expected_output)

    def test_insert(self):
        self.assertEqual(self.tree.root.value, 5)
        self.assertEqual(self.tree.root.left.value, 3)
        self.assertEqual(self.tree.root.right.value, 7)
        self.assertEqual(self.tree.root.left.right.value, 4)
        self.assertEqual(self.tree.root.right.left.value, 6)

    def test_display_inorder(self):
        expected_output = "3 4 5 6 7"
        self._test_display("inorder", expected_output)

    def test_display_preorder(self):
        expected_output = "5 3 4 7 6"
        self._test_display("preorder", expected_output)

    def test_display_postorder(self):
        expected_output = "4 3 6 7 5"
        self._test_display("postorder", expected_output)

    def test_display_level_order(self):
        expected_output = "5 3 7 4 6"
        self._test_display("level_order", expected_output)

    def test_height(self):
        self.assertEqual(self.tree.height(), 2)

    def test_find_min(self):
        self.assertEqual(self.tree.find_min(), 3)

    def test_find_max(self):
        self.assertEqual(self.tree.find_max(), 7)


if __name__ == '__main__':
    unittest.main()
