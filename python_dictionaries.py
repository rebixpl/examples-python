### Dictionary is a collection which is UNORDERED, CHANGEABLE and INDEXED. It has KEYS and VALUES
thisisdictionary = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}



## Accessing Items
print(thisisdictionary) # prints whole dictionary
print(thisisdictionary["model"]) # gets the value of the 'model' key, so -> dictionary["key"]
print(thisisdictionary.get("year")) # gets the value of the 'year' key, so -> dictionary.get("key")



## Change values
thisisdictionary["year"] = 2018
print(thisisdictionary.get("year"))
print("")



## Loop through a dictionary
# print all key names
for x in thisisdictionary:
    print(x)
print("")

# print all values
for x in thisisdictionary:
    print(thisisdictionary.get(x))
print("")

for x in thisisdictionary.values():
    print(x)
print("")

# Loop through both keys and values using items() function
for x, y in thisisdictionary.items():
    print(x, y)
print("")



## Check if key exists
if "brand" in thisisdictionary:
    print("Yes, 'brand' is one of the keys in the 'thisisdictionary' dictionary")
print("")



## Dictionary length
print(len(thisisdictionary)) # prints out the number of items in dictionary
print("")



## Adding items
thisisdictionary["color"] = "violet" # adding items to dictionary is done by -> dictionary["newKey"] = "newValue"
print(thisisdictionary)
print("")



## Removing items
thisisdictionary.pop("model") # dictionary.pop("key") -> removes item with specified key
print("")

del thisisdictionary["year"] # del dictionary["key"] -> removes item with specified key
print(thisisdictionary)
print("")

# using del to remove the entire dictionary
dictionary1 = {
    "val1": 20,
    "val2": 15
}
print(dictionary1)
del dictionary1 # del dictionary
# print(dictionary1) # ERROR: this dictionary now don't exist anymore

# using clear() to empty the dictionary
thisisdictionary.clear() # removes all the elements from the dictionary
print(thisisdictionary)
print("")



## Copy a dictionary
thisisdictionary = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

myDictionary = thisisdictionary.copy() # dictionary.copy() -> returns copy of dictionary
print(myDictionary)
print("")



## Nested dictionaries
myFamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Adolf",
        "year": 1894
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}
print(myFamily)

# the same in the other way
child1 = {
    "name": "Emil",
    "year": 2004
}

child2 = {
    "name": "Adolf",
    "year": 1894
}

child3 = {
    "name": "Linus",
    "year": 2011
}

myNewFamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}
print(myNewFamily)
print("")

if myFamily == myNewFamily:
    print("true")



## The dict() constructor -> it is possible to use dict() constructor to make a new dictionary
ultimateDictionary = dict(brand="Ford", model="Mustang", year=1964)
# !note that keywords are not string literals
# !note the use of equals rather than colon for the assignment
print(ultimateDictionary)
