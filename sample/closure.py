#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def lazy_sum(*num):
	def sum():
		result = 0
		for n in num:
			result = n + result
		return result
	return sum
f = lazy_sum(1, 3, 5, 7, 9)
# 调用lazy_sum 返回的是函数，不是结果
print(f)
# 调用 f() 返回求和结果
print(f())

def count():
	def f(j):
		def g():
			return j * j
		return g
	fs = []
	for i in range(1, 4):
		fs.append(f(i)) # f(i) 立即执行，因此i的当前值被传入f()
	return fs
f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())