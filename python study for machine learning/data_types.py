# Datatypes in Python
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
print(type(c)) # OUTPUT: <class 'complex'>
print(c) # OUTPUT: (3+6j)

compx = complex(3, 6) # complex(real, imaginary)
print(type(compx)) # OUTPUT: <class 'complex'>
print(compx) # OUTPUT: (3+6j)

cx = complex(3,6)
print("real part is: ", cx.real) # OUTPUT: 3.0
print("imaginary part is: ", cx.imag) # OUTPUT: 6.0
print("conjugate part is: ", cx.conjugate()) # OUTPUT: (3-6j)


#######################################################################
