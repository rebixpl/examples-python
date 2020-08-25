# Booleans

# Evaluate Values and Variables
# The bool() function allows you to evaluate any value,
# and give you True or False in return:

print(bool("Hello"))  # OUTPUT: True
print(bool(15))  # OUTPUT: True


def myFuncc():
    return True


if myFuncc():
    print("YES")
else:
    print("NO")

# isinstance() function
# Check if an object is an integer or not:
x = 2003
print(isinstance(x, int))  # OUTPUT: True

###########################################################################

# List
# Lists in python are written with square brackets.
myList = ["tea", "blood", "revenge", "lex talionis"]
print(myList)  # OUTPUT: ['tea', 'blood', 'revenge', 'lex talionis']

# You can access list items using index
print(myList[1])  # OUTPUT: blood

# Negative indexing means beginning from the end
print(myList[-1])  # OUTPUT: lex talionis

# Range of Indexes
print(myList[1:3])  # OUTPUT: ['blood', 'revenge']

# Change the item value
simpleList = ["water", "space goo", "serum"]
simpleList[2] = "black tomato"
print(simpleList)  # OUTPUT: ['water', 'space goo', 'black tomato']

# Loop through a list
simpleList = ["water", "space goo", "serum", "flame shaped tomato",
              "low poly car", "witchcraft", "Grimes", "minecraft", "meinkampf"]
for x in simpleList:
    print(x)
# OUTPUT:
# water
# space goo
# serum
# flame shaped tomato
# low poly car
# witchcraft
# Grimes
# minecraft
# meinkampf


# Check if item exists
listtt = ["falcon", "super heavy", "blaze", "horizon", "machines", "AI"]
if "blaze" in listtt:
    print("Yeah, 'blaze' is in the list")

# OUTPUT:
# Yeah, 'blaze' is in the list

# List length
listA = ["A", "B", "🦆"]
print(len(listA))  # OUTPUT: 3


# Add items to the list
# To add item to THE END use append() method:
thislist = ["apple", "banana", "cherry"]
thislist.append("metal flower")
print(thislist)  # OUTPUT: ['apple', 'banana', 'cherry', 'metal flower']

# To add item at SPECIFIED INDEX use insert() method:
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "metal flower")
print(thislist)  # OUTPUT: ['apple', 'banana', 'metal flower', 'cherry']


# REMOVE ITEMS FROM LIST

# To remove SPECIFIED ITEM use remove() method:
thislist = ["apple", "banana", "cherry"]
thislist.remove("apple")
print(thislist)  # OUTPUT: ['banana', 'cherry']

# To remove SPECIFIED INDEX ( or last item if index is not specified ) use pop() method:
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)  # OUTPUT: ['apple', 'cherry']
thislist.pop()
print(thislist)  # OUTPUT: ['apple']


# DEL KEYWORD

# It can remove specified index.
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)  # OUTPUT: ['banana', 'cherry']

# It can delete the list completly.
thislist = ["apple", "banana", "cherry"]
del thislist

# To clear the list use clear() method
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)  # OUTPUT: []


# COPY A LIST ####################################
# You cannot copy a list simply by typing list2 = list1, because:
# list2 will only be a reference to list1, and changes made in list1
# will automatically also be made in list2.

# Use copy() method:
thislist = ["apple", "banana", "cherry"]
myList = thislist.copy()
print(myList)  # OUTPUT: ['apple', 'banana', 'cherry']

# Use list() method:
thislist = ["apple", "banana", "cherry"]
myList = list(thislist)
print(myList)  # OUTPUT: ['apple', 'banana', 'cherry']


# JOIN TWO LISTS ##################################
# Use + operator
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)  # OUTPUT: ['a', 'b', 'c', 1, 2, 3]

# append all items from list2 into list 1, one by one:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)

print(list1)  # OUTPUT: ['a', 'b', 'c', 1, 2, 3]

# use extend() method:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list1.extend(list2)  # extend adds items from one list to another

print(list1)  # OUTPUT: ['a', 'b', 'c', 1, 2, 3]


# The list() constructor
myfuckinglist = list(("apple", "elppa", "pelap", "palepa"))
print(myfuckinglist)  # OUTPUT: ['apple', 'elppa', 'pelap', 'palepa']
