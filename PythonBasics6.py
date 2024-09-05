#Session 6
#Functions
#Example1
def myfun():
    print("hello")
myfun() #Calling the function
#Example2 - Passing arguments in the function
def myfun(name):
    print("Hello",name)
myfun("Sultana")
#Example 3
def cal(a,b):
    return(a+b)
sum=cal(10,20)
print(sum)
print(cal(10,20)) #alternate method
#Example 4 
def func():
    return
func() #None
#Example 5:
def cal(a,b):
    print(a+b)
  cal(10,20)
#Example1 - global and local variable
global_var=20 #declared as a global variable
def func():
        local_var=10
        global_var=20 #This is a local variable here as it is declared inside the function
        print(local_var)
        print(global_var)
func()
print(local_var) # Invlaid as we are trying to access the local varibale outside the function
print(global_var)
#Example 2 :
xy=100 #global variable
def cool():
    xy=200 #local variable
    print(xy)
cool()
#Example 3 : Using Global variable and updating it's value as a local variable
xy=100 #global variable
def cool():
    global xy #local variable
    xy=200
    print(xy)
cool()
#Example 4 :
def cool():
    global x
    x=100
    print(x)
cool()
print(x) #able to access x bcoz it is a global variable
#Example 1 
def func(i,j):
    print(i,j)
func(10,20) #Positional arguments
func(j=20,i=10) #explicitly mentioning the value of arguments - Keyword arguments 
#Example 2  : default values assigned to positional arguments
def func(i,j=10):
    print(i,j) # Will print output 100 200
func(100,200)
#Example 3 : Keyword arguments
def greetings(name,greetmsg):
    print(greetmsg+" "+name)
greetings(name='John',greetmsg="Hello")
#Example 4 
def myfunc(a,b,c):
    print(a,b,c)
myfunc(10,20,30) #positional parameters
myfunc(b=20,a=10,c=30) #Keyword arguments
myfunc(10,20,c=30) # combination of positional and keyword arguments
myfunc(10,b=20,c=30) 
myfunc(10,b=20,30)#This is wrong as postional argument must appear before any keyword argument
#Example 5
def largest(a,b):
    if a>b:
        return a,b 
    else:
        return b,a
          
print(largest(100,200))
print(largest(20,10))

res=largest(10,20)
print(res)
print((type(res)))
