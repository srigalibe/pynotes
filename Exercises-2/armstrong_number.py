def add_cubes(number):    
    """ Return True if the sum of the cubes of the digits in the number
        is equal to the number itself, else return False.
    
    >>> add_cubes(153)
    True    
    """

    # your code here



# Do not make changes to the code below
# Function used in main() to print 
# what each function returns vs. what it's supposed to return

def test(returned, expected):
    if returned == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{0} returned: {1} expected: {2}'.format(
        prefix, repr(returned), repr(expected)))


# Calls the above functions with interesting inputs.
def main():
    print('add_cubes')
    test(add_cubes(153), True)
    test(add_cubes(370), True)
    test(add_cubes(407), True)
    test(add_cubes(150), False)
    

if __name__ == '__main__':
    main()
