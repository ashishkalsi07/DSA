class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None

root=Node(20)
root.left=Node(10)
root.right=Node(30)
root.left.left=Node(40)
root.left.right=Node(50)
root.right.left=Node(60)
root.right.right=Node(70)

# pre order ---> root - left - right
def preorder(root):
    if root != None:
        print(root.key)
        preorder(root.left)
        preorder(root.right)
        
    

preorder(root)