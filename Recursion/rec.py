
#Direct Recursion
def func():
    print("Triggered")  
    func()

func()   # calling here 

#Indirect Recursion Code
def func1():
    print("Func 1 called")
    func2()

def func2():
    print("Func 2 called")

print("Before Func 1")
func1()
print("After Func 1")


#In python there is function call stack and it come with an limit such that no memory related erros came afterwards


# Ques -> Print your name 4 times
def print_name(Pname,count):
    if count == 0:
        return
    else:
        print(Pname)
        print_name(Pname,count-1)

print_name("Your Name here",4)
