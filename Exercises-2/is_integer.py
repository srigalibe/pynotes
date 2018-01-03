def is_integer(number):
    """ Return True if the string input is an integer, else return False.
    
    >>> is_integer('5')
    True
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
    print('is_integer')
    test(is_integer('15'), True)
    test(is_integer('ten'), False)
    

if __name__ == '__main__':
    main()
