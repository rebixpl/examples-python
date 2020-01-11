
##? defining multiple variables at one go
userAge, userName = 30, 'Peter'
print(userAge) # userAge = 30
print(userName) # userName = 'Peter'
print("")



##? interesting operators
x, y = 5, 2
#! Floor division (//):
result = x // y # result = 2 -> (rounds down the answer to the nearest whole number)
print(result)

#! Modulus (%):
result = x % y # result = 1 -> (gives the remainder when 5 is divided by 2)
print(result)

#! Exponent (**):
result = x ** y # result = 25 -> (5 to the power of 2 [5^2])
print(result)
print("")



##? formatting strings using the '%' operator
brand = "Apple"
exchangeRate = 1.2353648345

message = "The price of this %s laptop is %d USD and the exchange rate is %4.2f USD to 1 EUR" %(brand, 1299, exchangeRate)
print(message)

# In the example above, the string 'The price of this %s laptop is %d USD and the exchange rate is %4.2f USD to 1 EUR' is the string that we want to format.
# We use the %s, %d and %4.2f formatters as placeholders in the string.
# These placeholders will be replaced with the variable brand, the value 1299 and the variable exchangeRate respectively, as indicated in the round brackets.
# The %f formatter is used to format floats (numbers with decimals). Here we format it as %4.2f where 4 refers to the total length and 2 refers to 2 decimal places.



##? formatting strings using format()
message = "The price of this {0:s} laptop is {1:d} USD and the exchange rate is {2:4.2f} USD to 1 EUR".format("Apple", 1299, 1.2356838453)
print(message)

'''
The parameter 'Apple' has a position of 0,
1299 has a position of 1 and
1.235235245 has a position of 2.

When we write {0:s}, we are asking the interpreter to replace {0:s} with the parameter in position 0 and that it is a string (because the formatter is 's').

When we write {1:d}, we are referring to the parameter in position 1, which is an integer (formatter is 'd').

When we write {2:4.2f}, we are referring to the parameter in position 2, which is a float and we want it to be formatted with 2 decimal places and a total 
length of 4 (formatter is '4.2f').
'''

# Here we do not have to specify the position of the parameters. The interpreter will replace the curly brackets based on the order of the parameters provided.
message = "The price of this {} laptop is {} USD and the exchange rate is {} USD to 1 EUR".format("Apple", 1299, 1.25534534)
print(message)
print("")



##? creating dictionary using dict() method
userNameAndAge = dict(Peter=38, John=51, Alex=13, Alvin="Not Available")
print(userNameAndAge)



##? adding items to a dictionary
# -> dictionaryName[dictionary key] = data
userNameAndAge["Joe"] = 40
print(userNameAndAge)
print("")
