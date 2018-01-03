def country_host(dic, continent="Europe", name="hostname"):
    """ Return countries, host statuses.
    
    >>> country_host({"Europe":
                    {"Germany": [{"hostname": "host1"}],
                    "Poland": [{"hostname": "host2"}],
                    "Denmark": [{"hostname": "host3"}]}})
    [(Germany, host1), (Poland, host2), (Denmark, host3)]
    
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
    print('country_host')
    test(country_host({"Europe":
            {"Germany": [{"hostname": "host1"}],
             "Poland": [{"hostname": "host2"}],
             "Denmark": [{"hostname": "host3"}]}}), [('Germany', 'host1'), ('Poland', 'host2'), ('Denmark', 'host3')])
    

if __name__ == '__main__':
    main()
