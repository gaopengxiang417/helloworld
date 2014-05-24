__author__ = 'wangchen'
#coding=utf-8

import os
import time



#需要备份的文件
source_file = "/Users/wangchen/Documents/taobao/life/淘宝办公无线网络连接操作手册.doc"

#目的目录
target_path = "/Users/wangchen/Documents/taobao/life/"

#获取当天的日期
today = time.strftime("%Y%m%d")
#获取时间
now = time.strftime("%H%M%S")

#当天的目录
today_path = target_path + today

#判断目录是否存在
if not os.path.exists(today_path):
    os.mkdir(today_path)
    print "success create directory"

#具体的备份文件
target_file = today_path + os.sep + now + ".zip"

#备份的命令
zip_command = "zip -qr '%s' %s" % (source_file, target_file)

if os.system(zip_command) != 0:
    print "error"
else:
    print "success"

print os.sep
