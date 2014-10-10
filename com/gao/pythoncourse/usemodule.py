#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from __future__ import unicode_literals
from __future__ import division

__author__ = 'wangchen'

import moduletest


moduletest.greet("wangchen")
moduletest.greet("22")


#一些future功能的实现
print '\'xxx\' is a unicode?', isinstance('xxx', unicode)
print 'u\'xxx\' is a unicode', isinstance(u'xxx', unicode)
print '\'xxx\' is a str', isinstance('xxx', str)
print 'b\'xxx\' is a str', isinstance(b'xxx', str)

print '10 / 3 = ', 10 / 3
print '10 // 3= ', 10 // 3
print '10.0 / 3 = ', 10.0 / 3
