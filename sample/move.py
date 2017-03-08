#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def move(n, a, b, c):
    if n >= 1:
        move(n-1,a,c,b)
        print('move',a,'-->',c)
        move(n-1,b,a,c)

print(move(3, 'A', 'B', 'C'))