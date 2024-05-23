#1->Insert element at end of array/Lists:
a1=[1,2,3,4,10,5,6]
a1.append(100) # using method .append()
print(a1)

#2->Insert element at given index.
ele=int(input("Enter Element:"))
index=int(input("Enter Index:"))
a1.insert(index,ele)
print(a1) 

#3->List Delete and Shift.
del a1 
a1=[1,2,3,4,10,5,6]
print(a1) 

#4->Shift the List elements
n = int(input("Enter the number of shifts: "))

# Perform the left shifts
for _ in range(n):
    a1.append(a1.pop(0))

print(a1)
  
# Perform the right shifts
n = int(input("Enter the number of shifts: "))

# Perform the shifts to the right
for _ in range(n):
    a1.insert(0, a1.pop())

print(a1)
