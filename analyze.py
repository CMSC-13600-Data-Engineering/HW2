import pandas as pd

def get_google_catalog():
    return pd.read_csv('GoogleProducts.csv')

def get_amazon_catalog():
    return pd.read_csv('Amazon.csv')


def match():
    '''
    Match must return a list of tuples of amazon ids and google ids.
    For example:
    [('b000jz4hqo', http://www.google.com/base/feeds/snippets/11125907881740407428'),....]

    '''

    #YOUR CODE GOES HERE

    return []