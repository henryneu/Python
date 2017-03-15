#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):

	# @property装饰器用法
	@property
	def score(self):
		return self.__score

	@score.setter
	def score(self, value):
		if not isinstance(value, int):
			raise ValueError('score must be an integer')
		if value<0 or value>100:
			raise ValueError('score must between 0~100')
		self.__score = value

s = Student()
s.score = 99  # 实际转化为s.set_score(60)
print(s.score)  # 实际转化为s.get_score()