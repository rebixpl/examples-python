#! /usr/bin/python3

#! Python File Open



#? Open a File on the Server
f = open("demofiles/demofile1.txt", "r")
print(f.read()) # read() method reads the content of the file



#? Read Only Parts of the File -> file.read(number_of_characters_to_read)
f = open("demofiles/demofile1.txt", "r")
print(f.read(5)) # OUTPUT: Hello



#? Read Lines
# you can return one line by using file.readline() function
f = open("demofiles/demofile1.txt", "r")
print(f.readline())

# you can read multiple lines by calling readline() multiple times :)
print(f.readline())
print(f.readline())

# you can read whole file by looping through it
f = open("demofiles/demofile1.txt", "r")
for x in f:
    print(x)



#? Close files -> YOU SHULD ALWAYS CLOSE YOUR FILES WHEN YOU ARE DONE WITH THEM
# SYNTAX -> file.close()
f = open("demofiles/demofile1.txt", "r")
print(f.readline())
f.close()
