import sys
import example
import example as adder  # We can import a module by renaming it
# We can import specific names from a module without importing the module as a whole.
from math import pi, e


result = example.addTwoNumbers(23, 7)
resultAdder = adder.addTwoNumbers(25, 7.3)
print(result)
print(resultAdder)
print("pi = ", pi, " e = ", e)

# print(sys.path)

# We can use the dir() function to find out names that are defined inside a module.
print(dir(example))

# For example, the __name__ attribute contains the name of the module.

print(example.__name__)
