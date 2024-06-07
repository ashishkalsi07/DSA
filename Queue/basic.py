# We can implement queue Data strcuture in many ways using different data structures or modules available in python 
# Method 1 - By using List []
q=[]
q.append(20)
q.append(40)
q.append(80)
q.append(100)
# consider append() as an enqueue operation  
print(q)
q.pop(0)
q.pop(0)
# consider pop(0) as dequeue operation where we are removing first element from queue. 
print(q)

# till here items added from rear and poped out from font. 
print(q[0]) # to get front item of queue
print(q[-1]) # to get rear item of queue

print("No of items in queue",len(q)) # No of items or length of the queue

# All operation except pop(0) are constant time operation while pop(0) - removing first item from list is Linear time complexity

# Method 2 - using deque

from collections import deque

q=deque()
q.append(20)
q.append(40)
q.append(80) # consider .append() as enqueue operation
print("Queue implementation using deque",q)

# remove last items
q.popleft()
q.popleft()
# consider popleft() as dequeue operation
print(q)
print("Size or no. of items in queue", len(q))
q.append(10)
q.append(400)
# get front
print("Front item is",q[0])

# get rear
print("Rear item is",q[-1])




