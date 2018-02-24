def get_url(url):
    """ Remove the protocol string in the URL, return the remaining URL.
    
    >>> get_url('https://example.com/example')
    example.com/example
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
    print('get_url')
    test(get_url('ftp://example.com/example'), 'example.com/example')
    test(get_url('https://example.com/example'), 'example.com/example')
    test(get_url('http://example.com/example'), 'example.com/example')
    

if __name__ == '__main__':
    main()
