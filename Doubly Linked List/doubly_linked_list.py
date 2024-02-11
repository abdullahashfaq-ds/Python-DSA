class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.leng = 0

    def __str__(self):
        if self.head is None:
            return "Empty List"

        temp = self.head
        doubly_list = ""

        while temp:
            doubly_list += f"{temp.value} -> "
            temp = temp.next

        return doubly_list[:-4]

    def get_reverse(self):
        if self.tail is None:
            return "Empty List"

        temp = self.tail
        doubly_list = ""

        while temp:
            doubly_list += f"{temp.value} -> "
            temp = temp.prev

        return doubly_list[:-4]

    def append(self, value):
        node = Node(value)

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

        self.leng += 1
        return True

    def prepend(self, value):
        node = Node(value)

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

        self.leng += 1
        return True

    def pop(self):
        if self.head is None:
            return None

        if self.tail.prev is None:
            temp = self.tail
            self.head = None
            self.tail = None
        else:
            temp = self.tail
            self.tail = temp.prev
            self.tail.next = None
            temp.prev = None

        self.leng -= 1
        return temp

    def pop_first(self):
        if self.head is None:
            return None

        if self.head.next is None:
            temp = self.head
            self.head = None
            self.tail = None
        else:
            temp = self.head
            self.head = temp.next
            self.head.prev = None
            temp.next = None

        self.leng -= 1
        return temp

    def get(self, index):
        if index < 0 or index >= self.leng:
            return None

        if index < self.leng/2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.leng-1, index, -1):
                temp = temp.prev

        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.leng:
            return False
        elif index == 0:
            return self.prepend(value)
        elif index == self.leng:
            return self.append(value)

        node = Node(value)
        before = self.get(index-1)
        after = before.next

        node.next = after
        node.prev = before
        before.next = node
        after.prev = node

        self.leng += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.leng:
            return False
        elif index == 0:
            return self.pop_first()
        elif index == self.leng-1:
            return self.pop()

        before = self.get(index-1)
        temp = before.next

        before.next = temp.next
        temp.next.prev = before
        temp.next = None
        temp.prev = None

        self.leng -= 1
        return temp
