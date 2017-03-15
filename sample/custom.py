#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 由特殊用途的函数来定制类
class Student(object):
	def __init__(self, name):
		self.name = name

	def __getattr__(self, attr):  # 返回函数
		if attr=='score':
			return 99
		if attr=='age':
			return lambda: 25
		raise AttributeError('\'Student\' object has no attribute \'%s\'' %attr)

	def __call__(self):
		print('My name is %s' % self.name)

	def __str__(self):
		return 'Student object (name: %s)' % self.name
	__repr__ = __str__

s = Student('henry')
print(s)
print(s())
print(s.name)
print(s.score)  # 调用类不存在属性时，将会调用__getattr__来尝试获得属性
print(s.age())
# print(s.abc)

class Fib(object):
	def __init__(self):
		self.a, self.b = 0, 1

	def __iter__(self):
		return self  # 返回的实例本身就是迭代对象

	def __next__(self):
		self.a, self.b = self.b, self.a + self.b  # 计算数列下一个值
		if self.a > 100000:  # 循环结束条件
			raise StopIteration()
		return self.a  # 返回数列中下一个值

	def __getitem__(self, n):
		if isinstance(n, int):  # n是索引
			a, b = 1, 1
			for x in range(n):
				a, b = b, a + b
			return a
		if isinstance(n, slice):  # n是切片
			start = n.start
			stop = n.stop
			if start is None:
				start = 0
			a, b = 1, 1
			L = []
			for x in range(stop):
				if x >= start:
					L.append(a)
				a, b = b, a + b
		return L

for n in Fib():
	print(n)

f = Fib()
print(f[100])
print(f[0:5])
print(f[:5])