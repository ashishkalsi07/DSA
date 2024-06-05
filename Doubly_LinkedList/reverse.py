class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
        self.prev = None

# Initialize the doubly linked list
head = Node(10)
second = Node(20)
third = Node(30)
head.next = second
second.prev = head
second.next = third
third.prev = second

def printList(head):
    curr = head
    while curr is not None:
        print(curr.key, "<->", end=" ")
        curr = curr.next
    print("None")

def reverseList(head):
    curr = head
    prev = None
    while curr is not None:
        # Swap the next and prev pointers
        curr.next, curr.prev = curr.prev, curr.next
        # Move prev to the current node
        prev = curr
        # Move to the next node (which is the original prev node)
        curr = curr.prev
    # Return the new head (the original tail)
    return prev

print("Original list:")
printList(head)

head = reverseList(head)

print("Reversed list:")
printList(head)
