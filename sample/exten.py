#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Animal(object):
	def run(self):
		print('Animal running...')

class Dog(Animal):
	def run(self):
		print('Dog running...')

	def shout(self):
		print('Dog wang wang...')

class Cat(Animal):
	def run(self):
		print('Cat running...')

	def shout(self):
		print('Cat miao miao...')

class Pig(Animal):
	def run(self):
		print('Pig running slowly...')

def run_twice(animal):
		animal.run()
		animal.run()

dog = Dog()
cat = Cat()

print(dog.run())
print(cat.run())
print(run_twice(Animal()))
print(run_twice(Dog()))
print(run_twice(Cat()))
print(run_twice(Pig()))