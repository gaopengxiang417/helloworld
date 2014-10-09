__author__ = 'wangchen'
# coding=utf-8

from collections import Iterable
import functools

# 切片的使用

name_list = ["Michacl", "Sarah", "Tracy", "Bob", "Jack"]

# 最泵的办法
print [name_list[0], name_list[3]]

# 最高效的办法
print name_list[0:3]
print name_list[:3]
print name_list[-1]
print name_list[:]
print name_list[3:]
print name_list[4:100]

# 定义tuple
tuple_list = ("Michacl", "Sarsh", "Tracy", "Bob", "Jack")

print tuple_list[0:3]
print tuple_list[:]
print tuple_list[-2]


# 迭代的使用
dirc = {"name": "china", "age": "44", "street": "the publish of china"}

for key, value in dirc.iteritems():
    print key, value


# 字符串迭代
for c in "abc":
    print c


#是否是可迭代对象的判断
print isinstance("abc", Iterable)
print isinstance([1, 3, 4], Iterable)
print isinstance(12, Iterable)


#列表生成器，用来快速的创建列表
print range(1, 11)
print [x * x for x in range(1, 11)]
print [x * x for x in range(1, 11) if x % 2 == 0]

print [k + "=" + v for k, v in dirc.iteritems()]

print [s.lower() for s in name_list]


#生成器，用来解决变循环变计算的机制，减少内容使用
print [x * x for x in range(10)]
generator = (x * x for x in range(10))

for n in generator:
    print n,

print


def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1


print fab(5).next()
for n in fab(5):
    print n


#sort 排序
print sorted([23, 54, 1, 4, 65])


def sortfun(x, y):
    if x > y:
        return -1
    elif x < y:
        return 1
    else:
        return 0


print sorted([23, 45, 2, 13, 43], sortfun)


#忽略大小写的比较
def ignorecompare(s1, s2):
    u1 = s1.upper()
    u2 = s2.upper()

    if u1 > u2:
        return 1
    elif u1 < u2:
        return -1
    else:
        return 0


print sorted(["abd", "SD", "ssAS", "ASS"])


#函数作为返回值
def calc_sum(*args):
    def sum1():
        dx = 0
        for arg in args:
            dx = dx + arg
        return dx

    return sum1


f1 = calc_sum(1, 34, 54, 65, 784, 342)
f2 = calc_sum(1, 34, 54, 65, 784, 342)

print f1
print f2
print f1 == f2
print f1()
print f2()


#匿名函数的使用
ff = lambda x: x * x

print ff
print ff(3)


def buildlambda(x, y):
    return lambda: x * x + y * y


function = buildlambda(3, 4)
print buildlambda(3, 5)()
print function
print function()

print "*******************"

# fff = buildlambda()
# print fff
# print fff()


#函数可以赋值给变量，变量也能调用函数
def now():
    print '2014-10-09'


now_now = now
now_now()

print now_now.__name__
print now.__name__

#偏函数的使用
int2 = functools.partial(int, base=2)

print int2('11110000')

print "*******************"


#定义记录日志函数
def log(func):
    def wrapper(*args, **kwargs):
        print "call %s()..." % func.__name__
        return func(*args, **kwargs)

    return wrapper


@log
def now_log():
    print "2014-23-12"

now_log()


#定义接受参数的日志函数
def log_parameter(text):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print "%s %s()..." % (text, func.__name__)
            return func(*args, **kwargs)
        return wrapper
    return decorator


@log_parameter("china")
def now_log_parameter():
    print "now log parameter"


now_log_parameter()




