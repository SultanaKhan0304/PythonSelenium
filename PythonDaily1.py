#Day 1 - Python Daily Practice
Example 1 - Given an integer, , perform the following conditional actions:
If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird
#!/bin/python3
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
if n %2!=0:
    print("Weird")
elif n%2==0:
    if n<=5:
        print("Not Weird")
    elif n<20:
        print("Weird")
if n>20:
        print("Not Weird")
    
# Example 2 The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:
The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    print(a+b)
    print(a-b)
    print(a*b)
    
#Example 3 : The provided code stub reads two integers,  and , from STDIN.
Add logic to print two lines. The first line should contain the result of integer division,  // . 
The second line should contain the result of float division,  / .

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)
    
Example 4:The provided code stub reads and integer, , from STDIN. For all non-negative integers , print .
The list of non-negative integers that are less than  is . Print the square of each number on a separate line.
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i**2)




