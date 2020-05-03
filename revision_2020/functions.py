#! Function

# def function_name(arguments):
#       function code suite

movies2 = ["The Holy Grail", 1975, "The Life of Brian", 1979,
["Graham Champman",["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle"]]]

def print_lol(the_list):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item)
        else:
            print(each_item)

print_lol(movies2)
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