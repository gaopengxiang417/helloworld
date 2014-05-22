__author__ = 'wangchen'
#endoing=utf-8

import sys
import mymodel

print "i am command argument are"

for i in sys.argv:
    print i

print "the python path is:", sys.path, '\n'


if __name__ == "__main__":
    print "this program is used by itself"
else:
    print "i am being import by other model"


mymodel.saymodel()

print mymodel.version

print dir(sys)
print dir(mymodel)




