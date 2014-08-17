__author__ = 'wangchen'
#coding=utf-8

from collections import Iterable

#切片的使用

name_list = ["Michacl", "Sarah", "Tracy", "Bob", "Jack"]

#最泵的办法
print [name_list[0], name_list[3]]

#最高效的办法
print name_list[0:3]
print name_list[:3]
print name_list[-1]
print name_list[:]
print name_list[3:]
print name_list[4:100]

#定义tuple
tuple_list = ("Michacl", "Sarsh", "Tracy", "Bob", "Jack")

print tuple_list[0:3]
print tuple_list[:]
print tuple_list[-2]


#迭代的使用
dirc = {"name": "china", "age": "44", "street": "the publish of china"}

for key, value in dirc.iteritems():
    print key,value


#字符串迭代
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
