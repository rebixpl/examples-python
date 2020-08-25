if 5 > 2:
    print("Five is greater than two!")  # here is indentation
# This is comment
'''
This
is
Comment
'''


#################################################################


# variables do not need to be declared with particular type
x = 22
c = "speed"
print(x)  # OUTPUT: 22
print(c)  # OUTPUT: speed

# Python allows you to assign values to multiple variables in one line:
x, y, z = "suck", "my", "cock"
print(x)  # OUTPUT: "suck"
print(y)  # OUTPUT: "my"
print(z)  # OUTPUT: "cock"

# And you can assign the same value to multiple variables in one line:
x = y = z = "jd"
print(x)  # OUTPUT: "jd"
print(y)  # OUTPUT: "jd"
print(z)  # OUTPUT: "jd"


#################################################################


# Combine text and variable
x = "mycellum block"
print("I eat" + x)  # OUTPUT: I eat mycellum block

y = "big deadly robot"
o = "deathbringer"
z = y + o
print(z)  # OUTPUT: big deadly robot deathbringer


##################################################################


# Global variables can be used by everyone, both inside of functions and outside.
username = "Ahmed"  # this is global variable


def myFunc():
    print("welcome, " + username)


myFunc()


# If you create a variable with the same name inside a function, this variable will be local,
# and can only be used inside the function.
x = "water"


def mySecFunc():
    x = "human meat"
    print("Eat " + x)  # OUTPUT: Eat human meat


mySecFunc()

print("Eat " + x)  # OUTPUT: Eat water


##################################################################


# To create a global variable inside a function, you can use the global keyword.
x = "smoke weed"


def myfFfFunc():
    global x
    x = "uproot weed"


myfFfFunc()

print(x)  # OUTPUT: uproot weed
