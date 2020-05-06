
import os

#! Managing the files
# the_file = open('path_to_data_file.txt') # Open
# Do something with the data
# in 'the_file'
# the_file.close() # Close

# ?--------------------------------------------------------------
file_path = 'projects\HeadFirstPython\chapter3\sketch.txt'

# Check whether the file exists.
if os.path.exists(file_path):
    data = open(file_path) # opening the data file
    print(data.readline(), end='')  # printing one line of data
    # Output: Man: Is this the right room for an argument?
    print(data.readline(), end='')
    # Output: Other Man: I've told you once.

    print("")

    # Use the “seek()” method to return to the start of the file.
    data.seek(0)

    # Every line of the data is displayed on screen
    for each_line in data:

        try:
            """
            The split() method returns a list of strings, which are assigned to a list of
            target identifiers. This is known as multiple assignment:
            """
            (role, line_spoken) = each_line.split(
                ':', 1)  # The extra argument controls how “split()” splits. ( in how many parts it splits )
            print(role, end='')
            print(' said: ', end='')
            print(line_spoken, end='')
        except ValueError:
            pass

    """ OUTPUT: 
    Man: Is this the right room for an argument?
    Other Man: I've told you once.

    Man said:  Is this the right room for an argument?
    Other Man said:  I've told you once.
    Man said:  No you haven't!
    Other Man said:  Yes I have.
    Man said:  When?
    Other Man said:  Just now.
    Man said:  No you didn't!
    Other Man said:  Yes I did!
    Man said:  You didn't!
    Other Man said:  I'm telling you, I did!
    Man said:  You did not!
    Other Man said:  Oh I'm sorry, is this a five minute argument, or the full half hour?
    Man said:  Ah! (taking out his wallet and paying) Just the five minutes.
    Other Man said:  Just the five minutes. Thank you.
    Other Man said:  Anyway, I did.
    Man said:  You most certainly did not!
    Other Man said:  Now let's get one thing quite clear: I most definitely told you!
    Man said:  Oh no you didn't!
    Other Man said:  Oh yes I did!
    Man said:  Oh no you didn't!
    Other Man said:  Oh yes I did!
    Man said:  Oh look, this isn't an argument!
    Other Man said:  Yes it is!
    Man said:  No it isn't!
    Man said:  It's just contradiction!
    Other Man said:  No it isn't!
    Man said:  It IS!
    Other Man said:  It is NOT!
    Man said:  You just contradicted me!
    Other Man said:  No I didn't!
    Man said:  You DID!
    Other Man said:  No no no!
    Man said:  You did just then!
    Other Man said:  Nonsense!
    Man said:  (exasperated) Oh, this is futile!!
    Other Man said:  No it isn't!
    Man said:  Yes it is!
    """
    # Closing the File
    data.close()
else:
    print("The data file is missing")
