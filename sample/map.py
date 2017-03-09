#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import reduce

def f(x):
	return x * x * x

def g(x, y):
	return x + y 

def fn(x, y):
	return x * 10 + y

def char2num(s):
	return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

def str2int(s):
	def fn1(x, y):
		return x * 10 + y
	def char2int(s):
		return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
	return reduce(fn1, map(char2int, s))

# 这个缩进错误坑死我了
def str2float(s):
	def float2int(x, y):
		return x * 10 + y
	def str2num1(s):
		return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '.': '.'}[s]
	L = list(map(str2num1, s))
	n = L.index('.')
	front = [x for x in s[:n]]
	end = [y for y in s[n + 1:]]
	sf = reduce(float2int, map(str2num1, front))
	sn = reduce(float2int, map(str2num1, end))
	return sf+sn/(10**(len(s) - n - 1))

# lambda函数
def str2num(s):
	return reduce(lambda x, y: x * 10 + y, map(char2num, s))

r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
l = list(r)
print(l)
print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

red = reduce(g, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(red)

fnu = reduce(fn, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(fnu)

ch = reduce(fn, map(char2num, '123456'))
print(ch)

print(str2int('12345678'))
print(str2num('12345678'))

print(str2float('123456.789'))
print(str2float('123.456789'))