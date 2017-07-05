# -*- coding: utf-8 -*-
### tube
tu = (1, 2, 3, 4, 1)
#print tu.index(5)
print tu.count(1)
print tu == 1
print tu + tu
print tu * 3

tu1 = (3)
print type(tu1)
tu1 = (3,)
print type(tu1)
print len(tu1)
print tu1[0]
tu1 = 1,2,3,4,1
print tu1.index(1)
print tu1.count(1)
print type(tu1)
print tu1[2]

tu = (1, [2, 3, 4], 5)
tu[1][0] = 6
print tu

