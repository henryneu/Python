
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import types

# type
print('type(123) =', type(123))
print('type(\'123\') =', type('123'))
print('type(None) =', type(None))
print('type(abs) =', type(abs))

print('type(\'abc\')==str?', type('abc')==str)


class MyObject(object):
	name = 'object'
	def __init__(self):
		self.x = 9
	def power(self):
		return self.x * self.x

# attr
obj = MyObject() # 创建实例

print(obj.name)  # 因为实例并没有name属性，所以会继续查找class的name属性
print(MyObject.name)  # 类的name属性
obj.name = 'Henry'  # 给实例绑定name属性
print(obj.name)  # 由于实例的name属性优先级高于类的name属性，因此会屏蔽掉类的
print(MyObject.name)  # 但是类的name属性并没有改变
del obj.name  # 删除掉实例的name属性
print(obj.name)  #  再次打印实例的name属性，由于找不到，类的name属性将打印出来

print('hasattr(obj, \'x\') =', hasattr(obj, 'x')) # 有属性'x'吗？
print('hasattr(obj, \'y\') =', hasattr(obj, 'y')) # 有属性'y'吗？
setattr(obj, 'y', 19) # 设置一个属性'y'
print('hasattr(obj, \'y\') =', hasattr(obj, 'y')) # 有属性'y'吗？
print('getattr(obj, \'y\') =', getattr(obj, 'y')) # 获取属性'y'
print('obj.y =', obj.y) # 获取属性'y'

print('getattr(obj, \'z\') =',getattr(obj, 'z', 404)) # 获取属性'z'，如果不存在，返回默认值404

f = getattr(obj, 'power') # 获取属性'power'
print(f)
print(f())