class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

Root = Node(40)
Root.left = Node(30)
Root.left.left = Node(20)
Root.left.right = Node(35)
Root.right = Node(50)
Root.right.left = Node(45)
Root.right.right = Node(60)
Root.right.right.right = Node(100)
Root.right.right.right.right = Node(150)

def insert(root, x):
    if root is None:
        return Node(x)
    elif root.key == x:
        return root
    elif root.key > x:
        root.left = insert(root.left, x)
    else:
        root.right = insert(root.right, x)
    return root

Root = insert(Root, 55)

# To verify the insertion, you might want to print the tree in some form, for example using in-order traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=' ')
        inorder(root.right)

# Printing the tree in in-order to verify the insertion of 55
inorder(Root)
