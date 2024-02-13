class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.count = 0

    def __str__(self):
        if self.first is None:
            return "Empty Queue"

        queue = "First -> "
        temp = self.first

        while temp:
            queue += f"{temp.value} -> "
            temp = temp.next

        return queue + "None"

    def enqueue(self, value):
        node = Node(value)

        if self.first is None:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node

        self.count += 1

    def dequeue(self):
        if self.first is None:
            return None

        temp = self.first

        if temp.next is None:
            self.first = None
            self.last = None
        else:
            self.first = temp.next
            temp.next = None

        self.count -= 1
        return temp

    def get_count(self):
        return self.count

    def is_empty(self):
        return self.count == 0
