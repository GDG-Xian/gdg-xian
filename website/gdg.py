#!/usr/bin/env python
import os

from google.appengine.ext import ndb

import jinja2
import webapp2


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class Post(ndb.Model):
    content = ndb.StringProperty(indexed=False)
    created_at = ndb.DateTimeProperty(auto_now_add=True)
    updated_at = ndb.DateTimeProperty(auto_now_add=True)
    deleted_at = ndb.DateTimeProperty(auto_now_add=True)


class MainPage(webapp2.RequestHandler):
    def get(self):
        posts = Post.query().order(-Post.created_at)
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(posts))


application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
