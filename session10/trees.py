from collections import deque

class Node:
    def __init__(self, data):  
        self.data = data
        self.right = None
        self.left = None

def build_tree(arr):
    index = -1
    def build():
        nonlocal index
        index += 1
        if index >= len(arr) or arr[index] == -1:
            return None
        node = Node(arr[index])
        node.left = build()
        node.right = build()
        return node
    return build()
    
def Pre_Order_Traversal(root):
    if root is None:
        return
    print(root.data, end=" ")
    Pre_Order_Traversal(root.left)
    Pre_Order_Traversal(root.right)

def Level(node):
    result = []
    if not node:
        return result
    queue = deque()
    queue.append(node)
    while queue:
        e = queue.popleft()
        result.append(e.data)
        if e.left:
            queue.append(e.left)
        if e.right:
            queue.append(e.right)
    return result        




arr = [1, 2, -1, -1, 3, 8, -1, -1, 5, -1, 6,-1,-1]
root = build_tree(arr)

print("Pre-order Traversal:")
Pre_Order_Traversal(root)

print("\nLevel Order Traversal:")
print(Level(root))  