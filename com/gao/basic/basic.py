__author__ = 'wangchen'
#coding=utf-8
#字符换
print 'first string'
print "second string"
print '''this is
 third string .


  '''
#对于转移字符的展示
print "this is \" tss"

#对于行末的反斜杠用来标示下一行
print "the last lineyes \
      "
#如果一个字符换前面加r或者R标示是自然字符串，不需要进行转义
print r"newlines are created by ss\nss"

print "中国"

print u"unicode character 高鹏翔"

#字符串的自动连接
print 'first''second''and''third'

#变量和常量,变量只需要直接赋值，不需要声明变量的类型
i = 5
print i
i += 1
print i

s = "this is a multi linestring" \
    "new line"
print s

print("check")
print("ehck")

#运算符和操作数
print "********start to alg**********"
print 3 + 5  #加法
print 3 - 5  #减法
print 3 * 2  #乘法
print 3 * "l" #乘法
print 3 ** 3    #阶乘
print 4 / 3     #除法
print 4.0 / 3   #除法保留小数
print 4.0 // 3  #除法只输出整数
print 4 % 2     #莫
print 3 << 2
print 3 >> 2
print 3 & 1
print 3 | 2
print 3 < 4
print not True  #反向
print 3 != 4
print 3 == 4
print True and False
print True or False