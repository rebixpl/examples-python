#! /usr/bin/python3

##! try, except -> this statement controls how the program proceeds when an error occurs
'''
try:
    do something
except:
    do something else when an error occurs
'''

try:
    answer = 12/0
    print(answer)
except:
    print("An error occured!") # you will get an error, because you cannot divide a number by zero

# displaying more specific messages is shown below
try:
    userInput1 = int(input("Please enter a number: "))
    userInput2 = int(input("Please enter another number: "))
    answer = userInput1/userInput2
    print("The answer is ", answer)
    myFile = open("missing.txt", 'r')
except ValueError:
    print("ERROR: You did not enter a number!")
except ZeroDivisionError:
    print("ERROR: Cannot divide by zero!")
except Exception as e:
    print("UNKNOWN ERROR: ", e)



##? pre-defined error messages
# Python also comes with pre-defined error messages for each of the different types of errors. 
# If you want to display the message, you use the as keyword after the error type. 
# For instance, to display the default ValueError message, you write:
 
except ValueError as e:
print (e)
 
# e is the variable name assigned to the error. You can give it some other names, but it is common practice to use e. 
 
except Exception as e:
print ("Unknown error: ", e)
