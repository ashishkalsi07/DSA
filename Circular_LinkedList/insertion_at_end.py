class Node:
    def __init__(self,key):
        self.next=None
        self.key=key

head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=head



def insertatend(head,key):
    new_Node=Node(key)
    curr=head
    while(curr.next != head):
        curr=curr.next
    new_Node.next=head
    curr.next=new_Node
    return new_Node

head=insertatend(head,100)

def printList(head):
    if head is None:
        return
    curr = head
    while True:
        print(curr.key, "->", end=" ")
        curr = curr.next
        if curr == head:
            break
    print()
    
printList(head)