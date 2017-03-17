#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging

def foo(s):
	try:
		print('Try...')
		n = 10 / int('s')
		print('n:', n)
	except ValueError as e:
		print('ValueError', e)
	except ZeroDivisionError as e:
		print('ZeroDivisionError:', e)
	else:
		print('No Error!')
	finally:
		print('Finally...')
	print('END')

def main():
	foo(0)

main()