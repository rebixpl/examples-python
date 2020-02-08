# PYTHON SETS
#-----------------------------------------------------------------------------------------------------

## Set is a collection which is UNORDERED and UNINDEXED
# note: Sets are unordered, so you CANNOT be sure in which order the items will appear
thisisset = {"apple", "banana", "cherry"}
print(thisisset)



## ACCESS ITEMS - you cannot access items in a set by index, because set values are unordered nad dont have indexes
thisisset = {"apple", "banana", "cherry"}
#print(thisisset[2]) # ERROR: items are unordered

for i in thisisset:
    print(i)
    if i == "banana":
        print("'banana' value exists in thisisset")



## add(item) - you can use this to add ONE item to the set
thisisset.add("tomato")
print(thisisset)



## update([item, item, item...]) - you can use this to add MORE THAN ONE item to set
thisisset = {"apple", "banana", "cherry"}
thisisset.update(["onion", "tomato", "mango"])
print(thisisset)



## len(set) - get the length of a set
print(len(thisisset))



### REMOVE ITEMS
## remove(item) - removes item, if the item to remove does NOT EXIST causes ERROR
thisisset = {"apple", "banana", "cherry"}
thisisset.remove("apple")
print(thisisset)


## discard(item) - removes item, if the item to remove does NOT EXIST will NOT CAUSE ERROR
thisisset = {"apple", "banana", "cherry"}
thisisset.discard("cherry")
print(thisisset)


## pop() - removes last item, but sets are unordered, so REMOVES RANDOM ITEM, and that removed item is saved in return value of pop
thisisset = {"apple", "banana", "cherry"}
x = thisisset.pop()
print(x)
print(thisisset)


## clear() - empties the set
thisisset = {"apple", "banana", "cherry"}
thisisset.clear()
print(thisisset)


## del - deletes the set completely
thisisset = {"apple", "banana", "cherry"}
del thisisset
print(" ")




### JOIN TWO SETS
## set1.union(set2, set...) - returns a new set containing all items from both sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
print(" ")


## set1.update(set2) - inserts all the items from one set into another
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)



## copy() - copies the set
fruits = {"apple", "banana", "cherry"}
x = fruits.copy()
print(x)
print(type(x))
print(" ")



## difference(set) - returns a set that contains the difference between two sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)
print(z)



## intersection(set1, set2, set...) - compares sets and returns a set with items that is present in all sets
x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}
result = x.intersection(y, z)
print(result) # OUTPUT: {"c"}
