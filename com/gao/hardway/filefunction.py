__author__ = 'wangchen'
#coding=utf-8

import sys

#首先应该接受参数
script = sys.argv[0]
file_name = sys.argv[1]

#定义读取整个文件内容函数
def read_all(f):
    print f.read()


#定义搜索
def rewind(f):
    print f.seek(0)

#定义读取一行
def read_line(line_count, f):
    print line_count, f.readline()


#打开一个文件
file = open(file_name)

#读取文件内容
print "read all file content..."
read_all(file)

#定义搜索
print "let's rewind a "
rewind(file)

#读取一行一行
currentline = 1
read_line(currentline,  file)

currentline += 1
read_line(currentline, file)

currentline += 1
read_line(currentline, file)

