'''
Розширити структуру, яку побудували на уроці, можливістю вставки дерева в наявне дерево
та видалення піддерева з дерева, що існує.
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, root, value):
        if root is None:
            return Node(value)

        if value < root.value:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)
        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.value, end=' ')
            self.inorder(root.right)
            self.inorder(root.right)

    def insert_tree(self, other_root):
        if other_root is None:
            return

        def traverse(node):
            if node is None:
                return

            self.root = self.insert(self.root, node.value)
            traverse(node.left)
            traverse(node.right)

        traverse(other_root)

    def delete_subtree(self, root, value):
        if root is None:
            return None

        if root.value == value:
            return None

        root.left = self.delete_subtree(root.left, value)
        root.right = self.delete_subtree(root.right, value)

        return root