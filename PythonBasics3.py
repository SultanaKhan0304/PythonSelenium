# Session 3
# Control statements
# 2. Looping Statements

# range() function in python . range(10) or range(1,10)
# range(1,10,2) -  1 is starting point, 10 is ending point, 2 is increment 

# Example 1
print(range(10)) # this will only print range range(0, 10)
print (list(range(10))) #This will print the values of the range [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print (list(range(5,10))) # it will print till 9 , as it considers N-1 value [5, 6, 7, 8, 9]
print (list(range(1,10,2)))  # 2 will increment values by 2, prints odd numbers [1, 3, 5, 7, 9]
print(list(range(2,10,2))) #Prints even numbers [2, 4, 6, 8]
print (list(range(10,1,-1))) # This will print [10, 9, 8, 7, 6, 5, 4, 3, 2]
print(list(range(-10,-5))) # This will print [-10, -9, -8, -7, -6]

#While Loop

print 1....10 numbers 
i=1 
while i<=10:
    print(i)
    i=i+1
 print("Done!!")
    
# print 1 to 10 numbers in descending order 
i=10
while i>=1:
    print(i)
    i=i-1
print("Done!!")

# Print 1..10 numbers using For Loop

for i in range(10):
    print(i)
    
for i in range(1,11):
    print(i)
    
    #Print only even number between 1 to 20
    
for i in range(0,21,2): # Starts with 0, ends with 20 and increments by 2 
    print(i)

#Print only odd numbers between 1 to 20
for i in range(1,21,2):
    print(i)
    
 #Print numbers in descending order 
 
for i in range(10,0,-1):
    print(i)

#Print only multiples of 5 between 5 to 100
for i in range (5,101,5):
    print(i)

# Jumping statements - Break , continue 
for i in range(1,10):
    if i==5: # this will skip 5
        continue
    print(i)
print("prgram exited !!")

for i in range(1,10):
    if i==3 or i==5 or i==7: # This will skip 3,5,7
        continue
    print(i)
for i in range(3,7,2):
    print(i)
    
#Numbers and strings 
num1=100;
print(type(num1))
num2=10.5
print(type(num2))
print(max(10,20,30)) #max() function will return the highest number
print(min(10,20,30)) # min() function returns smallest value

#String Functions
s="welcome"
s='welcome'
s=str('welcome')
s=str("welcome")
name= str()
# Creating empty string variables
name=""
name=''
name=str()
#mutable - cannot change the value of the variable 
#immutable - can change the value of the variable
# string is immutable
str1="welcome"
print(id(str1)) # This will print the id or value of the memory where str1 is stored -> 133672711203440
str1=str1+" to python"
print(id(str1)) #133672711203440
print(str1)  
#Slicing operators 
#Starting index 0
#Ending index 1
str="welcome"
print (str[1:3]) #This will print el , as these are the values on index 1 and 2
print(str[:6]) #This will print welcom, as these are the values on index 0 to 5
print(str[2:]) #This will print lcome , as these are the values on index 2 to 5
print(str[1:-1]) # This will print elcom, as these are the values on index 1 . -1 will remove the last character.
print(str[1:-2]) # This will print elcom, as these are the values on index 1 . -1 will remove the last 2 character.
# Example 5 : ord() and chr()
print(ord('A')) # this will print the ASCII code of the given character
print(chr(65)) # this will print the character
# Example 6 : max() min() len()
print(max("abc")) #c
print(min("abc")) #a
print(len("welcome")) #7
# Example 7: in not in operators - trturns True/ False
s= "welcome"
print("come" in s) #True
print("lome"in s) #False
print("come" not in s) #False
print("lome"not in s) #True
# Example 8: String Comparison
print ("tim"== "tie")
print("free" != "freedom")
print("arrow"> "aron")
print("right">= "left")
print("teeth"<"tee")
print("yellow"<="fellow")
print("abc">"")
#Example 9 - Testing strings True/False
s="welcome to python"
print(s.isalnum()) # checks if the string contains number
#Example 9 - Testing strings True/False
s="welcome to python"
print(s.isalnum()) # checks if the string contains number
print("welcome".isalpha()) #checks if string contains only alphabets
print("2012".isdigit()) #True
print("first Number".isidentifier()) # checks if the string has python keywords #False
print (s.islower()) #True
print("WELCOME".isupper()) #True
print(" ".isspace()) #True
#Example 10 : Searching for substrings 
s="welcome to python"
print(s.endswith("thon")) #True
print(s.startswith("good")) #False
print(s.find("come")) #3
print(s.find("become")) #-1 Not found
print(s.count("o")) #3  returns the number of occurences of the substring in the string
#Example11 : Converting Strings
s="string in PYTHON"
s1=s.capitalize() #Only first character is capitalised
print(s1)
s2=s.title()
print(s2)
s3=s.lower()
print(s3)
s4=s.upper()
print(s4)
s5=s.swapcase()
print(s5)
s6= s.replace("in","on")
print(s6)
# OUTPUT- 
# String in python
# String In Python
# string in python
# STRING IN PYTHON
# STRING IN python
# strong on PYTHON
#Example11 : Reverse a string 
#Method1
s="welcome"
rev_str=""
for i in s:
    rev_str=i+rev_str
print("reversed string is ",rev_str) #emoclew
#Method2
s="welcome"
rev_str=s[::-1] #[start:end:-1]
print(rev_str) #emoclew
