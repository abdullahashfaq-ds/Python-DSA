import unittest
from linked_list import LinkedList


class LinkedListTestCase(unittest.TestCase):
    def setUp(self):
        self.linked_list = LinkedList()

    def test_append(self):
        self.linked_list.append(1)
        self.linked_list.append(2)
        self.linked_list.append(3)
        self.assertEqual(str(self.linked_list), "1 -> 2 -> 3")

    def test_prepend(self):
        self.linked_list.prepend(0)
        self.linked_list.prepend(-1)
        self.assertEqual(str(self.linked_list), "-1 -> 0")

    def test_pop_empty_list(self):
        result = self.linked_list.pop()
        self.assertIsNone(result)
        self.assertEqual(str(self.linked_list), "Empty list")

    def test_pop_one_element(self):
        self.linked_list.append(1)

        result = self.linked_list.pop()
        self.assertEqual(result.value, 1)
        self.assertEqual(str(self.linked_list), "Empty list")

    def test_pop_multiple_elements(self):
        self.linked_list.append(1)
        self.linked_list.append(2)
        self.linked_list.append(3)

        result = self.linked_list.pop()
        self.assertEqual(result.value, 3)
        self.assertEqual(str(self.linked_list), "1 -> 2")

    def test_pop_first_empty_list(self):
        result = self.linked_list.pop_first()
        self.assertIsNone(result)
        self.assertEqual(str(self.linked_list), "Empty list")

    def test_pop_first_one_element(self):
        self.linked_list.append(1)

        result = self.linked_list.pop_first()
        self.assertEqual(result.value, 1)
        self.assertEqual(str(self.linked_list), "Empty list")

    def test_pop_first_multiple_elements(self):
        self.linked_list.append(1)
        self.linked_list.append(2)
        self.linked_list.append(3)

        result = self.linked_list.pop_first()
        self.assertEqual(result.value, 1)
        self.assertEqual(str(self.linked_list), "2 -> 3")

    def test_get_valid_index(self):
        self.linked_list.append(1)
        self.linked_list.append(2)
        self.linked_list.append(3)

        result = self.linked_list.get(1)
        self.assertEqual(result.value, 2)

    def test_get_out_of_range_index(self):
        self.linked_list.append(1)
        self.linked_list.append(2)
        self.linked_list.append(3)
        self.assertIsNone(self.linked_list.get(5))

    def test_set_value_valid_index(self):
        self.linked_list.append(1)
        self.linked_list.append(2)
        self.linked_list.append(3)

        result = self.linked_list.set_value(1, 4)
        self.assertTrue(result)
        self.assertEqual(str(self.linked_list), "1 -> 4 -> 3")

    def test_set_value_out_of_range_index(self):
        self.linked_list.append(1)
        self.linked_list.append(2)
        self.linked_list.append(3)

        result = self.linked_list.set_value(5, 5)
        self.assertFalse(result)
        self.assertEqual(str(self.linked_list), "1 -> 2 -> 3")

    def test_insert_at_beginning(self):
        self.linked_list.append(2)
        self.linked_list.append(3)

        result = self.linked_list.insert(0, 1)
        self.assertTrue(result)
        self.assertEqual(str(self.linked_list), "1 -> 2 -> 3")

    def test_insert_in_middle(self):
        self.linked_list.append(1)
        self.linked_list.append(3)

        result = self.linked_list.insert(1, 2)
        self.assertTrue(result)
        self.assertEqual(str(self.linked_list), "1 -> 2 -> 3")

    def test_insert_at_end(self):
        self.linked_list.append(1)
        self.linked_list.append(2)

        result = self.linked_list.insert(2, 3)
        self.assertTrue(result)
        self.assertEqual(str(self.linked_list), "1 -> 2 -> 3")

    def test_insert_out_of_range(self):
        self.linked_list.append(1)
        self.linked_list.append(2)

        result = self.linked_list.insert(5, 5)
        self.assertFalse(result)
        self.assertEqual(str(self.linked_list), "1 -> 2")

    def test_remove_from_beginning(self):
        self.linked_list.append(1)
        self.linked_list.append(2)
        self.linked_list.append(3)

        result = self.linked_list.remove(0)
        self.assertEqual(result.value, 1)
        self.assertEqual(str(self.linked_list), "2 -> 3")

    def test_remove_from_middle(self):
        self.linked_list.append(1)
        self.linked_list.append(2)
        self.linked_list.append(3)

        result = self.linked_list.remove(1)
        self.assertEqual(result.value, 2)
        self.assertEqual(str(self.linked_list), "1 -> 3")

    def test_remove_from_end(self):
        self.linked_list.append(1)
        self.linked_list.append(2)
        self.linked_list.append(3)

        result = self.linked_list.remove(2)
        self.assertEqual(result.value, 3)
        self.assertEqual(str(self.linked_list), "1 -> 2")

    def test_remove_out_of_range(self):
        self.linked_list.append(1)
        self.linked_list.append(2)
        self.linked_list.append(3)

        result = self.linked_list.remove(5)
        self.assertFalse(result)
        self.assertEqual(str(self.linked_list), "1 -> 2 -> 3")

    def test_reverse_empty_list(self):
        self.linked_list.reverse()
        self.assertEqual(str(self.linked_list), "Empty list")

    def test_reverse_single_element_list(self):
        self.linked_list.append(1)
        self.linked_list.reverse()
        self.assertEqual(str(self.linked_list), "1")

    def test_reverse_multiple_elements(self):
        self.linked_list.append(1)
        self.linked_list.append(2)
        self.linked_list.append(3)

        self.linked_list.reverse()
        self.assertEqual(str(self.linked_list), "3 -> 2 -> 1")


if __name__ == "__main__":
    unittest.main()
