def get_values(dic):
    """ Return a list of values of a dictionary.
    
    >>> get_values({"i": 3, "o": 2, "u": 2})
    [3, 2, 2]
    """
    
    # your code here



# Do not make any changes to the code below
# Function used in main() to print 
# what each function returns vs. what it's supposed to return

def test(returned, expected):
    if returned == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{0} returned: {1} expected: {2}'.format(prefix, repr(returned), repr(expected)))



# Do not make any changes to the code below
# Calls the above functions with interesting inputs.
def main():
    print('get_values')
    test(get_values({"i": 3, "o": 2, "u": 2}), [3, 2, 2])
    

if __name__ == '__main__':
    main()
