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
        print(curr.key,"<->",end=" ")
        curr=curr.next
    print()

def insertion_at_front(head):
    new_node=Node(100)
    head.prev=new_node
    new_node.next=head
    head=new_node
    return head

def insertion_at_end(head):
    new_node=Node(1000)
    if head == None:
        return new_node
    else:
        curr=head
        while(curr.next != None):
            curr=curr.next
        curr.next=new_node
        new_node.prev=curr
        return head



printList(head)

head=insertion_at_front(head)

printList(head)

head=insertion_at_end(head)

printList(head)