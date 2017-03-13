#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
	"""docstring for Student"""
	def __init__(self, name, score):  # 第一个参数永远是self 表示创建的实例本身
		super(Student, self).__init__()
		self.__name = name
		self.__score = score

	def print_score(self):
		print('%s: %s' % (self.__name, self.__score))

	def get_grade(self):
		if self.__score >= 90:
			return 'A'
		elif self.__score >= 60:
			return 'B'
		else:
			return 'C'

	def set_name(self, name):
		self.__name = name

	def set_score(self, score):
		if 0 <= score <= 100:
			self.__score = score
		else:
			raise ValueError('error score')

	def get_name(self):
		return self.__name

	def get_score(self):
		return self.__score

emily = Student('Emily', 98)

emily.print_score()
print(emily.get_grade())

emily.set_name('Henry')
emily.set_score(99)
print(emily.get_name(), emily.get_score())