__author__ = 'wangchen'
#coding=utf-8

import sys

#首先从命令行接受需要读取的文件名称
filename = sys.argv[1]

#打开文件，下一步读取
file = open(filename)

#开始读取内容
file_read = file.read()
print file_read

#关闭文件流
file.close()


print "type the filename again"
input_filename = raw_input(">")

input_file = open(input_filename)

print input_file.read()

#关闭文件流
input_file.close()
