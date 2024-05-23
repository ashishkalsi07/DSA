#stores element as key:value pair . keys should be unique and value might be same . dictionary uses hashing internally
s={101:"abc",102:"def",104:"106"}
print(s)
s[100]='ash'   #add / insert new key:value pair in dictionary
print(len(s)) #prints number of key:values pair in a dictionary
s.pop(101)    
print(s)

del s[102]    # it delete the key:value pair from dictionary

s.popitem()    #removes last key:value pair
print(s)