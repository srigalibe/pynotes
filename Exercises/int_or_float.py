# Check if a string is an integer or a float.
# Consider it a float if it has any non-zero digits.
# For example, 3 and 3.0 are ints, but 3.002 is a float.

"""
For this exercise, define two functions.
One checks if an input string is an int.
The other checks if an input string is a float.
"""

def is_int(n):
    """ Return True if n is an integer.

    >>> is_int('3.0')
    True
    >>> is_int('3.002')
    False
    """

    # your code here

    
def is_float(n):
    """ Return True if n is a float.

    >>> is_float('3.0')
    >>> False
    >>> is_float('3.002')
    >>> True
    """

    # your code here


# Testing the functions

"""
nums = ['12', '12.3', '12.0', '123.002']

for num in nums:
    if is_int(num):
        print("{} can be safely converted to an integer.".format(num))
    elif is_float(num):
        print("{} is a float with non-zero digit(s) in the fractional-part.".format(num))
"""

# When your functions are ready, run the above loop. It should print:

"""
12 can be safely converted to an integer.
12.3 is a float with non-zero digit(s) in the fractional-part.
12.0 can be safely converted to an integer.
123.002 is a float with non-zero digit(s) in the fractional-part.
"""
