def combine_dict_values(dict_list):
    """ Return a dict with values added to existing keys
    
    d_list = [{'Money': .3, 'Strength': .25, 'Speed': .05},
                {'Money': .3, 'Age': 25, 'Speed': .7}, 
                {'Money': .3, 'Strength': .25, 'Power': 5}]
    
    >>> combine_dict_values(d_list)
    {'Age': 25,
    'Money': 0.8999999999999999,
    'Power': 5,
    'Speed': 0.75,
    'Strength': 0.5}
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
    d_list = [{'Money': .3, 'Strength': .25, 'Speed': .05},
                {'Money': .3, 'Age': 25, 'Speed': .7}, 
                {'Money': .3, 'Strength': .25, 'Power': 5}]
    
    result = {'Age': 25,
              'Money': 0.8999999999999999,
              'Power': 5,
              'Speed': 0.75,
              'Strength': 0.5}
    
    print('combine_dict_values')
    test(combine_dict_values(d_list), result)
    

if __name__ == '__main__':
    main()
