import os
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb

from utilityModels import Address,AgeRange


def parent_key():
    return ndb.Key('parents', 'parentslist')
    
def ageValidator(prop,value):
    '''
        Makes sure age is between 10 and 100
    '''
    if value > 10 and value < 100:
        return None
    raise TypeError("Invalid age")
    
parentKey =  parent_key()

class Parent(ndb.Model):
    """Models an individual entry with appropriate fields."""
    # We set the same parent key on the 'parent' to ensure each parent
    # is in the same entity group. Queries across the single entity group
    # will be consistent. However, the write rate to a single entity group
    # should be limited to ~1/second.
    parent = parent_key()
    user = ndb.UserProperty()
    name = ndb.StringProperty()
    signupDate = ndb.DateTimeProperty(auto_now_add=True)
    desc = ndb.TextProperty(indexed=False)
    
    parentAddress = ndb.StructuredProperty(Address)
    
    baby = ndb.IntegerProperty()
    toddler = ndb.IntegerProperty()
    kid = ndb.IntegerProperty()
    teenager = ndb.IntegerProperty()
    