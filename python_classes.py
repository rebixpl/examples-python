#! /usr/bin/python3

##! Python Classes and Objects

##? Create a class
class myClass:
    x = 5



##? Create a object
p1 = myClass()
print(p1.x) # output: 5



##? the __init__() function
# All classes have a function called __init__(), which is always executed when the class is being initiated.
# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:
class Person:
    def __init__(self, name, age):
        self.name = name # self in python is like this pointer in c++
        self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
print("")



##? Object methods
# Methods in objects are functions that belong to the object
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myFunc(self): # method
        print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myFunc()



##? The 'self' parameter
# The 'self' parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
# Id does not have to be named 'self', you can call it whatever you like, but it has ot be the FIRST parameter of any function in the class
class Person:
    def __init__(mySillyObject, name, age):
        mySillyObject.name = name
        mySillyObject.age = age

    def myFunc(abc):
        print("Hello, my name's " + abc.name)

p1 = Person("John", 36)
p1.myFunc()
print("")



##? modify object properties
p1.age = 40
print(p1.age)



##? delete object properties
del p1.age # del object.property
# print(p1.age) # ERROR: 'Person' object has no attribute 'age'



##? delete objects
del p1 # del object
# print(p1) # ERROR: name 'p1' is not defined



##? pass statement
# creates empty class definition
class Animals:
    pass
