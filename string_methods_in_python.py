# STRING METHODS IN PYTHON

## capitalize() - upper case the FIRST letter in sentence (string)
txt = "hello, im not from Earth."
x = txt.capitalize()
print(x)


## casefold() - makes the string lower case (its stronger, more aggresive that lower())
txt = "Hello, And Welcome To mY WoRlD!"
x = txt.casefold()
print(x)


## center(length, character - not required default is space) - centers the word(string) or in other words makes it appear in the middle, taking up the space of 'length' characters gived in 'character'
txt = "tomato"
x = txt.center(30, '.')
print(x) # output: ..............tomato...............


## count(valueToSearch, start - optional this is positon to start the search, end - optinal this is position to end the search) - returns the number of times a specified value appears in the string 
txt = "I love apples, apples are my favourite fruit. My family has apple orchard with many apple trees and as I like apples very much i enjoy eating all of the apples in our apple orchard. XD"
x = txt.count("apple")
print(x) # there are 7 apples


## endswitch(value, start optional its position to start search, end optional its position to end search) - returns True if the string ends with the specified 'value', otherwise False
txt = "Hello, welcome to my world!"
x = txt.endswith("world!")
print(x)
print(" ")


## expandtabs(tabsize) - sets the tab size to the specified number of whitespaces
txt = "h\te\tl\tl\to" # \t - its tab inside string 
print(txt)
print(txt.expandtabs(2))
print(txt.expandtabs(8))
print(" ")


## find(value - the value searched for, start, end) - finds first occurrence of the specified value and returns index
txt = "Hello, welcome to my world."
x = txt.find('o')
print(x)


## index(value - the value searched for, start, end) - it works in the same way like find() which is described up
x = txt.index('o')
print(x)


## format() method inserts numbers into strings
quantity = 3
itemno = 567
price = 49.95
myOrder = "I want {0} pieces of item {1} for {2} dollars." # {} - this is placeholder for number
print(myOrder.format(quantity, itemno, price)) # myOrder.format(0, 1, 2, ...) - you give here values to insert into placeholders


# isalnum() - returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9)
# Example of characters that are NOT alphanumeric: (space)!#%&.,? etc
txt = "CompanyNr.7"
print(txt.isalnum())


## isalpha() - returns True if all the characters are alphabet letters (a-z)
txt = "thisIsAlphabetString"
print(txt.isalpha())


## isdecimal() AND isdigit() AND isnumeric() - these methods returns True if all the characters are decimals (0-9) unicodes works as well
txt = "2"
txt2 = "\u0033" # unicode for 3
print(txt.isdecimal()) # true
print(txt2.isdecimal()) # true as well
print(txt.isdigit())
print(txt2.isdigit())
print(txt.isnumeric())
print(txt2.isnumeric())
print(" ")


## isidentifier() - returns True if the string is a valid identifier, otherwise False
# A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_). A valid identifier CANNOT start with a number, or contain any spaces.
a = "myFolder"
b = "Package002"
c = "4chan"
d = "my folder"
print(a.isidentifier()) # True
print(b.isidentifier()) # True
print(c.isidentifier()) # False
print(d.isidentifier()) # False
print(" ")


## islower() - returns True if all the characters are in lower case, otherwise False
a = "Hello world!"
b = "my name is Adolf"
c = "hehh 997ś"
print(a.islower()) # False
print(b.islower()) # False
print(c.islower()) # True, so numbers, symbols and spaces are not checked
print(' ')


## istitle() - returns True if all words in a text start with a upper case letter, AND the rest of the word are lower case letters, otherwise False
txt = "Hello, And Welcome To My World Nr 23!" # Symbols and numbers are ignored.
print(txt.istitle())


## isupper() - return True if all the characters are in upper case, otherwise False
txt = "HELLO EARTH"
print(txt.isupper())


## title() - makes the first letter in each word uppercase
txt = "Welcome to my world"
x = txt.title()
print(x) # output: "Welcome To My World"


## swapcase() - makes the lower case letters upper case and the upper case letters lower case
txt = "hello my NAME is ADOLF"
x = txt.swapcase()
print(x)


## strip(charcater - default is space so its optional) - removes any specified characters at he beginning and the end of string
txt = "....r...r...banana...r....."
x = txt.strip(".r")
print(x) # output: banana


## startswith(value, start, end) - returns True if the string starts with the specified value, otherwise False
txt = "Hello, welcome to my world."
print(txt.startswith("Hello"))


## zfill(len) - adds zeros (0) at the beginning of the string, until it reaches the specified length
txt = "50"
x = txt.zfill(10)
print(x) # output: 0000000050
