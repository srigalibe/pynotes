def round_seconds(dts):
    """ Return time rounded off to the nearest second.
    
    data = ['2017-06-25 00:31:53.993',
           '2017-06-25 00:32:31.224',
           '2017-06-25 00:33:11.223',
           '2017-06-25 00:33:53.876',
           '2017-06-25 00:34:31.219',
           '2017-06-25 00:35:12.634']
    
    >>> round_seconds(data)
    ['2017-06-25 00:31:54',
    '2017-06-25 00:32:31',
    '2017-06-25 00:33:11',
    '2017-06-25 00:33:54',
    '2017-06-25 00:34:31',
    '2017-06-25 00:35:13']
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
    rounded = ['2017-06-25 00:31:54',
              '2017-06-25 00:32:31',
              '2017-06-25 00:33:11',
              '2017-06-25 00:33:54',
              '2017-06-25 00:34:31',
              '2017-06-25 00:35:13']
    
    print('round_seconds')
    test(round_seconds(data), rounded)
    

if __name__ == '__main__':
    main()
