import turtle

qazi_turtle = turtle.Turtle()

# Square
def square():
    qazi_turtle.forward(100)
    qazi_turtle.right(90)
    qazi_turtle.forward(100)
    qazi_turtle.right(90)
    qazi_turtle.forward(100)
    qazi_turtle.right(90)
    qazi_turtle.forward(100)




elephant_weight = 3000
ant_weight = 0.1

# This is IF STATEMENT
if elephant_weight > ant_weight:
    square()
else:
    qazi_turtle.forward(100)




a = 200
b = 200

# This is IF STATEMENT with elif keyword
if b > a:
  print("b is greater than a")
elif a == b: #elif is just like else if in other programming languages
  print("a and b are equal")
else:
  print("a is greater than b")




# This is SHORT HAND IF
if a == b: print("a and b are equal")




# This is IF with AND, OR logical operator keywords
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")

if a > b or c > a:
    print("At least one of conditions is True")





# PASS statement
# if statements cannot be empty, but if you for some reason have an if
# statement with no content, put in the pass statement to avoid getting
# an error.
a = 33
b = 200
if b > a:
    pass
