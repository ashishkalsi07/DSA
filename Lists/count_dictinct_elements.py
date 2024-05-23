# Q-> Count number of distinct elements or unique elements in a list
l=[1,2,3,1,4]
res=0
for i in range(0,len(l)):
    if l[i] not in l[0:i]:
        res += 1

print(res)


# More Efficient way is to convert it to a set and just find out length using length function 

def distinct(l):
    # s = set(l)
    # return len(s)
    return len(set(l))
print(distinct(l))


