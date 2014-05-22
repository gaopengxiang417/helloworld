__author__ = 'wangchen'
#coding=utf-8


#定义了一个基本的函数功能
def sayhello():
    """
    define a function that just print a stirng
    """
    print "hello world"


sayhello()


#定义有参数的函数
def maxnumber(a, b):

    """比较两个数的大小"""

    print "the max number is : "
    if a > b:
        print a
    elif a < b:
        print b
    else:
        print a

maxnumber(3, 6)


#函数的局部变量的定义
def localFunction(x):

    """测试局部变量"""
    print "x=", x

    x = 2

    print "local x=", x

x = 40
localFunction(x)
print "this x=", x


#函数的全局变量定义
def globalFunction():

    global y
    print "first x=", y
    y = 4
    print "second x=", y

y = 1
print "y=", y
globalFunction()
print "last y=", y


#默认参数的定义,默认值参数只能放到最后
def sayhello(message, times=1):
    print message * times


sayhello("chian")
sayhello("hello", 6)


#关键字参数定义，可以解决默认参数的问题
def func(a, b=4, c=10):
    print "a=",a,"b=",b,"c=",c

func(3)
func(4, c=3)
func(c=2, a=5)
func(c=5, b=9,a=33)


#return语句的使用
def maxsium(a, b):
    if a > b:
        return a
    else:
        return b

print maxsium(3, 5)
print maxsium(5, 4)

print None


#docstring的定义
def printMax(a, b):
    """Prints the max numbers of two number.

    the two numbers must be integers"""

    if a > b:
        print a, "is the max"

    else:
        print b, "is the max"

printMax(4,6)
print printMax.__doc__



