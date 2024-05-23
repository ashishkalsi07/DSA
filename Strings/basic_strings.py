str1="ashish"
print(str1[2:5])          #string slicing
newstr1="".join(reversed(str1))                #reversing a string method 1
print(newstr1)

print(str1[::-1])                              #reversing a python string method 2

str1[0]='AK'                                   #Updating the charcter at 0th index
print(str1)


# string concatenation methods

str1='Ashish'
str2="Kalsi"
str3=str1 +" "+ str2
print(str3)


#as List same in python to delete any character , simply use del keyword then write string index
str1="Ashish"
del str1
print(str1)



# Q1-> replace character of a string
str1="Anmol"
str1=str1.replace(str1[0],"Kalsi")
print(str1)

# Q2-> count occurences of character in a string
test_str="AashishKalsi"    # a string
occurences={}    # an empty dictionary 
for i in test_str:
    if i in occurences:
        occurences[i] += 1
    else:
        occurences[i] = 1
print(occurences) 


from collections import Counter 
res=Counter(test_str)
print(res)


# Q3 ->Check if Strings are Anagrams silent = listen 
from collections import Counter
def anagrams(str1,str2):
    str1=str1.replace(" ","").lower()
    str2=str2.replace(" ","").lower()

    # return sorted(str1) == sorted(str2) # sort and compare the strings 
    # return Counter(str1) == Counter(str2) # Count the occurences of String characters 

print(anagrams("silent","listen"))




