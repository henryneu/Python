
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from types import MethodType

class Student(object):
	pass

class People(object):
	# slots 定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
	__slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称

class Boy(People):
	__slots__ = ('grade') # 子类也定义slots，则子类实例允许的属性就是自身的加父类的

def set_score(self, score):
	self.score = score

def set_age(self, age):
	self.age = age

Student.set_score = set_score  # 给类Student 绑定方法

s = Student()
s.name = 'Henry'
print(s.name)
s.set_age = MethodType(set_age, s)  # 给实例绑定一个方法
s.set_age(25)
s.set_score(98)  # 类绑定的方法，每一个实例都可以使用
print(s.age)
print(s.score)

s1 = Student()  # 创建一个新实例，测试类绑定的新方法
s1.set_score(99)
print(s1.score)

p = People()  # 创建一个新的实例
p.name = 'Emily'
p.age = 26
# p.score = 100  # 由于score没有在slots中，所以不能绑定
print(p.name)
print(p.age)
# print(p.score)

b = Boy()
# b.score = 99  # slots 对继承的子类不起作用
b.name = 'Mike'
b.age = 12
b.grade = 5
# print(b.score)
print(b.name)
print(b.age)
print(b.grade)