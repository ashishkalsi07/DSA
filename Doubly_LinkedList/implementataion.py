class  Node:
    def __init__(self,key):
        self.key=key
        self.next=None
        self.prev=None

head=Node(10)
second=Node(20)
third=Node(30)
head.next=second
second.next=third
second.prev=head

def printList(head):
    curr=head
    while(curr is not None):
        print(curr.key,"->",end=" ")
        curr=curr.next
    print()
    
printList(head)