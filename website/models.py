from google.appengine.ext import ndb

class Post(ndb.Model):
    content = ndb.StringProperty(indexed=False)
    created_at = ndb.DateTimeProperty(auto_now_add=True)
    updated_at = ndb.DateTimeProperty(auto_now_add=True)
    deleted_at = ndb.DateTimeProperty(auto_now_add=True)
