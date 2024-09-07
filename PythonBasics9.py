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




