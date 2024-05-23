# Q1 Sum of Natural Numbers
def natural_sum(num):
    count = 0
    sum = 0
    while(count <= num):
        sum = sum + count
        count=count+1
    return sum

    return num*(num+1)/2

print(natural_sum(3))

# l=[10,20,"gfg",40,True] - any data type
# List provides us Randome Access of elements
# Insertion , Deletion , Search are very slow in Python

# Question 1  Avg or Mean of a List.
l=[10,20,30,40]
def avg_of_list(l):
    sum = 0
    for i in l:
        sum += i
    return (sum/len(l))

print(avg_of_list(l))

# Q2 Separate Even and odd : Return 2 list even_no & odd_no

l=[10,15,22,1,4,7,98,3,6,33,11]
def separate(l):
    eve=[]
    odd=[]
    for i in l:
        if (i % 2) != 0:
            eve.append(i)
        else:
            odd.append(i)
    
    eve.sort()
    odd.sort()

    return (eve,odd)

eve,odd=separate(l)
print(eve,odd)

# Q3 Return list of small elements of given number
l=[1,2,3,4,5,6]

def ques3(l,num):
    small=[]
    for i in l:
        if( i < num):
            small.append(i)

    return small        
print(ques3(l,5))

****Slicing = [start:stop:jump]

l=[10,20,30,40,50,60]
print(l[0:3:2])
print(l[::-1])    # print in reverse order
l=[1,2,3,4,5,6]
l2=l[:]   #copy one list to other

print(l2) 

***List Comprehension in python
 
leve=[x for x in range(11)if x % 2 == 0]
lodd=[x for x in range(11)if x % 2 != 0]
print(leve,lodd)

def getsmaller(l,num):
    return [x for x in l if x < num ]

l=[1,2,3,4,5,6]
print(getsmaller(l,5))


# Q: WAP that takes lists as input and returns the largest element of list

l=[13,2,5,60,50,90]
def largest_element(l):
    res=l[0]
    for i in l:
        if i > res:
            res=i
    return res

print(largest_element(l))

# Q: WAP that takes lists as input and returns the second largest element of list

l=[13,2,5,60,50,90]
def _2largest_element(l):
    res=l[0]
    for i in l:
        if i > res:
            second=res
            res=i
    return second

print(_2largest_element(l))

# Q:Find only odd lements in list 
l=[12,3,4,56,10]
lodd=[x for x in l if x % 2!= 0 ]
print(lodd)

# Q: Rotate a List by 1 in left direction
l=[10,20,30,1,2,23]
l.append(l.pop(0))    #Method 1 
print(l)

l=[1,2,3,5,6,4]
l=l[1:]+l[0:1]     #Method 2
print(l)

# Q: Rotate a list by d times
l=[1,2,3,4,5,6,7,8,9]
d=3                       #Method 1
l=l[d:]+l[0:d]
print(l)


l=[1,2,3,4,5,6]
d=2
def rotateby_d(l,d):
    for i in range(0,d):
        l.append(l.pop(0))

rotateby_d(l,d)
print(l)
