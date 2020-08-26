# TUPLES ################################################
# In Python tuples are written with round brackets.

# Tuple → is a collection which is ordered and unchangeable.
# Allows duplicate members.

thisIsTuple = ("apple", "banana", "cherry")
print(thisIsTuple)  # OUTPUT: ('apple', 'banana', 'cherry')

# Access Tuple Items
print(thisIsTuple[1])  # OUTPUT: banana

# Negative Indexing
print(thisIsTuple[-1])  # OUTPUT: cherry

# Range of Indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])  # OUTPUT: ('cherry', 'orange', 'kiwi')


# Change TUple Values
# You CANNOT change tuple value. But you can convert tuple to list,
# change list and convert this list back to tuple.

x = ("apple", "banana", "cherry")
y = list(x)  # Convert tuple to list
y[1] = "kiwi"  # Change list
x = tuple(y)  # Convert list to tuple

print(x)  # OUTPUT: ('apple', 'kiwi', 'cherry')

# LOOP through a tuple
tupledTupleX = ("apple", "banana", "cherry", "berry",
                "blueberry", "faygo", "draco")

for x in tupledTupleX:
    print(x)

# OUTPUT:
# apple
# banana
# cherry
# berry
# blueberry
# faygo
# draco

# TUPLE LENGTH
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))  # OUTPUT: 3

# Create Tuple With One Item
# To create a tuple with only one item, you have to add a comma after
# the item, otherwise Python will not recognize it as a tuple.

# NOT A TUPLE
meinTuple = ("tomato")
print(type(meinTuple))  # OUTPUT: <class 'str'>

# TUPLE
meinTuple = ("tomato",)
print(type(meinTuple))  # OUTPUT: <class 'tuple'>


# Join two tuples
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2

print(tuple3)  # OUTPUT: ('a', 'b', 'c', 1, 2, 3)
print(type(tuple3))  # OUTPUT: <class 'tuple'>


# Remove tuple
uperTupel = ("jd", 2, "ddD")
del uperTupel  # delete whole tuple


# The tuple() constructor
thistuple = tuple(("my", "ur", "xs"))
print(thistuple)  # OUTPUT: ('my', 'ur', 'xs')

# Tuple count() method
# count() method returns the number of times a specified value appears
# in the tuple.

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5, 6, 3, 8, 3, 5, 5, 5, 2, 5, 2, 3, 6)
x = thistuple.count(5)  # returns how many times 5 appears in this tuple
print(x)  # OUTPUT: 6


# Tuple index() method
# The index() method finds the first occurrence of the specified value.

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5, 6, 3, 8, 3, 5, 5, 5, 2, 5, 2, 3, 6)
x = thistuple.index(7)
print(x)  # OUTPUT: 2

# SETS #####################################################################

# In Python sets are written with curly brackets. Sets are unordered,
# so you cannot be sure in which order the items will appear.

thisisset = {"tomato", "car", "machine learning", "gpt-3"}
print(thisisset)  # OUTPUT:

# Access Items
# Of course, you CANNOT access items by index, but you can use for loop
# or check if value is present in set:

thisisset = {"tomato", "car", "machine learning", "gpt-3"}
for item in thisisset:
    print(item)

# OUTPUT:
# car
# machine learning
# tomato
# gpt-3

# Check if "car" is present in the set:
print("car" in thisisset)  # OUTPUT: True

# Change Items ##
# You CANNOT change items in set after its creation, but you can add
# new items.

# add() → add one item
thisset = {"apple", "banana", "cherry"}
thisset.add("blueberry")

print(thisset)  # OUTPUT: {'blueberry', 'apple', 'cherry', 'banana'}


# update() → add more than one item
thisset = {"apple", "banana", "cherry"}
thisset.update(["grapes", "mango", "dragonfruit", "kiwi"])
# OUTPUT: {'kiwi', 'banana', 'mango', 'grapes', 'dragonfruit', 'cherry', 'apple'}
print(thisset)

# Remove Item

# remove() -> If the item to remove does not exist, remove() will raise
# an error.

thisset = {"a", "b", "c", "d", "e"}
thisset.remove("b")
print(thisset)  # OUTPUT: {'a', 'd', 'e', 'c'}

# discard() ->  If the item to remove does not exist, discard() will
# NOT raise an error.

thisset = {"a", "b", "c", "d", "e"}
thisset.discard("b")
print(thisset)  # OUTPUT: {'a', 'd', 'e', 'c'}

# pop() -> Sets are unordered, thus it deletes random item

# clear() -> empties the set
thisset = {"a", "b", "c", "d", "e"}
thisset.clear()
print(thisset)  # OUTPUT: set()

# del keyword → deletes the set completely
thisset = {"a", "b", "c", "d", "e"}
del thisset

# Join Two Sets
# union() → returns a new set with all items from both sets:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)  # OUTPUT: {'a', 1, 2, 3, 'c', 'b'}

# update() → inserts the items in set2 into set1:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)  # OUTPUT: {'a', 1, 2, 3, 'c', 'b'}

# The set() constructor
myset = set(("apple", "africa", "the planet of death"))
print(myset)  # OUTPUT: {'the planet of death', 'apple', 'africa'}
