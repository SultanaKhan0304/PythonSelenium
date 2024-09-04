#Session 2 
# Deleting Variables
r=2
s=1
del r # Deleting the variable r
# print (r) NameError: name 'r' is not defined
# print(s)  It will fail to run this line

#Operators
#Arithmetic Operators
a=5
b=2
add=a+b
print(add)
print(a+b)
print(a-b)
print(a*b)
print(a/b) 
print(a//b) #Returns Quotient value
print(a%b) # Returns Remainder value
print(a**b) # Returns Exponential value

#Relational Operators / comparison operators
#Always returns boolean value True/False
c=5
d=10
print(c>d)
print(c<d)
print(c==d)
print(c!=d)
print(c>=d)

#Logical Operators
# and or not - use alongwith boolean values
a=True
b=False
print(a and b)
print (a or b)
print (not a)

#Concatenation +

print(10+10)
print(10.5+12.0)
print(10+10.5)
print('welcome'+'python')
print(True+5) # Default value of True is 1
print(False+5) # Default value of False is 0
print(True+True)
# print(10+'welcome') - Not valid as both the values are of different data type
# print(True+'Welcome') - This is not valid too as both the values are of different data type
# We cannot concatenate different type of data types directly
#Approach1 for printing the values
name,age,sal="John",30,5000.50
print(name,age,sal) 
#Approach2 for printing the values
print( "Name is",name)
print ("Age is",age)
print("Salary is",sal)
#Approach3 for printing the values
print("Name is %s. Age is %d . Salary is %g" %(name,age,sal))
#Approach4 {} - using the format function to print the values
print("Name is {}. Age is {} . Salary is {}" .format(name,age,sal))
 #Taking Input from user 
#approach1
num1=int (input("Enter the First number"))
num2=int (input("Enter the second Number"))
print(type(num1))
print(type(num2))
#  If we are passing the values through console window at runtime, it will consider num1 and num2 as string , hence we specify the int type .
print(num1+num2)
#Approach 2
num3= input("Enter the first number")
num4= input("Enter the second number")
print (int(num3)+int(num4))

# Control statements
# 1. Conditional statements
#if if..else elif
#Example 1
age=15
if age>=18:
    print("Eligible  for vote")
else:
    print("Not Eligible for vote")

# Example 2
if True:
    print("true condition")
else:
    print("false condition")
    
# Example 3
if 1:
    print("one")
else:
    print("Not one")

# Example 4
num=10
if num%2==0:
    print("Even Number")
else:
    print("Odd Number")

#Example5 Ternary operator
num=10
print("Even Number") if num%2==0 else print("Odd number")

#Example 6 Multiple statements in a single line using Curly braces
a=20
{print("Hello"), print("python")} if a>=10 else {print("hi"), print("java")}

# Example 7 Multiple conditions can be handles using elif statement

weekno=4
if weekno==1:
    print("Sunday")
elif weekno==2:
    print("Monday")
elif weekno==3:
    print("tuesday")
elif weekno==4:
    print("Wednesday")
elif weekno==5:
    print("Thursday")
elif weekno==6:
    print("Friday")
elif weekno==7:
    print("Saturday")
else:
    print("Invalid week number") 
