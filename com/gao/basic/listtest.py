__author__ = 'wangchen'
#coding=utf-8


#动态的创建一个新的列表，原来的列表不做任何操作
ll = [3,5,6,1,2]

ll2 = [2 * i for i in ll if i >2]

print ll2


#函数中接受多个参数，其中*表示传入的参数按照list，如果是**表示传入的是一个字典
def powersum(power, *args):
    """返回多个参数的和"""

    total = 0
    for j in args:
        total += pow(j, power)

    return total

print powersum(2,3,4)
print powersum(2,3,4,5)


#lambda表达式的使用
def make_repeator(n):
    return lambda s: s * n


repeator = make_repeator(2)

print repeator("word")
print repeator(4)

#exec用来执行字符串中得python表达式
exec "print 'helo wangchen'"

#用eval来执行表达式运算
print eval("3 * 4")

mylist = ["first"]
assert len(mylist) >= 1

print mylist.pop()

# assert len(mylist) >= 1

#repr表达式,类似于string表达式
my = []
my.append("first")
my.append("secod")
print `my`

print repr(my)



