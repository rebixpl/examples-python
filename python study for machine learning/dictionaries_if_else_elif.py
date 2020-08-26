import os

# DICTIONARIES ##############################################
# In Python dictionaries are written with curly brackets, and they have
# keys and values.

sampleDictionary = {
    "brand": "Tesla",
    "model": "S",
    "year": 2020.
}

# OUTPUT: {'brand': 'Tesla', 'model': 'S', 'year': 2020.0}
print(sampleDictionary)

# Accessing Items
sampleDictionary = {
    "brand": "Tesla",
    "model": "S",
    "year": 2020.
}

# Get the value of the "brand" key
x = sampleDictionary["brand"]
print(x)  # OUTPUT: Tesla

x = sampleDictionary.get("brand")
print(x)  # OUTPUT: Tesla

# Change values
sampleDictionary = {
    "brand": "Tesla",
    "model": "S",
    "year": 2020.
}

sampleDictionary["model"] = "X"
# OUTPUT: {'brand': 'Tesla', 'model': 'X', 'year': 2020.0}
print(sampleDictionary)

# Loop through a dictionary
sampleDictionary = {
    "brand": "Tesla",
    "model": "S",
    "year": 2020.
}

for x in sampleDictionary:
    print(x)  # prints key names such as "brand"
    print(sampleDictionary[x])  # prints values such as "Tesla"


# You can return values using values() method
for x in sampleDictionary.values():
    print(x)  # OUTPUT: Tesla S 2020.0

# You can loop through both keys and values, by using the items() method:
for x, y in sampleDictionary.items():
    print(x, y)
# OUTPUT:
# brand Tesla
# model S
# year 2020.0

# Check if key exists
myDicc = {
    "brand": "Tesla",
    "model": "S",
    "year": 2020.
}

if "model" in myDicc:
    print("The key \"model\" exists in myDicc dictionary")

# Dictionary Length
print(len(myDicc))  # OUTPUT: 3


# Adding Items
myDicc = {
    "brand": "Tesla",
    "model": "S",
    "year": 2020.
}

myDicc["color"] = "platinium white"
# OUTPUT: {'brand': 'Tesla', 'model': 'S', 'year': 2020.0, 'color': 'platinium white'}
print(myDicc)

# REMOVING ITEMS #########
# pop() → Removes item by its key name:
myDicc = {
    "brand": "Tesla",
    "model": "S",
    "year": 2020.
}

myDicc.pop("brand")
print(myDicc)  # OUTPUT: {'model': 'S', 'year': 2020.0}

# popitem() → Removes the last inserted item:
myDicc = {
    "brand": "Tesla",
    "model": "S",
    "year": 2020.
}

myDicc.popitem()
print(myDicc)  # OUTPUT: {'brand': 'Tesla', 'model': 'S'}

# del keyword → removes item with specified key also deletes dictionary
# completly:
myDicc = {
    "brand": "Tesla",
    "model": "S",
    "year": 2020.
}

del myDicc["model"]
print(myDicc)  # OUTPUT: {'brand': 'Tesla', 'year': 2020.0}

del myDicc

# clear() → empties the dictionary
myDicc = {
    "brand": "Tesla",
    "model": "S",
    "year": 2020.
}

myDicc.clear()
print(myDicc)  # OUTPUT: {}

##################
os.system("cls")
##################

# Copy a Dictionary
myDicc = {
    "brand": "Tesla",
    "model": "S",
    "year": 2020.
}

newDIc = myDicc.copy()
print(newDIc)  # OUTPUT: {'brand': 'Tesla', 'model': 'S', 'year': 2020.0}


nextDicc = dict(myDicc)
print(nextDicc)  # OUTPUT: {'brand': 'Tesla', 'model': 'S', 'year': 2020.0}


# NESTED DICTIONARIES ####
# Dictionary can contain many dictionaries.

myFamily = {
    "child1": {
        "name": "Adolf",
        "age": 32
    },
    "child2": {
        "name": "X AE-XII",
        "age": 420
    },
    "child3": {
        "name": "Literally Linux",
        "age": 6.9
    }
}

# The dict() Constructor
myDict = dict(
    age=23, name="BT37 artificial life form, production year 2037, May 13")
# OUTPUT: {'age': 23, 'name': 'BT37 artificial life form, production year 2037, May 13'}
print(myDict)


# PYTHON IF ELSE ###############################################################
a = 33
b = 200
if a > b:
    print("b is greater than a")

# Else and Elif ( else if)
if b > a:
    print("b is greater than a")
elif b == a:
    print("a and b are equal")
else:
    print("a is greater than b")

# Short Hand If
if a > b:
    print("a is greater than b")

# Short Hand If...Else
a = 2
b = 330
print("A") if a > b else print("B")

# You can also have multiple else statements on the same line:
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")


# AND
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")

# OR
a = 200
b = 33
c = 500
if a > b or a > c:
    print("At least one of the conditions is True")


# Nested IF
x = 41
if x > 10:
    print("more than 10, ")
    if x > 20:
        print("more than 20!")
    else:
        print("but not above 20!")


# the pass statement
# You can use pass to avoid getting error when making empty statement
if a > b:
    pass
