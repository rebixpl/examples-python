#! /usr/bin/python3

###! Python Class Inheritance

##? Creating parent class (normal class)
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

# Use the Person class to create an object, and then execute the printname method:
x = Person("John", "Doe")
x.printname()



##? Creating a child class
#       * child class inherits the functionality from another class
#       * we declare the parent class as a parameter when creating the child class
class Student(Person):
    pass

# Now, the student class can execute the printname method: 
z = Student("Mike", "Olsen")
z.printname()



##? Adding the __init__() function to child class
class Tapster(Person):
    def __init__(self, fname, lname): # * The child's __init__() function OVERRIDES the inheritance if parent's __init__() function
        # To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
        Person.__init__(self, fname, lname)

c = Tapster("Duke", "Nukem")
c.printname()




##? Using the super() function and adding properties
#       * It makes the child class inherit all the methods and properties from its parent
#       * By using super() function you do not have to use the name of parent element
class Builder(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.yearOfBorn = year

v = Builder("Bob", "Builder", "1963")
print(v.yearOfBorn)



##? Adding methods
class Woman(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.yearOfBorn = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "you are woman born in", self.yearOfBorn)

b = Woman("Jadwiga", "Agiwdaj", "1915")
print(b.yearOfBorn)
b.welcome()

