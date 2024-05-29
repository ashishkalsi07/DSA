#Single Linked List:
class Node:
    def __init__(self,key):
        self.key=key
        self.next=None

#Creating a Linked List
head=Node(10)
head.next=Node(20)
head.next.next=Node(30)

#Traverse a Linked List
def printList(head):
    curr=head
    while(curr != None):
        print(curr.key,end="->")
        curr=curr.next

# Reverse a Linked List
def reverse_a_List(head):
    curr=head
    prev=None
    while curr is not None:
        next=curr.next
        curr.next=prev
        prev=curr
        curr=next
    return prev



printList(head)
head=reverse_a_List(head)
print()
printList(head)
