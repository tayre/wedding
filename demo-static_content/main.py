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

JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class LoginHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/login.html')
        self.response.write(template.render())

    def post(self):
        if self.request.get('pass') == 'password':
            self.response.set_cookie('TNTSESSION', '42')
            return webapp2.redirect('/', code=303, response = self.response) #Use PRG to avoid duplicate form submission

        else:
            return webapp2.redirect('/login') #PRG

class IndexHandler(webapp2.RequestHandler):
    def get(self):
        if self.request.cookies.get('TNTSESSION') != None: 
            template = JINJA_ENVIRONMENT.get_template('templates/index.html')
            self.response.write(template.render())

        else:
            template = JINJA_ENVIRONMENT.get_template('templates/login.html')
            self.response.write(template.render())

class RSVPHandler(webapp2.RequestHandler):
    def get(self):
        if self.request.cookies.get('TNTSESSION') != None: 
            template = JINJA_ENVIRONMENT.get_template('templates/rsvp.html')
            self.response.write(template.render())
        else:
            template = JINJA_ENVIRONMENT.get_template('templates/login.html')
            self.response.write(template.render())


routes = [
    ('/', IndexHandler),
    ('/login', LoginHandler),
    ('/rsvp', RSVPHandler),
]

app = webapp2.WSGIApplication(routes, debug=True)

def handle_404(request, response, exception):
    template = JINJA_ENVIRONMENT.get_template('templates/404.html')
    response.set_status(404)
    response.write(template.render())

def handle_500(request, response, exception):
    template = JINJA_ENVIRONMENT.get_template('templates/500.html')
    response.set_status(404)
    response.write(template.render())

app.error_handlers[404] = handle_404
app.error_handlers[500] = handle_500
