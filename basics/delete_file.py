#! /usr/bin/python3

#! Python Delete File


#? Delete a file
# to delete file you must import the 'os' module and run its 'os.remove()' function

import os
os.remove("demofiles/deletedemo.txt")



#? Check if file exists

# check if file exists, then delte it
import os
if os.path.exists("demofiles/deletedemo.txt"):
    os.remove("demofiles/deletedemo.txt")
else:
    print("The file does not exist!")



#? Delete a folder
# to delete ENTIRE FOLDER, use the 'os.rmdir()' method
import os 
os.rmdir("myfolder") # removes a folder 
