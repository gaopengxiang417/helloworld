#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import types

__author__ = 'wangchen'

# 面向过程的打印学生的函数
std1 = {"name": "michel", "score": 89}
std2 = {"name": "jake", "score": 77}


# 打印学生的相关东西
def print_student(std):
    print "%s : %s" % (std["name"], std["score"])


print_student(std1)
print_student(std2)


# 面向对象的解决方案
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print "%s : %s" % (self.name, self.score)


bart = Student("bart", 22)
ming = Student("ming", 42)

bart.print_score()
ming.print_score()


# python对于对象可以随意的定义自己的属性
bart.test = 232
print bart.test

# print ming.test


#python中定义私有的变量
class Techer(object):
    """teacher is a private object"""

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def print_score(self):
        print "%s : %s" % (self.__name, self.__age)

    """define the get method"""

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age


teacher = Techer("mr zhang", 31)
teacher.print_score()
print teacher.__doc__


#python中得继承和多态的说明

#首先定义一个基类
class Animal(object):
    """this is a base class"""

    def run(self):
        print "animal is running...."


class Dog(Animal):
    """this is a dog class"""

    def run(self):
        print "dog is running..."


class Cat(Animal):
    """this is a cat class"""

    def run(self):
        print "cat is running...."


dog = Dog()
cat = Cat()

dog.run()
cat.run()


#判断类的实例类型
l = list()
d = dict()
animal = Animal()

print isinstance(l, list)
print isinstance(d, dict)
print isinstance(dog, Animal)
print isinstance(dog, Dog)
print isinstance(animal, Animal)
print isinstance(animal, Dog)


#判断对象的类型 type()
print type(123)
print type("123")
print type(None)

#判断函数或者类
print type(abs)

print type("abc") == types.StringType
print type([]) == types.ListType

#读取对象的所有属性和方法
print dir("sdsd")


