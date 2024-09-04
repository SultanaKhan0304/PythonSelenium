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





