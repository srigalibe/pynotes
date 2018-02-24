def get_similar(author_list, author):
    """ Return a list of similar authors    
    
    authors = {'Ray Bradbury': ['Harlan Ellison', 'Robert Heinlein', 'Isaac Asimov', 'Arthur Clarke'],
    'Harlan Ellison': ['Neil Stephenson', 'Kurt Vonnegut', 'Richard Morgan', 'Douglas Adams'],
    'Kurt Vonnegut': ['Terry Pratchett', 'Tom Robbins', 'Douglas Adams', 'Neil Stephenson', 'Jeff Vandemeer'],
    'Thomas Pynchon': ['Isaac Asimov', 'Jorges Borges', 'Robert Heinlein'],
    'Isaac Asimov': ['Stephen Baxter', 'Ray Bradbury', 'Arthur Clarke', 'Kurt Vonnegut', 'Neil Stephenson'],
    'Douglas Adams': ['Terry Pratchett', 'Chris Moore', 'Kurt Vonnegut']}
    
    >>> get_similar(authors, 'Harlan Ellison')
    ['Chris Moore', 'Douglas Adams', 'Jeff Vandemeer', 'Kurt Vonnegut', 'Neil Stephenson', 'Terry Pratchett', 'Terry Pratchett', 'Tom Robbins']
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
    print('get_similar')
    
    authors = {'Ray Bradbury': ['Harlan Ellison', 'Robert Heinlein', 'Isaac Asimov', 'Arthur Clarke'],
    'Harlan Ellison': ['Neil Stephenson', 'Kurt Vonnegut', 'Richard Morgan', 'Douglas Adams'],
    'Kurt Vonnegut': ['Terry Pratchett', 'Tom Robbins', 'Douglas Adams', 'Neil Stephenson', 'Jeff Vandemeer'],
    'Thomas Pynchon': ['Isaac Asimov', 'Jorges Borges', 'Robert Heinlein'],
    'Isaac Asimov': ['Stephen Baxter', 'Ray Bradbury', 'Arthur Clarke', 'Kurt Vonnegut', 'Neil Stephenson'],
    'Douglas Adams': ['Terry Pratchett', 'Chris Moore', 'Kurt Vonnegut']}
    
    test(get_similar(authors, 'Harlan Ellison'), ['Chris Moore', 'Douglas Adams', 'Jeff Vandemeer', 'Kurt Vonnegut', 'Neil Stephenson', 'Terry Pratchett', 'Terry Pratchett', 'Tom Robbins'])
    

if __name__ == '__main__':
    main()
