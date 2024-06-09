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
root.left.left.left=Node(1000)
# Height of B.Tree = maximum number of nodes from leaf to root of Tree


def height(root):
    if root == None:
        return 0  # you can replace 0 with -1 if dont want to consider the root node for height 
    if root is not None:
        return max(height(root.left),height(root.right)) + 1
        # lh=height(root.left)
        # rh=height(root.right)
        # return max(lh,rh) + 1    

print(height(root)) 


