"""`appengine_config` gets loaded when starting a new application instance."""
import sys
import os.path
# add `lib` subdirectory to `sys.path`, so our `main` module can load
# third-party libraries.
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'lib'))

from gaesessions import SessionMiddleware
def webapp_add_wsgi_middleware(app):
    app = SessionMiddleware(app, cookie_key="##FdsafdS@#%$#565654231DF@#%$#565654DSAfds%$$#@$#@!")
    return app