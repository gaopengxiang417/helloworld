__author__ = 'wangchen'
#coding=utf-8

from sys import argv


#添加对于input的功能
name = raw_input("please write your name:")
print name

#这个事强制的解包功能，其实也就是把传入的argu一个参数分解成为多个对应的参数
#script, first, second, third = argv
script = argv[0]
first = argv[1]
second = argv[2]
third = argv[3]

print "the script is :", script
print "the first argument is:", first
print "the second argument is:", second
print "the fouth argument is:", third
