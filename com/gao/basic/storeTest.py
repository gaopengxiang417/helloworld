__author__ = 'wangchen'
#coding=utf-8

import cPickle

#首先定义要写入的内容
poem = """this is a poem
       the second line
    轻轻的你走了，就如你轻轻地来"""

txt = "test.txt"
writefile = file(txt, "w")

#首先写入文件内容
writefile.write(poem)
writefile.close()

#开始读取文件内容
readfile = file(txt)

while True:
    line = readfile.readline()
    if len(line) == 0:
        break

    print line

readfile.close()


#将对象持久化到文件中
shopfile = file("shop.data","w")


shoplist = ["first", "second", "third"]
cPickle.dump(shoplist, shopfile)
shopfile.close()

#删除内存中得数据
del shoplist

pickle_load = cPickle.load(file("shop.data"))

print pickle_load
