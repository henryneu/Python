#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 导入functools模块
import functools

# 两种情况都能适用
def log_double(t):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			print(t + ' begin call')
			res = func(*args, **kw)
			print(t + ' end call')
			return res
		return wrapper
	if isinstance(t, str):  # 判断传入的是否是字符串
		return decorator
	else:
		f = t
		t = ''
		return decorator(f)

@log_double
def a():
	print('double a')

@log_double('test')
def b():
	print('double b')

print(a())
print(b())