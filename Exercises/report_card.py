# Grading scores
# Take the following into consideration:
# Grade is 'Excellent' if score is greater than or equal to 75.
# Grade is 'Very good' if score is greater than or equal to 60.
# Grade is 'Good' if score is greater than or equal to 50.
# Grade is 'Not bad' if score is greater than or equal to 40.
# Grade is 'Bad' if score is greater than or equal to 30.
# Grade is 'Horrible' if score is greater than or equal to 20.
# Grade is 'Appalling' if score is below 20.


def get_report_card(name, score):
    """ Return a report card with name, score, and grade based on score.
    
    >>> get_report_card('Bob', 80)
    >>> OrderedDict([('Name', 'Bob'), ('Score', 80), ('Grade', 'Excellent')])
    """

    # your code here


# When your function is ready, run this loop.

"""
for k, v in get_report_card('Joe', 19).items():
    print("{}: {}".format(k, v))
"""

# It should print:

"""
Name: Joe
Score: 19
Grade: Appalling
"""
