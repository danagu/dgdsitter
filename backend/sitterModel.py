import os
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb

from utilityModels import Address,AgeRange


def sitter_key():
    return ndb.Key('sitters', 'sittersList')
    
def ageValidator(prop,value):
    '''
        Makes sure age is between 10 and 100
    '''
    if value > 10 and value < 100:
        return None
    raise TypeError("Invalid age")
    
sitterKey =  sitter_key()

class Sitter(ndb.Model):
    """Models an individual entry with appropriate fields."""
    # We set the same parent key on the 'Sitter' to ensure each Sitter
    # is in the same entity group. Queries across the single entity group
    # will be consistent. However, the write rate to a single entity group
    # should be limited to ~1/second.
    parent = sitter_key()
    user = ndb.UserProperty()
    name = ndb.StringProperty()
    age = ndb.IntegerProperty(validator=ageValidator)
    gender = ndb.BooleanProperty()
    signupDate = ndb.DateTimeProperty(auto_now_add=True)
    desc = ndb.TextProperty(indexed=False)
    
    sitterAddress = ndb.StructuredProperty(Address)
    preferredAgesProp = ndb.StructuredProperty(AgeRange,repeated=True)
    preferredAges = ndb.StringProperty(repeated=True)
    
    @classmethod
    def queryByAge(cls, preferredage):
        return cls.query(Sitter.preferredAges.IN(preferredage)) #ancestor='sitterKey',
        
    @classmethod
    def queryByGender(cls, male=False):
        return cls.query(Sitter.gender == male) #ancestor='sitterKey',
        
    @classmethod
    def queryByAgegender(cls,preffered_ages,male=False):
        return cls.query(ndb.AND(
                                Sitter.preferredAges.IN(preffered_ages),
                                Sitter.gender == male
                                )
                        )
