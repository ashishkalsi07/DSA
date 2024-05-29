class Node:
    def __init__(self,key):
        self.key=key
        self.next=None

#Creating a Linked List
head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)

#Traverse a Linked List
def printList(head):
    curr=head
    while(curr != None):
        print(curr.key,end="->")
        curr=curr.next

#Insertion At Begining in a List
def InsertionatBegining(head,data):
    new_node=Node(data)
    new_node.next=head
    return new_node

#Insertion at Last Node in List
def insertatend(head,data):
    new_node=Node(data)
    curr=head
    while(curr.next != None):
        curr=curr.next
    curr.next=new_node

#Insert at Given Position
def givenpos(head,data,pos):
    new_node=Node(data)
    curr = head
    if pos == 1:
        new_node.next=head
        head=new_node
        return head
    for i in range(pos-2):
        curr=curr.next
        if curr == None:
            return head
    new_node.next=curr.next
    curr.next=new_node
    return new_node
        


# Calling all function here
print(printList(head))
head=InsertionatBegining(head,1000)
print(printList(head))
insertatend(head,2000)
print(printList(head))
givenpos(head,3000,3)
print(printList(head))