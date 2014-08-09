__author__ = 'wangchen'
#coding=utf-8

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



