#Session 10 Exception Handeling and File Handeling
#exception Handeling
#Example 1
print("This is starting point of program")
print("This is starting point of program")
print("This is starting point of program")
print("This is starting point of program")
try:
    print(x)
except:
    print("Exception occured")
    
print("This is end of program")
print("This is end of program")
print("This is end of program")
print("This is end of program") 
#Session 10 Exception Handeling and File Handeling
#exception Handeling
#Example 2
print("This is the starting point of program..")
print("Program in progress")
try:    
    print(10/0)
except ZeroDivisionError:
    print("Program completed..") 
print("Program completed")
# Example 3 :Multiple except blocks - try,except else, finally
try:
    num1,num2=10,5
    result=num1/num2
    print("result is",result)
except ZeroDivisionError:
    print("Thrown ZeroDivisionError Exception")
except SyntaxError:
    print("Thrown Syntax Error exception")
except:
    print("Exception handled")
else:
    print("No exceptions occured")
finally:
    print("always execute")
# Example4 : Raising our own exceptions
def enterage(num):
    if num<0:
        raise ValueError("Only Integers are allowed")
    if num%2==0:
        print("even")
    else:
        print("odd")
        
print("checking number is even or off by calling function..")
num=-1
try:
    enterage(num)
except ValueError:
    print("value error exception occured and handled...")
enterage(-1)
print("program completed..")
#File Handling / working with text
#Example 1 : Writing data in to text file 
file=open("C:\DemoFiles\myfile.txt",'w') # W is write mode , R is read mode, A is append mode
file.write("This is my first statement\n")
file.write("This is my first statement\n")
file.write("This is my first statement\n")
file.write("This is my first statement")
file.close()
print("program completed")
#Example 2: reading data from text file
file=open("C:\DemoFiles\myfiles.txt",'r')
print(file.read()) #all lines are printed
print(file.readline()) #only first line is printed
file.close()
#Example 3 - Appending Data into text file
file=open("C:\DemoFiles\myfiles.txt",'w')
file.write("this is my sixth line\n")
file.write("This is my seventh line\n")
file.close()
print("program is completed")
