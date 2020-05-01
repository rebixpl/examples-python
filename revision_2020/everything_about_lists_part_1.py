movies = ["The Holy Grail", "The Life Of Brian", "Wolf From Grove Street Home"]

print(movies[2]) # OUTPUT: Wolf From Grove Street Home

print(movies) # OUTPUT: ['The Holy Grail', 'The Life Of Brian', 'Wolf From Grove Street Home']

print(len(movies)) #OUTPUT: 3

#-------------------------------

cast = ["Cleese", 'Palin', 'Jones', "Idle"]

#! Deletes last item in list
cast.pop()
print(cast) # OUTPUT: ['Cleese', 'Palin', 'Jones']

#! Adds one item to the end of the list
cast.append("Janusz") 
print(cast) # OUTPUT: ['Cleese', 'Palin', 'Jones', 'Janusz']

#! Adds Multiple items to the end of the list
cast.extend(["Rejmund", "Twoj Stary"]) # Extend powiększa listę o listę
print(cast) # OUTPUT: ['Cleese', 'Palin', 'Jones', 'Janusz', 'Rejmund', 'Twoj Stary']

#! removes specifi3e item
cast.remove("Rejmund") 
print(cast) # OUTPUT: ['Cleese', 'Palin', 'Jones', 'Janusz', 'Twoj Stary']

#! inserts data to specified index of list
cast.insert(1, "Powerful Space Laser Beam")
print(cast) # OUTPUT: ['Cleese', 'Powerful Space Laser Beam', 'Palin', 'Jones', 'Janusz', 'Twoj Stary']

print("")
print("")
#--------------------------------------------------
#! Using for x in y:
movies = ["The Holy Grail", 1975, "The Life of Brian", 1979, "The Meaning of Life", 1983]
for eachMovie in movies:
    print(eachMovie)

#   OUTPUT:
# The Holy Grail
# 1975
# The Life of Brian
# 1979
# The Meaning of Life
# 1983

#! Nested lists
movies2 = ["The Holy Grail", 1975, "The Life of Brian", 1979,
["Graham Champman",["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle"]]]

print(movies2[4][1][3]) # OUTPUT: Eric Idle

print("")
print("")

for allahuAkbar in movies2:
    print(allahuAkbar)

# OUTPUT: 
# The Holy Grail
# 1975
# The Life of Brian
# 1979
# ['Graham Champman', ['Michael Palin', 'John Cleese', 'Terry Gilliam', 'Eric Idle']]

print("")
print("")

#---------------------------------------------------
#! isinstance() -> it lets you check if a
#! specific identifier holds data of a specific type

names = ["Michael", "Amanda", "Trevor"]
#? Ask if “names” is a list (it is).
print(isinstance(names, list)) # OUTPUT:True

num_names = len(names)
#? Ask if “num_names” is a list (it isn’t).
print(isinstance(num_names, list)) # OUTPUT: False

print("")
print("")

#------------------------------------------------
#! Nested lists
for each_item in movies2:
    if isinstance(each_item, list):
        for nested_item in each_item:
            print(nested_item)
    else:
        print(each_item)

# OUTPUT:
# The Holy Grail
# 1975
# The Life of Brian
# 1979
# Graham Champman # This is a little better, but not by much…there’s another nested list here that’s not being processed properly.
# ['Michael Palin', 'John Cleese', 'Terry Gilliam', 'Eric Idle']

print("")
print("")

for each_item in movies2:
    if isinstance(each_item, list):
        for nested_item in each_item:
            if isinstance(nested_item, list):
                for deeper_item in nested_item:
                    print(deeper_item)
            else:
             print(nested_item)
    else:
        print(each_item)

# OUTPUT: 
# The Holy Grail
# 1975
# The Life of Brian
# 1979
# Graham Champman
# Michael Palin
# John Cleese
# Terry Gilliam
# Eric Idle