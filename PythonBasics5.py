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


