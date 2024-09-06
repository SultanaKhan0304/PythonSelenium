#Session 7 - OOPs concepts in Python
# Class and Objects 
#Example 1 
class MyClass:
    def myfun(self): # function created inside a class can be called as Method
        pass # this is none
    def display(self,name):
        print(name)
mc1=MyClass() #Object creation
mc1.myfun() #calling the fucntion
mc1.display("scott")
#Example2 - 
class MyClass:
    def m1(self):  # Instance method is invoked using object only
        print("This is instance method")
    @staticmethod # we can invoke by class directly, object not needed
    def m2(self,num):
        print(self,num)
mc=MyClass() #Object creation
mc.m1() #calling the method using object
MyClass.m2(100,200) # calling the static method directly without using object
#Example 3 :
class MyClass:
    a,b=10,20 #Class variables as they are created inside the class
    def add(self):
        print(self.a+self.b) # we cannot access the variables a,b directly inside the method, hence we are using self to acess those variables .
    def mul(self):
        print(self.a*self.b)
mc=MyClass() #Object creation
mc.add() #invoking the methods using object
mc.mul() 
# Example 4
i,j=15,25 #global variables
class MyClass:
    a,b=10,20 #class variables 
    def add(self,x,y): #x,y are local variables
        print(x+y) # x,y are local variables
        print(self.a+self.b) #accessing class variables 
        print(i+j) #easily accessible global variables
mc=MyClass() #creating an object
mc.add(100,200) #invoking the method
# Example 5 - How to access global variable if variable name is same ?
a,b=15,25 #global variables
class MyClass:
    a,b=10,20 #class variables 
    def add(self,a,b): #a,b are local variables
        print(a+b) # a,b are local variables
        print(self.a+self.b) #accessing class variables 
        print(globals()['a']+globals()['b']) # accessing global variables 
mc=MyClass() #creating an object
mc.add(100,200) #invoking the method
#Example 6 - creating multiple objects for one single class
class MyClass():
    def display(self):
        print("This is display method")
obj1=MyClass()
obj1.display()
obj2=MyClass()
obj2.display()
#Example 7 : Constructor 
class MyClass:
    def __init__(self): #Constructor
        print("This is constructor..")
    def m1(self):
        print("Hello")
    def m2(self,x,y):
        return(x+y)
mc=MyClass() #Object is created. No need to call using the object to invoke constructor
mc.m1() # however, method will need to be invoked using an object
print(mc.m2(10,20))
