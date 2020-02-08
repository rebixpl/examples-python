#! /usr/bin/python3

#! Python String Formatting



#? The format() method -> format() method allows you to format selected parts of a string
price = 49
txt = "The price is {} dollars"
print(txt.format(price)) # OUTPUT: The price is 49 dollars

#? You can add parameters inside the curly brackets to specify how to convert the value
txt = "The price is {:.2f} dollars"
print(txt.format(price)) # OUTPUT:  The price is 49.00  dollars

#? the same with multiple values
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity,itemno,price))



#? You can use index numbers to be sure that values are placed correctly
age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age,name)) # OUTPUT: His name is John. John is 36 years old.



#? You can also use named indexes by entering a name inside the curly brackets
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang")) # OUTPUT: I have a Ford, It is a Mustang.
