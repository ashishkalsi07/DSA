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


# size is number of nodes in tree
def size(root):
    if root == None:
        return 0
    else:
        return 1 + size(root.left) + size(root.right)
        '''
        ls = size(root.left)   # both works same way it just one line of code is preffered.
        rs = sie(root.right)
        return ls + rs + 1
        '''

value=size(root)
print(value)