#! /usr/bin/python3

#! File Handling
#? The basic function to work with files in python is 'open()' function
#? SYNTAX -> open("filename","mode") (default mode is "rt")

#? There are four different methods (modes) for opening a file:
# - "r" - read - deafult value, opens a file for reading, error if the file does not exist
# - "a" - append - opens a file for appending, creates the file if it does not exist
# - "w" - write - opens a file for writing, creates the file if it does not exist
# - "x" - create - creates the specified file, returns the error if the file exists

# - "t" - text - default value, text mode
# - "b" - binary - binary mode (e.g. images)



#? SYNTAX
f = open("demofile.txt")

# the code above is the same as
f = open("demofile.txt", "rt") # ("rt" are defaults)
