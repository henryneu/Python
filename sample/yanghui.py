#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 输出杨辉三角
# 第一种写法
max = int(input('Insert level: '))

def yanghui(max):
    L = [1]
    n = 1
    while n <= max:
        yield L
        L.append(1)
        K = tuple(L)
        for i in range(len(K)):
            L[i] = K[i-1] + K[i]
        L[0] = 1
        L[len(L) - 1] = 1
        n = n + 1

a = yanghui(max)
for k in range(max):
    print(next(a))

# 第二种写法
def yanghui1():
	L = [1]
	while True:
		yield L
		L.append(0)
		L = [L[i - 1] + L[i] for i in range(len(L))]

b = yanghui1()
for j in range(10):
	print(next(b))