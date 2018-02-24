def min_of_pairs(number):
    """ Return a number built from the min of
        each pair of the digits of the input number.
    
    >>> min_of_pairs('84372216')
    '4321'
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
    print('min_of_pairs')
    test(min_of_pairs('84372216'), '4321')
    

if __name__ == '__main__':
    main()
