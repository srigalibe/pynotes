''' Define a function that takes a locale and a format and
returns date in the format specified. '''

def get_date_in(loc, df):
    """ Return date in the format specified.
    
    >>> get_date_in('fr', "%d-%b-%Y")
    03-janv.-2018
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
    print('get_date_in')
    test(get_date_in('fr', "%d-%b-%Y"), '03-janv.-2018')
    test(get_date_in('zh', "%d %b %Y"), '03 1月 2018')
    test(get_date_in('tr', "%d-%b-%Y"), '03-Oca-2018')
    

if __name__ == '__main__':
    main()
