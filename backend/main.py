import os
import urllib
import logging
from google.appengine.api import users
import jinja2
import webapp2

from basePage import BaseHandler,JINJA_ENVIRONMENT
from sitterController import SitterController
from parentController import ParentController


class MainPage(BaseHandler):

    def get(self):
        template_values = {
        }

        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))




app = webapp2.WSGIApplication([
  ('/', MainPage),
  ('/sitterList', SitterController),
  ('/parentList', ParentController)
])