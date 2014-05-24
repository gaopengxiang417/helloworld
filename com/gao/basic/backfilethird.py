__author__ = 'wangchen'
#coding=utf-8
import os
import time

#首先指定需要拷贝的文件
source_file = "/Users/wangchen/Documents/taobao/life/淘宝办公无线网络连接操作手册.doc"

#目的文件的路径
target_path = "/Users/wangchen/Documents/taobao/life/"

#生成日期信息
today = time.strftime("%Y%m%d")
now = time.strftime("%H%M%S")

#当前的文件夹
today_path = target_path + today

#获取用户输入的文件名称
filename = raw_input("please enter the filename : ")

if len(filename) == 0:
    target = today_path + now + ".zip"
else:
    target = today_path + filename.replace(" ", "_") + ".zip"

#判断今天的文件夹是否存在
if not os.path.exists(today_path):
    os.mkdir(today_path)
    print "success to mkdir", today_path

zip_command = "zip -qr '%s' %s " % (source_file, target)

if os.system(zip_command) == 0:
    print "success to zip file"
else:
    print "error "
