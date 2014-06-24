__author__ = 'wangchen'
#coding=utf-8


#自定义函数的概念
#这里接受的是可变参数
def print_two(*args):
    first, second = args
    print "args: %r, %r" %(first, second)

#这里定义接受一个参数的函数
def print_one(one):
    print "arg: %r" %(one)


#这里不接受任何参数
def print_none():
    print "none is print"


print_two("china", "english")
print_one("USA")
print_none()


def cheese_crack(cheese, crack):
    print "you have %d cheeses!" % cheese
    print "you have %d of crack" % crack
    print "ok, that is enough for a party"
    print "start a new line"

print "we can give the function numbers directly"
cheese_crack(10, 40)

#传递变量给函数
print "now , we pass the argument by vairable"
cheese = 90
crack = 50
cheese_crack(cheese, crack)

#直接在参数进行计算
cheese_crack(90 + 20, 9 + 4)

#变量和常量相加
cheese_crack(cheese + 9, crack + 1)