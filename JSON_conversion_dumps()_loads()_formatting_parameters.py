#! /usr/bin/python3

###! Python JSON
#       * JSON is a syntax for storing and exchanging data

##? Parse JSON - Convert from JSON to Python
#       * if you have JSON string you can parse it by using the 'json.loads()' method. The result will be a Python dictionary.

import json # you need to import json module to use it!
# some JSON:
x = '{ "name" : "John", "age" : 30, "city" : "New York" }'

# parse x:
y = json.loads(x)

# the result is a Python DICTIONARY:
print(y["age"]) # OUTPUT: 30



##? Convert from Python to JSON
#       * you can convert python object into a JSON string by using the 'json.dumps()' method

import json
# a python object (dict):
x = {
    "name" : "John",
    "age" : 30,
    "city" : "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

x = 6.2342234
y = json.dumps(x)
print(y)

#* some examples:
print(json.dumps({"name":"John","age":30,}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("HELLO"))
print(json.dumps(32))
print(json.dumps(32.534663425235))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

#       * When you convert from Python to JSON, Python objects are converted into the JSON (JavaScript) equivalent:
# Python	JSON
# dict	      Object
# list	      Array
# tuple	    Array
# str	      String
# int	      Number
# float	    Number
# True	     true
# False	    false
# None	      null

print("")
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# convert into JSON:
c = json.dumps(x)
print(c) # the result is a JSON string
print("")



##? Format the result

#       * 'indent' parameter
c = json.dumps(x, indent=4)
print(c)
print("")

#       * 'separators' parameter ->  which means using a comma and a space to separate each object, and a colon and a space to separate keys from values
c = json.dumps(x, indent=4, separators=(". ", " = "))
print(c)
print("")

#       * 'sort_keys' parameter ->  sort the result alphabetically by keys
c = json.dumps(x, indent=4, sort_keys=True)
print(c)
