#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def is_odd(num):
	return num % 2 == 1

def not_empty(s):
	return s and s.strip()

print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))
print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))

# 生成从3开始的奇数
def ge_num():
	n = 1
	while True:
		n = n + 2
		yield n
# 筛选函数
def not_divi(n):
	return lambda x: x % n >0
# 产生素数序列
def prime():
	yield 2
	num_list = ge_num()  # 初始化序列
	while True:
		n = next(num_list)
		yield n
		new_num_list = filter(not_divi(n), num_list)  # filter 过滤构造新的序列

for x in prime():
	if x < 1000:
		print(x)
	else:
		break

# 判断一个数是否是回数
def is_palindrome(n):
	strn = str(n)
	i = 0
	if strn[i] == strn[len(strn) - i - 1]:
		return True
	else:
		return False
l = list(filter(is_palindrome, range(1, 1000)))
print(l)