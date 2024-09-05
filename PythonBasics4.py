#Session 4
#Collections  - List, Tuple, Set, Dictionary
#Example1 - List creation
mylist1=[10,20,30,40,50]
mylist2=["apple","banana","cherry"]
mylist3=["apple",10,"banana",20]
mylist=list()  #creation of empty list
print(mylist1)
print(mylist2)
print(mylist3)
print(mylist)
#Example2 - Accessing items from the list
mylist=["apple","banana","cherry"]
print(mylist[0])
print(mylist[2])
print(mylist[-1]) #returns the last element 
#Example3 - Range of indexes
mylist=["apple","banana","cherry","orange","kiwi","melon","mango"]
print(mylist[2:5]) # print the contents from 2 to 4 index
print(mylist[-4:-1]) #count is done from end in case of negative range
#Example 4 - change item value
mylist=["apple","banana","cherry","orange","kiwi","melon","mango"]
print(mylist)
mylist[0]="orange"
print(mylist)
# Example 5 - read the list items using loop statements 
mylist=["apple","banana","cherry","orange","kiwi","melon","mango"]
for i in mylist:
    print(i)
#Example 6 - Check if the item exists in the list or not 
mylist=["apple","banana","cherry"]
if "apple" in mylist:
    print("yes, apple is present")
else:
    print("No, apple is not present")
#Example 7 - List length
mylist=["apple","banana","cherry"]
print(len(mylist))
# Example 8 : Add items append() insert()
mylist=["apple","banana","cherry"]
mylist.append("orange") #add new value at the end of the list
print(mylist)
mylist.insert(1,"mango") # adds value in the middle of the list , specify index and value
print(mylist)
#Example 9 Remove item from the list
#pop() 
mylist=["apple","banana","cherry"]
mylist.pop(0)
print(mylist) #['banana', 'cherry']
#del() - Removes the item from the list
del mylist[1]
print(mylist)
#clear() function
mylist=["apple","banana","cherry"]
mylist.clear() # clears all items from the list
print(mylist) #empty list is print and variable is available -[]
#Example 10 copy list
mylist1=["apple","banana","cherry"]
mylist2=list(mylist1)
print(mylist1)
print(mylist2)
#COPY() FUNCTION
mylist1=["apple","banana","cherry"]
mylist2=mylist1.copy()
print(mylist1)
print(mylist2)
#Example 11 Combine/Join 2 lists using + operator
list1=['a','b',"c"]
list2=[1,2,3]
list3=list1+list2
print(list3)
#Example 12 Combine/Join 2 lists  using for loop statement
list1=['a','b',"c"]
list2=[1,2,3]
for i in list2:
    list1.append(i)
print(list1)
#Example 12 Combine/Join 2 lists by using extend function
list1=['a','b',"c"]
list2=[1,2,3]
list1.extend(list2)
print(list1)
# Tuple - It is ordered and unchangeable . () , Tuple is Immutable
mytuple=("apple","banana","cherry")
print(mytuple)
#Example2 - Access Tuple items
mytuple=("apple","banana","cherry")
print(mytuple[1])
print(mytuple[-1]) #cherry
#Example 3 - Range of indexes
mytuple=("apple","banana","cherry","kiwi","melon","mango")
print(mytuple[2:5])
mytuple=("apple","banana","cherry","orange","kiwi","melon","mango")
print(mytuple[-4:-1]) # ('orange', 'kiwi', 'melon')
#Example 4: Changing tuple items 
#by default tuple does not allow us to change value as it is immutable 
# so we use a workaround 
#tuple --> list(modify)--> tuple
mytuple=("apple","banana","cherry","orange","kiwi","melon","mango")
mylist=list(mytuple) #changed the tuple to list
mylist[0]="orange" #made the modification in the list
mytuple=tuple(mylist) #convert the list to tuple
print(mytuple)  #print the tuple
#Example 5 Reading tuple items using loop
mytuple=("apple","banana","cherry","orange","kiwi","melon","mango")
for i in mytuple:
    print(i)
#Example 6 Checking if item exists in the tuple
mytuple=("apple","banana","cherry","orange","kiwi","melon","mango")
if "berry" in mytuple:
    print("yes berry is present")
else:
    print("no, berry is not present")
#Example 7 Tuple length
mytuple=("apple","banana","cherry","orange","kiwi","melon","mango")
print(len(mytuple))
#Example 9 - copy tuple from one to another
mytuple1=("apple","banana","cherry")
mytuple2=mytuple1
print(mytuple2)
#Example 10 delete a tuple
mytuple1=("apple","banana","cherry")
del mytuple1 #removes the tuple completely
print(mytuple1)
#Example11 Join/Combine tuple
tuple1=(10,20,30)
tuple2=('a','b','c')
tuple3= tuple1+tuple2
print(tuple3)
#Example 12 - Compare 2 tuples 
tuple1=(10,20,30)
tuple2=(10,20,30)
if tuple1==tuple2:
    print("tuples are equal")
else:
    print("tuples are not equal")
