class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def maximum(root):
    if root is None:
        return float('-inf')
    else:
        lm = maximum(root.left)
        rm = maximum(root.right)
        root_key = root.key
        final = max(root_key, lm, rm)
        return final

# Define the tree structure
root = Node(20)
root.left = Node(10)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.left = Node(60)
root.right.right = Node(70)

# Find and print the maximum node key value
res = maximum(root)
print(res)
