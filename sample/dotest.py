#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import pdb
logging.basicConfig(level=logging.INFO)

# assert 用法
def fa(s):
	n = int(s)
	assert n != 0, 'n is zero!'
	return 10 / n

# logging 用法
def fl(s):
	n = int(s)
	pdb.set_trace()   # 运行到这里会自动暂停
	logging.info('n = %d' % n)
	print(10 / n)

def main():
	fa('1')
	fl('0')

main()