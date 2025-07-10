class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        def _insert(node, data):
            if not node:
                return Node(data)
            if data < node.data:
                node.left = _insert(node.left, data)
            else:
                node.right = _insert(node.right, data)
            return node
        self.root = _insert(self.root, data)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=' ')

tree = BinaryTree()
values = [10, 5, 15, 3, 7, 18]  
for val in values:
    tree.insert(val)

print("Post-order Traversal:")
tree.postorder(tree.root)
