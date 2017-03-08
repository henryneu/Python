#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def move(x, y, step, angle=0):
	dx = x + step * math.cos(angle)
	dy = y - step * math.sin(angle)
	return dx, dy

def power(x, n=2):
	s = 1
	while n > 0:
		n = n - 1
		s = s * x
	return s

def my_abs(x):
	if not isinstance(x, (int, float)):
		raise TypeError('bad operand type')
	if x >= 0:
		return x
	else:
		return -x

def quadratic(a, b, c):
	t = b*b-4*a*c
	if(t<0):
		print('方程无解')
	elif(t==0):
		x=(-b/(2*a))
		return x
	else:
		x1=(-b+math.sqrt(t))/(2*a)
		x2=(-b-math.sqrt(t))/(2*a)
		return x1, x2

def add_end(L=[]):
	L.append('END')
	return L

def person(name, age, **kw):
	print(name, age, kw)

def student(name, age, *, city, job):
	print(name, age, city, job)

extre = {'city':'Beijing', 'job':'Engineer'}

d = move(100, 100, 60, math.pi / 6)
print(d)

print(quadratic(2, 3, 1))
print(quadratic(1, 3, -4))

print(power(5))
print(add_end())
print(add_end())
person('Henry', 25, **extre)
student('Emily', 26, city='zhengzhou', job='Engineer')