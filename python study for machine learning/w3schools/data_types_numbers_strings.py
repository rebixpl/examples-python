# Datatypes in Python
import random
x = "Hello World"  # str
x = 20  # int
x = 20.5  # float
x = 1j  # complex
x = ["apple", "banana", "cherry"]  # list
x = ("apple", "banana", "cherry")  # tuple
x = range(6)  # range
x = {"name": "John", "age": 36}  # dict
x = {"apple", "banana", "cherry"}  # set
x = frozenset({"apple", "banana", "cherry"})  # frozenset
x = True  # bool
x = b"Hello"  # bytes
x = bytearray(5)  # bytearray
x = memoryview(bytes(5))  # memoryview

# Setting datatype
x = str("Hello World")  # str
x = int(20)  # int
x = float(20.5)  # float
x = complex(1j)  # complex
x = list(("apple", "banana", "cherry"))  # list
x = tuple(("apple", "banana", "cherry"))  # tuple
x = range(6)  # range
x = dict(name="John", age=36)  # dict
x = set(("apple", "banana", "cherry"))  # set
x = frozenset(("apple", "banana", "cherry"))  # frozenset
x = bool(5)  # bool
x = bytes(5)  # bytes
x = bytearray(5)  # bytearray
x = memoryview(bytes(5))  # memoryview


#########################################################################


# To verify the type of any object in Python, use the type() function:
z = 1j  # complex
y = 22.3  # float
print(type(z))  # OUTPUT: <class 'complex'>
print(type(y))  # OUTPUT: <class 'float'>


##########################################################################

# Python Numbers
x = 1    # int
y = 2.8  # float
z = 1j   # complex


##########################################################################

# Complex numbers in python
# Each complex number consist of one real part and one imaginary part.
# Complex numbers are written with a "j" as the imaginary part

# SYNTAX:
# complex([real[, imag]])

# Creating complex number
# method 1
c = 3 + 6j
print(type(c))  # OUTPUT: <class 'complex'>
print(c)  # OUTPUT: (3+6j)

compx = complex(3, 6)  # complex(real, imaginary)
print(type(compx))  # OUTPUT: <class 'complex'>
print(compx)  # OUTPUT: (3+6j)

cx = complex(3, 6)
print("real part is: ", cx.real)  # OUTPUT: 3.0
print("imaginary part is: ", cx.imag)  # OUTPUT: 6.0
print("conjugate part is: ", cx.conjugate())  # OUTPUT: (3-6j)


#######################################################################

# Numbers type conversion
x = 1    # int
y = 2.8  # float
z = 1j   # complex

# convert from int to float:
a = float(x)

# convert from float to int:
b = int(y)

# convert from int to complex:
c = complex(x)

print(type(a))  # OUTPUT: <class 'float'>
print(type(b))  # OUTPUT: <class 'int'>
print(type(c))  # OUTPUT: <class 'complex'>


# Generating random number

print(random.randrange(1, 100))  # OUTPUT: 48

##################################################################################

# 'hello' is the same as "hello"

# Multiline Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

print(a)

# Strings are Arrays
a = "hello"
print(a[1])  # OUTPUT: e

# Slicing
# You can return a range of characters by using the slice syntax.
b = "Hello, World!"
print(b[2:5])  # OUTPUT: llo
# b[start index: end index]


# Negative indexing
# Use negative indexes to start the slice from the end of the string:
b = "Hello, World!"
print(b[-5: -2])  # OUTPUT: orl

# String Length
# To get the string length, use len() method:
b = "Hello, World!"
print(len(b))  # OUTPUT:13


#########################################################################

# String Methods

# strip() method
# strip() method removes any whitespaces from the beginning or the end:
a = "     Hello, World!       "
print(a.strip())  # OUTPUT: Hello, World!


# lower() and upper()
a = "Hello, World!"
print(a.lower())  # OUTPUT: hello, world!
print(a.upper())  # OUTPUT: HELLO, WORLD!

# replace() method
# replace() method replaces string with another string
a = "Hello, Word!"
print(a.replace("W", "Disc"))  # OUTPUT: Hello, Discord!

# split() method
#
a = "Hello, World!"
print(a.split(","))  # OUTPUT: ['Hello', ' World!']

# check string
# Check if certain phrase or character is present in a string:
txt = "Filler text is text that shares some characteristics of a real written text, but is random or otherwise generated."
x = "jd" in txt  # Check if the phrase "jd" is present in the following text:
print(x)  # OUTPUT: False

# Check if the phrase "jd" is NOT present in the following text:
x = "jd" not in txt
print(x)  # OUTPUT: True

# Merging Strings
a = "ur"
b = "dad"
c = "is gay"

result = a + " " + b + " " + c
print(result)  # OUTPUT: ur dad is gay


# String Format
# The format() method takes the passed arguments, formats them,
# and places them in the string where the placeholders {  } are:
quantity = 4
itemNumber = 666233
price = 420.69
# You can use index numbers {0} to be sure the arguments are placed
# in the correct placeholders, but you don't have to
myOrder = "I want to pay {1} dollars for {0} pieces of item {2}."
print(myOrder.format(quantity, price, itemNumber))
# OUTPUT: I want to pay 420.69 dollars for 4 pieces of item 666233.

# Escape Characters
# To insert characters that are illegal in a string, use an escape character **`\`**.

# You can add double quotes to a string using escape character
txt = "We are the so-called \"Vikings\" from the north."

# Escape characters used in python:
# - \' → Single Quote
# - \" → Double Quote
# - \\ → Backslash
# - \n → New Line
# - \r → Carriage Return → Whenever you will use this special escape character \r, the rest of the content after the \r will come at the front of your line and will keep replacing your characters one by one until it takes all the contents left after the \r in that string. Whatever content is there after the \r will come at the beginning of our whole string.
# - \t → Tab
# - \b → Backspace
# - \f → Form Feed → Form feed is also a special character that, when encountered in code, causes printers to automatically advance one full page or the start of the next page. This form feed special character has a decimal value of 12 in the ASCII character set.
# - \ooo → Octal Value
# - \xhh → Hex Value
