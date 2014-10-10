#!/usr/bin/env python
# _*_ coding: utf-8 _*_

__author__ = 'wangchen'

import sys

#变量的别名
try:
    import cStringIO as StringIO
except ImportError:
    import StringIO

try:
    import json
except ImportError:
    import simplejson as json


def test():
    """define a test method to access argument"""
    args = sys.argv

    if len(args) == 1:
        print "hello world"
    elif len(args) == 2:
        print "hello , %s" % args[1]
    else:
        print "too many argument"


if __name__ == "__main__":
        test()


#私有变量和函数，必须已_ 或者__开头
def _private_1(name):
    print "hello, %s" % name


def _private_2(name):
    print "hi, %s" % name


def greet(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)



