class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree:
    def __init__(self, root):
        self.root = root

    def search(self, val):
        return self._search(self.root, val)

    def _search(self, node, val):
        if node is None:
            return None

        if node.val == val:
            return node

        if val < node.val:
            return self._search(node.left, val)

        return self._search(node.right, val)

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
            return

        self._insert(self.root, val)

    def _insert(self, node, val):
        if val > node.val:
            if node.right is None:
                node.right = Node(val)
            else:
                self._insert(node.right, val)
        elif val < node.val:
            if node.left is None:
                node.left = Node(val)
            else:
                self._insert(node.left, val)
        elif val == node.val:
            return

    def traverse(self):
        self._traverse(self.root)

    def _traverse(self, node):
        """Inorder traversal
        """
        if node is None:
            return
        self._traverse(node.left)
        print(node.val)
        self._traverse(node.right)




n_4 = Node(4)
n_11 = Node(11)
n_10 = Node(10, n_4, n_11)

n_30 = Node(30)
n_40 = Node(40)
n_33 = Node(33, n_30, n_40)

n_52 = Node(52)
n_61 = Node(61)
n_56 = Node(56, n_52, n_61)

n_82 = Node(82)
n_95 = Node(95)
n_89 = Node(89, n_82, n_95)

n_25 = Node(25, n_10, n_33)
n_75 = Node(75, n_56, n_89)

root = Node(50, n_25, n_75)

tree = Tree(root)
# print(tree.search(51))
# print(tree.search(75))

tree.traverse()