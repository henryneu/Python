#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import sqrt
from math import sin

# 函数作为参数传入
# 使用可变参数
def same(x, *fs):
	f = [f(x) for f in fs]
	return f

def do_fun(x=[], *fu):
	fx = [f(x_i) for x_i in x for f in fu]
	return fx

print(same(3, abs, sqrt, sin))
print(do_fun([1, 2, 4, 9], abs, sqrt, sin))