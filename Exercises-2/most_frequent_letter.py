def find_most_frequent_letter(text):
    """ Return the most frequent letter in text.
    
    >>> find_most_frequent_letter("This is a super long long long string. Please help count me")
    ('s', 5)
    """

    # your code here



# Do not make changes to the code below
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
    print('find_most_frequent_letter')
    test(find_most_frequent_letter("This is a super long long long string. Please help count me"), ('s', 5))
    

if __name__ == '__main__':
    main()
