__author__ = 'wangchen'
#coding=utf-8

import sys

#读取文件内容，然后清空，然后写入文件内容

#首先传入文件名称
script = sys.argv[0]
filename = sys.argv[1]

print "we are going to earse file %s" % filename
print "if you do not that ,please hit ctrl + c"
print "if you do want that ,hit return"

raw_input("?")

#首先打开文件并且清空
print "start to open file"
file = open(filename, "r+")

print "start to truncate file"
file.truncate(0)

#开始写入三行内容
print "i will write three line "

line1 = raw_input("line 1 :")
line2 = raw_input("line 2:")
line3 = raw_input("line 3:")

print "start to write three line"

file.writelines(line1)
file.writelines(line2)
file.writelines(line3)

file.flush()


#开始读取里面内容
print file.read()
file.close()


