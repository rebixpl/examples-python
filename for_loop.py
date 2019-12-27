import turtle

qazi_turtle = turtle.Turtle()
qazi_turtle.speed(15)

# Square
def square():
    qazi_turtle.forward(100)
    qazi_turtle.right(90)
    qazi_turtle.forward(100)
    qazi_turtle.right(90)
    qazi_turtle.forward(100)
    qazi_turtle.right(90)
    qazi_turtle.forward(100)

# Circle
def circle():
  for i in range(360):
    qazi_turtle.forward(1)
    qazi_turtle.right(1)

# Typical FOR loop
for i in range(5): # range(starting value = 0 default and not required, max value, step or increment value - not required default 1)
   print(i)        # - it counts in this example -> 0,1,2,3,4 [5], we use range() to loop through a set of code a specified number                  # of times
   qazi_turtle.forward(10)
   circle()
   square()


print("")


# Looping through a string
for x in "pomidory":
  if(x == "p"):
    continue # continue - stops the current iteration and continues with the next
  print(x)
  if(x == "r"):
    break # break - stops the loop

  
print("")


for a in range(2, 10, 2):
  print(a)
else: # else - specifies a block of code to be executed when the loop is finished
  print("Finaly finished range(2, 10, 2)")



for val in range(1, 20, 5):
  pass # we can use pass in for loop to create empty loop
