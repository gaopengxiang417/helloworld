__author__ = 'wangchen'
#coding=utf-8

print "let's practise everything"

#转义字符的使用
print "you'd need to know \'bout escape with \\ that do \n a new line and \t tabs"


#自带格式的字符串
poem = """
\tthe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print "---------------"
print poem
print "---------------"


three = 10 - 4 + 3 - 6
print "this number should be three: %s" % three

#自定义函数，返回多个值
def secret_formula(started):
    multiply = started * 4
    divide = started / 4
    add = started + 4
    return multiply, divide, add


started = 1000
first, second, third = secret_formula(started)

print "the start point is %d" % started
print "the multiply %d, the divide %d, the add %d" % (first, second, third)

