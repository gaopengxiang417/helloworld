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

#元组的定义
zoo = ("wolf", "elephant", "loin")
print "the number of zoo is ", len(zoo)

new_zoo = ("monkey", "mouse", zoo)
print "the length of new zoo is", len(new_zoo)

#元组是不会打乱以前的结构的，内部其实就是嵌套对象
print "all new_zoo,", new_zoo
print "third",new_zoo[2]
print "fouth,", new_zoo[2][2]


#元组在输出语句中得作用
age = 22
name = "wangchen"

print "%s is age %d" % (name, age)
print "why is %s play python" % name
# print "%s is age %d error" % name


#字典的使用，其实就是map的概念
db = {
    "hubei": "wuhan",
    "hunan": "changsha",
    "zhejiang": "hangzhou"
}
print "the db value is %s" % db
db["zhejiang"] = "error"
print "the db new value is %s" % db
del db["zhejiang"]

print "after delete is %s" % db

for key, value in db.items():
    print "city is %s, captital is %s" %(key, value)


if "china" in db:
    print "china is in db"

if db.has_key("hubei"):
    print "hubei is in dirctory"


#序列的使用
citylist = ["beijing", "shenzhen", "hangzhou", "nanjing"]

print "item 0 is ", citylist[0]
print "item 1 is ", citylist[1]
print "item 2 is ", citylist[2]
print "item 3 is ", citylist[3]
# print "item 4 is ", citylist[4]

#进行切片访问
print "item 1 to 3 is", citylist[1:3]
print "item 2 to end is", citylist[2:]
print "all is ", citylist[:]
print "from 1 to last second one is ", citylist[0:-1]

#对字符串进行切片
name = "iamachinese"

print "characters 1 3 is", name[1:3]
print "characters 2 end is", name[2:]


#引用的关系说明，拷贝对象只有通过slice的方式来进行
print "simple assignment"

myshoplist = ["apple", "mongo", "carrot", "banana"]
templist = myshoplist

print "init myshoplist", myshoplist
print "init templist", templist

#首先删除一个元素，两个列表都应该有变化
del myshoplist[0]

print "delete myshoplist", myshoplist
print "delete templist", templist

#通过切片的方式来进行拷贝
newlist = myshoplist[:]

del newlist[0]

print "newlist is", newlist
print "myshoplist is", myshoplist


#字符串的各种方法
myname = "wangchen"
if myname.startswith("wa"):
    print "yes ,i am start with wa"

if "che" in myname:
    print "yes , contain che"

if myname.find("e") != -1:
    print "yes, contain e"

print myname.find("n")
print myname.rfind("n")

delimiter = "_*_"
print delimiter.join(newlist)

