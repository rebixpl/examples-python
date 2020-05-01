
#! isinstance() -> it lets you check if a
#! specific identifier holds data of a specific type

names = ["Michael", "Amanda", "Trevor"]
#? Ask if “names” is a list (it is).
print(isinstance(names, list)) # OUTPUT:True

num_names = len(names)
#? Ask if “num_names” is a list (it isn’t).
print(isinstance(num_names, list)) # OUTPUT: False
