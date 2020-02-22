#! /usr/bin/python3

#! file_operation


######################? Reading the file

## ? opens the file
f = open("demofiles/myFile.txt", "r") # "r" parameter stands for reading

#* file.readline() -> reads the line of the text from file
firstline = f.readline()
secondline = f.readline()

print(firstline)
print(secondline)

#* removes the '\n' newline between the end of each line
print(firstline, end='')


##? using the loop to read through file
for line in f:
    print(line, end="")


##? closes the file, you should always clsoe the file
f.close()



######################? Writing to the file

f = open("demofiles/myFile.txt", "a") # "a" parameter stands for writing

##? file.write() ->  writes text string to the file
f.write('\n This sentence will be appended.')
f.write('\nPython is Fun!')

f.close()




######################? Opening and Reading Text Files by Buffer Size

inputFile = open('demofiles/myFile.txt', 'r')
outputFile = open('demofiles/myOutputFile.txt', 'w')

#? the value in parenthasis tells the read() function to read only 10 bytes
msg = inputFile.read(10)

#? using while loop to loop through the file 10 bytes at a time
while len(msg):
    outputFile.write(msg)
    msg = inputFile.read(10)

inputFile.close()
outputFile.close()




########################? Opening, Reading and Writing Binary Files
# Binary file refer to any file that in non text, such as image or video files.

# opens a image 
inputFile = open('demofiles/myImage.jpg', 'rb') # "rb" stands for 'read bianry'
outputFile = open('demofiles/myOutputImage.jpg', 'wb') # "wb" stands for 'write binary'
 
#! soemthign doesnot work idk what whatever
# while len(msg):
#   outputFile.write(msg)   

inputFile.close()
outputFile.close()




#######################? Deleting and Renaming Files
import os

#? removing a file -> remove(path)
os.remove("demofiles/myOutputImage.jpg")

#? renaming a file -> rename(old name, new name)
os.rename('demofiles/myImage.jpg', 'demofiles/myNewImage.jpg')
