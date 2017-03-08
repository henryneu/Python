#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 导入os模板
import os
# 列表生成式
L = ['Hello', 'Henry', 'World', 18, 'Apple', 'IBM', None]
L1 = [s.lower() for s in L if isinstance(s, str)]
L2 = [x * x for x in range(1, 11)]
L3 = [x * x for x in range(1, 11) if x % 2 ==0]
print(L)
print(L1)
print(L2)
print(L3)
# 列表生成式可以使用两个变量来生成list
d = {'x':'A', 'y':'B', 'z':'C',}
d1 = [k + '=' + v for k, v in d.items()]
print(d1)
# 列表生成式还可以使用两层或三层循环
d2 = [m + n for m in 'ABC' for n in 'XYZ']
print(d2)
# os.listdir可以列出当前目录下的所有文件和目录名
d3 = [d for d in os.listdir('.')]
print(d3)