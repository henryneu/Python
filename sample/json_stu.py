#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
# dict 序列化为 json
d = dict(name='Bob', age=20, score=88)
data = json.dumps(d)
print('JSON Data is a str:', data)

# 序列化为 file-like Object对象
f = open('js.txt', 'w')
data1 = json.dump(data, f)
f.close()
print('write to file', data1)

# json 反序列化为 dict
reborn = json.loads(data)
print(reborn)

# 反序列化 file-like Object对象
f = open('js.txt', 'r')
data2 = json.load(f)
f.close()
print('read from file', data2)

# 序列化类对象
class Student(object):

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return 'Student object (%s, %s, %s)' % (self.name, self.age, self.score)

s = Student('Bob', 20, 88)
std_data = json.dumps(s, default=lambda obj: obj.__dict__)
print('Dump Student:', std_data)
rebuild = json.loads(std_data, object_hook=lambda d: Student(d['name'], d['age'], d['score']))
print(rebuild)