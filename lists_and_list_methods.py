# This is a LIST
listZero = [1, 2, "string", 5.3, True, [32,3,53]]
print(listZero[2]) # You can access list using index,
print(listZero[-1]) # Negative indexes works too. (it starts from the end)
print(listZero[2:4]) # You can specify range of the indexes as well
print(listZero[:3])
print(listZero[3:])



# You can change the value of the list by using index:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "pear"
print(thislist)



## append(item) - adds item to the END if the list
names = ["Joe", "John", "James007"]
names.append("Gary")
print(names)
print(' ')



## insert(index, item) - adds an item at specified index
names = ["Mark", "John"]
names.insert(1, "Adolf")
print(names) # output: ["Mark", "Adolf", "John"]



## remove(item) - removes the specified item
names.remove("Adolf")
print(names)



## pop(index - deafult is last element) - removes the specified index
letters = ["a", "b", "c", "d"]
letters.pop(2)
print(letters)



## del - this keyword removes the specified index, it can also remove the list completly
myList = ["apple", "banana", "cherry"]
del myList[2]
print(myList)

del myList # entirely deletes list



## clear() - clears (empties) the list
myList = ["apple", "banana", "cherry"]
myList.clear()
print(myList)
print(" ")



## reverse() - reverses the order of the list
names = ["Adam", "Robert", "Adolf"]
names.reverse()
print(names)



## sort() - sorts the list alphabetically
cars = ["Ford", "BMW", "Volvo"]
cars.sort()
print(cars)

numbers = [6, 2, 3, 9, 1]
numbers.sort()
print(numbers) # output: 1, 2, 3, 6, 9



## LOOP THROUGH A LIST using FOR loop
myLetters = ["a", "b", "c", "f", "r", "q", "p", "l"]
for x in myLetters:
    print(x)



## CHECK IF ITEM EXISTS
if "g" in myLetters:
    print("Yes, 'g' is in the myLetters list.")
else:
    print("No, that item does not exist!")



## len(list) - prints the numer of items in the list
print(len(myLetters))



# COPY A LIST
## copy() - makes a copy of the list
thisList = ["apple", "banana", "cherry"]
myList = thisList.copy()
print(myList)
print(" ")

## list(list to copy from) - it is another way of making copy of the list
thisList = ["apple", "banana", "cherry"]
copy = list(thisList)
print(copy)



# JOIN TWO LISTS
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)
print(" ")

#This is the other way of joining lists:
for x in list2:
    list1.append(x)
print(list1)



# extend(list) - it adds list to the list
liczby = [1,2]
liczby.extend([4, 3, 52, 523, 6, 7])
print(liczby)

# you can add another list that way as well
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list1.extend(list2) 
print(list1)
print(" ")



## count(value searched for) - returns how many times the value appears in list
points = [1, 4, 2, 9, 7, 8, 9, 3, 1]
print(points.count(9))
