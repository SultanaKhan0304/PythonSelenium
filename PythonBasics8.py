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
        
