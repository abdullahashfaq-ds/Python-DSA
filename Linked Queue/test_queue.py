import unittest
from queue import Queue


class QueueTestCase(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_enqueue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)

        self.assertFalse(self.queue.is_empty())
        self.assertEqual(self.queue.get_count(), 3)
        self.assertEqual(
            str(self.queue),
            "First -> 1 -> 2 -> 3 -> None"
        )

    def test_dequeue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)

        dequeued_node = self.queue.dequeue()

        self.assertEqual(dequeued_node.value, 1)
        self.assertEqual(
            str(self.queue),
            "First -> 2 -> 3 -> None"
        )

        dequeued_node = self.queue.dequeue()

        self.assertEqual(dequeued_node.value, 2)
        self.assertEqual(
            str(self.queue),
            "First -> 3 -> None"
        )

    def test_dequeue_empty_queue(self):
        dequeued_value = self.queue.dequeue()

        self.assertIsNone(dequeued_value)
        self.assertTrue(self.queue.is_empty())
        self.assertEqual(self.queue.get_count(), 0)
        self.assertEqual(str(self.queue), "Empty Queue")


if __name__ == '__main__':
    unittest.main()
