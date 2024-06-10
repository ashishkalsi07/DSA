# Binary Search Tree is tree with following structure
# smallest key - left most child
# greatest key right most child

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

# This tree will look like this
'''
              40
        30          50
    20      35  45      60
                            100
                                  150          
              
observe for s tree , small child is on left side and right child is on Right side               
              
              
              
'''

def search_key(root, x):
    if root is None:
        return False
    if root.key == x:
        return True
    elif x > root.key:
        return search_key(root.right, x)
    else:
        return search_key(root.left, x)

# To check if the key exists in the tree
result = search_key(Root, 500)
print(result)
