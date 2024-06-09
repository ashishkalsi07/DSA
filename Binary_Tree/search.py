class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Constructing the binary tree
root = Node(20)
root.left = Node(10)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.left = Node(60)
root.right.right = Node(70)

def search(root, x):
    if root is None:
        return False
    if root.key == x:
        return True
    # Recursively search in the left and right subtrees
    return search(root.left, x) or search(root.right, x)

# Test the search function
print(search(root, 20))  # Output: True
print(search(root, 25))  # Output: False
