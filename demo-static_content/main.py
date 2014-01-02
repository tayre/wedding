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

class RSVPHandler(webapp2.RequestHandler):
    def get(self):
        if self.request.get('pass') == 'password':
            template = JINJA_ENVIRONMENT.get_template('templates/rsvp.html')
            self.response.write(template.render())
        else:
            template = JINJA_ENVIRONMENT.get_template('templates/login.html')
            self.response.write(template.render())

class HotelHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'data': 'lorem ipsum',
            'more_data': 'bar',
        }
        template = JINJA_ENVIRONMENT.get_template('templates/hotel.html')
        self.response.write(template.render(template_values))

class RegistryHandler(webapp2.RequestHandler):
    def get(self):
            template = JINJA_ENVIRONMENT.get_template('templates/registry.html')
            self.response.write(template.render())

            
routes = [
    ('/rsvp', RSVPHandler),
    ('/hotel', HotelHandler),
    ('/registry', RegistryHandler),
]

app = webapp2.WSGIApplication(routes, debug=True)

def handle_404(request, response, exception):
    template = JINJA_ENVIRONMENT.get_template('templates/404.html')
    response.set_status(404)
    response.write(template.render())

app.error_handlers[404] = handle_404
