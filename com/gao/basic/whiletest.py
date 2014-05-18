__author__ = 'wangchen'
#coding=utf-8

#测试while条件判断
number = 45
issuccess = True

while issuccess:
    guess = int(raw_input("please write a number"))
    if guess == number:
        print "you get the correct number.."
        issuccess = False

    elif guess > number:
        print "you input number bigger than number"
    else:
        print "you input is smaller than number"
else:
    print "else while block"
print "done"


#for in 的循环使用
for i in range(1,6):
    print i
else:
    print "close"

#break 语句的使用
while True:
    inputs = raw_input("enter input string:")
    if inputs == "china":
        print "echo"
        break
    else:
        print "error"
else:
    print "finally closed"