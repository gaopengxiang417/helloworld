__author__ = 'wangchen'
#coding=utf-8

import sys
import os

#实现问价拷贝功能

#首先命令行读取传入的原始文件和目的文件
script = sys.argv[0]
from_filename = sys.argv[1]
to_filename = sys.argv[2]

print "we are going copy from file %s to file %s" % (from_filename, to_filename)

#读取原始文件内容
fromfile = open(from_filename)
result = fromfile.read()

print "the length of from file is %d" % len(result)

print result

#校验目的文件是否存在
print "whether the target file is exist %r" % exit(to_filename)

#将内容写入目的文件
targetfile = open(to_filename, "w")

targetfile_write = targetfile.write(result)
targetfile.flush()

print "write length is %s " % targetfile_write
print "all right "

targetfile.close()
fromfile.close()
