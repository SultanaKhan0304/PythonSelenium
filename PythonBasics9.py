#Session 9
#Modules and Packages
#calculator.py
def add(num1,num2):
    print(num1+num2)
def mul(num1,num2):
    print(num1*num2)
#operations.py - created a new file /module
#Approach1
import calculator
calculator.add(100,200)
calculator.mul(10,20)
#Approach2 
from calculator import add,mul
add(100,200)
mul(10,20)
#Approach 3
from calculator import *
add(100,200)
mul(10,20 )
#animal.py - created a new file / module1
def fly():
    print("Animal cannot fly")
def color():
    print("Animal is black")

#bird.py - created a 2nd  file / module2
def fly():
    print("Animal cannot fly")
def color():
    print("Animal is black")
#animalbird.py - 3rd module is created 
# we will invoke the same functions of Module 1 and Module 2 from Module 3
#Approach 1 
import animal
import bird
animal.fly()
animal.color()
bird.fly()
bird.color()
#Approach 2
from animal import *
fly()
color()
from bird import *
fly()
color()
#a.py - Module 1
class Animal:
    def display(self):
        print("I like cow")
#b.py - Module 2
class Bird:
    def display(self):
        print("I like bird")
#ab.py - Module 3
#Approach 1
import a
import b
obj1=a.Animal() #Animal() class belongs to Module a
obj1.display()
obj2=b.Bird()
obj2.display()
#Approach 2 - Importing module name with function name
from a import Animal
from b import Bird 
obj1=Animal()
obj1.display()
obj2=Bird()
obj2.display()
#Packages - Collection of Modules 
#created a package with name - pack1
#created below modules inside the package pack1
#Module 1
def display():
    print("Display function from Module1")
#Module 2
def show():
    print("This is show function from Module2") 

#client.py
#Created new module client.py which is not part of package pack1 
#so we cannot directly import 
#Approach 1 - use sys.path to access the package and its modules
import sys
sys.path.append("Mention the complete path of package pack1")
import module1
import module2
module1.display()
module2.show()
#Approach 2 
from module1 import*
from module2 import*
display()
show()



