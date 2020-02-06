#! /usr/bin/python3

##! Arrays in python
# An array is a special variable, which can hold more than one value at a time.
cars = ["Ford", "Volvo", "BMW", "Tesla"]



##? Getting value of the array item
x = cars[0] # array[index]
print(x)



##? Modifying the value of item in array
cars[0] = "Toyota"
print(cars)



##? getting the length of an array
x = len(cars) # len(array)
print(x)



##? looping array elements
for x in cars:
    print(x)
print("")



##? adding array elements
cars.append("Honda") # array.append(new item)
print(cars)



##? removing array elements
cars.pop(1) # array.pop(index)
print(cars)

cars.remove("Tesla") # array.remove("item name")
print(cars)
