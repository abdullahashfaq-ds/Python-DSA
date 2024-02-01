class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.leng = 0

    def __str__(self):
        if self.head is None:
            return "Empty list"

        temp = self.head
        linked_list = ""

        while temp:
            linked_list += f"{temp.value} -> "
            temp = temp.next

        return linked_list[:-4]

    def append(self, value):
        node = Node(value)

        if self.head is None:
            self.head = node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = node

        self.leng += 1
        return True

    def prepend(self, value):
        node = Node(value)

        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

        self.leng += 1
        return True

    def pop(self):
        if self.head is None:
            return None

        if self.head.next is None:
            temp = self.head
            self.head = None
        else:
            pre, temp = None, self.head
            while temp.next:
                pre = temp
                temp = temp.next

            pre.next = None

        self.leng -= 1
        return temp

    def pop_first(self):
        if self.head is None:
            return None

        if self.head.next is None:
            temp = self.head
            self.head = None
        else:
            temp = self.head
            self.head = temp.next
            temp.next = None

        self.leng -= 1
        return temp

    def get(self, index):
        if index < 0 or index >= self.leng:
            return None

        temp = self.head
        for _ in range(index):
            temp = temp.next
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

        temp = self.get(index-1)
        new_node = Node(value)
        new_node.next = temp.next
        temp.next = new_node

        self.leng += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.leng:
            return False
        elif index == 0:
            return self.pop_first()
        elif index == self.leng-1:
            return self.pop()

        pre = self.get(index-1)
        temp = pre.next

        pre.next = temp.next
        temp.next = None

        self.leng -= 1
        return temp

    def reverse(self):
        pre = None
        temp = self.head

        while temp:
            after = temp.next
            temp.next = pre
            pre = temp
            temp = after

        self.head = pre
