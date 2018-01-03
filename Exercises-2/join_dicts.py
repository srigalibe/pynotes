def join_dicts(dict1, dict2):
    """ Return dict1 after extending it with dict2
    
    >>> join_dicts({1:'a', 2:'b', 3:'c'}, {1:'d', 2:'e'})
    {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
    """
    
    # Your code here




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



# Do not make changes to the code below
# Calls the above functions with interesting inputs.
def main():
    print('join_dicts')
    test(join_dicts({1:'a', 2:'b', 3:'c'}, {1:'d', 2:'e'}), {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'})
    

if __name__ == '__main__':
    main()
