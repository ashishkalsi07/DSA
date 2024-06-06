# We can implement stack in python through number of ways like
'''
1. By using List [] Data structure
2. By using Deque from collections
3. By creating a Linked List implementation of stack class and design all function for operations
'''
# *************************************************************Method_1*********************************************
from collections import deque
stack = deque()
stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)
# append func. add items from top inside the sstack or push items into the stack
print("My stack items are",stack)

stack.pop()
stack.pop()
# pop func remove last inserted / appended items in stack 
print("My stack items are",stack)
stack.append(25)
print("My stack items are",stack)
size=len(stack)
print("No of items in my Stack is",size)

# ************************************************************Method_2************************************************************
print("List Implementation of Stack")
stack=[]
stack.append(20)
stack.append(10)
stack.append(50)
stack.append(40)
stack.append(30)
print(stack)

stack.pop()
stack.pop()

print(stack)

size=len(stack)
print(size)

# *********************************************************Method_3**************************************************************
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class MyStack:
    def __init__(self):
        self.head=None
        self.size=1


    def push(self,x):
        temp=Node(x)
        temp.next=self.head
        self.head=temp
        self.size=self.size + 1

    def size(self):
        return self.size()
    
    def peek(self):
        return self.head.data
        
s=MyStack()
s.push(30)
s.push(40)
s.push(50)
s.push(500)
s.push(90)
print("Size of my Stack is",s.size)

