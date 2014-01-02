#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
import jinja2
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class LoginHandler(webapp2.RequestHandler):
    def get(self):
        if self.request.get('pass') == 'password':
            template_values = {
                'data': 'private page',
                'more_data': 'bar',
            }
            template = JINJA_ENVIRONMENT.get_template('templates/page.html')
            self.response.write(template.render(template_values))
        else:
            template = JINJA_ENVIRONMENT.get_template('templates/login.html')
            self.response.write(template.render())

class LinkHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'data': 'lorem ipsum',
            'more_data': 'bar',
        }
        template = JINJA_ENVIRONMENT.get_template('templates/page.html')
        self.response.write(template.render(template_values))


routes = [
    ('/link1', LinkHandler),
    ('/link2', LinkHandler),
    ('/login', LoginHandler),
]

app = webapp2.WSGIApplication(routes, debug=True)

def handle_404(request, response, exception):
    template = JINJA_ENVIRONMENT.get_template('templates/404.html')
    response.set_status(404)
    response.write(template.render())

app.error_handlers[404] = handle_404
