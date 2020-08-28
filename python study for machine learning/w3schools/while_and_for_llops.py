# WHILE LOOPS ########################################################
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

###################
print("")
###################

# CONTINUE STATEMENT
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

# OUTPUT:
# 1
# 2 # note there is no 3
# 4
# 5
# 6

###################
print("")
###################

# The else Statement
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

# OUTPUT:
# 1
# 2
# 3
# 4
# 5
# i is no longer less than 6

# FOR LOOPS #############################################################
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)


print("")

# Looping through a string
for x in "succ":
    print(x)

# OUTPUT:
# s
# u
# c
# c

# Range() function
# With range() function we can loop through code specified ammount of times:

for x in range(4):
    print(x)

# OUTPUT:
# 0
# 1
# 2
# 3

# Else in for loop
# The else keyword in a for loop specifies a block of code to be
# executed when the loop is finished:
for x in range(3):
    print(x)
else:
    print("finished!")

# NESTED LOOPS
adj = ["red", "big", "tasty"]
fruits = ["apple", "kiwi", "dick"]

for x in adj:
    for y in fruits:
        print(x, y)

# OUTPUT:
# red apple
# red kiwi
# red dick
# big apple
# big kiwi
# big dick
# tasty apple
# tasty kiwi
# tasty dick

# The pass statement
for x in [0, 1, 2]:
    pass

# Program to add natural
# numbers up to 
# sum = 1+2+3+...+n

n = int(input("Enter n: "))
sum = 0
counter = 1

while counter <= n:
    sum  += counter
    counter += 1
    print(sum)
else:
    print("while loop has ended")
    
print("The sum is", sum)