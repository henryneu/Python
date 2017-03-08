#!/usr/bin/env python3
# -*- coding: utf-8 -*-

L = [x * x for x in range(10)]
print(L)
g = (x * x for x in range(10))
print(g)

def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		# print(b)
		yield b
		a, b = b, a + b
		n = n + 1
	return 'done'

for n in fib(20):
	print(n)

# 捕获异常
f = fib(8)
while True:
	try:
		x = next(f)
		print('g', x)
	except StopIteration as e:
		print('Generator return value:', e.value)
		break