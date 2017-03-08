#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fact(n):
	if n == 1:
		return 1
	else:
		return n * fact(n-1)

def facte(n):
	return facter(n, 1)

def facter(num, result):
	if num == 1:
		return result
	return facter(num - 1, num * result)

print(fact(6))
print(fact(100))

print(facte(6))
print(facte(100))
