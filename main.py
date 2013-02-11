#!/usr/bin/env python

import webapp2
import jinja2
import os
from datetime import date, timedelta
from google.appengine.ext import db

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
	def get_gamedate(self, today='4/7'):
		t = today.split('/')
		d = date(2009, int(t[0]), int(t[1]))
		return d
	
	def get_yesterday(self, startdate):
		yesterday = startdate - timedelta(days=1)
		if yesterday < date(2009, 4, 7):
			return None
		return yesterday.strftime("%m/%d")
		
	def get_tomorrow(self, startdate):
		tomorrow = startdate + timedelta(days=1)
		if tomorrow > date(2010, 1, 31):
			return None
		return tomorrow.strftime("%m/%d")
		
	def get_items(self, day):
		return ['Do nothing']

	def get(self, *ar, **kw):
		try:
			today = self.get_gamedate(ar[0])
		except:
			today = self.get_gamedate()
	
		template_values = {
			'prev': self.get_yesterday(today),
			'today': today.strftime("%m/%d"),
			'next': self.get_tomorrow(today),
			'todo': self.get_items(today)
		}
		
		template = jinja_environment.get_template('templates/date.html')
		self.response.out.write(template.render(template_values))


app = webapp2.WSGIApplication([
  ('/', MainHandler),
  (r'/([0-9]+/[0-9]+)', MainHandler),
], debug=True)
