#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 导入functools模块
import functools

# 不带参数的decorator
def log(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		print('begin call %s():' %func.__name__)
		res = func(*args, **kw)
		print('end call %s():' %func.__name__)
		return res
	return wrapper

# 带参数的decorator
def log_t(*text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			print('%s %s():' %(text[0], func.__name__)) # 调用函数前打印日志
			res = func(*args, **kw)
			print('%s %s():' %(text[1], func.__name__)) # 调用函数后打印日志
			return res
		return wrapper
	return decorator

@log
def now():
	print('2017.3.11')

@log_t('execute', 'end')
def new():
	print('2017.3.11:11:28')

print(now())
print(new())

print(now.__name__)
print(new.__name__)