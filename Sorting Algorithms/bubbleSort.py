# compare the adjacents elements
# Flow
# first pass move the largets element to the last positon 
# in second pass move the second largest element to the second last position ... 

l=[10,4,5,9]
def bubble_sort(l):
    n=len(l)
    for i in range(n-1):
        for j in range(n-i-1):
            if(l[j] > l[j+1]):
                l[j],l[j+1]=l[j+1],l[j]

bubble_sort(l)
print(l)

