class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return

        self._insert_aux(self.root, value)

    def _insert_aux(self, root, value):
        if root.left is None and value < root.value:
            root.left = Node(value)
            return

        elif root.right is None and value >= root.value:
            root.right = Node(value)
            return

        if value < root.value:
            self._insert_aux(root.left, value)
        else:
            self._insert_aux(root.right, value)

    def display(self, method="inorder"):
        if method == "inorder":
            self._traverse_inorder(self.root)

        elif method == "preorder":
            self._traverse_preorder(self.root)

        elif method == "postorder":
            self._traverse_postorder(self.root)

        elif method == "level_order":
            self._traverse_level_order(self.root)

        print()

    def _traverse_inorder(self, root):
        """[left, root, right] -> return data in ascending order"""
        if root:
            self._traverse_inorder(root.left)
            print(root.value, end=" ")
            self._traverse_inorder(root.right)

    def _traverse_preorder(self, root):
        """[root, left, right]"""
        if root:
            print(root.value, end=" ")
            self._traverse_preorder(root.left)
            self._traverse_preorder(root.right)

    def _traverse_postorder(self, root):
        """[left, right, root]"""
        if root:
            self._traverse_postorder(root.left)
            self._traverse_postorder(root.right)
            print(root.value, end=" ")

    def _traverse_level_order(self, root):
        queue = [root]

        while len(queue) != 0:
            node = queue.pop(0)
            print(node.value, end=" ")

            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)

    def height(self):
        if self.root is None:
            return -1
        return self._height_aux(self.root)

    def _height_aux(self, root):
        if root is None:
            return -1

        return max(
            self._height_aux(root.left),
            self._height_aux(root.right),
        ) + 1

    def find_min(self):
        return self._min_aux(self.root)

    def _min_aux(self, root):
        if root.left is None:
            return root.value

        return self._min_aux(root.left)

    def find_max(self):
        return self._max_aux(self.root)

    def _max_aux(self, root):
        if root.right is None:
            return root.value

        return self._max_aux(root.right)
