#! /usr/bin/python3

def check_match(x):
    if (x):
        print("Yes, there is at least one match!")
    else:
        print("No match")

###! Python RegEx
#       * it forms a search pattern
#       * it can be used to check if a string contains the specified search pattern

##? RegEx Module
import re  # importing RegEx

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

check_match(x)



##? Metacharacters
txt = "The rain in Spain falls mainly in the plain!"

#*   [] -> A set of characters ->  "[a-m]"
# Find all lower case characters alphabetically between "a" and "m":
x = re.findall("[a-m]", txt)
print(x)
check_match(x)

#*   \    -> Signals a special sequence (can be used to escape characters) -> "\d"
txt2 = "That will be 59 dollars"
# Find all digit characters:
x = re.findall("\d", txt2)
print(x)

#*  .    -> Any character -> "he..o"
#*   ^    -> Starts with  ->"^hello"
#*   $    -> Ends with -> "world$"
#*  *    -> Zero or more occurences -> "aix*"
# Check if the string contains "ai" followed by 0 or more "x" characters:
x = re.findall("aix*", txt)
print(x)
check_match(x)

#*  +   -> One or more occurences   -> "aix+"
# Check if the string contains "ai" followed by 1 or more "x" characters:
x = re.findall("aix+", txt)
print(x)
check_match(x)

#*  {}  -> Exactly the specified number of occurences -> "al{2}"
# Check if the string contains "a" followed by exactly two "l" characters:
x = re.findall("al{2}", txt)
print(x)
check_match(x)

#*  |   -> Either or -> "falls|stays"
# Check if the string contains either "falls" or "stays":
x = re.findall("falls|stays", txt)
print (x)
check_match(x)

#* ()   -> Capture and group



##? Special Sequences
print("")
txt = "The rain in Spain"

#*  \A  -> Returns a match if the specified characters are at the beginning of the string -> "\AThe"
#* \b   -> Returns a match where the specified characters are at the beginning or at the end of a word -> r"\bain" OR r"ain\b"
#*  \B  -> Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word ->  r"\Bain" OR r"ain\B"
# Check if "ain" is present, but NOT at the beginning of a word:
x = re.findall(r"\Bain", txt)
print(x)
check_match(x) # OUTPUT: ['ain', 'ain'], Yes, there is at least one match!

#*  \d  -> Returns a match where the string contains digits (numbers from 0-9)-> "\d"
#*  \D  -> Returns a match where the string DOES NOT contain digits -> "\D"
#*  \s  -> Returns a match where the string contains a white space character  -> "\s"
# Return a match at every white-space character:
x = re.findall("\s", txt)
print(x)
check_match(x) # OUTPUT: [' ', ' ', ' '], Yes, there is at least one match!

#*  \S  -> Returns a match where the string DOES NOT contain a white space character -> "\S"
#*  \w  -> Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character) -> "\w"
# Return a match at every word character (characters from a to Z, digits from 0-9, and the underscore _ character):
x = re.findall("\w", txt)
print(x)
check_match(x) # OUTPUT: ['T', 'h', 'e', 'r', 'a', 'i', 'n', 'i', 'n', 'S', 'p', 'a', 'i', 'n'], Yes, there is at least one match!

#*  \W  -> Returns a match where the string DOES NOT contain any word characters -> "\W"
#*  \Z  -> Returns a match if the specified characters are at the end of the string -> "Spain\Z"
# Check if the string ends with "Spain":
x = re.findall("Spain\Z", txt)
print(x)
check_match(x) # OUTPUT: ['Spain'],There is a match!



##? Sets
print("")
txt = "The rain in Spain"

#*  [arn]   -> Returns a match where one of the specified characters (a, r, or n) are present
#* [a-n]    -> Returns a match for any lower case character, alphabetically between a and n
#* [^arn]  -> Returns a match for any character EXCEPT a, r, and n
# Check if the string has other characters than a, r, or n:
x = re.findall("[^arn]", txt)
print(x)
check_match(x) # OUTPUT: ['T', 'h', 'e', ' ', 'i', ' ', 'i', ' ', 'S', 'p', 'i'], Yes, there is at least one match!

#* [0123]   -> Returns a match where any of the specified digits (0, 1, 2, or 3) are present
#* [0-9]    -> Returns a match for any digit between 0 and 9
txt2 = "8 times before 11:45 AM"
# Check if the string has any digits:
x = re.findall("[0-9]", txt2)
print(x)
check_match(x) # OUTPUT: ['8', '1', '1', '4', '5'], Yes, there is at least one match!

#* [0-5][0-9]   -> Returns a match for any two-digit numbers from 00 and 59
# Check if the string has any two-digit numbers, from 00 to 59:
x = re.findall("[0-5][0-9]", txt2)
print(x)
check_match(x) # OUTPUT: ['11', '45'], Yes, there is at least one match!

#* [a-zA-Z] -> Returns a match for any character alphabetically between a and z, lower case OR upper case
# Check if the string has any characters from a to z lower case, and A to Z upper case:
x = re.findall("[a-zA-Z]", txt2)
print(x)
check_match(x) # OUTPUT: ['t', 'i', 'm', 'e', 's', 'b', 'e', 'f', 'o', 'r', 'e', 'A', 'M'], Yes, there is at least one match!

#* [+]  -> In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string
# Check if the string has any + characters:
x = re.findall("[+]", txt2)
print(x)
check_match(x) # OUTPUT: [], No match
print("")



##? findall() Function
#       * it returns a list containing all matches

import re 

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x) # OUTPUT: ['ai', 'ai']



##? search() Function
#       * searches the string for match and returns a Match object

import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located  in position: ", x.start())



##? split() Function
#       * returns a list where the string has been split at each match

import re 

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x) # OUTPUT: ['The', 'rain', 'in', 'Spain']



##? sub() Function
#       * replaces the matches with text of your choice

import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x) # OUTPUT: The9rain9in9Spain

#       * You can control the number of replacements by specifying the 'count' parameter:
x = re.sub("\s", "9", txt, 2)
print(x) # OUTPUT: The9rain9in Spain



##? Match Object
#       * this is an object containing information about the search and result

import re

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) # this will print an object


#* .span() -> returns a tuple containing the start-, and end positions of the match
# Search for an upper case "S" character in the beginning of a word, and print its position:
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span()) # OUTPUT: (12, 17)


#* .string -> returns the string passed into the function
# The string property returns the search string:
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string) # OUTPUT: The rain in Spain


#* .group() -> returns the part of the string where there was a match
# Search for an upper case "S" character in the beginning of a word, and print the word:
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
x = x.group()
print(x) # OUTPUT: Spain
