#! /usr/bin/python3

###! Python Scope

##? Local Scope 
#       * a variable created inside a function is available only inside that function
def myFunc():
    x = 300
    def myInnerFunc():
        print(x) # 'x' can be used in function inside function
    myInnerFunc()

myFunc()
# print(x) # ERROR: name 'x' is not defined



##? Global Scope
#       * a variable created outsied a function is global and can be used by anyone
x = 300

def myFunction():
    print(x)

myFunction()

print(x)



##? Naming variables
#* If you operate with the same variable name inside and outside of a function, Python will treat them as two separate variables, 
# * one available in the global scope (outside the function) and one available in the local scope (inside the function)



##? Global keyword
#       * 'global' keyword makes the variable global
def myFunc2():
    global c
    c = 203

myFunc2()
print(c) # OUTPUT: 203

#       * Also, use the 'global' keyword if you want to make a change to a global variable inside a function.
v = 758

def myFunc3():
    global v 
    v = 700

myFunc3()
print(v)
