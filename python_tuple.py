# PYTHON TUPLES 
#-----------------------------------------------------------------------------------------------------

## Tuple is a collection which is ORDERED and UNCHANGEABLE!
thisistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thisistuple)
print(thisistuple[3:-1]) # you can access tuple elements by using index



## Changing tuple values
#thisistuple[2] = "lettuce" # ERROR: you can't change tuple value, but you can convert tuple into a list and you will be able to change it, then you can convert list into tuple like below:
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "tomato"
x = tuple(y)
print(x)
print(" ")



## Looping through tuple
for x in thisistuple:
    print(x)
print(" ")



## Check if item exists
if "kiwi" in thisistuple:
    print("Yes, 'kiwi' exists in thisistuple.")
else:
    print("No, 'kiwi' does not exist in thisistuple.")



## len(tuple) - prints out how many items a tuple has
print(len(thisistuple))



## Tuple with one item - to create tuple with one item you have to add a COMMA after the item, unless Python will not recognize the variable as a tuple
oneVal = ("apple",) # <-- COMMA HERE BIETCH
print(type(oneVal))



## Remove items - you CANNOT remove items from Tuple cause they're unchangeable, but you can delete the tuple completly
x = ("apple", "banana", "cherry")
#del thisistuple[2] # ERROR: you can't remove item
del thisistuple



## Join two tuples
t1 = ("a", "b", "c")
t2 = (1, 2, 3)
t3 = t1 + t2
print(t3)
print(" ")



## count(value) - return the number of times a specified value appears in the tuple
thisistuple = (1, 2, 3, 3, 4, 4, 4, 5, 1, 6, 7)
x = thisistuple.count(4)
print(x)



## index(value) - finds the first occurrence of the specified value
x = thisistuple.index(5)
print(x)
