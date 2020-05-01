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
