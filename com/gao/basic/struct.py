__author__ = 'wangchen'
#coding=utf-8

shoplist = ["first", "second", "third", "fouth"]

#print the length
print "the length of list is:", len(shoplist)

#print the list
print "the list is",
for item in shoplist:
    print item,

#添加元素
print "\nstart to new list"
shoplist.append("last")
print shoplist

#排序列表
shoplist.sort()
print shoplist

#删除元素
temp = shoplist[0]
del shoplist[0]

print "i got", temp
print shoplist


