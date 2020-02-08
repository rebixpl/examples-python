# This is a string
s = "helo world" 
s2 = 'hello world'

print(s[1]) # index of s string/variable we put in - variable[index] (gets character at position index)


# You can create MULTILINE STRING by using three double quotes (""") or three singe quotes (''')
veryLongStr = """this is very very
long string and i would paste there
some shit: Lorem ipsum dolor sit amet,
consectetur adipiscing elit, sed do 
eiusmod tempor incididunt ut labore 
et dolore magna aliqua."""

print(veryLongStr)
print(" ")


# SLICING
print(veryLongStr[19:32]) # get the characters from position 19 to position 32(not included)


# NEGATIVE INDEXING
print(s[-7:-2]) # Use negative indexes to start the slice from the END of the string
print(" ")


# STRING LENGTH
print(len(veryLongStr)) # len(string) - returns the length of the string (in characters)
print(" ")



# STRING METHODS

## strip() - removes any whitespaces from the beginning or the end of string 
a = " Hello, World! "
print(a.strip()) # output: "Hello, World!"

## lower() - resturns string in lower case
a = "HELLO, WORLD!"
print(a.lower()) # output: "hello, world!"

## upper() - returns the string in upper case
a = "hello, world!"
print(a.upper()) # output: "HELLO, WORLD!"

## replace() - replaces a string with another string
print(a.replace("l", "x")) # string.replace("string for replace","string replacement")

## split() - this method splits the string into substrings if it finds instances of the separator
print(a.split(",")) # string.split("separator") # output: "['hello', 'world!']"



#CHECK STRING - IN or NOT IN 
txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt # check if the phrase "ain" is present in the following text
print(x)

x = "ain" not in txt # check if the phrase "ain" is NOT present in the following text
print(x)

print(" ")



# STRING COMBINING
a = "Hello, "
b = "World!"
c = a + b
print(c)
print(" ")



# format() method inserts numbers into strings
quantity = 3
itemno = 567
price = 49.95
myOrder = "I want {0} pieces of item {1} for {2} dollars." # {} - this is placeholder for number
print(myOrder.format(quantity, itemno, price)) # myOrder.format(0, 1, 2, ...) - you give here values to insert into placeholders



# Placing double quotes "" inside string
txt = "We are the so-called \"Vikings\" from the north"
print(" ")
print(txt)



