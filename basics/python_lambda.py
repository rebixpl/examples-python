#! /usr/bin/python3

##! Python Lambda -> lambda function is anonymous function, it can take any number of arguments, but can only have one expression
# -> lambda arguments : expression
x = lambda a : a + 10
print(x(5)) # output: 15

x = lambda a,b : a*b
print(x(5, 6)) # output: 30

x = lambda a,b,c : a+b+c
print(x(5, 6, 2)) # output: 13



##? lambda inside function
def myFunc(n):
    return lambda a : a*n

myDoubler = myFunc(2)
myTripler = myFunc(3)

print(myDoubler(11)) # output: 22
print(myTripler(11)) # output: 33
