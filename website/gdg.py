#!/usr/bin/env python
import os

import jinja2
import webapp2
import markdown

from google.appengine.ext import ndb


def markdown_filter(content):
    return markdown.markdown(content)


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
JINJA_ENVIRONMENT.filters['markdown'] = markdown_filter


class Post(ndb.Model):
    content = ndb.StringProperty(indexed=False)
    created_at = ndb.DateTimeProperty(auto_now_add=True)
    updated_at = ndb.DateTimeProperty(auto_now_add=True)
    deleted_at = ndb.DateTimeProperty(auto_now_add=True)


class MainPage(webapp2.RequestHandler):
    def get(self):
        posts = Post.query().order(-Post.created_at)
        template = JINJA_ENVIRONMENT.get_template('index.html')
        values = {
            'posts': posts
        }
        self.response.write(template.render(values))


class AddPost(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('add.html')
        self.response.write(template.render())

    def post(self):
        post = Post()
        post.content = self.request.get('content')
        post.put()
        self.redirect('/')


application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/add', AddPost)
], debug=True)
