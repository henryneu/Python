#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

specify_str = 'dict'

def rela_path(dirname):
    results = []
    # os.walk() for 当前目录root，当前目录下的全部子目录名dirs，当前目录下的所有文件名files in os.walk()
    for root, dirs, files in os.walk(dirname):
        results += [os.path.relpath(os.path.join(root, x), start=dirname) for x in files if specify_str in x]

    for result in results:
        print(result)

rela_path(os.getcwd())  # os.getcwd()返回当前的目录