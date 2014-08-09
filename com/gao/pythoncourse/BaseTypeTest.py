__author__ = 'wangchen'
#coding=utf-8

import math

#字符串的转义
print "\\\t\\"
print r"\\\t\\"
print r"""\\\t\\
    sdf
    sds
"""

True
False
None

print None
print True

a = "xyz"
b = a
a = "lll"
print b

#tuple一定初始化，就不能修改,这里应该是引用不能修改
classmated = ("first", "second", "third")
print classmated

t = (1,2)
print t

tt = (1,)
print tt


#python里面的for 循环例子
for mate in classmated:
    print mate,

for i in range(2,30):
    print i,

print
#while循环
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n -= 2

print sum


#raw_input得到的永远是字符串


#set使用,set需要一个list作为传入参数
s = set([1,2,3])
print s

s = set([1,2,3,4,5,2,1,3])
print s

#添加元素
s.add(3)
s.add(22)

print s

#删除元素
s.remove(3)
print s

s1 = set([5,6,7,87,45,2,4,1])

#set可以做交际和并集
print s & s1
print s | s1


#自定义函数
def my_abs(x):

    if not isinstance(x, (int, float)):
        raise TypeError("bad operand type")

    if x > 0:
        return x
    else:
        return -x


#空函数，pass作为占位符，以后写
def null_fun():
    pass

# print my_abs("s")

#python中是支持多只返回 ，其实是返回一个tuple

def move(x, y, step, angle=0):

    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

result = move(100,100,40,math.pi / 6)
print result


#函数的参数和默认参数

def my_power(x, n=2):

    s = 1
    while n > 0:
        n -= 1
        s *= x
    return s

print my_power(4,4)
print my_power(3)


#默认参数的坑
def add_end(l = []):
    l.append("end")
    return l

print add_end(["first", 12])
print add_end([23, 5, 5])

print add_end()
print add_end()


def add_end_new(l = None):
    if l is None:
        l = []

    l.append("end")
    return l

print add_end_new()
print add_end_new()

#可变参数的功能
def calc(*numbers):

    sum = 0
    for i in numbers:
        sum = sum + n * n
    return sum


print calc(1, 3, 5)


#关键字参数，用来解决传入0个或者任意多个参数名的参数
def person(name, age, **kwargs):
    print "name:", name, "age:", age, "others:",kwargs


print person("chian", 45, city="beijing")
json = {"first": 1, "second": 2}

print person("kkkk", 44, jons = json)

#各种参数组合
def func(a, b, c = 0, *args, **kwargs):
    print a,b,c,args,kwargs

func(1, "88", 43, "43", "kkkk", ke={"kk":"ss"})