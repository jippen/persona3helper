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
            if line[0] == day:
                tmp = line
                break

        self.current = tmp[0]
        self.dow = tmp[1]
        self.prev = tmp[2]
        self.next = tmp[3]

        self.quiz = tmp[4]
        self.exam = tmp[5:9]
        self.exam = filter(None, self.exam)
        self.arcana = tmp[10]
        self.after_school = tmp[11]
        self.answers = tmp[12:15]
        self.answers = filter(None, self.answers)
        self.quest = tmp[16]
        self.courage = tmp[17]
        self.charm = tmp[18]
        self.academic = tmp[19]
        self.tartarus = tmp[20]
        self.late_night = tmp[21]

class MainHandler(webapp2.RequestHandler):
    def get(self, *ar, **kw):
        today = Day(ar[0])

        template_values = {
            'prev': today.prev,
            'today': today.current,
            'dow': today.dow,
            'next': today.next,
            'quiz': today.quiz,
            'arcana': today.arcana,
            'after_school': today.after_school,
            'exam': today.exam,
            'arcana': today.arcana,
            'answers': today.answers,
            'quest': today.quest,
            'courage': today.courage,
            'charm': today.charm,
            'academic': today.academic,
            'tartarus': today.tartarus,
            'late_night': today.late_night
        }
        
        template = jinja_environment.get_template('templates/date.html')
        self.response.out.write(template.render(template_values))


app = webapp2.WSGIApplication([
  ('/', MainHandler),
  (r'/([0-9]+/[0-9]+)', MainHandler),
], debug=True)
