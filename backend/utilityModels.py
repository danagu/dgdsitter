from google.appengine.ext import ndb

class Address(ndb.Model):
  street = ndb.StringProperty()
  city = ndb.StringProperty()
  neighborhood = ndb.StringProperty()
  
class AgeRange(ndb.Model):
  ageName = ndb.StringProperty()
  ageYears = ndb.JsonProperty()
  
  
  