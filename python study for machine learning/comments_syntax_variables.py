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
