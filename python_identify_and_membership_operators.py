## PYTHON IDENTITY OPERATORS
x = "abc"
z = "abc"
print(x is z) # Returns TRUE if both variables are the same objects
print(x is not z) # Returns TRUE if both variables are NOT the same object



## PYTHON MEMBERSHIP OPERATORS
x = ["apple", "banana"]
print("pineapple" in x) # Returns True if a sequence with the specified value is present in the object
print("pineapple" not in x) # Returns True if a sequence with the specified value is not present in the object
