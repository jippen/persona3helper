#!/usr/bin/env python

import webapp2
import jinja2
import os
import yaml
from datetime import date
from google.appengine.ext import db


jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self, *ar, **kw):
        fh = open('persona3fes.yaml', 'r')
        guide = yaml.load(fh)
        today = guide[ar[0]]
        today['today'] = ar[0]
        dow  = '???'
        
        month, day = (int(x) for x in ar[0].split('/'))
        if month == 1:
            d = date(2010, month, day)
            dow = d.strftime("%A")
        elif month != 99:
            d = date(2009, month, day)
            dow = d.strftime("%A")

        today['dow'] = dow
        today['courage'] = guide['courage']
        today['charm'] = guide['charm']
        today['academic'] = guide['academic']

        template = jinja_environment.get_template('templates/date.html')
        self.response.out.write(template.render(today))

app = webapp2.WSGIApplication([(r'/([0-9]+/[0-9]+)', MainHandler)], debug=True)