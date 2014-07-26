__author__ = 'wangchen'
#coding=utf-8

#自定义class
class TheThing(object):
    """this is a my define class"""

    def __init__(self):
        """this ia a init method"""
        self.number = 0

    def some_function(self):
        print "i got called"

    def add_me_up(self, more):
        self.number += more
        return self.number

a = TheThing()
b = TheThing()

a.some_function()
b.some_function()

print a.add_me_up(5)
print b.add_me_up(5)

print TheThing.__doc__
print a.__init__().__doc__

