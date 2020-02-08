#! /usr/bin/python3

###! Importing modules
##? import moduleName
import random

##? using function from module
#? moduleName.function()
random.randrange(1, 10)

##? making name of module shorter
#? import moduleName as shortName
import random as r
r.randrange(1, 10)

##? importing functions from the module
#? from moduleName import name1, name2, nameN..
from random import randrange, randint
#   *To use this function you dont need to write the dot notation, just write function()
randint(2, 32)



###! Defining functions
def checkIfPrime(numberToCheck):
    for x in range(2, numberToCheck):
        if numberToCheck % x == 0:
            return False
    return True

answer = checkIfPrime(13)
print(answer)
print("")



###! Python lambda
##? A lambda function is a small anonymous function and it have only one expression
##* lambda arguments : expression

x = lambda a : a + 10
print(x(23)) # OUTPUT: 33

x = lambda a, b : a * b
print(x(5, 6)) # OUTPUT: 30
print("")



###! Python randint()

##? First you need to import random module
import random

##? then you can generate random integers -> random.randint(min value, max value)
randomInt = random.randint(1, 23)
print(randomInt)

##? you can generate random float value using -> random.random() (it does not require max or min value)
randomFloat = random.random();
print(randomFloat)
