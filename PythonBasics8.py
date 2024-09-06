#Session 8
#Example 8
class MyClass:
    name="john" #declaring class variable
    def __init__(self,name): #constructor expecting one argument
        print(name)
        print(self.name) #accessing the class variable
mc=MyClass("David") #Passing parameter to the constructor
