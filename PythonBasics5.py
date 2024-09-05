#Session 5
# Collections  - List, Tuple, Set, Dictionary
#Set 
#Example 1 - creating  a set
myset={"apple","banana","cherry"}
print(myset) #Output - {'cherry', 'apple', 'banana'}- is not in the same order
#Example2 - accessing items from the set 
myset={"apple","banana","cherry"}
for i in myset:
    print(i)
#Example3 - value exists in set or not
myset={"apple","banana","cherry"}
print("banana" in myset) #True
print("banana2" in myset) #False
#Example4 - adding items to the set
#add()- we can add single item at a time , update() - we can add multiple items at a time
myset={"apple","banana","cherry"}
myset.add("orange")
print(myset)
myset2={"apple","banana","cherry"}
myset2.update(["orange","mango", "grapes"])
print(myset2)
#Example5- Find the length of the set
myset={"apple","banana","cherry"}
print(len(myset))
#Example 6 - Remove items from the set - remove()  , discard()
myset={"apple","banana","cherry"}
myset.remove("banana")
print(myset)
myset.remove("xyz") #Removing item which is not availabe in set gives KeyError: 'xyz'
print(myset)
myset.discard("xyz") #Removing item which is not availabe in set gives no Error
# Example7 - clear all items from the set
myset={"apple","banana","cherry"}
myset.clear()
print(myset) # Output is an empty set - set()
del myset
print(myset) #NameError: name 'myset' is not defined
# Example7 - Joining 2 sets - union()
set1={"1","2","3"}
set2={"a","b","c"}
set3=set1.union(set2)
print(set3)
#update()
set1={"1","2","3"}
set2={"a","b","c"}
set1.update(set2)
print(set1)
# Dictionary
#Example1 - creating dictionary
mydic={101:"x",102:'y',103:"z"} #Key value pairs
print(mydic)
#Example 2 Acessing items from Dictionary
mydic={
    "brand":"Hyundai",
    "model":"i10",
    "year":2021
}
print(mydic["brand"])
print(mydic["model"])
#using get()
print(mydic.get("brand"))
#Example 3 Change values in the Dictionary
mydic={
    "brand":"Hyundai",
    "model":"i10",
    "year":2021
}
print(mydic)
mydic["year"]=2022
print(mydic)
#Example 4 - Reading items from Dictionary using loop
mydic={
    "brand":"Hyundai",
    "model": "i10",
    "year":2020
}
for i in mydic:
    print(i) #This only prints the key
    print(mydic[i]) #This will print the values
#This for loop will print the values
for i in mydic.values():
    print(i)
#This for loop will print the keys and values both
for x,y in mydic.items():
    print(x,y)
#Example 5 - Check if key exists in dictionary or not
mydic={
    "brand":"Hyundai",
    "model": "i10",
    "year":2020
}
if "model" in mydic:
    print("exist")
else:
    print("not exist")
print("model" in mydic) #True
#Example7- Adding items to the dictionary
mydic={
     "brand":"Hyundai",
     "model": "i10",
    "year":2020
 }
mydic["color"]="red"
print(mydic)
#Example 8 - remove items from the dictionary
mydic={
     "brand":"Hyundai",
     "model": "i10",
    "year":2020
 }
mydic.pop("year") #pop() function
print(mydic)
del mydic["model"] # del for removing 
print(mydic
del mydic #remove the complete dictionary
print(mydic) # This will not print as it is removed "NameError: name 'mydic' is not defined"
mydic.clear()
print(mydic) # This will print empty dictionary - {}
#Example 9 copy the dictionary into another dictionary
mydic={
     "brand":"Hyundai",
     "model": "i10",
    "year":2020
 }
mydic2=mydic
print(mydic2)
#By using copy() function
mydic1=mydic.copy()
print(mydic1)

