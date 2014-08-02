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


#animal is a object
class Animal(object):
    pass

class Dog(Animal):
    def __init__(self, name):
        self.name = name


class Cat(Animal):
    def __init__(self, name):
        self.name = name

class Person(object):

    def __init__(self, name):
        self.name = name
        self.pet = None

class Employee(Person):
    def __init__(self, name, salary):
        super(Employee, self).__init__(name)
        self.salary = salary

class Fish(object):
    pass



