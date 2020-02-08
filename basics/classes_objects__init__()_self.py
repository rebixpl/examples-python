#! /usr/bin/python3

###! Python Classes and Objects

##? Creating a class -> use keyword 'class'
class MyClass:
    x = 5

print(MyClass)



##? Creating a class object ->  objectname = classname()
object1 = MyClass()
print(object1.x) # OUTPUT: 5
print("")



##? The __init__() function and object methods
#   * All classes have this function and it is always executed when the class object is being initiated
#   * you can use it to assign values

class Person:
    def __init__(self, name, age): ##* the 'self parameter is described below (it is like 'this' in C++)
        self.name = name
        self.age = age

    def myFunc(self): ##* Object method
        print("Hello my name is " + self.name)

p1 = Person("Adolf", 32)

print(p1.name)
print(p1.age)
p1.myFunc()
print("")



##? The 'self' parameter
#   * 'self' parameter is a reference to the current instance of the class and is used to access variables that belong to the class (like this in c++)
#   * it does not have to be named 'self', but it has to be the first parameter of any function in the class

class Animal:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myFunc(abc):
        print("I'm a " + abc.name)

a1 = Animal("Dog", 5)
a1.myFunc()
print(a1.age)
print("")



##? Modify object properties
p2 = Person("John", 44)

p2.age = 39 # modifying the age value

print(p2.age)




##? Delete object properties
p3 = Person("Anna", 23)

del p3.age # deleting age property

print(p3.age) # ERROR: 'Person' (p3) has no attribute 'age'




##? Deleting objects
p4 = Person("Korwin", 69)

del p4 # deleting whole p4 object

print(p4)



##? The pass statement
#   * it creates empty class

class Kurwa:
    pass
