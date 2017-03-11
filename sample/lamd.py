#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# lambda 表示匿名函数
# 匿名函数是一个对象，可以赋值给一个变量
f = lambda x: x * x
print(f(3))
print(list(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

def fun_lam(x, y):
	return lambda: x * x + y * y
f1 = fun_lam(3, 4)
print(f1())