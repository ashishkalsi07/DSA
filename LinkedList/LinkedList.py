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

#Now Searching within a Linked List
def search_List(head,ele):
    curr=head
    pos=1
    while(curr != None):
        if(curr.key == ele):
            print("Key Found in List at Position",pos)
            return
        curr=curr.next
        pos=pos+1
    print("Not Found in List")


# Calling all function here
print(printList(head))
# print()    #New Line Separator is required when we are not printing the last address - None
search_List(head,30)