def get_unique_chars(a_list):
    """ Return a list of unique chars with the chars sorted.
    
    >>> get_unique_chars(['AC', 'AF', 'CF'])
    ['A', 'C', 'F']
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
    print('get_unique_chars')
    test(get_unique_chars(['AC', 'AD', 'CD']), ['A', 'C', 'D'])
    test(get_unique_chars(['AC', 'AF', 'CF']), ['A', 'C', 'F'])
    

if __name__ == '__main__':
    main()
