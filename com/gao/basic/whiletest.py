__author__ = 'wangchen'
#coding=utf-8

#测试while条件判断
number = 45
guess = int(raw_input("please write a number"))
issuccess = True

while issuccess:
    if guess == number:
        print "you get the correct number.."
        issuccess = False

    elif guess > number:
        print "you input number bigger than number"
    else:
        print "you input is smaller than number"

print "done"

