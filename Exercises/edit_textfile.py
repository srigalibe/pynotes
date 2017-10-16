# Insert a string after a word in a specific line of a text file

"""

Input file
line 1: value1
line 2: value2
line 3: value3
line 4: value4
line 5: value5

Insert, for example, "NAME" in the line number 3 just after "line" so
the file would become:

Output file
line 1: value1
line 2: value2
line NAME 3: value3
line 4: value4
line 5: value5

"""

def insert_string(in_file, line, insertion):
    """ Return a list of lines after inserting a word in a specific line. """

    # your code here


def write_to(outfile, from_infile):
    """ Write to a new file lines returned by the above function """

    # your code here
