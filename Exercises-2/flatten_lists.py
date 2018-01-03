def flatten(a_list):
    """ Return a list after transforming the inner lists
        so they only contain strings.
    
    >>> flatten([[[],["a"],"a"],[["ab"],[],"abc"]])
    [['', 'a', 'a'], ['ab', '', 'abc']]
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
    print('{0} returned: {1} expected: {2}'.format(
        prefix, repr(returned), repr(expected)))


# Calls the above functions with interesting inputs.
def main():
    print('flatten')
    test(flatten([[[],["a"],"a"],[["ab"],[],"abc"]]), [['', 'a', 'a'], ['ab', '', 'abc']])
    

if __name__ == '__main__':
    main()
