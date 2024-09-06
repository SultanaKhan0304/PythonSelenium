#Session 8
#Example 8
class MyClass:
    name="john" #declaring class variable
    def __init__(self,name): #constructor expecting one argument
        print(name)
        print(self.name) #accessing the class variable
mc=MyClass("David") #Passing parameter to the constructor
#Example 9
class Emp:   
    def __init__(self,eid,ename,sal):
        self.eid=eid
        self.ename=ename
        self.sal=sal
    def display(self):
        print(self.eid,self.ename,self.sal)     
e1=Emp(101,"John",5000)
e1.display()
e2=Emp(102,"Scott",7000)
e2.display()
#Example 10
class Emp:
    def __init__(self,eid,ename,sal):
        self.eid=eid
        self.ename=ename
        self.sal=sal
    def __str__(self): #Type of constructor to return string type of value
        return(self.ename)
e1=Emp(101,"John",5000)
print(e1)
#Inheritance
#Example1 
class A:
    def m1(self):
        print("this is m1 method from class A")
class B(A): # B is child class of A
    def m2(self):
        print("this is m2 method from class B")
bobj=B()
bobj. m1() #m1 is a method of class A , but acessible from Class B as it is the child
bobj.m2()
#Example 2 Single Inheritance
class A:
    x,y=10,20
    def m1(self):
        print(self.x+self.y)

class B(A):
    a,b=100,200
    def m2(self):
        print(self.a-self.b)
bobj=B()
bobj.m1()
bobj.m2()
#Example 3 Multilevel inheritance
class A:
    x,y=10,20
    def m1(self):
        print(self.x+self.y)
class B(A):
    a,b=100,200
    def m2(self):
        print(self.a-self.b)
class C(B):
    i,j=5,2
    def m3(self):
        print(self.i*self.j)
cobj=C() # Object of C will be able to access m1, m2,m3 
cobj.m1()
cobj.m2()
cobj.m3()
#Example 4 Hierarchy Inheritance
class A:
    x,y=10,20
    def m1(self):
        print(self.x+self.y)
class B(A):
    a,b=100,200
    def m2(self):
        print(self.a-self.b)
class C(A):
    i,j=5,2
    def m3(self):
        print(self.i*self.j)
bobj=B() # can only access Class A and Class B
bobj.m1()
bobj.m2()
cobj=C() # can only access class A aand Class C
cobj.m1()
cobj.m3()
#Example 5 Multiple Inheritance - 2 parents for 1 child class
class A:
    x,y=10,20
    def m1(self):
        print(self.x+self.y)
class B:
    a,b=100,200
    def m2(self):
        print(self.a-self.b)
class C(A,B): #Child of Class A and Class B
    i,j=5,2
    def m3(self):
        print(self.i*self.j)
cobj=C() # can  access class A , Class B, Class C
cobj.m1()
cobj.m2()
cobj.m3()
