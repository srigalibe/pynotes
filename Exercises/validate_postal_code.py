# Validate Postal Code (Canadian)

"""

Define a function postalValidate(S) which first checks if S represents
a postal code (Canadian) which is valid:

    first, delete all spaces;
    the remainder must be of the form L#L#L# where L are letters
    (in either lower or upper case) and # are numbers.
    
If S is not a valid postal code, return the boolean False.
If S is valid, return a version of the same postal code in the nice format
L#L#L# where each L is capital.

Use the following methods to do this exercise:
str.replace(), str.isalpha(), str.isdigit(), and str.upper()

"""

def postalValidate(S):
    """ Return False if S is not a valid postal code.
    If S is valid, return it in the format L#L#L# where each L is capital.
    
    >>> postalValidate(' d3 L3 T3')
    >>> 'D3L3T3'
    """

    # your code here


# Use these arguments to test your function.

"""
‘H0H0H0’, ‘postal’, ‘ d3 L3 T3’, ‘ 3d3 L3 T’, ‘’, ‘n21 3g1z’, ‘V4L1D’,
‘K1A 0A3’, ‘H0H0H’
"""
