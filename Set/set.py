'''
# Set is another Data Structure in Python which stores 
-distinct elements 
-unordered 
-No Indexing 
-Union, Intersection, Searching is very fast because internally it use Hashing

s1={10,20,30}
print(type(s1))

s={}    # this does not create any empty set ,it creates an empty dictionary so better write this way

set1=set()
print(type(set1))   # now here we have created a set using set object 

some function are update() add()
'''
s1={1,2,3,4,5}
s1.add(10)
print(s1)

s1.update([100])    #does not work with set hence it is used to update set from other data structure like list
print(s1)


# some functions - add(),clear(),discard(),remove() 
# discard simply removes the item from set if present in set but remove raise error if we provide the item that is not in set
# we can also perform like operations like Union, Intersection, difference between two sets .
s2={4,5,6}
print(s1 | s2)   # union of two sets
print(s1 - s2)  # or it can written as print(s1.differnce(s2))
#print(s1.difference(s2))

