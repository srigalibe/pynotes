''' Define a function that takes a 3-D list and
converts it to a 2-D list in-place. '''


def get_2D(lst):
    """ Convert the list to 2-D in-place.
    
    my_list = [[['item1','item2']],[['item3', 'item4']]]
    >>> get_2D(my_list)
    [['item1', 'item2'], ['item3', 'item4']]
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
    my_list = [[['item1','item2']],[['item3', 'item4']]]
    print('get_2D')
    test(get_2D(my_list), [['item1', 'item2'], ['item3', 'item4']])
    

if __name__ == '__main__':
    main()
