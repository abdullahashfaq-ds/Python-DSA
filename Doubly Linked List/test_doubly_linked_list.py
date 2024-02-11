import unittest
from doubly_linked_list import DoublyLinkedList


class DoublyLinkedListTestCase(unittest.TestCase):
    def setUp(self):
        self.doubly_linked_list = DoublyLinkedList()

    def test_append_one_element(self):
        self.doubly_linked_list.append(1)

        self.assertEqual(
            str(self.doubly_linked_list),
            "1"
        )
        self.assertEqual(
            str(self.doubly_linked_list.get_reverse()),
            "1"
        )

    def test_append_multiple_elements(self):
        self.doubly_linked_list.append(1)
        self.doubly_linked_list.append(2)
        self.doubly_linked_list.append(3)

        self.assertEqual(
            str(self.doubly_linked_list),
            "1 -> 2 -> 3"
        )
        self.assertEqual(
            str(self.doubly_linked_list.get_reverse()),
            "3 -> 2 -> 1"
        )

    def test_prepend_one_element(self):
        self.doubly_linked_list.prepend(1)

        self.assertEqual(
            str(self.doubly_linked_list),
            "1"
        )
        self.assertEqual(
            str(self.doubly_linked_list.get_reverse()),
            "1"
        )

    def test_prepend_multiple_elements(self):
        self.doubly_linked_list.prepend(3)
        self.doubly_linked_list.prepend(2)
        self.doubly_linked_list.prepend(1)

        self.assertEqual(
            str(self.doubly_linked_list),
            "1 -> 2 -> 3"
        )
        self.assertEqual(
            str(self.doubly_linked_list.get_reverse()),
            "3 -> 2 -> 1"
        )

    def test_pop_empty_list(self):
        popped_node = self.doubly_linked_list.pop()

        self.assertIsNone(popped_node)
        self.assertEqual(
            str(self.doubly_linked_list),
            "Empty List"
        )
        self.assertEqual(
            str(self.doubly_linked_list.get_reverse()),
            "Empty List"
        )

    def test_pop_single_element(self):
        self.doubly_linked_list.append(1)
        popped_node = self.doubly_linked_list.pop()

        self.assertEqual(popped_node.value, 1)
        self.assertEqual(
            str(self.doubly_linked_list),
            "Empty List"
        )
        self.assertEqual(
            str(self.doubly_linked_list.get_reverse()),
            "Empty List"
        )

    def test_pop_multiple_elements(self):
        self.doubly_linked_list.append(1)
        self.doubly_linked_list.append(2)
        self.doubly_linked_list.append(3)

        popped_node = self.doubly_linked_list.pop()

        self.assertEqual(popped_node.value, 3)
        self.assertEqual(
            str(self.doubly_linked_list),
            "1 -> 2"
        )
        self.assertEqual(
            str(self.doubly_linked_list.get_reverse()),
            "2 -> 1"
        )

    def test_pop_first_empty_list(self):
        popped_node = self.doubly_linked_list.pop_first()

        self.assertIsNone(popped_node)
        self.assertEqual(
            str(self.doubly_linked_list),
            "Empty List"
        )
        self.assertEqual(
            str(self.doubly_linked_list.get_reverse()),
            "Empty List"
        )

    def test_pop_first_single_element(self):
        self.doubly_linked_list.append(1)
        popped_node = self.doubly_linked_list.pop_first()

        self.assertEqual(popped_node.value, 1)
        self.assertEqual(
            str(self.doubly_linked_list),
            "Empty List"
        )
        self.assertEqual(
            str(self.doubly_linked_list.get_reverse()),
            "Empty List"
        )

    def test_pop_first_multiple_elements(self):
        self.doubly_linked_list.append(1)
        self.doubly_linked_list.append(2)
        self.doubly_linked_list.append(3)

        popped_node = self.doubly_linked_list.pop_first()

        self.assertEqual(popped_node.value, 1)
        self.assertEqual(
            str(self.doubly_linked_list),
            "2 -> 3"
        )
        self.assertEqual(
            str(self.doubly_linked_list.get_reverse()),
            "3 -> 2"
        )

    def test_get_valid_index(self):
        self.doubly_linked_list.append(1)
        self.doubly_linked_list.append(2)
        self.doubly_linked_list.append(3)
        self.doubly_linked_list.append(4)

        value = self.doubly_linked_list.get(1).value
        self.assertEqual(value, 2)

        value = self.doubly_linked_list.get(3).value
        self.assertEqual(value, 4)

    def test_get_out_of_range_index(self):
        self.doubly_linked_list.append(1)
        self.doubly_linked_list.append(2)
        self.doubly_linked_list.append(3)

        value = self.doubly_linked_list.get(5)
        self.assertIsNone(value)

    def test_set_value_valid_index(self):
        self.doubly_linked_list.append(1)
        self.doubly_linked_list.append(2)
        self.doubly_linked_list.append(3)

        result = self.doubly_linked_list.set_value(1, 4)

        self.assertTrue(result)
        self.assertEqual(
            str(self.doubly_linked_list),
            "1 -> 4 -> 3"
        )
        self.assertEqual(
            str(self.doubly_linked_list.get_reverse()),
            "3 -> 4 -> 1"
        )

    def test_insert_at_beginning(self):
        self.doubly_linked_list.append(2)
        self.doubly_linked_list.append(3)

        result = self.doubly_linked_list.insert(0, 1)

        self.assertTrue(result)
        self.assertEqual(
            str(self.doubly_linked_list),
            "1 -> 2 -> 3"
        )

    def test_insert_in_middle(self):
        self.doubly_linked_list.append(1)
        self.doubly_linked_list.append(3)

        result = self.doubly_linked_list.insert(1, 2)

        self.assertTrue(result)
        self.assertEqual(
            str(self.doubly_linked_list),
            "1 -> 2 -> 3"
        )

    def test_insert_at_end(self):
        self.doubly_linked_list.append(1)
        self.doubly_linked_list.append(2)

        result = self.doubly_linked_list.insert(2, 3)

        self.assertTrue(result)
        self.assertEqual(
            str(self.doubly_linked_list),
            "1 -> 2 -> 3"
        )

    def test_insert_out_of_range(self):
        self.doubly_linked_list.append(1)
        self.doubly_linked_list.append(2)

        result = self.doubly_linked_list.insert(5, 5)

        self.assertFalse(result)
        self.assertEqual(
            str(self.doubly_linked_list),
            "1 -> 2"
        )

    def test_remove_from_beginning(self):
        self.doubly_linked_list.append(1)
        self.doubly_linked_list.append(2)
        self.doubly_linked_list.append(3)

        result = self.doubly_linked_list.remove(0)

        self.assertEqual(result.value, 1)
        self.assertEqual(
            str(self.doubly_linked_list),
            "2 -> 3"
        )

    def test_remove_from_middle(self):
        self.doubly_linked_list.append(1)
        self.doubly_linked_list.append(2)
        self.doubly_linked_list.append(3)

        result = self.doubly_linked_list.remove(1)

        self.assertEqual(result.value, 2)
        self.assertEqual(
            str(self.doubly_linked_list),
            "1 -> 3"
        )

    def test_remove_from_end(self):
        self.doubly_linked_list.append(1)
        self.doubly_linked_list.append(2)
        self.doubly_linked_list.append(3)

        result = self.doubly_linked_list.remove(2)

        self.assertEqual(result.value, 3)
        self.assertEqual(
            str(self.doubly_linked_list),
            "1 -> 2"
        )

    def test_remove_out_of_range(self):
        self.doubly_linked_list.append(1)
        self.doubly_linked_list.append(2)
        self.doubly_linked_list.append(3)

        result = self.doubly_linked_list.remove(5)

        self.assertFalse(result)
        self.assertEqual(
            str(self.doubly_linked_list),
            "1 -> 2 -> 3"
        )

    def test_remove_empty_list(self):
        result = self.doubly_linked_list.remove(0)

        self.assertFalse(result)
        self.assertEqual(
            str(self.doubly_linked_list),
            "Empty List"
        )


if __name__ == '__main__':
    unittest.main()
