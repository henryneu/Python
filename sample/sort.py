#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python内置的sorted函数可以对list进行排序
print(sorted([36, 5, -12, 9, -21]))
# Python内置的sorted函数也可以接收一个key函数实现对list的自定义排序
print(sorted([36, 5, -12, 9, -21], key = abs))
# 对字符串进行默认排序
print(sorted(['bob', 'about', 'Zoo', 'Credit']))
# 按小写字母的顺序排序
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
# 在上面的基础上倒序排列
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse = True))

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# 按名字排序
def by_name(t):
	return t[0]
# 按成绩排序
def by_score(t):
	return t[1]
ln = list(sorted(L, key = by_name))
ls = list(sorted(L, key = by_score))

print(ln)
print(ls)