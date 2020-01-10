
##! Python Conditions

##? Elif, else
a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b: # elif is short for "else if"
    print("a and b are equal")
else:
    print("a is greater than b")



##? Short hand IF
a = 200
b = 33
if a > b: print("a is greater than b")
print("")



##? And
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")



##? Or
if a > b or a > c:
    print("At least one of the conditions is True")
print("")



##? Nested IF
x = 41
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")
print("")



##? pass statement
a = 33
b = 200

if b > a:
    pass # if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error
