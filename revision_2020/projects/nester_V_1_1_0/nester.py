
""" This is the “nester.py" module, and it provides one function called
print_lol() which prints lists that may or may not include nested lists. """


def print_lol(the_list, indent=False, level=0):
    """To turn a required argument to a function into an optional argument, provide
    the argument with a default value. When no argument value is provided, the
    default value is used. When an argument value is provided, it is used instead
    of the default. The key point is, of course, that the default value for the
    argument effectively makes the argument optional."""

    """This function takes a positional argument called “the_list", which is any
    Python list (of, possibly, nested lists). Each data item in the provided list
    is (recursively) printed to the screen on its own line. A second argument called 
    “level" is used to insert tab-stops when a nested list is encountered"""
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, indent,  level+1)
        else:
            if indent: # this is shorter version of | if indent == True
                for tab_stop in range(level):
                    print("\t", end='')
            print(each_item)


# ------------------------------------------------------------------
# #! Usage of range(x):
# for num in range(5):
#     print(num)

# OUTPUT:
# 0
# 1
# 2
# 3
# 4
