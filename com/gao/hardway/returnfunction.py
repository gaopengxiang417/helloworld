__author__ = 'wangchen'
#coding=utf-8


#自定义一些函数，最基本的加减乘除
def add(a, b):
    print "add %d + %d" % (a, b)
    return a + b

def substrct(a, b):
    print "subtrct %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "multiply %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "divide %d / %d" % (a, b)
    return a / b


#开始基本的计算调用，注意其中的返回值
add_result = add(30, 3)
substrct_result = substrct(40, 60)
mutiply_result = multiply(40, 2)
divide_result = divide(20, 5)


print "the add result %d, subtrct result %d, mutiply result %d,divide result %d" % (add_result, substrct_result, mutiply_result, divide_result)

#下面的是复合调用
what = add(add_result, substrct(substrct_result, multiply(mutiply_result, divide(divide_result, 2))))

print "the final result is %s" % what