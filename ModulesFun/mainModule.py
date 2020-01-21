#! /usr/bin/python3

###! Python Modules
#       * a module is the same as a code library
#       * to create a module just safe python code in a file with a '.py' extension

##? Use a module
import myModule
myModule.greeting("Jonathan")



##? Variables in module
import myModule2
a = myModule2.person1["age"]
print(a) # OUTPUT: 34



##? Re-naming a module
#       * you cancreate an alias when you import a module by using the as keyword:
import myModule2 as mm2 
n = mm2.person1["name"]
print(n)



##? Build-in modules
# importing platform module for example
import platform
m = platform.system()
print(m)



##? dir() function
#       * this function shows all the function names in a module
import platform
a = dir(platform)
print("")
print(a)
print("")



##? Import From module
#       * You can choose to import only parts from a module, by using the 'from' keyword.
from myModule3 import person2

print(person2["name"])