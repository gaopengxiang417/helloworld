__author__ = 'wangchen'
#coding=utf-8

import os
import time


#需要备份的文件
sourcefile = "/Users/wangchen/Documents/taobao/life/个人总结.pages"

#备份以后的目的地
targetpath = "/Users/wangchen/Documents/taobao/life/"

#备份的具体的路径和文件名称
target = targetpath + time.strftime("%Y%m%d%H%M%S") + ".zip"

#进行压缩的命令
zip_command = "zip -qr '%s'%s" % (target, ''.join(sourcefile))

#校验是否压缩成功
if os.system(zip_command) == 0:
    print "successful backup", target
else:
    print "error"

