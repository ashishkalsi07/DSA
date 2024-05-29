class Node:
    def __init__(self,key):
        self.key=key
        self.next=None

head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)

# Print the list
def printList(head):
    curr=head
    while(curr != None):
        print(curr.key,end="->")
        curr=curr.next

# Deletion First Node
def delete_first_node(head):
    curr=head
    head=curr.next
    return head

# Deletion  last node
def delete_last_node(head):
    curr=head
    while(curr != None):
        if(curr.next.next == None):
            curr.next = None
        curr=curr.next
    return head

# Deletion by node position
def delete_node_bypos(head,pos):
    curr=head
    for i in range(pos-1):
        curr=curr.next

printList(head)
head=delete_first_node(head)
print()
printList(head)
head=delete_last_node(head)
print()
printList(head)
# delete_node_bypos(head,3)