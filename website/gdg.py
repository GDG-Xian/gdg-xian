#!/usr/bin/env python
import webapp2

from google.appengine.api import oauth
from google.appengine.api import users

from framework import Handler
from models import Post


class IndexHandler(Handler):
    def get(self):
        posts = Post.query().order(-Post.created_at)
        self.render_template('index.html', posts=posts)


class LoginHandler(Handler):
    def get(self):
        self.render_template('login.html')

    def post(self):
        self.response.write(self.request.arguments())


application = webapp2.WSGIApplication([
    ('/', IndexHandler),
    ('/login', LoginHandler)
], debug=True)
