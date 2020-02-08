#! /usr/bin/python3

#! Python File Write


#? Write to an Existing File
# To write to an existing file, you must add a parameter to the open() function:
# - "a" - append - will append to the end of the file
# - "w" - write - will overwrite any existing content

f = open("demofiles/demofile2.txt", "a")
f.write("Now the file has more content!") # you write to a file by using file.write("content")
f.close()
f = open("demofiles/demofile2.txt", "r") # open file to read after appending
print(f.read())

print(" ")

# overwriting the content of the file
f = open("demofiles/demofile2.txt", "w")
f.write("Whoops! I've deleted the content!")
f.close()
f = open("demofiles/demofile2.txt", "r") # open file to read after overwriting
print(f.read())



#? Create a New File
# To create a new file in Python, use the open() method, with one of the following parameters:
# - "x" - create - will create a file, returns an error if the fiel exists
# - "a" - append - will create a file if the specified file does not exist
# - "w" - Write - will create a file if the specified file does not exist

f = open("myFile.txt", "x") # a new empty file is created!

f = open("myFile.txt", "w") # create a new file if it does not exist!
