#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import reduce

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

print(str2float('1234.56789'))