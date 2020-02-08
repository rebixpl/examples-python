#! /usr/bin/python3

##? this command checks out the version of python actually using and you need to write that line of code at the top to use python 3
import sys 
print(sys.version_info)

##? input()
myName = input("Please enter your name: ")
myAge = input("What about your age: ")
print("Hello World, my name is ", myName, " and I am ", myAge, " years old.")
print("")



##? printing a long message
print('''Hello world,
My name is James Bond
and I am 20 yrs old. ''')
print("")



##? escape characters
# \n -> prints a newline
print("Hello\nWorld")

# \\ -> prints the backshlash character
print("\\")

# \" -> prints double quote
print("I am 5'9\" tall")

# \' -> pritns single quote
print('I am 5\'9\" tall')

# raw string -> (stops using escape characters)
print(r"Hello\tWorld")
print("")
