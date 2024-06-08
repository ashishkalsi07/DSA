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


# This is basic implementation or how we can creata a tree using class 

'''    
         20 
    10        30
40     50  60     70
'''
# Tree we have created looks something like this above representation

'''
We have 3 different methods to traverse a tree 
In order ---> left - root - right 
pre order ---> root - left - right
post order ----> left - right - root
'''