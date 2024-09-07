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

