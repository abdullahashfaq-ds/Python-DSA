class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.count = 0

    def __str__(self):
        if self.top is None:
            return "Empty Stack"

        stack = "Head -> "
        temp = self.top

        while temp:
            stack += f"{temp.value} -> "
            temp = temp.next

        return stack + "None"

    def push(self, value):
        node = Node(value)

        if self.top is None:
            self.top = node
        else:
            node.next = self.top
            self.top = node

        self.count += 1

    def pop(self):
        if self.top is None:
            return None

        temp = self.top
        self.top = temp.next
        temp.next = None

        self.count -= 1
        return temp

    def get_count(self):
        return self.count

    def is_empty(self):
        return self.count == 0
