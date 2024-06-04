# Method 1 - linear Time implementation
class Node():
    def __init__(self,key):
        self.key=key
        self.next=None
        
head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)
head.next.next.next.next=head

def insertion_at_begining(head,key):
    curr=head
    while(curr.next != head):
        curr=curr.next
    new_node=Node(key)
    curr.next=new_node
    new_node.next=head
    return head

def printList(head):
    start = head
    while True:
        print(head.key, "->", end=" ")
        head = head.next
        if head == start:
            break
    print(head.key)  # To print the last element connecting to the start node


insertion_at_begining(head,100)
printList(head)


# Method 2 Constant Time Solution create a node between 1 and 2 node and swap the data between 1 and new node created - alternatively you will see that by swapping you have inserted the node in begining.

def bymethod2(head,key):
    newNode=Node(key)
    if head == None:  
        newNode.next=newNode
        return newNode
    else:
        newNode.next=head.next
        head.next=newNode
        head.key,newNode.key=newNode.key,head.key
        return head

bymethod2(head,400)
printList(head)