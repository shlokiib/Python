class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert_bst(root, data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insert_bst(root.left, data)
    else:
        root.right = insert_bst(root.right, data)
    return root

def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.data, end=' ')
        inorder_traversal(node.right)

def mirror(node):
    if node:
        mirror(node.right)
        print(node.data,end =' ')
        mirror(node.left)

arr = [50, 30, 70, 20, 40, 60, 80]


root = None
for val in arr:
    root = insert_bst(root, val)

print("BST :")
inorder_traversal(root)
print()
print(mirror(root))
