
##! Python while loops
i = 1
while i < 6:
    print(i)
    i += 1
print("")



#? break statement
i = 1
while i < 6:
    print(i)
    if i == 3:
        break # it stops the loop even if condition is true
    i += 1
print("")



#? continue statement
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue # it stops the CURRENT iteration and continues with the next one
    print(i)
print("")



#? else statement
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6") # this code runs when the condition is no longer true
