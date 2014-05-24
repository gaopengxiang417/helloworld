__author__ = 'wangchen'
#coding=utf-8


#基本的try语句块
try:
    s = raw_input("please write -->")

except EOFError:
    print "why write a eofexceptio"
    exit()
except:
    print "other except"

print "done"



#try else
class MyException(Exception):
    """define base own exception"""

    def __int__(self, lenth, atleast):
        Exception.__init__(self)
        self.lenth = lenth
        self.atleast = atleast


try:
    s = raw_input("pleast write ->")
    if len(s) < 3:
        raise MyException(len(s), 3)

except:
    print "why write eroor"
else:
    print "all is right"

finally:
    print "enter finally block"

