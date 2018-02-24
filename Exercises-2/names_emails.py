'''
Create a textfile named test.txt with these two lines in it:
Oleg, oserdyuk@aligngeneral.com
Tomash, tbarbarasz@aligngeneral.com
'''

def get_contacts(filename):
    """ Return names and emails extracted from the textfile.    
    
    >>> get_contacts('test.txt')
    (['Oleg', 'Tomash'], ['oserdyuk@aligngeneral.com', 'tbarbarasz@aligngeneral.com'])
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
    print('get_contacts')
    test(get_contacts('test.txt'), (['Oleg', 'Tomash'], ['oserdyuk@aligngeneral.com', 'tbarbarasz@aligngeneral.com']))
    

if __name__ == '__main__':
    main()
