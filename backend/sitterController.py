import os
import urllib
import logging
from google.appengine.api import users
import jinja2
import webapp2

from basePage import BaseHandler,JINJA_ENVIRONMENT
from sitterModel import Sitter

class SitterController(BaseHandler):
    
    def addUser(self):
        '''
            Function used for sign up
        '''
        sitter = Sitter()

        if users.get_current_user():
            sitter.user = users.get_current_user()

        sitter.name = self.request.get('name')
        try:
            sitter.age = int(self.request.get('age'))
        except ValueError:
            sitter.age = 0
        sitter.gender = ('male' == self.request.get('gender'))
        sitter.desc = self.request.get('desc')
        # addressString = self.request.get('addr')
        sitter.preferredAges = self.request.get_all('ages')
        
        newKey = sitter.put()

        self.redirect('/sitterList?' +newKey.urlsafe())
    
    def listUsers(self,is_filter=False):
        '''
            Function creates a webpage listing all sitters
        '''
        sitters_query = Sitter.query()
        if is_filter:
            self.response.write("FILTER")
            requested_gender = self.request.get('gender')
            requested_ages = self.request.get_all('ages')
            
            if requested_gender and requested_ages:
                sitters_query = Sitter.queryByAgegender(requested_ages,requested_gender=='male')
            elif requested_ages:
                sitters_query = Sitter.queryByAge(requested_ages)
            elif requested_gender:
                # import pdb; pdb.set_trace()
                sitters_query = Sitter.queryByGender(requested_gender=='male')
        sitters = sitters_query.fetch(10)
       
        template_values = {
            'sitters': sitters,
        }

        template = JINJA_ENVIRONMENT.get_template('sitterlist.html')
        self.response.write(template.render(template_values))
        
        
    def get(self):
        return self.listUsers()
        
        
    def post(self):
        if self.request.get('Operation') == 'Add':
            self.addUser()
        else:
            self.listUsers(True)