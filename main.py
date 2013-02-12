#!/usr/bin/env python

import webapp2
import jinja2
import os
import csv
from google.appengine.ext import db

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class Day():
    def __init__(self, day):
        file = open(os.path.join(os.path.dirname(__file__), 'data.csv'))
	fileReader = csv.reader(file)
	tmp = []
	for line in fileReader:
            if line[1] == day:
                tmp = line
                break

        self.current = tmp[1]
	self.prev = tmp[2]
        self.next = tmp[3]

        self.quiz = tmp[4]
        self.exam = tmp[5:9]
        self.exam = filter(None, self.exam)
        self.where = tmp[10]
        self.answers = tmp[11:-1]
        self.answers = filter(None, self.answers)

class MainHandler(webapp2.RequestHandler):
    def get(self, *ar, **kw):
        today = Day(ar[0])

        template_values = {
            'prev': today.prev,
            'today': today.current,
            'next': today.next,
            'quiz': today.quiz,
            'where': today.where,
            'exam': today.exam,
            'answers': today.answers
        }
        
        template = jinja_environment.get_template('templates/date.html')
        self.response.out.write(template.render(template_values))


app = webapp2.WSGIApplication([
  ('/', MainHandler),
  (r'/([0-9]+/[0-9]+)', MainHandler),
], debug=True)
