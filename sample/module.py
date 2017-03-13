#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 表示模块的文档注释
'a test module'  

# 作者
__author__ = 'neu Henry'

import sys

def test():
	args = sys.argv
	if len(args) == 1:
		print('Hello, world!')
	elif len(args) == 2:
		print('Hello, %s!' % args[0])
	else:
		print('Too many argument!')

if __name__ == '__main__':
	test()