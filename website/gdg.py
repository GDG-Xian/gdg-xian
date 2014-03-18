#!/usr/bin/env python
import webapp2
import random
import string

from google.appengine.api import oauth
from google.appengine.api import users

from gaesessions import get_current_session

from framework import Handler
from models import Post


class IndexHandler(Handler):
    def get(self):
        posts = Post.query().order(-Post.created_at)
        self.render_template('index.html', posts=posts)


class LoginHandler(Handler):
    def get(self):
        state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                          for x in xrange(32))
        session = get_current_session()
        session['state'] = state
        # Set the Client ID, Token State, 
        # and Application Name in the HTML while serving it.
        self.render_template('login.html', CLIENT_ID='231159767160-67mkdefbtjuu47kbrgj20vddj9ggo4fh.apps.googleusercontent.com', STATE=state)

    def post(self):
        self.response.write(self.request.arguments())


# TODO Implements the server side flow
# https://developers.google.com/+/web/signin/server-side-flow
application = webapp2.WSGIApplication([
    ('/', IndexHandler),
    ('/login', LoginHandler)
], debug=True)
