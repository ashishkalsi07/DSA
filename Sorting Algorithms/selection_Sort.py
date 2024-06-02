# basic one 
# comparison based algorithm
# in - place algorithm
# not that much stable
# heap sort foundation

# flow - find out the minimum element and put it at first posiion 
# find out the second minimum element and put it at second position

l=[2,1,3,5,4,6]
def selection_sort(l):
    n=len(l)
    for i in range(n-1):
        min_index=i
        for j in range(i+1,n):
            if l[j] < l[min_index]:
                min_index=j
        l[min_index],l[i]=l[i],l[min_index]

selection_sort(l)
print(l)    