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


# python中定义私有的变量
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


#给一个类的实例绑定属性
class StudentOne(object):
    pass


s = StudentOne()
s.name = "wangchen"
print s.name
print s


#给一个类的实例绑定一个方法,好像这个版本的python不能动态添加方法
# def set_age(self, age):
#     self.age = age
#
# from types import MethodType
#
# s.set_age = MethodType(set_age, s, StudentOne)
#
# s.set_age = 3232
# print s.age


#slott的使用，主要是定义一个类能够添加的属性有哪些
class StudentTwo(object):
    __slots__ = ("name", "age")


student_two = StudentTwo()
student_two.name = "ksdfsd"
student_two.age = "898"

# student_two.ssds = "sdsd"//不应该出现的属性

print student_two.name
print student_two.age


#同时slots只会在当前的类中有效，子类是不做任何限制的
class StudentThird(StudentTwo):
    pass


student_third = StudentThird()
student_third.ss = "sdsd"
print student_third.ss


#一般的限制对象的参数的方法
class StudentFour(object):
    def get_score(self):
        return self._score

    def set_score(self, score):

        if not isinstance(score, int):
            raise ValueError("score must be on integer!")

        if score < 0 or score > 100:
            raise ValueError("score should between 0 ~ 100")

        self._score = score


student_four = StudentFour()
student_four.set_score(22)
print student_four.get_score()

#student_four.set_score(8898)
#print student_four.get_score()


#装饰器的方式来解决直接调用属性的方法
class StudentFive(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):

        if not isinstance(value, int):
            raise ValueError("not int")
        if value < 0 or value > 100:
            raise ValueError("not correct")

        self._score = value


student_five = StudentFive()
student_five.score = 80
print student_five.score


#多重继承的测试
class Animal(object):
    pass


#大类
class Mammal(Animal):
    pass


class Bird(Animal):
    pass


#功能类
class Runnable(object):
    def run(self):
        print("running...")


class Flyable(object):
    def fly(self):
        print "fly....."


#各种动物
class Dog(Mammal, Runnable):
    pass


class Bat(Mammal, Flyable):
    pass

Dog().run()
Bat().fly()


#定制类,主要是类似于__xxx__这样的特殊变量或者函数名
class Master(object):

    def __init__(self, name):
        self.name = name

    """define describle object,用来描述打印出来的字符串，给用户看的"""
    def __str__(self):
        return "master object (name : %s)" % self.name

    """用来给开发中调试使用"""
    def __repr__(self):
        return "master object(name=%s)" % self.name

    """对于不存在的属性，能够动态的返回"""
    def __getattr__(self, item):
        if item == "score":
            return 99

    """对实例进行直接调用"""
    def __call__(self, *args, **kwargs):
        print "my name is %s" % args[0]


print Master("wangchen")


#对于__iter__（）方法的定义
class Fib(object):

    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def next(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100:
            raise StopIteration()
        return self.a

    """定义获取指定位置的元素方法"""
    def __getitem__(self, item):
        a, b = 1, 1
        for i in range(item):
            a, b = b, a + b
        return a

for i in Fib():
    print i

fib = Fib()

print fib[3]
print fib[4]
print fib[5]

master = Master("sds")
print master.name
print master.score
master("sdsds")