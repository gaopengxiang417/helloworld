__author__ = 'wangchen'
#coding=utf-8

import sys

script = sys.argv[0]
username = sys.argv[1]

prompt = ">>"

print "hi, %s, i am in the script %s" % (username, script)
print "i would like to ask your some question"
print "do you like me %s?" % username
like = raw_input(prompt)


print "where do you live? %s" % username
lives = raw_input(prompt)

print "what kind of computer do you have?"
computer = raw_input(prompt)

print "what do you like eat？"
eat = raw_input(prompt)

print """
all right,so you said %r like me,
you live in %r,not sure where that is
and you have a %r computer,nice
and you like to eat %r""" % (like, lives, computer, eat)

