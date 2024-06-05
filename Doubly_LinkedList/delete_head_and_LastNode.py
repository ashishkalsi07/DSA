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


def delete_headNode(head):
    if head == None:
        return None
    if head.next == None:
        return None
    else: 
        head=head.next
        head.prev=None
        return head

def delete_LastNode(head):
    curr=head
    
    while curr.next.next != None:
        curr=curr.next
    curr.next=None
    return head
    

printList(head)

head=delete_headNode(head)

printList(head)

head=delete_LastNode(head)

printList(head)

