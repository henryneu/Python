#!/usr/bin/env python3
# -*- coding: utf-8 -*-

d = {'Michael':95, 'Henry':96, 'Emily':97}
d['Lucy'] = 94
d['Lucy'] = 91
key = (1, 2, 3)
d[key] = 98
print(d['Michael'])
d.pop('Michael')
print(d)
print('Tom' in d)
print(d.get('Tom'))
print(d.get('Tom'), -1)

s1 = set([1, 2, 2, 3, 3])
s2 = set([2, 3, 4])
s3 = set((1, 2))

s1.add(4)
s1.add(4)
s1.remove(4)
print(s1)
print(s2)
print(s1 & s2)
print(s1 | s2)
print(s3)
