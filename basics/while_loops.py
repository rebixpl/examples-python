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


qazi = 'happy'
while qazi == 'happy':
    qazi_turtle.forward(10)
    qazi = 'sad'

# The WHILE loop
i = 0
while i < 6:
    i += 1
    if i == 2:
        continue  # continue statement stop the current iteration, and continues with the next
    if i == 4:
        break  # the break statement can stop the loop even if the while condition is true
    square()
    print(i)
else:  # else statement we can run a block of code once when the condition no longer is true
    print("i is no longer less than 6")
