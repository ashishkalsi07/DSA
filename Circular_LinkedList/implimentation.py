class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

# Creating the linked list
head = Node(10)
head.next = Node(12)
head.next.next = Node(14)
head.next.next.next = Node(16)
head.next.next.next.next = head  # Create the cycle

def printList(head):
    start = head
    while True:
        print(head.key, "->", end=" ")
        head = head.next
        if head == start:
            break
    print(head.key)  # To print the last element connecting to the start node

printList(head)
