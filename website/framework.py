import os

import jinja2
import markdown
import webapp2


def markdown_filter(content):
    return markdown.markdown(content)


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + '/templates'),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
JINJA_ENVIRONMENT.filters['markdown'] = markdown_filter


class Handler(webapp2.RequestHandler):
    def render_template(self, template, **kwargs):
        template = JINJA_ENVIRONMENT.get_template(template)
        self.response.write(template.render(kwargs))
