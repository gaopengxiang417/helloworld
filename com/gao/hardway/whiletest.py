__author__ = 'wangchen'
#coding=utf-8

i = 0
numbers = []

while i < 6:
    print "at the top i is %d" % i

    numbers.append(i)

    i += 1
    print "the number now is %d" % i
    print "at the bottom is %d" % i

print "numbers:"

for number in numbers:
    print number