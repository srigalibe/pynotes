def remove_spaces(a_list):
    """ Return a result after removing spaces in the sublists.
    
    >>> remove_spaces([['A(x) | B(x)'], ['Function(x,y) | K(x)']])
    [['A(x)|B(x)'], ['Function(x,y)|K(x)']]
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



# Calls the above functions with interesting inputs.
def main():
    print('remove_spaces')
    test(remove_spaces([['A(x) | B(x)'], ['Function(x,y) | K(x)']]), [['A(x)|B(x)'], ['Function(x,y)|K(x)']])
    test(remove_spaces([['text- with -spaces'], ['A(x) | B(x)']]), [['text-with-spaces'], ['A(x)|B(x)']])    

if __name__ == '__main__':
    main()    
