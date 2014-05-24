__author__ = 'wangchen'
#coding=utf-8


#首先定义一个类
class Myclass:
    pass


myclass = Myclass()
print myclass


#定义一个类，并且里面有他的方法
class Person:
    def sayhi(self):
        print "hello , say "


person = Person()
person.sayhi()


#init方法的使用，他主要是用来进行一些类初始化的时候准备工作
class InitPerson:
    def __init__(self, name):
        self.name = name

    def sayhi(self):
        print "hello", self.name


init_person = InitPerson("wangchen")
init_person.sayhi()


#类变量和对象变量的使用
class ClassPerson:
    """this class is used to represt a person"""
    population = 0

    __private_variable = 4

    def __init__(self, name=None):
        """define the init method to init object parameter"""
        self.name = name
        print "(this name is %s)" % name

        ClassPerson.population += 1


    def __del__(self):
        """delete one person number"""

        ClassPerson.population -= 1

        print "the population is %s" % ClassPerson.population

    def howmany(self):
        """calaulate the person numbers"""

        print "how many person is %s" % ClassPerson.population
        print ClassPerson.__private_variable


wangchen = ClassPerson("wangchen")
wangchen.howmany()

haha = ClassPerson("haha")
haha.howmany()

print ClassPerson.__init__.__doc__
print ClassPerson.howmany.__doc__


#基类于继承的关系
class BaseSchema:
    """定义了基本的学生和老师的基类"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

        print "init base object, name %s" % name

    def tell(self):
        print "this name is %s, the age is %s" % (self.name, self.age)


class Teacher(BaseSchema):
    """定义了基本的老师的导出类"""

    def __int__(self, name, age, salary):
        BaseSchema.__init__(self, name, age)
        self.salary = salary

        print "the teacher name is %s" % name


    def tell(self):
        BaseSchema.tell(self)
        print "the salary is %s" % self.salary


class Student(BaseSchema):
    """定义了基本的学生的导出类"""

    def __int__(self, name, age, mark):
        BaseSchema.__init__(self, name, age)
        self.mark = mark

        print "the student name is %s " % name

    def tell(self):
        BaseSchema.tell(self)
        print "the mark is %s" % self.mark


teacher = Teacher("Dr tae", 44, 4343)
student = Student("St lou", 23, 90)

teacher.tell()
student.tell()


