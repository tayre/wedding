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
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        if self.request.get('pass') == 'password':
            self.response.out.write('authorized');
        else:
            self.response.out.write('<form method="get"><input type="password" name="pass"/><input type="submit" value="login"/></form>')

class HotelHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write('<b>hotel stuff here</b>');


app = webapp2.WSGIApplication([
    ('/rsvp', MainHandler),
    ('/hotel', HotelHandler),
], debug=True)

