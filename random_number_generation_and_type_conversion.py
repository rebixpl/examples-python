def printOut(inputValue):
    print(inputValue)
    print(type(inputValue))
    print()

## TYPE CONVERSION
x = 1 # int
y = 3.14 # float
z = 1j # complex

# int -> float
a = float(x)
printOut(a)

# float -> int
a = int(y)
printOut(a)

# int -> complex
a = complex(x)
printOut(a)




## RANDOM NUMBER - you need to import 'random' first, then use random.randrange(start, stop, step) to generate random number (start is min value and stop is max value to be draw)
import random
print(random.randrange(1, 10))
