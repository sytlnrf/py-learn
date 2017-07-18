# -*- coding: utf-8 -*-
# from __future__ import division
import math
import random
from decimal import Decimal
# ### tube
# tu = (1, 2, 3, 4, 1)
# #print tu.index(5)
# print tu.count(1)
# print tu == 1
# print tu + tu
# print tu * 3
# 
# tu1 = (3)
# print type(tu1)
# tu1 = (3,)
# print type(tu1)
# print len(tu1)
# print tu1[0]
# tu1 = 1,2,3,4,1
# print tu1.index(1)
# print tu1.count(1)
# print type(tu1)
# print tu1[2]
# 
# tu = (1, [2, 3, 4], 5)
# tu[1][0] = 6
# print tu
# 
# ### number format
# import math
# nua = 3
# nub = 4
# nuc = -4
# print nua / nub
# print nua // nub
# print nua / nuc
# print nua // nuc
# print math.floor(2.5)
# print math.floor(-2.5)
# print math.trunc(2.5)
# print math.trunc(-2.5)
# j = 4
# print j
# print 2+3j*j
# 
# print oct(64), hex(64), bin(64)
# print int('64'), int('100', 8), int('40', 16), int('01000000',2)
# x = 3
# print bin(x)
# print x | 2
# print x & 1
# print x ^ 1
# print x << 1
# print x >> 1
print round(2.567) 
print round(2.567, 2) 
print round(-2.567) 
print round(-2.567, 2) 
print '%.2f' % (1.0 / 3)
print round(1.0 / 3, 2)
print type(round(-2.567, 2))
 
print random.random()
print random.randint(1, 10)
print random.choice([1,4,6,7,8])

print 0.1 + 0.1 + 0.1 - 0.3
print Decimal('0.1')  + Decimal('0.1') + Decimal('0.1') - Decimal('0.3') 
print 1999 + 1.33
