def get_nonduplicates(list_one, list_two):
    """ Return a list that contains items of the second list that are not in the first list.    
    
    >>> get_nonduplicates([[1,2,3,4,5], [1,2,4,6,7]], 
                          [[1,2,3,4,5], [1,2,4,6,7], [1,2,3,6,8], [1,2,3,0,9], [1,2,6,7,6]])
    [[1, 2, 3, 6, 8], [1, 2, 3, 0, 9], [1, 2, 6, 7, 6]]
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
    print('get_nonduplicates')
    test(get_nonduplicates([[1,2,3,4,5], [1,2,4,6,7]], [[1,2,3,4,5], [1,2,4,6,7], [1,2,3,6,8], [1,2,3,0,9], [1,2,6,7,6]]), 
                          [[1, 2, 3, 6, 8], [1, 2, 3, 0, 9], [1, 2, 6, 7, 6]])
    

if __name__ == '__main__':
    main()
