__author__ = 'wangchen'
#coding=utf-8

print "Hello world"
print "hello again"
print "i like typing this"
print "this is fun"
print "yes,printing"
print "i would rather than you 'not'"
print 'i said "not " to touch that'

print "add a line"
# print "this line is comment"

#a comment , so you can read your program later
#anything after the # is ignored by python

print "I could have code like this." # and comment after this is ignored

# you can use comment to disable  or comment a piece of code
# print "this will not be print"

print "This will run"

# i will count the eggs

print "Hens:", 25 + 30 / 6
print "Roosters:", 100 - 25 * 3 % 4

# i will count the chickens

print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6
print "is that true 3 + 2 < 5 - 7", 3 + 2 < 5 - 7
print "what's that 3 + 2:", 3 + 2
print "what's that 5 - 7:", 5 - 7
print "that's why it's false"

print "how about some more"
print "is that greator: ", 5 > 12
print "is greator or equal:", 5 >= -4
print "is less or equal:", 5 <= -2

print 30.0 / 13

# 变量的使用
cars = 100
spaces_in_cars = 4.0
drivers = 30
passengers = 90
cars_not_driver = cars - drivers
cars_driven = drivers
carpool_capcity = cars_driven * spaces_in_cars
average_passengars_per_car = passengers / cars_driven

print "there are", cars, "can driven"
print "there are only", drivers, "drivers available"
print "there will be", cars_not_driver, "empty cars"
print "we can transport", carpool_capcity, "people today"
print "we have", passengers,"to carpool today"
print "we need to put about", average_passengars_per_car, "in each car"


# 变量和格式化的打印

my_name = "wangchen"
my_age = 27 # not a lie
my_height = 171 #cm
my_weight = 58 # kg
my_eyes = 'yellow'
my_teeth = "white"
my_hair = "black"

print "let's talk about %s ." % my_name
print "he is %d cm height" % my_height
print "he is %d kg " % my_weight
print "he got %s eyes and %s hair" % (my_eyes, my_hair)
print "he teeth are usually %s" % my_teeth
print "he is %r name" % my_name
print "he age is %r" % my_age

# python中得所有的格式化的功能
print "the integer is %d" % my_age #整形

print "the octor is %o" % my_age #八进制

print "the floot is %f" % 34.3434 #浮点
print "the floot is %6.2f" % 34.34343 #保留进制的浮点
print "the floot is %06.2f" %23.43434 #前面补位

print "the %d %%" % 23 #用来在格式化字符串中输出 %

print "the number is %e" % 234.454545 #科学计数法

# 变量和格式化打印联合一起使用

x = "there are %d types of people" % 10
binary = "binary"
do_not = "don't"
y = "those who know %s and those who %s" % (binary, do_not)

print x
print y

print "i said : %r" % x
print "i also said: '%s'." % y

hilarious = False
joke_evaluation = "isn't that joke so funny ? %r"

print joke_evaluation % hilarious

w = "this is the left side of ..."
e = "a string with a right side..."

print w + e

print "mary had a little lamb"
print "its fleece was white as %s." % "snow"
print "and everywhere that mary went"
print "." * 10

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# 如果用print打印的时候，如果后面加上一个逗号，那么下面的打印行会喝这一行合并
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12


# 测试format格式
formats = "%r %r %r %r"

print formats % (1, 2, 3, 4)
print formats % ("one", "two", "three", "four")
print formats % (True, False, False, True)
print formats % (formats, formats, formats, formats)
print formats % ("i had the thing", "that you type right",
                 "but it didn't sing", "so i said goognight")


# here is some new strange stuff,remember type it right
days = "mon tue wed thu fri sat sun"
months = "jan\nfeb\nmar\napr\nmay\njun\njul\naug"

print "these days", days
print "there months", months

print """
there is something going here
with the three double-quotes
we'll touch as much as we can
even 4 lines if we like ,
"""

# python中得转移功能
tabby_cat = "\ti'm tabby in"
persian_cat = "i'm split\n on a line"
backslash_cat = "i'm \\ a \\ cat"

fat_cat = """
l'll do a list:
\t* cat foot
\t* fish
\t* catninp\n\t"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

#三个单引号的功能,三个单引号里面的内容不会进行任何的转换
print '''i'll do a list\t*cat\tfish'''

#转移和格式化
print "i love \n %s, ok \t a table " % "china"

#%r来转移单引号和双引号,如果%r,里面如果有单引号会把外面转化为双引号
print "i love %r that" % 'a \'quit'
print "i love %s that" % 'a \'quit'

print "how old are you?",
age = raw_input("please write you age:")
print "how tall are you?",
tall = raw_input("please write you tall:")
print "how much are your weight?",
weight = raw_input("please write you weight:")

print "so,your are %s old,and your height is %s and your weight is %s" % (age, tall, weight)


#raw_input and input 区分这两者的不同
raw_string = raw_input("raw input:")
input_string = input("input:")



