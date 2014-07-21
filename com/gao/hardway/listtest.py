__author__ = 'wangchen'
#coding=utf-8

#首先定义三种类型的列表，其中有混合类型的列表

the_count = [1, 2, 3, 4, 5]
fruits = ["apple", "orange", "pears", "apriots"]
change = [1, "pennies", 2, "dimes", 3, "quartes"]

#第一种类型的循环
for number in the_count:
    print "this is count %d" % number


#对于其他类型的循环
for fruit in fruits:
    print "a fruit of type %s" % fruit

#对于混合类型的循环
for i in change:
    print "i got %r" % i


#定义一个空得列表
elements = []

#添加几个元素
for i in range(1, 6):
    print "start to append element %d to list" % i
    elements.append(i)

for i in elements:
    print "element was: %d" % i
