class Node:
    def __init__(self,key):
        self.key=key
        self.next=None

head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)
head.next.next.next.next=head


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

def deletion_at_front(head):
    curr=head
    while(curr.next != head):
        curr=curr.next
    curr.next=head.next
    head=head.next
    return head

def delete_kTh_node(head,k):
    curr=head
    for i in range(k-2):
        curr=curr.next
    curr.next=curr.next.next
    return head
    
printList(head)

head=deletion_at_front(head)

printList(head)

head=delete_kTh_node(head,3)

printList(head)