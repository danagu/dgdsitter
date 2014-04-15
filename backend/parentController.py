import os
import urllib
import logging
from google.appengine.api import users
import jinja2
import webapp2

from basePage import BaseHandler,JINJA_ENVIRONMENT
from parentModel import Parent,parentKey

class ParentController(BaseHandler):
    
    def addUser(self):
        '''
            Function used for sign up
        '''
        parent = Parent()
        import pdb; pdb.set_trace()
        if users.get_current_user():
            parent.user = users.get_current_user()

        parent.name = self.request.get('name')
        parent.desc = self.request.get('desc')
        addressString = self.request.get('addr')
        try:
            parent.baby = int(self.request.get('baby'))
        except ValueError:
            parent.baby = 0
        try:
            parent.toddler = int(self.request.get('toddler'))
        except ValueError:
            parent.toddler = 0
        try:
            parent.kid = int(self.request.get('kid'))
        except ValueError:
            parent.kid = 0
        try:
            parent.teenager = int(self.request.get('teenager'))
        except ValueError:
            parent.teenager = 0
        
        
        newKey = parent.put()

        self.redirect('/parentList?' +newKey.urlsafe())
    
    def listUsers(self,is_filter=False):
        '''
            Function creates a webpage listing all parents
        '''
        parents_query = Parent.query()
        parents = parents_query.fetch(10)
       
        template_values = {
            'parents': parents,
        }

        template = JINJA_ENVIRONMENT.get_template('parentlist.html')
        self.response.write(template.render(template_values))
        
        
    def get(self):
        return self.listUsers()
        
        
    def post(self):
        if self.request.get('Operation') == 'Add':
            self.addUser()
        else:
            self.listUsers(True)