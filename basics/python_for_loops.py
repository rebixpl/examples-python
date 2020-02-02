
##! python FOR loops

#? looping through a list
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
print("")



#? looping through a string
for x in "banana":
    print(x)
print("")



#? break statement
for x in fruits:
    print(x)
    if x == "banana":
        break
print("")



#? continue statement
for x in fruits:
    if x == "banana":
        continue
    print(x)
print("")



#? range() function -> To loop through a set of code a specified number of times, we can use the range() function
for x in range(6):
    print(x)
print("")

for x in range(2, 30, 3): # range(start, stop, step)
    print(x)
print("")



#? else in for loop
for x in range(6):
    print(x)
else: # The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
    print("finally finished!")
print("")



#? nested for loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)
print("")



#? pass statement
for x in [0, 1, 2]:
    pass
